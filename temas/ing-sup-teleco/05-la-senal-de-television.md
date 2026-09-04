# Tema 5 del específico de Ingeniería Superior · Telecomunicación · La señal de televisión: conceptos, características y parámetros

Las siglas y símbolos de este tema, presentados de entrada: la luminancia (**Y**) y las dos diferencias
de color (**R-Y** y **B-Y**), que digitalizadas se llaman **Cb** y **Cr**; los cuadros por segundo
(**c/s**) y los campos por segundo; el hercio (**Hz**); el milisegundo (**ms**); el bit por segundo
(**bit/s**) con sus múltiplos **Mbit/s** y **Gbit/s**; el borrado vertical (**VBI**, *vertical blanking
interval*) y el horizontal; la interfaz digital en serie (**SDI**); la relación de aspecto (**AR**); el
código de tiempo (**TC**, *timecode*); la señal de sincronismo de tres niveles (**trilevel**) y la de
banda base (**black burst**); y la señal de referencia de audio digital (**word clock**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 5):
> «La señal de televisión. Conceptos, características y parámetros.»

**Seis palabras, y detrás el punto que sostiene la mitad del anexo**: **los temas 6, 7, 8, 11, 12, 13,
15 y 19 hablan de qué se le hace a esta señal, y éste dice qué ES.**

**Y la idea que ordena el punto entero, dicha antes de ningún parámetro**: **una señal de televisión no
es una imagen: es una imagen ANALIZADA, es decir, convertida en una secuencia ordenada de valores en el
tiempo.** **Todo lo demás —el sincronismo, el borrado, el entrelazado, el muestreo— existe para que el
receptor pueda deshacer ese análisis y volver a montar la imagen en el sitio y en el instante
correctos.**

<!-- indice -->
<!-- /indice -->

## 1. El análisis de la imagen

**Los cuatro conceptos de partida, en el orden en que se construyen:**

| Concepto | Qué es |
|---|---|
| **EXPLORACIÓN o barrido** | **Recorrer la imagen punto a punto y línea a línea**, convirtiéndola en una sucesión de valores |
| **LÍNEA** | **Un recorrido horizontal completo** |
| **CUADRO o imagen** | **El conjunto de líneas que forman una imagen entera** |
| **CAMPO** | **La mitad de las líneas de un cuadro**, en el barrido entrelazado |

**Los dos tipos de barrido, con lo que los distingue:**

| | **PROGRESIVO** | **ENTRELAZADO** |
|---|---|---|
| **Cómo recorre** | **Todas las líneas en orden**, de arriba abajo | **Primero las impares y después las pares**, en dos campos |
| **Qué manda por cuadro** | **Un cuadro entero** | **Dos campos, medio cuadro cada uno** |
| **Ancho de banda a igual cadencia** | **El doble** | **La mitad** |
| **Qué gana** | **Nitidez en el movimiento y en el detalle vertical** | **Ancho de banda**: es un truco de compresión anterior a la compresión |
| **Qué pierde** | Nada, salvo ancho de banda | **Artefactos con el movimiento**: peine, parpadeo de línea |

**Y la lectura histórica que hay que saber dar, porque explica por qué el entrelazado sigue existiendo**:
**el entrelazado se inventó para engañar al ojo con la mitad de información.** **Refresca la pantalla
al doble de frecuencia de la que manda imágenes completas**, y **así evita el parpadeo sin doblar el
ancho de banda.** **Era un compromiso genial cuando el ancho de banda era el problema**, y **hoy es una
herencia que complica todo lo que se hace después**: **comprimir, escalar, convertir de norma y
congelar un cuadro son más difíciles con material entrelazado.**

**Cómo se nombra un formato**, que es la notación que hay que saber leer:

| Notación | Qué dice |
|---|---|
| **1080i50** | **1080 líneas activas**, **entrelazado**, **50 CAMPOS por segundo** —es decir, 25 cuadros— |
| **1080p25** | **1080 líneas**, **progresivo**, **25 CUADROS por segundo** |
| **1080p50** | **1080 líneas**, **progresivo**, **50 CUADROS por segundo** |
| **2160p50** | **2160 líneas**, **progresivo**, **50 cuadros** |

**La trampa de esa notación, y es de las que un examen persigue**: **la cifra que va detrás de la letra
NO significa lo mismo en las dos.** **En entrelazado son CAMPOS; en progresivo son CUADROS.** **Por eso
1080i50 y 1080p25 mandan el mismo número de imágenes completas por segundo** —veinticinco— **y ocupan
aproximadamente el mismo ancho de banda**, mientras que **1080p50 ocupa el doble.**

## 2. Las dos familias de cadencia, y por qué

**El mundo tiene dos normas de cadencia y su origen es la red eléctrica**, no la imagen:

| Familia | Cadencia | Dónde |
|---|---|---|
| **De 50** | **50 campos o 25 cuadros por segundo**, y sus derivados de 50 progresivos | **Europa y buena parte del mundo** |
| **De 60** | **60 campos o 30 cuadros**, con la variante de 59,94 | **América y Japón** |

**Por qué la red eléctrica, que es la explicación que hay que saber dar**: **cuando la iluminación de
un plató parpadea a la frecuencia de la red y la cámara explora a otra cadencia, aparece una banda que
recorre la imagen.** **Sincronizar la cadencia con la red elimina ese batido**, y **de ahí que donde la
red va a cincuenta hercios la televisión vaya a cincuenta campos, y donde va a sesenta, a sesenta.**

**La consecuencia práctica que un examen pregunta directamente**: **una señal que llega de América es,
con mucha mayor probabilidad, de la familia de sesenta.** **Ante cuatro opciones que mezclan las dos
familias, la de sesenta es la que corresponde**, y **la conversión de norma —de una familia a la otra—
es una de las operaciones más delicadas de un centro de intercambio**, porque **no hay un número entero
de cuadros de una en la otra.**

**Y la variante de 59,94, que hay que saber por qué existe**: **es la de sesenta bajada en una parte por
mil**, y **procede de la introducción del color en un sistema que ya emitía en blanco y negro**: hubo
que desplazar ligeramente la cadencia para que la subportadora de color no batiera con el sonido.
**Su herencia es el código de tiempo con salto de cuadro**, que **descarta números de cuadro —no
cuadros— para que el reloj del código no se aleje del reloj de pared.**

## 3. La señal en el tiempo: sincronismo y borrado

**Una línea de imagen no es sólo imagen.** **La estructura temporal, que hay que saber enumerar:**

| Parte | Qué es |
|---|---|
| **Línea ACTIVA** | **La parte que contiene imagen** |
| **BORRADO HORIZONTAL** | **El hueco entre el final de una línea y el principio de la siguiente** |
| **BORRADO VERTICAL** | **El hueco entre el final de una imagen y el principio de la siguiente** |
| **SINCRONISMO horizontal y vertical** | **Las marcas que dicen dónde empieza cada línea y cada imagen** |

**Para qué siguen existiendo los borrados en digital, que es la pregunta conceptual del epígrafe**:
**en analógico servían para dar tiempo al haz a volver.** **En digital no hay haz que vuelva, y sin
embargo el borrado se conserva**, por dos razones: **compatibilidad de estructura** y, sobre todo,
**porque es donde caben los datos auxiliares.** **En el borrado de una señal digital viajan el audio
embebido, el código de tiempo, los subtítulos y los metadatos**, y **eso convierte lo que era un hueco
en el canal de servicio de la señal.**

**Las referencias de sincronismo de una instalación, que hay que saber nombrar y no confundir:**

| Referencia | Para qué |
|---|---|
| **Señal de negro con ráfaga de color** | **La referencia clásica de definición estándar**, que sigue distribuyéndose |
| **Sincronismo de TRES NIVELES** | **La referencia de alta definición**: su flanco es simétrico y se detecta con más precisión |
| **Reloj de palabra** | **La referencia de AUDIO digital**: marca la frecuencia de muestreo |
| **Referencia de PRECISIÓN por red** | **La referencia de una instalación sobre red de paquetes**, que se estudia en el tema 19 |

**Y la regla de instalación que ordena las cuatro**: **una instalación tiene UNA sola referencia
maestra y todo lo demás se engancha a ella.** **Dos referencias independientes en el mismo centro
producen deslizamiento**, y **el deslizamiento se ve como un salto de imagen o se oye como un clic.**

## 4. El color

**Tres componentes, y hay que saber por qué no se transmiten los tres colores primarios:**

| Representación | Qué lleva |
|---|---|
| **Rojo, verde y azul** | **Los tres primarios**: es como capta el sensor y como muestra la pantalla |
| **Luminancia y dos diferencias de color** | **El brillo por un lado y el color por otro** |

**Las dos razones de la segunda, y son las que hay que saber decir:**

1. **COMPATIBILIDAD.** **Un receptor de blanco y negro sólo necesita la luminancia**, y **la
   transmisión en luminancia más diferencias permitió que el color no rompiera lo que ya había.**
2. **ECONOMÍA.** **El ojo distingue mucho menos detalle en el color que en el brillo**, así que **las
   diferencias de color se pueden transmitir con menos resolución sin que se note.** **Eso es el
   submuestreo, y es el epígrafe siguiente.**

**Los parámetros del color que hay que manejar:**

| Parámetro | Qué es |
|---|---|
| **ESPACIO DE COLOR o gama** | **Qué colores puede representar el sistema** |
| **FUNCIÓN DE TRANSFERENCIA** | **Cómo se reparten los valores digitales entre lo oscuro y lo claro** |
| **PROFUNDIDAD DE BITS** | **Cuántos escalones tiene cada componente** |
| **NIVELES de referencia** | **Qué valor digital es el negro y cuál el blanco**: el margen legal frente al margen completo |

**Y el aviso que un examen premia sobre el último**: **en televisión el negro y el blanco NO son el
cero y el máximo del código.** **Se dejan márgenes por arriba y por abajo**, y **por eso una señal
tratada como si fuera de margen completo sale con los negros aplastados y los blancos quemados.** **Es
el error de conversión más frecuente entre el mundo de la televisión y el de la informática.**

## 5. El submuestreo de color

**El parámetro más preguntable del punto**, y **hay que saber leer su notación de tres cifras.**

**Qué significa cada cifra**: **la primera es la referencia de muestreo de luminancia; la segunda,
cuántas muestras de crominancia hay por línea respecto a esa referencia; y la tercera, si en la línea
siguiente vuelve a haber muestras de crominancia o no.**

| Estructura | Qué hace |
|---|---|
| **4:4:4** | **Sin submuestreo**: tantas muestras de color como de brillo |
| **4:2:2** | **Mitad de muestras de color en HORIZONTAL**, todas las líneas |
| **4:2:0** | **Mitad en horizontal Y mitad en vertical**: la crominancia se muestrea en líneas alternas |
| **4:1:1** | **Un cuarto en horizontal**, todas las líneas |

**Y la cuenta que un examen pide hacer, con la regla que la resuelve**: **en 4:2:0, por cada cien
muestras de luminancia de la imagen ENTERA, cada componente de diferencia de color tiene VEINTICINCO.**
**La razón es que se divide por dos en horizontal y por dos en vertical**, es decir **por cuatro**, y
**la cuenta hay que hacerla sobre la imagen entera y no sobre una línea suelta**, que es donde está la
trampa: **quien piense sólo en horizontal contesta cincuenta.**

**Y las tres reglas de oficio del epígrafe:**

1. **Cada escalón de submuestreo se paga en el tratamiento posterior.** **Una incrustación por color
   sobre material 4:2:0 tiene los bordes sucios**, y **por eso el croma se rueda al menos en 4:2:2 y
   preferiblemente en 4:4:4.**
2. **El submuestreo NO se recupera.** **Convertir 4:2:0 a 4:4:4 interpola: inventa lo que no está.**
3. **La cadena vale lo que su eslabón más pobre.** **Grabar en 4:4:4 y emitir por un enlace 4:2:0 no
   mejora la emisión**, aunque **sí mejora todo lo que se haga antes de ese enlace.**

## 6. Los regímenes binarios y el cálculo del retardo

**Cuánto ocupa una señal de televisión sin comprimir, que es una cuenta que un ingeniero tiene que
saber plantear**: **muestras por línea, por líneas por imagen, por imágenes por segundo, por bits por
muestra, por número de componentes.** **De ahí salen los regímenes de las interfaces del tema 3**, y
**la razón de que cada salto de formato multiplique el ancho de banda.**

**Los órdenes de magnitud que el propio cuadernillo de esta ocupación confirma en su plantilla:**

| Formato | Interfaz | Régimen aproximado |
|---|---|---|
| **Definición estándar** | **Serie de definición estándar** | **270 Mbit/s** |
| **1080i50** | **Alta definición** | **1,5 Gbit/s** |
| **1080p50** | **3 gigabits** | **3 Gbit/s** |
| **2160p50 por un solo enlace** | **12 gigabits** | **12 Gbit/s** |

**Y la cuenta de PÍXELES entre formatos, que es la otra pregunta de aritmética del punto**: **una
imagen de 2160 líneas tiene el doble de líneas y el doble de columnas que una de 1080**, así que
**CUATRO veces más píxeles por cuadro.** **La cadencia no entra en esa cuenta**: **la pregunta es por
cuadro**, y **quien mezcle la cadencia con la resolución contesta ocho o dieciséis.**

**El cálculo del RETARDO en milisegundos, que es la tercera cuenta y la más práctica**: **un cuadro
dura el inverso de la cadencia de cuadros.**

| Cadencia | Duración de un cuadro |
|---|---|
| **25 cuadros por segundo** | **40 ms** |
| **50 cuadros por segundo** | **20 ms** |
| **30 cuadros por segundo** | **33,3 ms** |

**Aplicado a un desajuste de audio y vídeo**: **cinco cuadros de retraso en una señal de cincuenta
cuadros por segundo son CIEN milisegundos.** **La regla es cuadros por duración de cuadro**, y **la
duración de cuadro sale de la cadencia de CUADROS, no de campos.** **Ése es el punto donde se falla:
en una señal entrelazada de cincuenta campos, el cuadro dura cuarenta milisegundos y no veinte.**

**Y por qué importa el desajuste, que es la lectura de oficio**: **el oído tolera mucho peor el audio
ADELANTADO que el retrasado.** **En la naturaleza el sonido siempre llega después de la imagen**, así
que **un retraso pequeño resulta natural y un adelanto, no.** **Por eso las tolerancias de las
recomendaciones no son simétricas**, y **el temario no las reproduce porque no las ha leído en su
fuente.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ninguna cifra de líneas totales frente a activas, ningún número de muestras por
   línea, ninguna duración de borrado, ningún nivel digital de negro y de blanco y ninguna tolerancia
   de desajuste entre audio y vídeo.** **Son dato de recomendación de la Unión Internacional de
   Telecomunicaciones y de norma de la Sociedad de Ingenieros de Cine y Televisión**, y **una cifra
   que no se ha leído en su fuente no se escribe.** **Lo que el temario da es qué parámetro decide
   qué.**
2. **Los cuatro regímenes binarios del epígrafe 6 son los que el propio cuadernillo de esta ocupación
   pone en las opciones de sus preguntas 23 y 84**, y **la plantilla oficial confirma cuál es el que
   corresponde a la alta definición.** **El temario declara esa procedencia.**
3. **Las cadencias de cincuenta y de sesenta se dan como familias y con su origen en la frecuencia de
   la red**, que **es explicación histórica de dominio común**: **el temario no la atribuye a ninguna
   fuente.** **La cifra de 59,94 se da como «sesenta bajada en una parte por mil»**, que es su
   definición, **y no como un valor medido.**
4. **La notación de submuestreo se explica por lo que significa cada cifra**, y **el temario no afirma
   que exista una norma que la fije**, porque **no se ha consultado ninguna.** **La cuenta de las
   veinticinco muestras por cada cien de luminancia es aritmética** y **la plantilla oficial de la
   pregunta 24 la confirma.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la
   codificación y la compresión, al tema 6**; **los estándares de alta y ultraalta definición, al tema
   8**; **los instrumentos que miden estos parámetros, al tema 12**; **la referencia de precisión por
   red, al tema 19**; **y las interfaces con su régimen binario, al tema 3.**

**El resto del tema va como oficio y así se declara**: la idea de que una señal de televisión es una
imagen analizada y de que todo lo demás existe para deshacer ese análisis, la lectura del entrelazado
como un truco de compresión anterior a la compresión y como una herencia que complica lo que viene
después, la advertencia de que la cifra de la notación significa campos en un caso y cuadros en el
otro, la explicación de por qué la cadencia viene de la red eléctrica, la observación de que una señal
de América es con mucha probabilidad de la familia de sesenta, la explicación del origen del 59,94 y
del código de tiempo con salto de cuadro, la lectura del borrado digital como canal de servicio de la
señal, la regla de una sola referencia maestra por instalación, las dos razones de transmitir
luminancia y diferencias, el aviso sobre el margen legal frente al completo, la regla de que la cuenta
del submuestreo se hace sobre la imagen entera, las tres reglas de oficio del submuestreo, la cuenta de
píxeles entre formatos con la advertencia de no mezclar la cadencia, la regla de calcular el retardo
con la duración de cuadro y no de campo, y la observación de que el oído tolera peor el audio
adelantado. **Nada de eso está en un boletín oficial ni en ninguna fuente consultada para este
proyecto**, y el tema no lo presenta como si lo estuviera.
