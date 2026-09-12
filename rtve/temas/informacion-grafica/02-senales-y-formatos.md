# Tema 2 del específico de Información Gráfica y Captación de Imagen y Sonido · Señales y formatos: de la señal a la medida

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Información Gráfica y Captación de Imagen y Sonido · punto 2 |
| **Sirve para** | **Información Gráfica y Captación de Imagen y Sonido** |
| **Fuente** | **Recomendaciones UIT-R BT.2100-1**, de cuyo apartado sobre las tres funciones de transferencia sale la respuesta oficial **palabra por palabra**; **BT.2020-2** y **BT.709-6**. El resto —instrumentos de medida, muestreo y señales de prueba— **va como oficio y así se declara** |
| **Identificador** | **UIT-R BT.709-6** · **UIT-R BT.2020-2** · **UIT-R BT.2100-1**. No tienen identificador del BOE: se citan por su número de recomendación |
| **Redacción que se estudia** | Las **ediciones vigentes**. **El enunciado de una pregunta cita la edición 2 de la BT.2100 y este tema se ha verificado contra la edición 1**, que es la disponible: el párrafo coincide palabra por palabra |
| **Sólo con la plantilla** | **Una pregunta** —la identificación de una señal de prueba— **depende enteramente de una imagen** que un temario escrito no puede reproducir ni contrastar. **La respuesta descansa en la plantilla oficial**, y el tema aporta qué dibuja cada señal en un monitor de forma de onda |
| **Extensión** | **4.734 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la alta definición (**HD**) y la ultra alta
definición (**UHD**); la interfaz digital serie (**SDI**); la luminancia (**Y**) y los tres primarios
(**RGB**); la función de transferencia optoelectrónica (**OETF**, *opto-electronic transfer
function*), la electroóptica (**EOTF**) y la optoóptica (**OOTF**); la cuantificación perceptual
(**PQ**, *perceptual quantizer*) y la curva híbrida logarítmica-gamma (**HLG**); el monitor de forma
de onda, que el examen abrevia **M.F.O.**; la imagen dentro de imagen (**PiP**, *picture in
picture*); el códec de audio sin pérdida de Apple (**ALAC**, *Apple Lossless Audio Codec*); el
dispositivo de acoplamiento de carga (**CCD**) y el semiconductor complementario de óxido metálico
(**CMOS**); el kilohercio (**kHz**) y el megahercio (**MHz**); la línea alternada en fase (**PAL**) y la línea
nacional norteamericana (**NTSC**); el voltio (**v**, como lo escribe el
examen); y la Unión Internacional de Telecomunicaciones (**UIT**, o **ITU** en su sigla inglesa, como
la escribe uno de los enunciados), cuyo sector de radiocomunicaciones (**UIT-R**) publica las
recomendaciones **BT.601**, **BT.709**, **BT.2020** y **BT.2100**.

> Enunciado de la convocatoria (Anexo 2, temario específico de Información Gráfica y Captación de
> Sonido, puntos 2 y 3.5):
> «Principios básicos de señales y formatos: cableado, señal analógica y digital, alta definición.»
> «Sistemas de grabación: formatos, muestreo, compresión, codificación y soportes.»

**Doce preguntas.** Y es el punto donde este examen **cita una recomendación de la Unión Internacional
de Telecomunicaciones por su número dentro del enunciado**, cosa que no hace ningún otro cuadernillo
del proyecto: **la pregunta 25 pide la función de la OETF «según la recomendación ITU-R BT.2100-2»**.

<!-- indice -->

## Índice

- [1. De la escena a la pantalla: las tres funciones de transferencia](#1-de-la-escena-a-la-pantalla-las-tres-funciones-de-transferencia)
- [2. Las gammas normalizadas](#2-las-gammas-normalizadas)
- [3. La profundidad de bits](#3-la-profundidad-de-bits)
- [4. El submuestreo cromático](#4-el-submuestreo-cromático)
- [5. La resolución y la relación de aspecto](#5-la-resolución-y-la-relación-de-aspecto)
- [6. La luminancia en UHD](#6-la-luminancia-en-uhd)
- [7. El teorema del muestreo](#7-el-teorema-del-muestreo)
- [8. Los instrumentos de medida](#8-los-instrumentos-de-medida)
- [9. El blanco y los tres voltajes](#9-el-blanco-y-los-tres-voltajes)
- [10. Las funciones de un monitor profesional](#10-las-funciones-de-un-monitor-profesional)
- [11. Las señales de prueba](#11-las-señales-de-prueba)
- [12. Los datos que el examen ha preguntado](#12-los-datos-que-el-examen-ha-preguntado)
- [13. Trazabilidad](#13-trazabilidad)

<!-- /indice -->

## 1. De la escena a la pantalla: las tres funciones de transferencia

**La cadena de televisión no es lineal en ningún punto**, y hay tres funciones que describen las tres
conversiones que ocurren en ella. **La Recomendación UIT-R BT.2100 las define las tres juntas**, y el
examen pregunta por la primera.

**La Recomendación UIT-R BT.2100, en su apartado sobre la relación entre las tres funciones, dice
literalmente:**

**«OETF: función de transferencia optoelectrónica, que transforma la luz lineal de la escena en la
señal de vídeo, normalmente en el interior de una cámara.»**

**«EOTF: función de transferencia electroóptica, que transforma la señal de vídeo en la luz lineal de
la pantalla.»**

**«OOTF: función de transferencia optoóptica que cumple el cometido de aplicar las "opciones de
reproducción".»**

Y añade: **«Estas funciones están relacionadas, por lo que solo dos de las tres son
independientes.»**

**La función que realiza la OETF es transformar la luz lineal de la escena en la señal de vídeo,
normalmente en el interior de una cámara.** Ésa es la respuesta oficial a la pregunta 25, y es
**literalmente la definición de la Recomendación que el propio enunciado cita**.

**Y aquí está lo notable de esta pregunta**: **las tres opciones falsas son las definiciones de las
otras dos funciones**, copiadas también de la misma Recomendación:

| Opción | Qué define en realidad |
|---|---|
| «Transforma la señal de vídeo en la luz lineal de la pantalla» | **La EOTF** |
| «Aplica las opciones de reproducción en la pantalla» | **La OOTF** |
| «Transforma la señal de vídeo en luz lineal de la escena» | **Una inversión inventada**: cambia «escena» por «pantalla» en la definición de la EOTF |

**Es la pregunta mejor construida de este cuadernillo**: **las cuatro opciones salen del mismo párrafo
de la norma**, y **sólo se contesta sabiendo qué letra va con qué dirección**.

**La regla que las separa, y la que hay que memorizar:**

| Función | De qué a qué | Dónde ocurre |
|---|---|---|
| **OETF** | **Óptico → eléctrico**: luz de la escena → señal | **En la cámara** |
| **EOTF** | **Eléctrico → óptico**: señal → luz de la pantalla | **En el monitor** |
| **OOTF** | **Óptico → óptico**: luz de la escena → luz de la pantalla | **Es el resultado de las otras dos** |

**La mnemotecnia**: **la primera letra dice de dónde se parte.** **OETF empieza por «O» de óptico, y
la óptica es la escena: parte de la luz.** **EOTF empieza por «E» de eléctrico: parte de la señal.**

**Un aviso sobre la edición citada**: **el enunciado cita la BT.2100-2 y este temario se ha verificado
contra la BT.2100-1**, que es la edición de la que este proyecto dispone. **El párrafo de las tres
definiciones es el mismo en las dos**, y la respuesta oficial coincide palabra por palabra con la
edición consultada. **Lo que no se ha podido comprobar es si la edición 2 introduce algún matiz en
ese párrafo**, y así se declara.

## 2. Las gammas normalizadas

**Una gamma normalizada es una curva de transferencia con nombre**, y el operador la elige en la
cámara según el destino del material.

| Nombre | Qué es |
|---|---|
| **Rec. 709** o **R709** | **La curva normalizada de la alta definición**, la de la Recomendación UIT-R BT.709. **Es la gamma estándar en HD** |
| **Rec. 2020** | La de la ultra alta definición |
| **PQ** y **HLG** | **Las dos curvas de alto rango dinámico** de la Recomendación UIT-R BT.2100 |
| **Curvas logarítmicas de fabricante** | Las de cada casa, para producción con etalonaje posterior |

**La gamma estándar en HD es la R709.** Ésa es la respuesta oficial a la pregunta 80.

**Las tres opciones falsas son nombres de curvas de fabricante o inventados**: **«S709»** es una curva
de una casa concreta que imita el aspecto de la Rec. 709 **pero no es la norma**; **«HG1»** y **«G33»**
**no designan ninguna gamma normalizada**.

**La distinción que la pregunta mide**: **una gamma normalizada la publica un organismo de
normalización; una gamma de fabricante la publica una casa.** **La letra que precede al número lo
delata**: **«R» de recomendación frente a la inicial de la marca.**

## 3. La profundidad de bits

**La profundidad de bits es con cuántos niveles se anota cada muestra de la señal**: ocho bits dan 256
niveles por canal, diez bits dan 1.024 y doce bits dan 4.096.

**Al aumentar la profundidad de color se consiguen más niveles de brillo, más gama de colores,
degradados más suaves, y aumenta el peso de los archivos generados.** Ésa es la respuesta oficial a la
pregunta 14.

**Los cuatro efectos de la respuesta, y los cuatro son ciertos:**

| Efecto | Por qué |
|---|---|
| **Más niveles de brillo** | Es la definición: **más valores posibles por muestra** |
| **Más gama de colores** | **Más combinaciones de los tres canales**: de 16,7 millones a más de mil millones |
| **Degradados más suaves** | **Es la desaparición del *banding***: hay escalones intermedios donde antes no había |
| **Más peso de los archivos** | **Cada muestra ocupa más bits** |

**Las tres opciones falsas atribuyen a la profundidad de bits cosas que no hace**, y la clave está en
dos palabras: **contraste** y **rango dinámico**.

| Opción | Qué afirma de más |
|---|---|
| a) | «Aumentamos el contraste y la relación de contraste» |
| b) | «Aumentamos el nivel de brillo, el rango dinámico, la relación de contraste» |
| d) | «Mayor contraste y mayor rango dinámico» |

**Y aquí hay una costura que conviene ver, porque el mismo cuadernillo se contradice.** **La pregunta
94 pregunta si una codificación con mayor profundidad de bit afecta al espacio de color y al margen
dinámico, y la respuesta oficial es que afecta a los dos.** **La pregunta 14, en cambio, descarta como
falsas tres opciones precisamente por decir que aumenta el rango dinámico.**

**Cómo se resuelve la aparente contradicción**, y es lo que hay que tener claro para acertar las dos:

- **La profundidad de bits no crea rango dinámico: lo hace utilizable.** **El rango dinámico que una
  cámara puede capturar lo determina el sensor**, no el número de bits con que se anota.
- **Pero al codificar un rango dinámico amplio con pocos bits, los escalones se hacen tan grandes que
  el rango deja de ser aprovechable.** **Con más bits, el mismo rango se representa sin roturas.**
- **Por eso la respuesta de la 94 es correcta —afecta— y la de la 14 también —no es lo que se
  «consigue»—.** **Una habla de lo que la profundidad *afecta* y la otra de lo que la profundidad
  *produce***, y la diferencia entre los dos verbos es toda la distinción.

**La respuesta oficial a la pregunta 94 es que la mayor profundidad de bit afecta tanto al espacio de
color como al margen dinámico.** **Las tres opciones falsas** son las dos que dicen «sólo» una de las
dos cosas y una tercera que **hace depender el efecto del tipo de sensor** —«afecta más con tecnología
CCD que con un CMOS»—, que **es falso: la profundidad de codificación es independiente de la
tecnología del sensor.**

## 4. El submuestreo cromático

**El submuestreo cromático es una técnica que reduce la resolución de los componentes de la
crominancia para disminuir el tamaño de los archivos sin una pérdida significativa de calidad.** Ésa
es la respuesta oficial a la pregunta 18.

**Por qué funciona, que es lo que hay que entender**: **el ojo humano distingue mucho mejor los
detalles de brillo que los de color**. **Guardar la mitad, o la cuarta parte, de la información de
color es una pérdida que casi no se ve**, y **ahorra la mitad o dos tercios del caudal**.

| Notación | Qué guarda | Dónde se usa |
|---|---|---|
| **4:4:4** | **Una muestra de color por píxel**: sin submuestreo | Grafismo, croma, cine |
| **4:2:2** | **La mitad de muestras de color en horizontal** | **El estándar de producción de televisión** |
| **4:2:0** | La mitad en horizontal **y la mitad en vertical** | **Emisión y distribución** |

**Las tres opciones falsas de la pregunta 18 dicen todas lo contrario**, y ése es todo el mecanismo:

| Opción | Qué afirma | Por qué es falsa |
|---|---|---|
| a) | «Aumenta la información de la crominancia» | **La reduce**: para eso está |
| b) | «Aumenta la resolución de la luminancia» | **No toca la luminancia**: sólo la crominancia |
| c) | «Aumenta la resolución de la crominancia disminuyendo el tamaño de los archivos» | **Se contradice a sí misma**: no se puede aumentar la información y bajar el peso a la vez |

**La palabra que resuelve la pregunta es «reduce»**, y **la opción c) es la trampa mejor puesta porque
afirma dos cosas incompatibles en la misma frase.** Es el mismo mecanismo que la pregunta 93 del
cuadernillo de Montaje de Equipos, donde una opción también se contradecía sola.

**El aviso de oficio, que es lo que le importa a un operador**: **el submuestreo limita lo que se puede
hacer después**. **Un croma sobre material 4:2:0 recorta mal**, porque **el borde del recorte se
calcula sobre información de color que no está**. Por eso **el material destinado a incrustación se
graba en 4:2:2 como mínimo, y mejor en 4:4:4**.

## 5. La resolución y la relación de aspecto

**La relación de aspecto de la imagen en el formato UHD es 1:1,78, o 16/9.** Ésa es la respuesta
oficial a la pregunta 26, y **la Recomendación UIT-R BT.2100, en su Cuadro 1, «Características
espaciales y temporales de la imagen», da como forma del contenedor de imagen el valor «16:9»**,
junto con cómputos de píxeles de **«7 680 × 4 320»**, **«3 840 × 2 160»** y **«1 920 × 1 080»**.

**Las dos formas de escribir lo mismo**, que es lo que la pregunta pone a prueba: **16/9 es una
fracción y 1,78 es su valor decimal.** **16 ÷ 9 = 1,777…**, así que **1:1,78 y 16/9 son la misma
proporción escrita de dos maneras.**

**Las tres opciones falsas son relaciones de aspecto reales de otros formatos**, todas ellas
emparejadas incoherentemente con «16/9»:

| Valor decimal | A qué formato corresponde |
|---|---|
| **1,37** | **El formato académico** del cine sonoro clásico |
| **1,85** | **Un panorámico de proyección** cinematográfica |
| **1,66** | **Otro panorámico europeo** de proyección |

**La forma de contestarla sin dudar**: **hacer la división.** **16 dividido por 9 da 1,78 y no da
ninguna de las otras tres.** **Las cuatro opciones dicen «16/9», así que la que tenga el decimal
correcto es la buena.**

## 6. La luminancia en UHD

**La señal de luminancia en vídeo UHD se forma como Y = 0,2627 R + 0,6780 G + 0,0593 B.** Ésa es la
respuesta oficial a la pregunta 33, y son **los coeficientes que la Recomendación UIT-R BT.2020 recoge
en su Cuadro 4** para la televisión de ultra alta definición.

**Las tres opciones falsas son coeficientes reales de otras recomendaciones, o deformaciones de
ellos:**

| Opción | Qué es |
|---|---|
| **0,2126 / 0,7152 / 0,0722** | **Los coeficientes VERDADEROS de la Recomendación UIT-R BT.709**, la de la alta definición. **Es la respuesta correcta a otra pregunta** |
| **0,2122 / 0,7156 / 0,0722** | **Los de la BT.709 con dos dígitos movidos** |
| **0,2993 / 0,5872 / 0,1145** | **Los de la BT.601**, la de definición estándar, **con un decimal añadido a cada uno** |

**La tabla que resuelve esta pregunta y la del tema 1 de Edición y Montaje:**

| Recomendación | Para qué | R | G | B |
|---|---|---|---|---|
| **UIT-R BT.601** | Definición estándar | 0,299 | 0,587 | 0,114 |
| **UIT-R BT.709** | **Alta definición** | 0,2126 | 0,7152 | 0,0722 |
| **UIT-R BT.2020** | **Ultra alta definición** | **0,2627** | **0,6780** | **0,0593** |

**La forma de distinguirlas sin memorizar los nueve números**: **mírese el coeficiente del verde.**
**0,587 es definición estándar; 0,7152 es alta definición; 0,6780 es ultra alta definición.** **Con
esa sola cifra se separan las tres.**

**Y una observación que ayuda a descartar deformaciones**: **los tres coeficientes de cualquiera de las
tres recomendaciones suman exactamente uno.** **0,2627 + 0,6780 + 0,0593 = 1.** **La opción con
0,2122 y 0,7156 suma 1,0000 también**, así que ese truco no la descarta; **la de 0,2993 / 0,5872 /
0,1145 suma 1,0010**, y **ésa sí se cae sola**.

## 7. El teorema del muestreo

**El principio de Nyquist recomienda una frecuencia de muestreo de al menos dos veces la frecuencia
más alta de la señal muestreada.** Ésa es la respuesta oficial a la pregunta 68.

**Por qué el doble**, que es lo que hay que entender: **para reconstruir una onda hacen falta al menos
dos muestras por ciclo**, una en cada semiciclo. **Con menos, la onda reconstruida no es la
original**: aparece **una frecuencia más baja que no estaba**, y ese defecto se llama **solapamiento**
o *aliasing*.

**De ahí salen las cifras de la práctica:**

| Señal | Frecuencia máxima | Muestreo de uso |
|---|---|---|
| **Audio audible** | **20 kHz** | **48 kHz** en televisión; 44,1 kHz en disco |
| **Vídeo en definición estándar** | Unos 5,5 MHz de luminancia | 13,5 MHz |

**Las tres opciones falsas son cifras concretas donde el enunciado pide un principio general:**

| Opción | Qué es en realidad |
|---|---|
| «Al menos 44 kHz» | **Una frecuencia de muestreo concreta**, la del disco compacto. **No es el principio** |
| «3,58 MHz» | **La frecuencia de la subportadora de color del sistema NTSC** |
| «4,43 MHz» | **La frecuencia de la subportadora de color del sistema PAL** |

**La forma de contestarla**: **el enunciado pregunta por un principio, y sólo una opción enuncia una
regla en lugar de dar un número.** **Las otras tres son datos reales de otro sitio**, y las dos
últimas son **precisamente las subportadoras que un operador de televisión conoce de memoria**, lo que
las hace tentadoras.

**El corolario que se pregunta en otros exámenes de este proyecto**: **el filtro antialias**, que va
antes del muestreo y **corta las frecuencias por encima de la mitad de la frecuencia de muestreo**,
precisamente para que el teorema se cumpla.

## 8. Los instrumentos de medida

**Un vectorscopio sirve para medir la crominancia.** Ésa es la respuesta oficial a la pregunta 41.

| Instrumento | Qué mide | Qué se ve en él |
|---|---|---|
| **Monitor de forma de onda** | **La LUMINANCIA**, línea a línea | **Un perfil del brillo**, con el pedestal de negros abajo y el blanco arriba |
| **Vectorscopio** | **La CROMINANCIA**: tono y saturación | **Un diagrama polar** con las cajas de los seis colores de barras |
| **Histograma** | El reparto estadístico de los niveles | Cuántos píxeles hay en cada nivel |

**Cómo se lee un vectorscopio**, que es lo que da sentido a la respuesta: **el ángulo alrededor del
centro es el *tono* y la distancia al centro es la *saturación***. **El centro es la ausencia de color**,
así que **una imagen en blanco y negro se ve como un punto en el centro** y **una imagen con dominante
se ve como un punto desplazado hacia el color de la dominante**.

**Las dos opciones falsas de impedancia** —«niveles de impedancia de entrada» y «de salida»— **miden
una propiedad eléctrica del circuito**, que se comprueba con un puente o un analizador, **no con un
instrumento de imagen**. **Y la de luminancia es la trampa buena**, porque **es lo que mide el otro
instrumento de la pareja**.

**La regla que separa los dos**: **la forma de onda dice si la exposición está bien; el vectorscopio
dice si el color está bien.** **Son dos preguntas distintas y hacen falta los dos.**

## 9. El blanco y los tres voltajes

**Dada una superficie blanca que el vectorscopio muestra sin ninguna dominante, y cuya señal mide un
voltio en el monitor de forma de onda desde el pedestal de negros hasta el recorte de blancos, los
valores de voltaje de cada canal son R = 0,30 v, G = 0,59 v y B = 0,11 v.** Ésa es la respuesta
oficial a la pregunta 97.

**De dónde salen esas tres cifras**, y es lo que hace la respuesta razonable en lugar de arbitraria:
**son los coeficientes de la luminancia de la Recomendación UIT-R BT.601** —0,299, 0,587 y 0,114—
**redondeados a dos decimales**. **Su suma es exactamente uno**, y por eso **suman el voltio de la
señal completa**.

**El razonamiento de la pregunta, paso a paso:**

1. **La superficie es blanca sin dominante**, así que **los tres primarios están en su valor máximo a
   la vez**: es blanco de referencia.
2. **La señal de luminancia mide un voltio de negro a blanco.**
3. **La luminancia se construye pesando los tres primarios**, y **los pesos suman uno**.
4. **Por tanto, la contribución de cada canal al voltio de luminancia es su coeficiente expresado en
   voltios**: **0,30 del rojo, 0,59 del verde y 0,11 del azul**.

**Lo que la pregunta enseña, más allá del número**: **el verde aporta casi el 60 % del brillo
percibido, el rojo el 30 % y el azul apenas el 11 %.** **Ésa es la razón de que un error en el canal
azul se note mucho menos que el mismo error en el verde**, y de que **el submuestreo cromático sea
posible**.

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| **0,33 / 0,33 / 0,33** | **Reparte el voltio a partes iguales.** Es lo que saldría si los tres primarios pesaran lo mismo, **y no lo hacen** |
| **0,39 / 0,50 / 0,11** | **Suma exactamente uno**, pero **los coeficientes no son los de ninguna recomendación** |
| **0,39 / 0,40 / 0,21** | **Suma uno**, y tampoco corresponde a ninguna |

**La opción b) es la trampa mejor puesta**, porque **es la respuesta intuitiva**: si el blanco son los
tres primarios a la vez, parece que deberían pesar lo mismo. **Lo que la descarta es saber que la
luminancia no es una media, es una media PONDERADA**, y que **los pesos vienen de cómo ve el ojo**.

**Una advertencia sobre las cifras**: **el enunciado usa los coeficientes de la definición estándar**
—los de la BT.601— **redondeados**, no los de alta definición ni los de UHD. **Con los de la BT.709
las tres cifras serían 0,21 / 0,72 / 0,07**, y con los de la BT.2020, **0,26 / 0,68 / 0,06**. **La
respuesta oficial es correcta si se entiende que la pregunta usa el reparto clásico**, que es el que
la literatura de medida de señal de vídeo maneja con esas tres cifras redondas.

## 10. Las funciones de un monitor profesional

**Un monitor de referencia tiene funciones que un monitor de consumo no tiene**, y están para
comprobar la señal, no para verla bonita.

| Función | Qué hace |
|---|---|
| ***Blue Only*** | **Muestra sólo el canal azul en blanco y negro.** Sirve para **ajustar croma y fase** con barras de color, y para **ver el ruido**, que suele ser peor en el azul |
| ***Underscan*** | **Muestra la imagen completa, incluidos los bordes** que un monitor normal recorta. Sirve para **ver el borde real del cuadro** y los defectos de los extremos |
| ***PiP*** | **Imagen dentro de imagen**: dos fuentes a la vez, para comparar |
| **Marcadores y zonas de seguridad** | Dibujan los límites de título y de acción |
| **Falso color y cebras** | Señalan zonas por su nivel de exposición |
| ***ALAC*** | **NO es una función de monitor: es un códec de audio sin pérdida** |

**La función que NO pertenece a la de los monitores profesionales es ALAC.** Ésa es la respuesta
oficial a la pregunta 74, y el motivo es de categoría: **ALAC es el códec de audio sin pérdida de
Apple**, y **no tiene nada que ver con un monitor de imagen**.

**La forma de contestarla**: **de las cuatro opciones, tres son funciones de visualización y una es un
formato de audio.** **Se descarta por categoría, sin saber qué hace cada función.**

**Y las otras tres conviene saberlas**, porque **el examen las nombra y un operador las usa**: **el
*blue only* para el ajuste con barras, el *underscan* para revisar bordes y el *PiP* para comparar
dos fuentes.**

## 11. Las señales de prueba

**Una señal de prueba es una señal generada, de forma conocida, que sirve para comprobar y ajustar la
cadena.** Las tres que un operador maneja:

| Señal | Qué es | Para qué |
|---|---|---|
| **Barras de color** | Bandas verticales de los seis colores más blanco y negro | **Ajuste de croma, fase y nivel** |
| **Rampa** o **diente de sierra** | **Una subida lineal del negro al blanco**, que en el monitor de forma de onda dibuja **una diagonal recta** | **Comprobar la linealidad**: cualquier curvatura o escalón delata un defecto |
| **Multiburst** | Grupos de frecuencias crecientes | Comprobar la respuesta en frecuencia |

**La pregunta 71 muestra una imagen y pide identificarla, y la respuesta oficial es «señal test diente
de sierra».** **Las tres opciones falsas** —señal de prueba de audio, señal de prueba de UHD y «señal
test de corrección de *bokeh*»— **son distractores de distinta calidad**: la primera y la segunda son
categorías reales, y **la tercera no existe**: **el *bokeh* es el aspecto del desenfoque de un
objetivo y no se corrige con una señal de prueba.**

**Una declaración expresa sobre esta pregunta**: **el enunciado depende enteramente de una imagen**
—«esta imagen corresponde a una»—, **y una imagen no se puede reproducir en un temario escrito ni
verificar contra una fuente**. **La respuesta descansa en la plantilla oficial**, y lo que este tema
aporta es **qué dibuja cada señal de prueba en un monitor de forma de onda**, que es lo que permite
reconocerla: **la rampa o diente de sierra dibuja una diagonal recta, y ninguna de las otras tres
opciones dibuja eso.**

## 12. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 14 | Qué se obtiene al aumentar la profundidad de color | c) Más niveles, más gama, degradados suaves y más peso ✔ |
| 18 | Qué es el submuestreo cromático | d) Reduce la resolución de la crominancia ✔ |
| 25 | Qué función realiza la OETF | d) Transforma la luz de la escena en señal de vídeo ✔ |
| 26 | Relación de aspecto en UHD | a) 1:1,78 o 16/9 ✔ |
| 33 | Luminancia en vídeo UHD | d) 0,2627 R + 0,6780 G + 0,0593 B ✔ |
| 41 | Para qué sirve un vectorscopio | b) Para medir la crominancia ✔ |
| 68 | Qué recomienda el principio de Nyquist | b) Al menos el doble de la frecuencia más alta ✔ |
| 71 | Qué señal de prueba muestra la imagen | a) Diente de sierra ✔ **·** sólo con la plantilla |
| 74 | Qué función NO es de monitores profesionales | a) ALAC ✔ |
| 80 | Cuál es una gamma estándar en HD | a) R709 ✔ |
| 94 | Si la profundidad de bit afecta al color y al rango | d) Afecta a los dos ✔ |
| 97 | Voltajes de R, G y B para reproducir el blanco | a) 0,30 / 0,59 / 0,11 ✔ |

**Las doce respuestas oficiales son correctas**, y **una descansa sólo en la plantilla**: la que
depende de una imagen.

**Tres avisos de estudio.** **La pregunta 25 tiene las cuatro opciones sacadas del mismo párrafo de la
norma**, así que **sólo se contesta sabiendo qué letra va con qué dirección**. **La 26 se resuelve
haciendo una división** —16 entre 9—, sin memorizar nada. **Y la 33 usa como distractor los
coeficientes verdaderos de la Recomendación de alta definición**: quien se sepa una sola terna puede
marcar la equivocada con toda confianza.

**Un aviso sobre la aparente contradicción entre la 14 y la 94**, que está explicada en el epígrafe 3:
**la 14 pregunta qué se *consigue* y la 94 pregunta a qué *afecta***, y por eso una descarta el rango
dinámico y la otra lo incluye. **Las dos respuestas oficiales son correctas**, y **quien no vea la
diferencia entre los dos verbos falla una de las dos.**

## 13. Trazabilidad

**Las fuentes técnicas que este tema cita:**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Recomendación UIT-R BT.2100-1** | El apartado sobre la relación entre la OETF, la EOTF y la OOTF, con las **tres definiciones citadas literalmente**, y el **Cuadro 1**, con la forma del contenedor **«16:9»** y los tres cómputos de píxeles |
| | **Recomendación UIT-R BT.2020-2** | Los coeficientes de la luminancia de ultra alta definición, del Cuadro 4 |
| | **Recomendación UIT-R BT.709-6** | Los coeficientes de la alta definición y su condición de gamma normalizada |
| **Quinto: la plantilla oficial** | **Una afirmación**: la identificación de la señal de prueba de la pregunta 71 | Pregunta 71 |

**Dos declaraciones expresas:**

1. **La pregunta 71 depende enteramente de una imagen**, y una imagen no se puede reproducir en un
   temario escrito ni contrastar con una fuente. **La respuesta descansa en la plantilla oficial.** Lo
   que el tema sostiene es **qué dibuja cada señal de prueba en un monitor de forma de onda**, que es
   lo que permite reconocerla.
2. **El enunciado de la pregunta 25 cita la edición 2 de la Recomendación UIT-R BT.2100 y este tema se
   ha verificado contra la edición 1**, que es la que este proyecto ha podido consultar. **El párrafo
   de las tres definiciones coincide palabra por palabra con la respuesta oficial en la edición
   consultada**, y **no se ha podido comprobar si la edición 2 introduce algún matiz en ese
   párrafo.**

**El resto del tema va como oficio y así se declara**: la lectura de un vectorscopio y de un monitor
de forma de onda, las funciones de un monitor de referencia, el teorema del muestreo, el
comportamiento del submuestreo cromático y el reparto de voltajes del blanco. **Nada de eso está en un
boletín oficial**, y el tema no lo presenta como si lo estuviera.
