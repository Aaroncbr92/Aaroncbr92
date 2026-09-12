# Esquema · Tema 2 del específico de Información Gráfica y Captación de Imagen y Sonido · Señales y formatos: de la señal a la medida

**Siglas**: la Unión Internacional de Telecomunicaciones (**UIT**, o **ITU** en su sigla inglesa,
como la escribe uno de los enunciados).

Telegrama. **Cada línea lleva delante de dónde sale**: `[2100]` = Recomendación UIT-R BT.2100-1 ·
`[2020]` = Recomendación UIT-R BT.2020-2 · `[709]` = Recomendación UIT-R BT.709-6 · `[of]` = oficio ·
`[plan]` = plantilla oficial.

**Siglas**: el códec de audio sin pérdida de Apple (**ALAC**, *Apple Lossless
Audio Codec*); el dispositivo de acoplamiento de carga (**CCD**) y el semiconductor complementario
de óxido metálico (**CMOS**); la función de transferencia optoelectrónica (**OETF**,
*opto-electronic transfer function*), la electroóptica (**EOTF**) y la optoóptica (**OOTF**); la
alta definición (**HD**) y la ultra alta definición (**UHD**); la Unión Internacional de
Telecomunicaciones (**UIT**, o **ITU** en su sigla inglesa, como la escribe uno de los enunciados),
cuyo sector de radiocomunicaciones (**UIT-R**) publica las recomendaciones **BT.601**, **BT.709**,
**BT.2020** y **BT.2100**; Unión Internacional de Telecomunicaciones (**UIT**, o **ITU** en su sigla
inglesa, como la escribe uno de los enunciados).

**Cabecera.** Enunciado: «2. Señales y formatos: cableado, señal analógica y digital, alta definición
· 3.5. Sistemas de grabación» · **12 preguntas** · **el ÚNICO cuadernillo del proyecto que cita una
recomendación de la UIT DENTRO del enunciado** · **una descansa sólo en la plantilla (71), porque
depende de una imagen**.

<!-- indice -->

## Índice

- [Las tres funciones de transferencia](#las-tres-funciones-de-transferencia)
- [Las gammas normalizadas](#las-gammas-normalizadas)
- [La profundidad de bits y la aparente contradicción](#la-profundidad-de-bits-y-la-aparente-contradicción)
- [El submuestreo cromático](#el-submuestreo-cromático)
- [Aspecto y luminancia en UHD](#aspecto-y-luminancia-en-uhd)
- [Nyquist](#nyquist)
- [Los instrumentos](#los-instrumentos)
- [El blanco y los tres voltajes](#el-blanco-y-los-tres-voltajes)
- [Las funciones del monitor y las señales de prueba](#las-funciones-del-monitor-y-las-señales-de-prueba)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las tres funciones de transferencia

- **PREGUNTA 25** · `[2100]` · **La OETF TRANSFORMA LA LUZ LINEAL DE LA ESCENA EN LA SEÑAL DE VÍDEO,
  NORMALMENTE EN EL INTERIOR DE UNA CÁMARA.**
- **ES LA PREGUNTA MEJOR CONSTRUIDA DEL CUADERNILLO**: **las CUATRO opciones salen del MISMO PÁRRAFO de
  la norma.** La Recomendación dice literalmente:
- `[2100]` · **«OETF: función de transferencia optoelectrónica, que transforma la luz lineal de la
  escena en la señal de vídeo, normalmente en el interior de una cámara.»**
- `[2100]` · **«EOTF: función de transferencia electroóptica, que transforma la señal de vídeo en la
  luz lineal de la pantalla.»**
- `[2100]` · **«OOTF: función de transferencia optoóptica que cumple el cometido de aplicar las
  "opciones de reproducción".»** Y añade: **«Estas funciones están relacionadas, por lo que solo dos de
  las tres son independientes.»**

| Función | De qué a qué | Dónde |
|---|---|---|
| **OETF** | **Óptico → eléctrico**: luz de la escena → señal | **EN LA CÁMARA** |
| **EOTF** | **Eléctrico → óptico**: señal → luz de la pantalla | **EN EL MONITOR** |
| **OOTF** | Óptico → óptico | **El resultado de las otras dos** |

- **LA MNEMOTECNIA**: **la PRIMERA letra dice de dónde se parte.** **OETF empieza por «O» de óptico, y
  la óptica es la escena: parte de la LUZ.** **EOTF empieza por «E»: parte de la SEÑAL.**
- **LA CUARTA OPCIÓN ES UNA INVERSIÓN INVENTADA**: «transforma la señal en luz lineal de la ESCENA»
  —cambia «pantalla» por «escena» en la definición de la EOTF—.
- **AVISO**: **el enunciado cita la EDICIÓN 2 y el temario se ha verificado contra la EDICIÓN 1.** **El
  párrafo coincide palabra por palabra con la respuesta oficial en la edición consultada.**

## Las gammas normalizadas

- **PREGUNTA 80** · **La gamma estándar en HD es R709.**
- **LAS FALSAS SON CURVAS DE FABRICANTE O INVENTADAS**: **«S709»** imita el aspecto de la Rec. 709
  **pero no es la norma** · **«HG1»** y **«G33»** **no designan ninguna gamma normalizada**.
- **LA DISTINCIÓN**: **una gamma NORMALIZADA la publica un organismo; una de FABRICANTE la publica una
  casa.** **La letra delante del número lo delata: «R» de recomendación frente a la inicial de la
  marca.**

## La profundidad de bits y la aparente contradicción

- **PREGUNTA 14** · **Al aumentar la profundidad de color se consiguen MÁS NIVELES DE BRILLO, MÁS GAMA
  DE COLORES, DEGRADADOS MÁS SUAVES y MÁS PESO de los archivos.** **Los cuatro efectos, y los cuatro
  ciertos.**
- **LAS TRES FALSAS AÑADEN «CONTRASTE» Y «RANGO DINÁMICO».**
- **PREGUNTA 94** · **Una mayor profundidad de bit AFECTA TANTO AL ESPACIO DE COLOR COMO AL MARGEN
  DINÁMICO.**
- **LA COSTURA QUE HAY QUE VER**: **la 14 descarta como falsas las opciones que dicen «rango dinámico»
  y la 94 dice que sí afecta.** **Las dos respuestas son correctas**, y se resuelve así:
- **LA PROFUNDIDAD NO CREA RANGO DINÁMICO: LO HACE UTILIZABLE.** **El rango lo determina el SENSOR.**
  **Pero un rango amplio codificado con pocos bits se rompe en escalones y deja de ser
  aprovechable.**
- **LA 14 PREGUNTA QUÉ SE *CONSIGUE*; LA 94, A QUÉ *AFECTA*.** **Quien no vea la diferencia entre los
  dos verbos falla una de las dos.**
- **Y LA TERCERA FALSA DE LA 94** hace depender el efecto del tipo de sensor —CCD frente a CMOS—:
  **falso, la profundidad de codificación es independiente de la tecnología del sensor.**

## El submuestreo cromático

- **PREGUNTA 18** · **REDUCE LA RESOLUCIÓN DE LOS COMPONENTES DE LA CROMINANCIA para disminuir el
  tamaño de los archivos sin pérdida significativa de calidad.**
- **POR QUÉ FUNCIONA**: **el ojo distingue mucho mejor los detalles de BRILLO que los de COLOR.**

| Notación | Qué guarda | Dónde |
|---|---|---|
| **4:4:4** | Una muestra de color por píxel | Grafismo, croma, cine |
| **4:2:2** | **La mitad en horizontal** | **El estándar de producción** |
| **4:2:0** | La mitad en horizontal **y en vertical** | Emisión y distribución |

- **LAS TRES FALSAS DICEN LO CONTRARIO**: «aumenta la crominancia» · «aumenta la luminancia» —**no toca
  la luminancia**— · **«aumenta la resolución de la crominancia DISMINUYENDO el tamaño»**, que **SE
  CONTRADICE A SÍ MISMA**: no se puede añadir información y bajar el peso a la vez.
- **AVISO DE OFICIO**: **el submuestreo limita lo que se puede hacer después.** **Un croma sobre 4:2:0
  recorta mal**, porque **el borde se calcula sobre información de color que no está.**

## Aspecto y luminancia en UHD

- **PREGUNTA 26** · **La relación de aspecto en UHD es 1:1,78 o 16/9.** `[2100]` · el **Cuadro 1** da
  como forma del contenedor **«16:9»**, con cómputos de **«7 680 × 4 320»**, **«3 840 × 2 160»** y
  **«1 920 × 1 080»**.
- **CÓMO SE CONTESTA SIN MEMORIZAR**: **16 ÷ 9 = 1,777…** **Las cuatro opciones dicen «16/9»: la que
  tenga el decimal correcto es la buena.** Falsas: **1,37** (formato académico) · **1,85** y **1,66**
  (panorámicos de proyección).
- **PREGUNTA 33** · `[2020]` · **La luminancia en UHD es Y = 0,2627 R + 0,6780 G + 0,0593 B.**

| Recomendación | Para qué | R | G | B |
|---|---|---|---|---|
| **BT.601** | Definición estándar | 0,299 | 0,587 | 0,114 |
| **BT.709** | Alta definición | 0,2126 | 0,7152 | 0,0722 |
| **BT.2020** | **Ultra alta definición** | **0,2627** | **0,6780** | **0,0593** |

- **LA FORMA DE DISTINGUIRLAS SIN MEMORIZAR NUEVE NÚMEROS**: **mírese el coeficiente del VERDE.**
  **0,587 = estándar · 0,7152 = alta · 0,6780 = ultra alta.**
- **LA FALSA MEJOR PUESTA SON LOS COEFICIENTES VERDADEROS DE LA BT.709.** Y **la de 0,2993/0,5872/0,1145
  SUMA 1,0010**: **ésa se cae sola**, porque **los tres coeficientes de cualquiera de las tres
  recomendaciones suman EXACTAMENTE UNO.**

## Nyquist

- **PREGUNTA 68** · **El principio de Nyquist recomienda muestrear AL MENOS DOS VECES LA FRECUENCIA MÁS
  ALTA de la señal.**
- **POR QUÉ EL DOBLE**: **hacen falta al menos dos muestras por ciclo**, una por semiciclo. **Con
  menos, aparece una frecuencia más baja que no estaba: el SOLAPAMIENTO.**
- **LAS TRES FALSAS SON CIFRAS DONDE EL ENUNCIADO PIDE UN PRINCIPIO**: **44 kHz** (el muestreo del
  disco compacto) · **3,58 MHz** (la subportadora de color de NTSC) · **4,43 MHz** (la de PAL). **Las
  dos últimas son las que un operador conoce de memoria, y por eso son tentadoras.**
- **SÓLO UNA OPCIÓN ENUNCIA UNA REGLA en lugar de dar un número.**

## Los instrumentos

- **PREGUNTA 41** · **Un vectorscopio mide la CROMINANCIA.**

| Instrumento | Qué mide | Qué se ve |
|---|---|---|
| **Monitor de forma de onda** | **La LUMINANCIA**, línea a línea | **Perfil del brillo**, con el pedestal de negros abajo |
| **Vectorscopio** | **La CROMINANCIA** | **Diagrama polar**: **ángulo = TONO, distancia al centro = SATURACIÓN** |

- **EL CENTRO ES LA AUSENCIA DE COLOR**: **una imagen en blanco y negro es un punto en el centro; una
  con dominante, un punto desplazado hacia el color de la dominante.**
- **LAS DOS FALSAS DE IMPEDANCIA** miden **una propiedad eléctrica del circuito**, no de la imagen. **Y
  la de LUMINANCIA es la trampa buena**: es lo que mide el otro instrumento de la pareja.
- **LA REGLA**: **la forma de onda dice si la EXPOSICIÓN está bien; el vectorscopio, si el COLOR está
  bien.**

## El blanco y los tres voltajes

- **PREGUNTA 97** · **Con una superficie blanca sin dominante y un voltio de negro a blanco: R = 0,30 v
  · G = 0,59 v · B = 0,11 v.**
- **DE DÓNDE SALEN**: **son los coeficientes de la BT.601 —0,299 / 0,587 / 0,114— REDONDEADOS.** **Su
  suma es exactamente UNO**, y por eso suman el voltio.
- **EL RAZONAMIENTO**: blanco sin dominante → **los tres primarios al máximo** · la luminancia es una
  **media PONDERADA** → **la contribución de cada canal es su coeficiente en voltios**.
- **LO QUE LA PREGUNTA ENSEÑA**: **el verde aporta casi el 60 % del brillo percibido, el rojo el 30 % y
  el azul apenas el 11 %.** **Por eso un error en el azul se nota mucho menos**, y **por eso el
  submuestreo cromático es posible.**
- **LA TRAMPA MEJOR PUESTA ES 0,33 / 0,33 / 0,33**, porque **es la respuesta intuitiva**: si el blanco
  son los tres a la vez, parece que deberían pesar igual. **Lo que la descarta es saber que la
  luminancia NO es una media, es una media PONDERADA.**
- **AVISO**: **el enunciado usa los coeficientes de la DEFINICIÓN ESTÁNDAR redondeados.** Con los de
  alta definición serían **0,21 / 0,72 / 0,07**, y con los de UHD, **0,26 / 0,68 / 0,06**.

## Las funciones del monitor y las señales de prueba

- **PREGUNTA 74** · **La función que NO es de monitores profesionales es ALAC**: **es un códec de audio
  sin pérdida.** **Se descarta POR CATEGORÍA.**

| Función | Qué hace |
|---|---|
| ***Blue Only*** | **Sólo el canal azul en blanco y negro**: ajuste de croma y fase, y **ver el ruido** |
| ***Underscan*** | **La imagen COMPLETA, con los bordes** que un monitor normal recorta |
| ***PiP*** | **Dos fuentes a la vez**, para comparar |

- **PREGUNTA 71** · `[plan]` · **La imagen corresponde a una SEÑAL TEST DIENTE DE SIERRA.**

| Señal de prueba | Qué dibuja en el monitor de forma de onda | Para qué |
|---|---|---|
| **Barras de color** | Escalones | Croma, fase y nivel |
| **Rampa / DIENTE DE SIERRA** | **UNA DIAGONAL RECTA** | **Comprobar la LINEALIDAD** |
| **Multiburst** | Grupos de frecuencias | Respuesta en frecuencia |

- **DECLARACIÓN**: **el enunciado depende ENTERAMENTE de una imagen**, que no se puede reproducir ni
  contrastar. **La respuesta descansa en la plantilla.** **Lo que el tema sostiene es qué dibuja cada
  señal**: **la rampa dibuja una diagonal recta, y ninguna otra opción dibuja eso.**
- **Y LA CUARTA OPCIÓN NO EXISTE**: **«señal test de corrección de *bokeh*»**: **el *bokeh* es el
  aspecto del desenfoque de un objetivo y no se corrige con una señal de prueba.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 14 | Qué se obtiene al aumentar la profundidad de color | c) Más niveles, más gama, degradados suaves, más peso ✔ |
| 18 | Qué es el submuestreo cromático | d) Reduce la resolución de la crominancia ✔ |
| 25 | Qué función realiza la OETF | d) Luz de la escena → señal de vídeo ✔ |
| 26 | Relación de aspecto en UHD | a) 1:1,78 o 16/9 ✔ |
| 33 | Luminancia en vídeo UHD | d) 0,2627 / 0,6780 / 0,0593 ✔ |
| 41 | Para qué sirve un vectorscopio | b) Medir la crominancia ✔ |
| 68 | Qué recomienda Nyquist | b) Al menos el doble de la frecuencia más alta ✔ |
| 71 | Qué señal de prueba muestra la imagen | a) Diente de sierra ✔ **·** sólo con la plantilla |
| 74 | Qué función NO es de monitores profesionales | a) ALAC ✔ |
| 80 | Gamma estándar en HD | a) R709 ✔ |
| 94 | Si la profundidad de bit afecta al color y al rango | d) A los dos ✔ |
| 97 | Voltajes de R, G y B para el blanco | a) 0,30 / 0,59 / 0,11 ✔ |

**Las doce oficiales son correctas y una descansa sólo en la plantilla.** · **Aviso de estudio**: **la
25 tiene las cuatro opciones sacadas del mismo párrafo de la norma** · **la 26 se resuelve con una
DIVISIÓN** · **la 33 usa como distractor los coeficientes VERDADEROS de la alta definición.** ·
**Aviso sobre la 14 y la 94**: **una pregunta qué se *consigue* y la otra a qué *afecta*.** **Las dos
respuestas son correctas.**
