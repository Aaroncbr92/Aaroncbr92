# Tema 21 del específico de Ingeniería Superior · Telecomunicación · Sonido

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 23 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual**, para la regulación básica de la radiodifusión sonora. **El resto del punto va como oficio**: las normas técnicas de audio están tras muro de pago |
| **Identificador** | `BOE-A-2022-11311` · BOE núm. 163, de 08/07/2022 |
| **Redacción que se estudia** | La vigente el **21/12/2022**, que es la inicial. Se citan **los apartados 3 y 4 del artículo 76**, **el 77.1**, **el 78.2**, **el 80.4** y **el 83.3** |
| **Único punto con norma** | **Es el único del temario específico de esta ocupación que se apoya en el Boletín Oficial del Estado.** Su último enunciado pide la regulación básica de la radiodifusión sonora, que es el título IV de la ley |
| **Extensión** | **5.022 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: el hercio (**Hz**) y su múltiplo **kHz**;
el decibelio (**dB**) y el decibelio a escala plena (**dBFS**); el bit y el byte; la interfaz de audio
digital profesional de dos canales (**AES3**), conocida también por el nombre conjunto de las dos
asociaciones que la publicaron (**AES/EBU**); la interfaz digital multicanal de audio (**MADI**); el
conversor de frecuencia de muestreo (**SRC**); la modulación por impulsos codificados (**PCM**); y la
Ley General de Comunicación Audiovisual (**LGCA**), que es la Ley 13/2022, de 7 de julio.

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 23):
> «Sonido. Señales analógicas y digitales de audio. Medida y control de la señal. Formatos.
> Estándares. Equipos. Estándares de digitalización. Formato contenedor y códec de audio. Formatos de
> compresión. Transporte de la señal. Regulación básica de la radiodifusión sonora en España.»

**Este punto tiene dos mitades que no se parecen en nada** y **conviene saberlo antes de empezar**:
**nueve enunciados de técnica de sonido y uno de derecho.** **El último —la regulación básica de la
radiodifusión sonora en España— es el único de todo el temario específico de esta ocupación que se
apoya en una norma publicada en el Boletín Oficial del Estado**, y **por eso va citado literalmente,
con su identificador y su redacción, mientras el resto del tema va como oficio declarado.**

**Y la idea que ordena la parte técnica**: **el sonido es una magnitud física con tres atributos, y
casi todo lo que se pregunta consiste en saber cuál de los tres se está tocando.** **Quien confunde
intensidad con frecuencia falla la pregunta más fácil del cuadernillo, y quien confunde el nivel de una
señal con la impresión de volumen falla la más difícil.**

<!-- indice -->

## Índice

- [1. La señal de sonido y sus atributos](#1-la-señal-de-sonido-y-sus-atributos)
- [2. De la señal analógica a la digital](#2-de-la-señal-analógica-a-la-digital)
- [3. La interfaz digital profesional y sus bits de servicio](#3-la-interfaz-digital-profesional-y-sus-bits-de-servicio)
- [4. Medida y control de la señal](#4-medida-y-control-de-la-señal)
- [5. Los equipos: captación y escucha](#5-los-equipos-captación-y-escucha)
- [6. Formatos, contenedores, códecs y compresión](#6-formatos-contenedores-códecs-y-compresión)
- [7. El transporte de la señal](#7-el-transporte-de-la-señal)
- [8. La regulación básica de la radiodifusión sonora en España](#8-la-regulación-básica-de-la-radiodifusión-sonora-en-españa)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. La señal de sonido y sus atributos

**El sonido es una onda de presión que viaja por un medio elástico.** **De esa definición salen los
atributos con que se describe, y hay que saber cuál determina qué:**

| Atributo físico | Qué determina en la percepción |
|---|---|
| **Frecuencia** | **el tono o altura**: si el sonido es grave o agudo |
| **Amplitud o intensidad** | **la sonoridad**: si suena fuerte o flojo |
| **Composición armónica** | **el timbre**: qué instrumento o qué voz es |
| **Duración** | **la longitud**: cuánto dura, no cómo suena |
| **Velocidad de propagación** | **nada de la percepción**: es una propiedad del medio, no de la onda |

**La pregunta 80 del cuadernillo de esta ocupación pide cuál de los atributos fundamentales determina
el tono o la altura del sonido, y la plantilla oficial da como buena la frecuencia.** **Las tres
opciones falsas son intensidad, velocidad y duración**, que son **precisamente las tres filas
siguientes de la tabla.** **Es una pregunta de tabla y se responde con la tabla.**

**El aviso de oficio que hace falta aquí**: **la velocidad de propagación no es un atributo del sonido
sino del medio por el que viaja.** **Aparece en las opciones de esta clase de preguntas justamente
porque suena a magnitud de sonido y no lo es.**

## 2. De la señal analógica a la digital

**La señal analógica es una tensión que copia la forma de la onda de presión.** **La digital es una
sucesión de números que la describen.** **Convertir de una a otra son dos operaciones y sólo dos:**

1. **El muestreo**: **tomar el valor de la señal a intervalos regulares.** **Cuántas veces por segundo
   se toma es la frecuencia de muestreo, y se mide en kilohercios.**
2. **La cuantificación**: **asignar a cada muestra un número de una escala finita.** **Cuántos escalones
   tiene esa escala lo dice el número de bits por muestra.**

**Qué decide cada una, que es lo que se pregunta:**

| Decisión | Qué limita |
|---|---|
| **La frecuencia de muestreo** | **la frecuencia más alta que se puede representar** |
| **Los bits por muestra** | **la finura con que se distinguen niveles, y con ella el margen dinámico** |

**Y la regla de oficio que las une**: **para representar una frecuencia hay que muestrear a más del
doble de ella.** **Por debajo de ese límite las frecuencias altas no desaparecen: reaparecen
disfrazadas de frecuencias bajas que nunca estuvieron ahí, y eso ya no se puede deshacer.** **Por eso
todo convertidor lleva delante un filtro que corta lo que no va a poder representar.** **Filtrar antes
es la única defensa; después ya es tarde.**

**El corolario que ordena las cifras del oficio**: **las frecuencias de muestreo habituales están por
encima del doble del límite de la audición humana**, y **de ahí que las que aparecen en los enunciados
de examen sean todas de ese orden.** **El cuadernillo de esta ocupación nombra tres**: **44,1 y 48
kilohercios en su pregunta 64, y 96 kilohercios con 24 bits por muestra en su pregunta 4.**

**El problema práctico que de ahí se deriva y que se pregunta**: **dos equipos digitales que muestrean
a distinta frecuencia no se pueden conectar sin más.** **La pregunta 64 plantea un mezclador digital
trabajando a 48 kilohercios que recibe una señal digital a 44,1, y pregunta qué hay que hacer.** **La
plantilla da como buena usar un conversor de frecuencia de muestreo.**

**Por qué las otras tres opciones no valen, que es lo que hay que saber explicar:**

| Opción | Por qué no |
|---|---|
| **Meterla por una entrada analógica** | **exige convertir a analógico y volver a digital: dos conversiones y la degradación de las dos, cuando existe una solución en el dominio digital** |
| **Usar un atenuador** | **un atenuador cambia el nivel, no la frecuencia de muestreo: no resuelve el problema planteado** |
| **Decir que no se puede** | **sí se puede, y el equipo que lo hace tiene nombre propio** |

**Y el aviso de oficio**: **la conversión de frecuencia de muestreo no es gratis.** **Recalcula
muestras que no se tomaron e introduce su propio error, además de retardo.** **Cuando se puede, lo
correcto es sincronizar toda la instalación a una misma frecuencia y no convertir nada.**

## 3. La interfaz digital profesional y sus bits de servicio

**El formato con el que dos equipos profesionales se pasan audio digital lleva dos canales en una
trama, y esa trama no lleva sólo las muestras: lleva cuatro bits de servicio por cada una.** **Se
nombran por su inicial y hay que saber para qué sirve cada uno:**

| Bit | Nombre | Para qué sirve |
|---|---|---|
| **V** | **validez** | **decir si la muestra es apta o no para un procesado posterior, como convertirla a analógica** |
| **U** | **usuario** | **transportar información del usuario, ajena a la muestra** |
| **C** | **estado de canal** | **describir el propio flujo: formato, uso, frecuencia y demás** |
| **P** | **paridad** | **permitir detectar errores en la trama** |

**La pregunta 50 pide para qué se usa el bit de validez, y la plantilla da como buena exactamente la
tercera columna de la primera fila**: **indicar que la muestra de audio es apta o no para un procesado
adicional, como su conversión a señal analógica.**

**La trampa de esa pregunta está en las otras tres opciones, porque las tres son verdad… de otro bit**:
**la detección de errores es del bit de paridad, la información de usuario es del bit de usuario, y lo
relativo a la frecuencia de muestreo va en el estado de canal.** **Es la pregunta que separa a quien se
sabe la tabla de quien reconoce las palabras.**

**Y aquí engancha la parte 31 de la familia de normas de transporte de medios por red, que se estudia
en el tema 19**: **lo que esa parte transporta de forma transparente son precisamente estos cuatro
bits**, y **por eso no basta con llevar el audio: hay que llevar la trama.**

**El paso a muchos canales**: **cuando hacen falta más de dos, la interfaz multicanal lleva por un solo
enlace un haz de canales digitales.** **La pregunta 4 del cuadernillo pregunta cuántos audios monofónicos
digitales caben en una señal de esa interfaz, y la plantilla oficial da como buena la cifra de
sesenta y cuatro.** **Este temario recoge esa cifra como la que la plantilla confirma para el caso que
la pregunta plantea**, y **no da ninguna otra capacidad de esa interfaz, porque son dato de la norma
que la define y este proyecto no la tiene.**

## 4. Medida y control de la señal

**El enunciado los nombra juntos y son cosas distintas**: **medir es saber qué nivel hay; controlar es
decidir qué nivel se deja pasar.**

**Los instrumentos de medida, con lo que cada uno mide y para qué se usa:**

| Instrumento | Qué mide | Para qué |
|---|---|---|
| **Medidor de valor medio** | **el nivel promediado, con respuesta lenta** | **se acerca a la sensación de volumen; no ve los picos** |
| **Medidor de picos** | **el valor instantáneo máximo** | **evita la saturación del convertidor: es el que protege** |
| **Medidor de sonoridad** | **el nivel percibido según una ponderación normalizada** | **igualar el volumen entre programas** |
| **Medidor de correlación** | **la relación de fase entre los dos canales de un estéreo** | **detectar contrafase y comprobar la compatibilidad monofónica** |
| **Sonómetro** | **la presión sonora en el aire de una sala** | **acústica y ruido; no mide señales eléctricas** |

**La pregunta 57 pide con qué instrumento se detecta si una señal estéreo está en fase o en contrafase,
y la plantilla da como buena el medidor de correlación.** **Las otras tres opciones son los otros tres
instrumentos de la tabla**, y **ninguno de ellos mira la relación entre canales: los tres miden nivel,
cada uno a su manera.**

**Por qué importa la contrafase, que es lo que hay detrás de la pregunta**: **si los dos canales de un
estéreo van invertidos entre sí, al sumarlos para escuchar en monofonía se cancelan.** **En una casa de
radio y televisión, donde una parte del público escucha en un solo altavoz, una contrafase no detectada
es un programa que se emite prácticamente mudo para esa parte del público.** **De ahí que el medidor de
correlación sea instrumento de control central y no un lujo de estudio.**

**Y la distinción de nivel que hay que saber decir**: **el nivel de pico y la sonoridad no son lo
mismo.** **Dos programas pueden tener el mismo pico y sonar uno mucho más fuerte que otro, porque la
sonoridad depende de cuánto tiempo se mantiene la señal arriba y no de dónde llega un instante.**
**El pico se vigila para no romper; la sonoridad, para no molestar.**

## 5. Los equipos: captación y escucha

**El micrófono**: **el transductor que convierte presión sonora en tensión.** **Se clasifica por dos
criterios independientes y se confunden a menudo:**

- **Por cómo transduce**: **de bobina móvil, de condensador, de cinta.**
- **Por su patrón polar**: **de qué direcciones capta y de cuáles no.**

**Los patrones polares, que es lo que se pregunta:**

| Patrón | De dónde capta | Cuándo se elige |
|---|---|---|
| **Omnidireccional** | **de todas las direcciones por igual** | **ambiente, sonido de sala, cuando no hay ruido que rechazar** |
| **Cardioide** | **sobre todo de delante; rechaza lo de atrás** | **una fuente concreta situada al frente, con ruido alrededor** |
| **Bidireccional** | **de delante y de atrás; rechaza los lados** | **dos fuentes enfrentadas, como una entrevista cara a cara** |
| **Cañón** | **un ángulo frontal muy estrecho** | **distancia: cuando no se puede acercar el micrófono** |

**La pregunta 79 plantea un entorno ruidoso y un entrevistado situado al frente, y pregunta qué tipo de
micrófono se usaría.** **La plantilla da como buena el cardioide**, y **el razonamiento es la segunda
columna de la tabla**: **capta lo de delante, que es donde está el entrevistado, y rechaza lo de atrás,
que es de donde viene buena parte del ruido.**

**La cuarta opción de esa pregunta merece comentario porque es la trampa**: **inalámbrico no es un tipo
de patrón polar, sino una forma de llevar la señal.** **Un micrófono inalámbrico tiene además su
patrón, que puede ser cualquiera de los tres anteriores.** **Mezclar la clasificación por patrón con la
clasificación por enlace es el error que la opción busca.**

**La escucha multicanal**: **un sistema de cinco canales más el de graves tiene tres altavoces delante
—izquierdo, central y derecho—, dos detrás y un altavoz de graves.** **El central lleva sobre todo el
diálogo; los traseros, el ambiente y los efectos.**

**La pregunta 6 pregunta dónde se coloca el altavoz de graves en una sala de escucha de ese tipo, y la
plantilla da como buena que su colocación no es especialmente crítica y que puede ir prácticamente en
cualquier sitio.** **La razón de oficio que sostiene esa respuesta**: **el oído localiza la procedencia
de un sonido por diferencias de tiempo y de intensidad entre los dos oídos, y ambas se vuelven
inservibles cuando la longitud de onda es mucho mayor que la cabeza.** **Las frecuencias que ese
altavoz reproduce son justamente las de longitud de onda larga**, y **por eso el oyente no sabe decir
de dónde vienen.**

**El matiz de oficio que hay que añadir para no decir una tontería**: **eso vale para la localización,
no para la respuesta de la sala.** **Un altavoz de graves colocado en una esquina excita los modos
propios del recinto y suena más, y colocado en el centro puede caer en un mínimo y no oírse.** **La
posición no cambia de dónde parece venir el sonido, pero sí cuánto suena**, y **por eso en una sala
bien tratada se busca su sitio midiendo.**

## 6. Formatos, contenedores, códecs y compresión

**Tres palabras que el enunciado nombra seguidas y que se confunden a diario:**

| Concepto | Qué es | Ejemplo de pregunta que lo distingue |
|---|---|---|
| **Codificación** | **cómo se representan las muestras** | **sin comprimir o comprimido** |
| **Códec** | **el algoritmo que comprime y descomprime** | **cuánto reduce y qué pierde** |
| **Contenedor** | **el envoltorio de fichero que guarda uno o varios flujos con sus datos descriptivos** | **qué códecs admite dentro** |

**La regla que evita el error**: **el contenedor no dice cómo suena.** **Dos ficheros con la misma
extensión pueden llevar dentro códecs distintos, y un mismo códec puede ir en contenedores distintos.**
**Preguntar «qué calidad tiene este formato» sin mirar el códec no tiene respuesta.**

**Los dos grandes tipos de compresión de audio y en qué se diferencian:**

1. **Sin pérdida**: **el descomprimido es idéntico bit a bit al original.** **Reduce menos y se usa en
   archivo y en intercambio.**
2. **Con pérdida**: **descarta información que el oído no va a echar de menos y no se puede
   recuperar.** **Reduce mucho más y es lo que se usa en distribución.**

**Cómo funciona la compresión con pérdida, en una idea**: **aprovecha que un sonido fuerte tapa a otro
más flojo cercano en frecuencia o inmediatamente posterior en el tiempo.** **Lo que queda tapado no se
codifica, porque no se iba a oír.** **De ahí que la calidad de un códec con pérdida no se juzgue por lo
que conserva sino por lo bien que acierta al decidir qué tirar.**

**El aviso de explotación que cierra el epígrafe, y que es de método antes que de oficio**: **comprimir
con pérdida dos veces seguidas no descarta dos veces lo mismo.** **Cada paso decide sobre lo que le
llega, y lo que el primero dejó como estaba puede parecerle prescindible al segundo.** **Por eso en
producción se trabaja sin comprimir o sin pérdida y se comprime una sola vez, al final.**

## 7. El transporte de la señal

**Las formas de llevar audio de un sitio a otro, ordenadas por lo que cada una resuelve:**

| Forma | Qué la caracteriza |
|---|---|
| **Analógica simétrica** | **dos conductores en oposición y una malla: el ruido que entra en los dos se cancela al restarlos** |
| **Digital de dos canales** | **la trama profesional del epígrafe 3, por cable de par o por coaxial** |
| **Digital multicanal** | **un haz de canales por un solo enlace, por coaxial o por fibra** |
| **Por red de datos** | **flujos separados sobre protocolo de tiempo real, con reloj repartido: es el tema 19** |
| **Por radioenlace** | **cuando no hay cable: enlaces de micrófono y de reportaje** |

**La idea que explica la primera fila y que se pregunta en muchas ocupaciones**: **la conexión
simétrica no elimina el ruido por blindaje, sino por resta.** **El ruido se induce por igual en los dos
conductores y desaparece al hacer la diferencia entre ellos.** **Por eso una tirada larga se hace
simétrica y no se hace más gruesa.**

## 8. La regulación básica de la radiodifusión sonora en España

**Aquí acaba el oficio y empieza la norma.** **El enunciado pide la regulación básica de la
radiodifusión sonora en España, y esa regulación está en el título IV de la Ley 13/2022, de 7 de julio,
General de Comunicación Audiovisual**, que **lleva por rúbrica «La prestación del servicio de
comunicación audiovisual radiofónico y sonoro a petición».** **Se cita en su redacción vigente el 21 de
diciembre de 2022, que es la inicial: la ley no había sido modificada.**

**Lo primero, la distinción sobre la que se construye todo el título**: **hay dos servicios y no
uno.** **El radiofónico, que es la radio; y el sonoro a petición, que es el catálogo que el oyente
elige.** **El régimen se parece, pero no coincide, y las preguntas viven en la diferencia.**

**El primer artículo del título fija el régimen jurídico, y sus apartados 3 y 4 son la clave de todo
lo demás:**

**Artículo 76**, apartados 3 y 4:

> «3. La prestación del servicio de comunicación audiovisual radiofónico y del servicio de comunicación
> audiovisual sonoro a petición **requiere comunicación fehaciente ante la autoridad audiovisual
> competente y previa al inicio de actividad**, siendo de aplicación lo dispuesto al respecto en el
> apartado 1 del artículo 17 y en el capítulo II del título II.
> 4. La prestación del servicio de comunicación audiovisual radiofónico mediante ondas hertzianas
> terrestres **requerirá licencia previa otorgada mediante concurso por la autoridad audiovisual
> competente**, de conformidad con lo previsto en este Título, siendo también de aplicación lo dispuesto
> en el apartado 2 del artículo 17 y en las secciones 1.ª y 2.ª del capítulo III del título II.»

---

**La regla en una línea, que es como hay que llevarla al examen**: **si se usa espectro radioeléctrico,
hace falta licencia obtenida en concurso; si no se usa, basta con comunicar antes de empezar.** **Lo
que separa los dos regímenes no es el contenido ni el tamaño de la emisora: es el uso de las ondas
hertzianas terrestres, porque son un dominio público limitado.**

**Quién da la licencia lo dice el precepto siguiente:**

**Artículo 77**, apartado 1:

> «El otorgamiento de licencias para la prestación del servicio de comunicación audiovisual radiofónico
> mediante ondas hertzianas terrestres **cuyo ámbito geográfico sea superior al de una Comunidad
> Autónoma corresponde al Consejo de Ministros**.»

---

**Y su apartado 2 remite a las Comunidades Autónomas la determinación de la autoridad competente para
las licencias de ámbito autonómico y local.** **La regla de reparto**: **por encima de una Comunidad
Autónoma, el Consejo de Ministros; dentro de una, la Comunidad.**

**El artículo 78 pone los límites de concentración, y son la materia de pregunta más probable de todo
el título porque son cifras.** **Los cuatro que la ley fija:**

| Límite | Qué dice el artículo |
|---|---|
| **Apartado 1** | **nadie puede controlar más del cincuenta por ciento de las licencias que coincidan sustancialmente en su ámbito** |
| **Apartado 2** | **nadie puede controlar más de cinco licencias en un mismo ámbito de cobertura** |
| **Apartado 3, letra a)** | **nadie puede controlar más de un tercio de las licencias de ámbito estatal, total o parcial** |
| **Apartado 3, letra b)** | **en una misma Comunidad Autónoma, nadie puede controlar más del cuarenta por ciento de las licencias existentes en ámbitos con una sola licencia** |

**El apartado 2, por ser el más redondo, se cita literalmente:**

**Artículo 78**, apartado 2:

> «**Ninguna persona física o jurídica podrá controlar más de cinco licencias en un mismo ámbito de
> cobertura.**»

---

**Y dos reglas de aplicación que el propio artículo añade y que se preguntan**: **su apartado 4 deja
fuera del cómputo las emisoras gestionadas de forma directa por entidades públicas**, y **su apartado 6
aplica los límites de forma independiente a las licencias digitales y a las analógicas.** **Esa
independencia es la que impide sumar unas y otras al hacer la cuenta.**

**El artículo 79 permite la emisión en cadena**: **un mismo prestador con licencias en varios ámbitos,
o con acuerdos con otros titulares, puede emitir parte de su programación en cadena.** **Es lo que hace
posible la radio de ámbito nacional con desconexiones locales.**

**El artículo 80 somete a autorización previa los negocios jurídicos sobre licencias, y de él salen
tres reglas que hay que retener**: **la transmisión y el arrendamiento exigen que hayan pasado al menos
dos años desde la adjudicación inicial**; **el arrendatario pasa a tener la consideración de prestador
del servicio**; y **la prohibición que se cita, por ser terminante:**

**Artículo 80**, apartado 4:

> «**En todo caso, está prohibido el subarriendo.**»

---

**El artículo 81 regula la radio comunitaria sin ánimo de lucro por ondas hertzianas terrestres, y sus
tres condiciones son de examen**: **se presta en ámbito local o inferior y con licencia de la autoridad
autonómica, reservándose el Estado el dominio público radioeléctrico necesario**; **no puede incluir
comunicación comercial, salvo la de bienes y servicios del propio ámbito de cobertura y los anuncios de
servicio público o benéficos**; y **su licencia no se puede transmitir, arrendar ni ceder.**

**El artículo 82 regula la cesión de la señal para su difusión por cualquier soporte**, con **una
diferencia que hay que saber**: **el licenciatario privado puede ceder libremente a terceros
inscritos**, mientras que **el prestador del servicio público cederá sin contraprestación económica**,
garantizando en todo caso su derecho a acceder a los datos de consumo de sus contenidos.

**El penúltimo bloque del título protege a los menores en estos servicios, y trae la limitación
horaria que más se pregunta:**

**Artículo 83**, apartado 3:

> «3. Los prestadores del servicio de comunicación audiovisual radiofónico podrán emitir programas
> **relacionados con el esoterismo y las paraciencias, basados en la participación activa de los
> oyentes, entre la 1:00 y las 5:00 horas**, y **tendrán responsabilidad subsidiaria sobre los delitos
> que puedan cometerse** y los daños que puedan causarse a través de dichos programas.»

---

**Su apartado 4 aplica la misma franja de la una a las cinco a los programas de juegos de azar y
apuestas**, con **dos salvedades**: **los sorteos de las loterías reservadas en exclusiva a los
operadores designados**, y **los juegos de concursos conexos o subordinados a la actividad ordinaria
del prestador, siempre que no sirvan para promocionar otro juego.**

**El artículo 84 impone a los servicios sonoros a petición la incorporación gradual de herramientas de
accesibilidad en sus programas o contenidos ofrecidos mediante catálogo.**

**Y el artículo 85 cierra el título con las comunicaciones comerciales**, con **dos particularidades
frente a la televisión que son de pregunta**: **no se les aplica la limitación horaria del apartado 5
del artículo 123**, y **pueden patrocinar toda la programación salvo los noticiarios**, así como
**emplazar producto en toda la programación salvo noticiarios, programas de protección del consumidor,
religiosos e infantiles.**

**La tabla de la que se cuelga todo el título, para repasar:**

| Artículo | Qué resuelve |
|---|---|
| **76** | **comunicación previa sin espectro; licencia en concurso con espectro** |
| **77** | **Consejo de Ministros por encima de una Comunidad Autónoma; la Comunidad, dentro** |
| **78** | **los cuatro límites de concentración, con las emisoras públicas fuera del cómputo** |
| **79** | **emisión en cadena** |
| **80** | **negocios sobre licencias: autorización, dos años, prohibición de subarriendo** |
| **81** | **radio comunitaria sin ánimo de lucro** |
| **82** | **cesión de la señal, con el matiz del prestador público** |
| **83** | **menores, y la franja de la una a las cinco** |
| **84** | **accesibilidad de los servicios sonoros a petición** |
| **85** | **comunicaciones comerciales, patrocinio y emplazamiento** |

## 9. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual** (`BOE-A-2022-11311`), **en su redacción vigente el 21 de diciembre de 2022** | **Los apartados 3 y 4 del artículo 76**, **el apartado 1 del artículo 77**, **el apartado 2 del artículo 78** y **el apartado 4 del artículo 80**, citados literalmente; y **el apartado 3 del artículo 83**, citado literalmente |

**Seis declaraciones expresas:**

1. **La ley se ha leído en el volcado del texto consolidado a la fecha de corte que este proyecto
   guarda**, y **el volcado deja constancia de que sus bloques tienen una sola redacción**: **el texto
   del artículo 76 al 85 no ha cambiado desde su publicación.** **El estudio general de esta ley está
   en el tema 7 del bloque común y aquí sólo se toma su título IV**, que **es lo único que el enunciado
   de este punto pide.**
2. **Lo que de esos artículos no va entre comillas va resumido, no citado**: **los apartados 1, 3, 4 y
   6 del artículo 78; los artículos 79, 81, 82, 84 y 85 enteros; los apartados 1 a 3 del artículo 80; y
   los apartados 1, 2 y 4 del artículo 83.** **El resumen no añade obligación ni límite que la norma no
   diga, y las cifras que aparecen en él —el cincuenta por ciento, el tercio, el cuarenta por ciento,
   los dos años y la franja de la una a las cinco— están todas en el articulado citado arriba.**
3. **Las siete respuestas que la plantilla oficial confirma se recogen con su número de pregunta y con
   el razonamiento que lleva a cada una**: **los sesenta y cuatro audios monofónicos de la interfaz
   multicanal, en la pregunta 4**; **la colocación no crítica del altavoz de graves, en la 6**; **el
   cometido del bit de validez, en la 50**; **el medidor de correlación para la fase, en la 57**; **el
   conversor de frecuencia de muestreo, en la 64**; **el micrófono cardioide en entorno ruidoso, en la
   79**; y **la frecuencia como atributo que determina el tono, en la 80.**
4. **Las cifras técnicas de este tema son sólo las que la plantilla confirma**: **los sesenta y cuatro
   canales de la pregunta 4, y las frecuencias de muestreo de 44,1, 48 y 96 kilohercios y los 24 bits
   por muestra que aparecen en los enunciados de las preguntas 4 y 64.** **El tema no da ninguna otra
   capacidad de esa interfaz, ninguna tasa de compresión, ningún margen dinámico, ningún nivel de
   referencia, ninguna frecuencia de corte del altavoz de graves y ninguna distancia de colocación.**
   **Son dato de norma técnica o de fabricante, que este proyecto no tiene**, y **una cifra que no se
   ha leído en su fuente no se escribe.**
5. **Las normas técnicas de audio que este tema describe se nombran por lo que hacen y no por su
   articulado**: **son normas de asociaciones de ingeniería, no del Boletín Oficial del Estado**, y
   **este proyecto no tiene su texto.** **Por eso el temario explica qué lleva cada trama y para qué
   sirve cada bit, y no atribuye a ninguna de ellas ningún parámetro que no venga de la plantilla.**
6. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **el
   transporte de audio por red y el reparto de reloj, al tema 19**; **el sonido dentro de la producción
   y sus equipos de estudio, al tema 12**; **el tratamiento de audio en postproducción, al tema 15**;
   **la radio digital y su sistema de difusión, al tema 22**; **el marco regulador de las
   telecomunicaciones y el dominio público radioeléctrico, al tema 1**; y **el estudio completo de la
   Ley 13/2022, al tema 7 del bloque común.**

**El resto del tema va como oficio y así se declara**: la advertencia de que la velocidad de
propagación no es atributo del sonido sino del medio, la explicación de que las frecuencias por encima
del límite de muestreo reaparecen disfrazadas y de que filtrar antes es la única defensa, las tres
razones por las que las otras opciones de la conversión de frecuencia no valen y el aviso de que
convertir no es gratis, la lectura de que las tres opciones falsas del bit de validez son verdad de
otro bit, la explicación de por qué la contrafase deja mudo al público que escucha en monofonía, la
distinción entre vigilar el pico para no romper y la sonoridad para no molestar, la advertencia de que
inalámbrico no es un patrón polar, la razón por la que el oído no localiza las frecuencias graves y el
matiz de que la posición del altavoz de graves sí cambia cuánto suena aunque no de dónde parece venir,
la regla de que el contenedor no dice cómo suena, la idea del enmascaramiento como fundamento de la
compresión con pérdida y el aviso de no comprimir dos veces, y la explicación de que la conexión
simétrica cancela el ruido por resta y no por blindaje. **Nada de eso está en un boletín oficial ni en
ninguna fuente consultada para este proyecto**, y el tema no lo presenta como si lo estuviera.
