# Tema 8 del específico de Ingeniería Superior · Telecomunicación · Alta y ultraalta definición: estándares de producción e intercambio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 8 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son las normas técnicas de interfaz, color y rango dinámico, **tras muro de pago**, así que **va como oficio**; de ellas **sólo se recoge lo que la plantilla confirma** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Segundo banco** | **Once preguntas.** Y **la ultraalta definición no se define por el número de píxeles**: el rango dinámico y la gama de color aportan más a igual tasa |
| **Extensión** | **2.951 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la alta definición (**HD**) y la ultraalta
definición (**UHD**), con sus dos escalones (**UHD/4K** y **UHD2/8K**); la interfaz digital en serie
(**SDI**) en sus grados (**HD-SDI**, **3G-SDI**, **6G-SDI** y **12G-SDI**); el alto rango dinámico
(**HDR**) y el rango dinámico estándar (**SDR**); la gama amplia de color (**WCG**, *wide colour
gamut*); el cuantificador perceptual (**PQ**) y la gamma logarítmica híbrida (**HLG**); la tabla de
consulta de color (**LUT**, *look-up table*); la Sociedad de Ingenieros de Cine y Televisión
(**SMPTE**), la Unión Internacional de Telecomunicaciones (**ITU**) y la Unión Europea de Radiodifusión
(**EBU**); la división en cuadrantes (**SQD**, *square division*) y el entrelazado de dos muestras
(**2SI**, *two sample interleave*); el gigabit por segundo (**Gbit/s**); y la candela por metro
cuadrado (**cd/m²**), unidad de luminancia.

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 8):
> «Televisión de alta definición HD. Ultra alta definición (UHD/4K, UHD2/8K). Estándares de producción
> e intercambio de contenidos en Alta Definición. Normas SMPTE, ITU y EBU.»

**Es el punto que más preguntas ha dado de toda la ocupación —once de las ochenta y seis del
específico— y el único cuyo enunciado NOMBRA organismos de normalización.**

**Y eso obliga a un aviso de método que va aquí y no en la trazabilidad, porque condiciona cómo se lee
el tema entero**: **las normas de esos tres organismos no son legislación y no están en el Boletín
Oficial del Estado.** **Este proyecto no las ha comprado ni consultado**, así que **cuando este tema
identifica una norma por su número lo hace porque el propio cuadernillo de esta ocupación la nombra y
su plantilla oficial confirma cuál es la que corresponde**, y **eso va dicho cada vez.** **Lo que el
temario no hace nunca es describir el contenido de una norma que no ha leído.**

**Y la idea que ordena el punto**: **la ultraalta definición NO es «más píxeles».** **Son cuatro cosas a
la vez** —**más resolución, más rango dinámico, más gama de color y más profundidad de bits**— **y las
tres últimas se notan más que la primera.**

<!-- indice -->

## Índice

- [1. Los formatos y su aritmética](#1-los-formatos-y-su-aritmética)
- [2. Las interfaces](#2-las-interfaces)
- [3. Llevar ultraalta definición por cuatro enlaces](#3-llevar-ultraalta-definición-por-cuatro-enlaces)
- [4. El rango dinámico y la gama de color](#4-el-rango-dinámico-y-la-gama-de-color)
- [5. Las tablas de consulta de color](#5-las-tablas-de-consulta-de-color)
- [6. El intercambio de material](#6-el-intercambio-de-material)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Los formatos y su aritmética

**La escalera de resoluciones, con la cuenta que un examen pide:**

| Formato | Rejilla | Respecto al anterior |
|---|---|---|
| **Alta definición** | **1920 × 1080** | — |
| **Ultraalta definición, primer escalón** | **3840 × 2160** | **El doble de líneas y el doble de columnas: CUATRO veces más píxeles** |
| **Ultraalta definición, segundo escalón** | **7680 × 4320** | **Otras cuatro veces: dieciséis respecto a la alta definición** |

**La regla de la cuenta, y es donde se falla**: **la comparación de píxeles POR CUADRO no depende de la
cadencia.** **Una señal de 2160 líneas progresiva a cincuenta cuadros tiene cuatro veces más píxeles
por cuadro que una de 1080 entrelazada a cincuenta campos**, **no ocho ni dieciséis**: **la cadencia
cambia cuántos cuadros por segundo hay, no cuántos píxeles tiene cada uno.** **Quien mezcle las dos
cosas contesta ocho.**

**Y la nota sobre el vocabulario comercial, que hay que dar una vez**: **«4K» y «8K» son nombres del
cine y del mercado, no designaciones de formato de televisión.** **Los formatos de difusión son de 3840
y de 7680 columnas**, y **el 4K cinematográfico tiene 4096.** **En un pliego se escribe la rejilla, no
el apodo.**

## 2. Las interfaces

**Cada salto de formato multiplica el régimen binario, y por eso hay una escalera de interfaces:**

| Interfaz | Régimen aproximado | Para qué formato basta |
|---|---|---|
| **Definición estándar en serie** | **270 Mbit/s** | Definición estándar |
| **Alta definición en serie** | **1,5 Gbit/s** | **1080i50 y 1080p25** |
| **3 gigabits** | **3 Gbit/s** | **1080p50** |
| **6 gigabits** | **6 Gbit/s** | Ultraalta definición con submuestreo y cadencia moderados |
| **12 gigabits** | **12 Gbit/s** | **2160p50 por un solo cable** |

**La cifra que un examen pregunta directamente**: **una señal de alta definición 1080i50 sin comprimir
va a unos 1,5 gigabits por segundo.** **No 270 megabits, que es definición estándar; ni 3 gigabits, que
es el doble y corresponde a 1080p50.**

**Y las normas que identifican esas interfaces**, con **la procedencia declarada**: **el propio
cuadernillo de esta ocupación pregunta cuál define la interfaz de seis gigabits, y su plantilla oficial
responde `SMPTE ST 2081-1`.** **Este temario lo recoge como dato confirmado por la plantilla**, y
**añade la regla que lo hace memorizable**: **la serie 2081 es la de seis gigabits y la 2082, la de
doce.** **Del contenido de ninguna de las dos se afirma nada más.**

**El mapeado de la interfaz de tres gigabits**, que es la otra pregunta de norma: **el cuadernillo
pregunta qué formatos de mapeado define `SMPTE ST 425-1`, y su plantilla confirma que son TRES**:
**nivel A, nivel B de enlace doble y nivel B de flujo doble.** **Ni dos ni cuatro.** **La lectura de
oficio que hay que añadir**: **el nivel A lleva la señal como un flujo único a tres gigabits, y los de
nivel B la llevan como dos flujos de alta definición multiplexados**, lo que **permite compatibilidad
con equipamiento anterior.**

## 3. Llevar ultraalta definición por cuatro enlaces

**Antes de que existiera la interfaz de doce gigabits, una señal de ultraalta definición se llevaba por
CUATRO enlaces de tres gigabits**, y **hay dos maneras de repartirla que un examen distingue:**

| Método | Cómo reparte | Qué lleva cada uno de los cuatro |
|---|---|---|
| **División en CUADRANTES** | **Parte la imagen en cuatro trozos**, arriba-izquierda, arriba-derecha, abajo-izquierda y abajo-derecha | **Un cuarto de la imagen**: un cuadrante |
| **ENTRELAZADO DE DOS MUESTRAS** | **Toma muestras alternas en horizontal y en vertical** | **Una imagen COMPLETA submuestreada**, es decir **una copia en alta definición de toda la escena** |

**Y la consecuencia práctica que es la pregunta**: **si se quiere obtener una copia en alta definición
de la señal en cada uno de los cuatro enlaces, SIN equipamiento adicional, el método es el entrelazado
de dos muestras.** **Con división en cuadrantes cada enlace lleva sólo un trozo de la imagen**, así que
**para ver la escena entera hace falta recomponer los cuatro.**

**Las dos observaciones de oficio del epígrafe:**

1. **Con cuatro enlaces hay que vigilar el DESFASE entre ellos.** **Cuatro cables de distinta longitud
   llegan en instantes distintos**, y **el receptor tiene que alinearlos.** **Es una fuente de averías
   que no existe con un solo cable de doce gigabits.**
2. **Distribuir ultraalta definición por cuadrantes multiplica el equipamiento.** **Cada señal que
   haya que repartir a tres destinos necesita CUATRO distribuidores, uno por cuadrante**, y **cada uno
   con al menos tres salidas.** **Ésa es la aritmética que un examen plantea como problema de sala.**

## 4. El rango dinámico y la gama de color

**Aquí está lo que de verdad distingue a la ultraalta definición**, y **hay que separar tres cosas que
se confunden:**

| Concepto | Qué es |
|---|---|
| **RESOLUCIÓN** | **Cuántos píxeles hay** |
| **GAMA DE COLOR** | **Qué colores se pueden representar**: cuán saturados llegan a ser |
| **RANGO DINÁMICO** | **Cuánta distancia hay entre el negro más oscuro y el blanco más brillante** |

**Las dos funciones de transferencia del alto rango dinámico**, que es la pregunta más repetida del
punto:

| | **Cuantificador perceptual** | **Gamma logarítmica híbrida** |
|---|---|---|
| **Cómo define el brillo** | **En valores ABSOLUTOS de luminancia**: un código es una cantidad de luz | **En valores RELATIVOS**, como toda la televisión anterior |
| **De dónde viene** | Del cine y del dominio del máster | **De la radiodifusión** |
| **Compatibilidad con equipos de rango estándar** | **Poca**: en un monitor de rango estándar se ve mal | **ALTA**: la parte baja de su curva es prácticamente la de siempre |
| **Dónde encaja mejor** | **Producción controlada**, con máster y monitorado calibrado | **DIRECTO**, donde hay que servir a los dos mundos a la vez |

**Y la respuesta razonada a la pregunta del directo**: **en una retransmisión deportiva en ultraalta
definición con alto rango dinámico, la ventaja principal de la gamma logarítmica híbrida frente al
cuantificador perceptual es la COMPATIBILIDAD SIMULTÁNEA en el monitorado**, es decir, **que el mismo
flujo sirve para equipos que ven alto rango dinámico y para los que ven rango estándar**, con gama
amplia y al menos diez bits de procesado. **No es que comprima más ni que use ondículas** —la función
de transferencia no comprime nada—, **ni que dé más profundidad de color** —eso es otro parámetro—,
**ni que el cuantificador perceptual esté limitado a la ultraalta definición.**

**La función de transferencia del cuantificador perceptual está identificada en el cuadernillo**, y
**su plantilla confirma que la norma que la define es `SMPTE ST 2084`.** **Se recoge como dato
confirmado por la plantilla**, con **la advertencia de que la recomendación que define la gama amplia
de color es otra cosa y otro organismo**: **confundir la función de transferencia con el espacio de
color es el error que esa pregunta busca.**

**Las dos recomendaciones de la Unión Internacional de Telecomunicaciones que el cuadernillo nombra**,
con lo que su plantilla confirma de cada una:

| Recomendación | Qué confirma la plantilla |
|---|---|
| **`ITU-R BT.2020`** | **Su profundidad de bits máxima por componente es de DOCE bits** |
| **`ITU-R BT.2100`** | **NO define ningún formato ENTRELAZADO** —sólo progresivos— y **NO define ningún espacio de color para rango estándar** |

**Y las dos lecturas que hay que sacar, porque son las que un examen premia:**

1. **La ultraalta definición nace PROGRESIVA.** **El entrelazado es una herencia de la alta definición
   y hacia atrás**, y **la recomendación del alto rango dinámico no lo contempla.** **Por eso, entre
   cuatro formatos, el entrelazado es el que no está definido.**
2. **La recomendación del alto rango dinámico es de ALTO RANGO DINÁMICO.** **Para rango estándar no
   define ningún espacio de color, porque no es lo suyo**: **eso está en las recomendaciones
   anteriores.** **La respuesta es «ninguno», y las otras tres opciones ofrecen espacios de color que
   existen pero que esa recomendación no define para ese caso.**

## 5. Las tablas de consulta de color

**Qué es una tabla de consulta**: **una correspondencia que, para cada valor de entrada, da un valor de
salida.** **Aplicada a color, transforma una imagen de un espacio o de una curva a otra.**

**Para qué se usa en un centro de producción:**

| Uso | Qué hace |
|---|---|
| **Conversión de alto rango dinámico a rango estándar y al revés** | **Es su uso característico**, y **el que un examen pregunta** |
| **Conversión entre gamas de color** | Adaptar material de una cámara a la paleta del programa |
| **Monitorado** | **Ver en un monitor de rango estándar lo que se está grabando en alto rango** |
| **Etalonaje** | Aplicar una intención estética repetible |

**Y las dos cosas que una tabla de consulta NO hace**, porque son las opciones falsas de esa pregunta:
**no convierte una norma de sesenta a una de cincuenta** —eso es conversión de norma, y es
interpolación temporal— **ni convierte de progresivo a entrelazado** —eso es un desentrelazador o un
entrelazador— **ni cambia la relación de aspecto.** **Una tabla de consulta trabaja sobre el VALOR de
cada píxel, no sobre el tiempo ni sobre la geometría.**

**Y el aviso de oficio que hay que dar sobre su uso**: **una conversión de alto rango a rango estándar
con tabla de consulta es una decisión creativa disfrazada de operación técnica.** **Hay muchas maneras
de comprimir el rango y ninguna es neutra**, así que **la tabla se elige, se aprueba y se documenta**,
y **se aplica siempre la misma en toda la producción.**

## 6. El intercambio de material

**Lo que el enunciado llama «estándares de producción e intercambio»**, y **lo que un centro tiene que
pactar antes de recibir un fichero:**

| Qué se pacta | Por qué |
|---|---|
| **CONTENEDOR y su variante de empaquetado** | **Decide si el fichero es autocontenido o viene con material y metadatos aparte** |
| **CÓDEC y su tasa** | Decide la calidad y si se puede editar directamente |
| **Estructura de MUESTREO y profundidad de bits** | 4:2:2, 4:2:0, diez o doce bits |
| **FUNCIÓN DE TRANSFERENCIA y espacio de color** | **Rango estándar o alto rango, y con qué curva** |
| **CADENCIA y barrido** | Y si hay que convertir de norma |
| **Configuración de las pistas de audio** | Cuántas, en qué orden y qué lleva cada una |
| **Código de tiempo y punto de inicio** | Para que el material encaje donde tiene que encajar |
| **METADATOS obligatorios** | Título, episodio, versión, subtítulos, audiodescripción |

**Y el orden correcto de una conversión, que el cuadernillo pregunta como problema y conviene razonar**:
**si hay que entregar en un formato de alta definición y rango estándar un material de ultraalta
definición con alto rango dinámico y códec de producción, hay TRES operaciones y su orden importa**:
**aplicar la tabla de consulta para pasar de alto rango a rango estándar**, **reducir la resolución a
alta definición** y **transcodificar al códec de entrega.**

**Por qué en ese orden, que es lo que hay que saber explicar**: **la conversión de rango se hace sobre
el material de más calidad**, porque **es donde más información hay para decidir**; **el escalado
después**, y **la transcodificación al final**, porque **es la operación que pierde y no conviene
arrastrar sus pérdidas por las anteriores.** **Y la opción que dice que no hace falta la tabla porque
el original tiene más información de color confunde tener información con saber qué hacer con ella**:
**un material de alto rango visto como rango estándar sin conversión sale lavado, no mejor.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Las normas que este punto nombra no son legislación y no están en el Boletín Oficial del Estado** |

**El aviso de método sobre este punto sin norma del boletín es el del tema 3**, con **el matiz que este
tema da en su cabecera y que hay que repetir aquí**: **el enunciado nombra tres organismos de
normalización, y sus normas no se han consultado.**

**Cinco declaraciones expresas:**

1. **Este tema identifica CINCO normas por su número** —`SMPTE ST 2081-1` para la interfaz de seis
   gigabits, `SMPTE ST 425-1` para el mapeado de tres gigabits, `SMPTE ST 2084` para el cuantificador
   perceptual, `ITU-R BT.2020` y `ITU-R BT.2100`—, **y las cinco proceden del cuadernillo de esta
   ocupación, confirmadas por su plantilla oficial en las preguntas 9, 13, 39, 61, 59 y 78.** **El
   temario declara esa procedencia y no afirma nada más del contenido de ninguna de ellas**: **no las
   ha leído.**
2. **Los cuatro datos que este tema atribuye a esas normas son exactamente los que la plantilla
   confirma**: **los tres mapeados de la interfaz de tres gigabits**, **los doce bits de profundidad
   máxima**, **la ausencia de formato entrelazado** y **la ausencia de espacio de color para rango
   estándar.** **Ningún otro.**
3. **Este tema NO da ninguna cifra de luminancia máxima, ninguna coordenada de primario de color,
   ninguna capacidad de canal y ningún número de niveles.** **Son dato de las normas que no se han
   consultado**, y **una cifra que no se ha leído en su fuente no se escribe.**
4. **Los regímenes binarios de las interfaces del epígrafe 2 son los que el propio cuadernillo pone en
   las opciones de sus preguntas 23 y 84**, con **la plantilla confirmando cuál corresponde a la alta
   definición.** **Se declara esa procedencia.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la señal y
   su submuestreo, al tema 5**; **la codificación y la compresión, al tema 6**; **el transporte de
   ultraalta definición por red, al tema 19**; **la medida y el monitorado, al tema 12**; **y el
   etalonaje, al tema 15.**

**El resto del tema va como oficio y así se declara**: la idea de que la ultraalta definición son
cuatro cosas a la vez y no sólo píxeles, la regla de que la cuenta de píxeles por cuadro no depende de
la cadencia, la nota sobre el vocabulario comercial frente a la rejilla, la regla mnemotécnica de que
la serie 2081 es la de seis gigabits y la 2082 la de doce, la lectura de que los niveles B permiten
compatibilidad con equipamiento anterior, la comparación entre los dos métodos de reparto por cuatro
enlaces con su consecuencia práctica, las dos observaciones sobre el desfase entre enlaces y sobre la
aritmética de los distribuidores, la separación entre resolución, gama y rango dinámico, la comparación
razonada entre las dos funciones de transferencia y el descarte de las tres opciones falsas, las dos
lecturas sobre por qué la ultraalta definición nace progresiva y por qué la recomendación de alto rango
no define espacio para rango estándar, las cuatro cosas que una tabla de consulta no hace, el aviso de
que una conversión de rango es una decisión creativa disfrazada de técnica, la lista de lo que se pacta
en un intercambio y el razonamiento del orden correcto de una conversión. **Nada de eso está en un
boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo presenta como si
lo estuviera.
