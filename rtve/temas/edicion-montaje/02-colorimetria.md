# Tema 2 del específico de Edición, Montaje y Procesos Audiovisuales · Colorimetría y el color en televisión

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 2 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Recomendaciones UIT-R BT.709-6**, **BT.2020-2** y **BT.2100-1**, del sector de radiocomunicaciones de la Unión Internacional de Telecomunicaciones. El resto —leyes de Grassmann, LUT y curvas logarítmicas— **va como oficio y así se declara** |
| **Identificador** | **UIT-R BT.709-6** · **UIT-R BT.2020-2** · **UIT-R BT.2100-1**. No tienen identificador del BOE: se citan por su número de recomendación |
| **Redacción que se estudia** | Las **ediciones vigentes**: la **6** de la BT.709, la **2** de la BT.2020 y la **1** de la BT.2100 |
| **Aviso de reparto** | **Diez preguntas de un subpunto que ocupa una frase del programa.** Es el punto que más renta por línea de anexo de toda la ocupación, y **ninguna de sus respuestas descansa sólo en la plantilla** |
| **Extensión** | **3.431 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: los tres primarios rojo, verde y azul (**RGB**); la
luminancia (**Y**) y las dos señales de diferencia de color (**Cb** y **Cr**, o **U** y **V** en la
notación analógica); la luminancia constante (**CL**, *constant luminance*) y la no constante
(**NCL**, que el examen escribe **NFL**); el alto rango dinámico (**HDR**, *high dynamic range*),
con su curva híbrida logarítmica-gamma (**HLG**, *hybrid log-gamma*), y el rango dinámico estándar
(**SDR**); la tabla de consulta (**LUT**, *look-up table*); la candela por
metro cuadrado (**cd/m²**), que en la industria se llama ***nit***; la Unión Internacional de
Telecomunicaciones (**UIT**), cuyo sector de radiocomunicaciones (**UIT-R**) publica las
recomendaciones **BT.709**, **BT.2020** y **BT.2100**; y la Comisión Internacional de la Iluminación
(**CIE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, punto 1.3):
> «Conceptos básicos de colorimetría.»

**Diez preguntas de un solo subpunto.** Es el punto que más renta por línea de programa de toda la
ocupación: **el anexo le dedica una frase y el examen le dedica diez preguntas**.

<!-- indice -->

## Índice

- [1. Cómo se ve el color, y las leyes de Grassmann](#1-cómo-se-ve-el-color-y-las-leyes-de-grassmann)
- [2. Los colores no espectrales](#2-los-colores-no-espectrales)
- [3. De RGB a luminancia: la señal Y](#3-de-rgb-a-luminancia-la-señal-y)
- [4. Luma constante y luma no constante](#4-luma-constante-y-luma-no-constante)
- [5. La gamma y las curvas logarítmicas](#5-la-gamma-y-las-curvas-logarítmicas)
- [6. La profundidad de bits y el *banding*](#6-la-profundidad-de-bits-y-el-banding)
- [7. El HDR y el nit](#7-el-hdr-y-el-nit)
- [8. Las LUT](#8-las-lut)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. Cómo se ve el color, y las leyes de Grassmann

**El ojo humano tiene tres tipos de conos**, sensibles a zonas distintas del espectro visible. **De
ahí sale todo lo demás**: como la percepción del color se reduce a tres respuestas, **basta con tres
estímulos para reproducir cualquier color percibido**. Eso es la **síntesis aditiva**, y es el
principio sobre el que funciona una pantalla.

**Las leyes de Grassmann** son las que formalizaron esa idea en el siglo XIX, y el examen pregunta por
la primera.

**Por síntesis aditiva del color es posible conseguir todos los colores percibidos mezclando tres
franjas del espectro visible en la proporción de intensidad adecuada, siempre que ninguno de los tres
iluminantes elegidos pueda obtenerse por mezcla de los otros dos: eso es la primera ley de
Grassmann.** Ésa es la respuesta oficial a la pregunta 10.

**Las cuatro leyes, en una tabla, que es como se distinguen:**

| Ley | Qué dice |
|---|---|
| **Primera** | **Hacen falta tres estímulos independientes** —ninguno obtenible de los otros dos— para igualar cualquier color |
| **Segunda** | **Un color se puede sustituir por su mezcla equivalente** sin que la igualación cambie |
| **Tercera** | **La suma de dos mezclas equivalentes sigue siendo equivalente**: la igualación es aditiva |
| **Cuarta** | **La intensidad de una mezcla es la suma de las intensidades** de sus componentes |

**La palabra que identifica la primera** es **«independientes»**, o su formulación equivalente: **que
ninguno se obtenga por mezcla de los otros dos**. **Quien lea esa cláusula en el enunciado no necesita
saberse las otras tres.**

## 2. Los colores no espectrales

**Un color espectral es el que corresponde a una sola longitud de onda del espectro visible**: los que
se ven al descomponer la luz blanca en un prisma, del violeta al rojo.

**Un color no espectral es el que no corresponde a ninguna longitud de onda**, y sólo se percibe
**mezclando los dos extremos del espectro**.

**Los colores no espectrales son el púrpura y el magenta.** Ésa es la respuesta oficial a la pregunta
83, y el motivo es geométrico: en el diagrama de cromaticidad de la CIE, **los colores espectrales
forman la herradura y los púrpuras y magentas están en la recta que cierra sus dos extremos**. **Esa
recta se llama, literalmente, «línea de los púrpuras».**

**Las tres opciones falsas mezclan espectrales con no espectrales:**

| Opción | Por qué no |
|---|---|
| «El azul y el verde» | **Los dos son espectrales** |
| «El magenta y el verde» | **El magenta sí lo es; el verde no**: la pareja no vale |
| «El púrpura y el azul» | **El púrpura sí; el azul no** |

**La consecuencia práctica, que es lo que le importa al montador**: **el magenta no se puede
representar con una longitud de onda**, y por eso **no aparece en el arcoíris**. Es una mezcla que el
cerebro construye.

## 3. De RGB a luminancia: la señal Y

**La televisión no transmite rojo, verde y azul.** Transmite **una señal de luminancia y dos de
diferencia de color**, porque el ojo distingue mucho mejor los detalles de brillo que los de color, y
eso permite **dedicar menos ancho de banda al color sin que se note**.

**La luminancia se construye pesando los tres primarios**, y los pesos no son iguales: **el verde
aporta la mayor parte del brillo percibido y el azul la menor**.

**La construcción de la señal de luminancia en la Recomendación UIT-R BT.709 es Y = 0,2126 R + 0,7152
G + 0,0722 B.** Ésa es la respuesta oficial a la pregunta 7, y la Recomendación la recoge en su
**Cuadro 1, apartado 3.2, «Determinación de la señal de luminancia»**, con esos tres coeficientes.

**El distractor mejor construido de esta pregunta es la opción b)**: **Y = 0,2627 R + 0,6780 G +
0,0593 B**. **No está inventado: son los coeficientes de la Recomendación UIT-R BT.2020**, la de la
televisión de ultra alta definición, recogidos en su Cuadro 4. **Es la respuesta correcta a otra
pregunta.**

| Recomendación | Para qué | R | G | B |
|---|---|---|---|---|
| **UIT-R BT.601** | Definición estándar | 0,299 | 0,587 | 0,114 |
| **UIT-R BT.709** | **Alta definición** | **0,2126** | **0,7152** | **0,0722** |
| **UIT-R BT.2020** | Ultra alta definición | 0,2627 | 0,6780 | 0,0593 |

**Las otras dos opciones falsas son deformaciones**: la c) escribe **0,279 / 0,587 / 0,134**, que se
parece a los coeficientes de la BT.601 con el primero y el tercero cambiados —los de la BT.601 son
0,299 y 0,114—; y la d) escribe **0,2637 / 0,6790 / 0,0593**, que son los de la BT.2020 con dos
dígitos movidos.

**Cómo se estudia esta pregunta**: **memorizando la terna de la BT.709 y reconociendo la de la
BT.2020**. Las dos falsas restantes se descartan solas si se sabe que **los tres coeficientes de
cualquiera de estas recomendaciones suman exactamente uno**: 0,2126 + 0,7152 + 0,0722 = 1, y 0,279 +
0,587 + 0,134 = 1 también, pero **con el reparto de la definición estándar mal copiado**.

## 4. Luma constante y luma no constante

**Ésta es la pregunta más difícil del punto, y se contesta con una sola palabra: cuándo.**

**La diferencia entre los sistemas de luma constante y no constante es que la luma constante realiza
el procesado de Y a través de las señales RGB antes de que se hayan corregido en gamma, y en la no
constante se procesan después de la corrección de gamma de las señales RGB.** Ésa es la respuesta
oficial a la pregunta 5.

| Sistema | Orden de las operaciones |
|---|---|
| **Luma constante (CL)** | **Primero se calcula Y** a partir del RGB lineal, **y después se corrige la gamma** |
| **Luma no constante (NCL)** | **Primero se corrige la gamma** de cada primario, **y después se calcula Y'** a partir del R'G'B' ya corregido |

**Por qué existen las dos.** **La luma constante es la correcta desde el punto de vista de la
colorimetría**: al calcular la luminancia sobre señales lineales, **Y contiene toda la información de
brillo** y las señales de diferencia de color no arrastran nada de ella. **La no constante es la que
se usa en la práctica**, porque es la que heredó toda la cadena de radiodifusión desde la televisión
en color analógica, y **cambiarla obligaría a cambiarlo todo**.

**La consecuencia visible del sistema no constante**: **una parte de la luminancia se cuela por los
canales de color**, y cuando esos canales se submuestrean —4:2:2, 4:2:0— **se pierde brillo en los
colores muy saturados**. Es el defecto conocido, y es la razón de que la Recomendación UIT-R BT.2020
ofrezca **las dos variantes**: la constante «cuando lo más importante es la retención exacta de la
información de luminancia», y la no constante «cuando lo más importante es utilizar las mismas
prácticas operativas» de la cadena existente.

**Las tres opciones falsas de la pregunta 5 son variaciones de la misma frase**, y **sólo dos cosas
cambian entre ellas**: **si el proceso va antes o después**, y **si lo que se corrige es la gamma o la
rasterización**. **La rasterización no pinta nada aquí**: es el paso de una imagen vectorial a una de
píxeles, y **no es una etapa de la codificación de color**. Las dos opciones que la nombran se
descartan sin más; de las dos que quedan, **la buena es la que pone la luma constante *antes***.

**Un aviso de grafía**: **el examen escribe «NFL» donde la literatura escribe «NCL»**, *non-constant
luminance*. **No es otra cosa: es una errata del enunciado.**

## 5. La gamma y las curvas logarítmicas

**La gamma es la relación no lineal entre el valor codificado de una señal y la luz que finalmente
sale de la pantalla.** Existe porque **el ojo no percibe el brillo linealmente**: distingue mucho
mejor los cambios en las zonas oscuras que en las claras. **Codificar linealmente sería malgastar
bits en las luces y quedarse corto en las sombras.**

**La Recomendación UIT-R BT.709 fija la precorrección no lineal de las señales primarias con un
exponente de 0,45**, que es aproximadamente la inversa de 2,2. **De ahí sale la gamma de 2,2 que todo
el mundo cita.**

**Las curvas logarítmicas** son otra cosa, y son de rodaje, no de emisión. **Un plano capturado con
una curva de gamma logarítmica genera una imagen más lavada que necesita de un proceso posterior de
corrección de color.** Ésa es la respuesta oficial a la pregunta 72.

**Por qué sale lavada, que es lo que hay que entender:**

- **La curva logarítmica reparte los valores disponibles a lo largo de todo el rango dinámico del
  sensor**, en lugar de concentrarlos donde quedarían bien a la vista.
- **El resultado es una imagen de bajo contraste y baja saturación**: gris, plana, «lavada».
- **Pero conserva información en las altas luces y en las sombras** que una curva de emisión habría
  recortado.
- **Por eso exige etalonaje**: la imagen logarítmica **es material de trabajo, no imagen final**.

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «Recoge directamente la información que genera el sensor» | **Eso es el RAW**, no el logarítmico. **El log ya es una codificación** |
| «Genera un contraste adecuado para la visualización final» | **Justo lo contrario**: no es imagen final |
| «Menor rango dinámico pero con un *look* más definitivo» | **Las dos mitades son falsas**: da MÁS rango dinámico y MENOS *look* definitivo |

## 6. La profundidad de bits y el *banding*

**La profundidad de bits es con cuántos niveles se anota cada muestra de la señal.** Ocho bits dan 256
niveles por canal; diez bits dan 1.024; doce bits dan 4.096.

**La principal ventaja de utilizar una profundidad de 10 bits frente a 8 bits en un muestreo de vídeo
es un mayor rango dinámico y una gradación de color más suave.** Ésa es la respuesta oficial a la
pregunta 94.

**Las tres opciones falsas se caen todas por la misma razón: más bits nunca es menos peso.**

| Opción | Por qué no |
|---|---|
| «Menor tamaño de archivo» | **Al contrario**: más bits, más peso |
| «Mayor tasa de cuadros por segundo» | **La profundidad de bits no tiene nada que ver con la cadencia** |
| «Mejor compatibilidad con dispositivos antiguos» | **Al contrario**: los antiguos son de 8 bits |

**Y de ahí sale la pregunta 13.** **El *color banding* se produce por una escasa profundidad de
color.** Ésa es la respuesta oficial.

**Qué es el *banding*, en una frase**: **cuando una degradación suave —un cielo, una pared iluminada—
no tiene niveles suficientes para representarse, el degradado se rompe en franjas visibles.** No es un
fallo de la pantalla: **es que faltan escalones**.

**Las tres opciones falsas de la pregunta 13, y por qué son la trampa exacta:**

| Opción | Por qué no |
|---|---|
| «Por una alta profundidad de color» | **Es lo contrario de la respuesta**: con más bits hay menos *banding* |
| «Por una alta resolución temporal» | **La resolución temporal son los cuadros por segundo**: no produce franjas |
| «Por una baja resolución espacial» | **La resolución espacial son los píxeles**: da una imagen blanda o pixelada, **no franjas en un degradado** |

**La distinción que resuelve la pregunta**: **resolución espacial es cuántos píxeles hay; profundidad
de color es cuántos valores puede tomar cada uno.** **El *banding* es un problema de la segunda, no de
la primera.**

## 7. El HDR y el nit

**El alto rango dinámico amplía la distancia entre el negro más oscuro y el blanco más brillante que
una imagen puede representar.** No es más resolución: **es más recorrido de brillo**, y con él **más
detalle en las luces y en las sombras a la vez**.

**La unidad que se utiliza para medir el brillo de una pantalla de alto rango dinámico es el nit.**
Ésa es la respuesta oficial a la pregunta 66.

| Unidad | Qué mide | Nota |
|---|---|---|
| ***Nit*** | **Luminancia**: **una candela por metro cuadrado** | **Es el nombre de industria de la cd/m²** |
| **Candela** | **Intensidad luminosa** de una fuente | **No incluye la superficie**: no es luminancia |
| **Candela por centímetro cuadrado** | Luminancia, pero **en otra escala**: 1 cd/cm² = 10.000 nits | **No es la unidad de uso** |
| **Lumen** | **Flujo luminoso** total emitido | Es lo que se mide en un proyector, no en una pantalla |

**Las tres opciones falsas son unidades reales de fotometría**, y ése es todo el mecanismo de la
pregunta: **hay que saber cuál de las cuatro mide luminancia de superficie**. **El nit y la candela
por centímetro cuadrado miden lo mismo en escalas distintas; sólo el nit es el de uso corriente.**

**Las cifras que dan sentido a la unidad**: una pantalla de rango dinámico estándar trabaja alrededor
de **100 nits**; la Recomendación UIT-R BT.2100, que es la del HDR, contempla monitores de referencia
de **1.000 cd/m² o más** con un negro de **0,005 cd/m² o menos**.

**Y de ahí sale la pregunta 50.** **Para etalonar en HDR un máster con salida en HDR se necesita un
monitor con *High Dynamic Range*.** Ésa es la respuesta oficial, y es de sentido común profesional:
**no se puede juzgar lo que no se ve.**

**Las tres opciones falsas, y por qué se caen:**

| Opción | Por qué no |
|---|---|
| «Un monitor con *Hybrid* Dynamic Range» | **«Hybrid Dynamic Range» no existe.** La palabra *hybrid* pertenece a **HLG**, *hybrid log-gamma*, que es **una curva de HDR, no un tipo de monitor** |
| «Es indiferente, el HDR sólo afecta a la grabación» | **Falso**: el HDR afecta a toda la cadena, y **el etalonaje es donde más** |
| «Un monitor SDR con el espacio de color en BT.2020» | **Confunde gama de color con rango dinámico.** BT.2020 amplía **qué colores**, no **cuánto brillo** |

**La distinción que la última opción pone a prueba, y que conviene fijar**: **la gama de color y el
rango dinámico son dos ejes distintos.** **Se puede tener gama amplia con rango estándar, y al revés.**

## 8. Las LUT

**Las LUT son tablas de consulta para transformar el color de una imagen.** Ésa es la respuesta
oficial a la pregunta 40.

**Cómo funcionan, en una frase**: **para cada combinación de entrada de rojo, verde y azul, la tabla
da una combinación de salida**. No calcula: **consulta**. De ahí el nombre, *look-up table*.

| Tipo | Qué hace |
|---|---|
| **LUT técnica** o de conversión | **Traduce entre espacios**: de logarítmico a Rec. 709, de una gama a otra. **Es corrección, no estilo** |
| **LUT creativa** o de *look* | **Aplica un aspecto**: una paleta, un viraje, un aire de época |
| **LUT 1D** | Una tabla por canal: **cambia curvas de tono**, no relaciones entre canales |
| **LUT 3D** | Una tabla sobre el cubo RGB: **puede cambiar el tono y la saturación**, no sólo el brillo |

**Las tres opciones falsas de la pregunta 40 llevan la LUT a otro sitio**: «ajustar la exposición» es
lo que hace **el diafragma o un control de ganancia**; «filtros de sonido» **no tiene nada que ver**;
y «un tipo de lente» **es una confusión con el vocabulario óptico**.

**El aviso de oficio, que es lo que separa al montador del aficionado**: **una LUT no corrige un plano
mal expuesto.** Se aplica **después** de haber ajustado exposición y balance, **no en lugar de
ajustarlos**. Aplicada sobre material mal expuesto **exagera el error en vez de corregirlo**.

## 9. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 5 | Diferencia entre luma constante y no constante | c) La constante procesa Y antes de la corrección de gamma ✔ |
| 7 | Construcción de la luminancia en la Rec. UIT-R BT.709 | a) Y = 0,2126 R + 0,7152 G + 0,0722 B ✔ |
| 10 | A qué ley corresponde el enunciado de la síntesis aditiva | a) Primera ley de Grassmann ✔ |
| 13 | Por qué se produce el *color banding* | d) Por una escasa profundidad de color ✔ |
| 40 | Qué son las LUT | c) Tablas de consulta para transformar el color ✔ |
| 50 | Monitor para etalonar en HDR un máster HDR | b) Un monitor con *High Dynamic Range* ✔ |
| 66 | Unidad del brillo de una pantalla HDR | a) *Nit* ✔ |
| 72 | Qué genera una curva de gamma logarítmica | b) Una imagen más lavada que necesita corrección ✔ |
| 83 | Cuáles son colores no espectrales | c) El púrpura y el magenta ✔ |
| 94 | Ventaja de 10 bits frente a 8 bits | b) Mayor rango dinámico y gradación más suave ✔ |

**Las diez respuestas oficiales son correctas**, y **dos se sostienen con norma técnica delante**: la
7, con la Recomendación UIT-R BT.709, y la 66, con las cifras de referencia de la BT.2100.

**Dos avisos de estudio.** **La pregunta 5 tiene cuatro opciones casi idénticas**, y la diferencia
está en dos palabras: **antes o después**, y **gamma o rasterización**. **Y la pregunta 7 usa como
distractor los coeficientes verdaderos de otra recomendación**: quien se sepa una sola terna **puede
marcar la equivocada con toda confianza**.

**Un aviso de grafía**: el enunciado de la pregunta 5 escribe **«NFL»** donde la literatura escribe
**«NCL»**, y el de la 50 llama **«Hybrid Dynamic Range»** a algo que no existe.

## 10. Trazabilidad

**Las fuentes técnicas que este tema cita:**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Recomendación UIT-R BT.709-6** | El apartado 3.1, con el exponente **0,45** de la precorrección no lineal, y el 3.2, con los tres coeficientes de la luminancia |
| | **Recomendación UIT-R BT.2020-2** | El Cuadro 4, con los coeficientes de la ultra alta definición, y sus notas sobre la luminancia constante y la no constante |
| | **Recomendación UIT-R BT.2100-1** | Las cifras de referencia del monitor de HDR: **1.000 cd/m²** o más de pico y **0,005 cd/m²** o menos de negro |

**Ninguna respuesta de este tema descansa sólo en la plantilla.**

**Lo que va como oficio, y así se declara**: las cuatro leyes de Grassmann —cuya formulación varía de
un manual a otro, aunque el contenido de la primera es el que el enunciado transcribe—, la definición
de las LUT y su tipología, y la descripción del comportamiento de una curva logarítmica. **Ninguna de
esas tres cosas está en una recomendación de la UIT**, y el tema no las presenta como si lo
estuvieran.

**Una declaración expresa sobre la numeración de las leyes de Grassmann**: **el orden en que se
enuncian no es universal.** Distintos manuales las ordenan de manera distinta, y **este tema sigue el
que el propio enunciado presupone**, que es el más extendido. **La respuesta oficial es correcta
dentro de esa numeración**, y quien encuentre otra ordenación en un manual **no está ante un error del
examen**, sino ante una convención distinta.
