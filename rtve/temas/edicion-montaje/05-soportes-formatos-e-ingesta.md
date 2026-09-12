# Tema 5 del específico de Edición, Montaje y Procesos Audiovisuales · Soportes, formatos, grabación e ingesta

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 5 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los soportes, los formatos, el encapsulado y la ingesta, y **va como oficio**, salvo cinco datos de catálogo que descansan en la plantilla |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Cinco preguntas** —el audio de un formato de grabación, el modo de un menú de grabador, las opciones de recurrencia de un sistema de ingesta, un perfil de encapsulado y la capacidad de un disco— **citan producto de fabricante y no se han podido contrastar**. Es el punto con más afirmaciones de quinto nivel de esta ocupación |
| **Extensión** | **3.347 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el formato avanzado de autoría (**AAF**, *advanced
authoring format*); el formato de intercambio de material (**MXF**, *material exchange format*), con
sus perfiles operacionales **Op1a** y **Op1b-Atom**; la modulación por impulsos codificados (**PCM**,
*pulse-code modulation*); la cinta lineal abierta (**LTO**, *linear tape open*); la lista de decisión
de edición (**EDL**, *edit decision list*); el formato gráfico de intercambio (**GIF**), el mapa de
bits (**BMP**), los gráficos de red portátiles (**PNG**) y el formato del grupo conjunto de expertos
en fotografía (**JPEG**); el formato de imagen etiquetada (**TIFF**); los contenedores de Apple
(**MOV**), de la familia MPEG (**MP4**) y de Microsoft (**AVI**), y el contenedor libre **OGG**; el
lenguaje de marcado extensible (**XML**); la interfaz digital serie (**SDI**); la alta
definición (**HD**) y su variante de la casa Sony (**HDCAM**); el disco profesional de esa misma casa
(**XDCAM**); el códec de Avid (**DNxHR**); el formato de emisión **IMX**; la Sociedad de Ingenieros
de Cine y Televisión (**SMPTE**); y el archivo, en el sentido de conservación a largo plazo.

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, puntos 2.2, 2.4, 4.1, 4.2, 4.3 y 4.4):
> «Soportes y formatos.»
> «Documentación y catalogación de ficheros.»
> «Conocimientos básicos de equipos y soportes de grabación.»
> «Equipos de almacenamiento en disco óptico (xd-cam) y disco duro.»
> «Ingesta en servidores de edición y redacción digital.»
> «Formatos de comprensión, encapsulado, importación y exportación de ficheros.»

**Ocho preguntas.** Y es el punto donde el examen más se apoya en **máquinas concretas de un
fabricante**: dos preguntas citan modelos de grabador y de disco por su referencia, y una cita el
sistema de ingesta de una casa. **Cuatro de las ocho descansan sólo en la plantilla**, y van
declaradas.

<!-- indice -->

## Índice

- [1. Contenedor, códec y esencia](#1-contenedor-códec-y-esencia)
- [2. El AAF y los formatos de intercambio de proyecto](#2-el-aaf-y-los-formatos-de-intercambio-de-proyecto)
- [3. El MXF y sus perfiles operacionales](#3-el-mxf-y-sus-perfiles-operacionales)
- [4. Los formatos de imagen fija](#4-los-formatos-de-imagen-fija)
- [5. El XDCAM: el soporte óptico profesional](#5-el-xdcam-el-soporte-óptico-profesional)
- [6. El audio en el XDCAM HD422](#6-el-audio-en-el-xdcam-hd422)
- [7. La LTO y el archivo a largo plazo](#7-la-lto-y-el-archivo-a-largo-plazo)
- [8. La ingesta](#8-la-ingesta)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. Contenedor, códec y esencia

**Ésta es la distinción que ordena todo el tema**, y la que el examen da por sabida:

| Concepto | Qué es | Ejemplos |
|---|---|---|
| **Esencia** | **El material en sí**: las imágenes y el sonido | Los cuadros y las muestras |
| **Códec** | **Cómo se comprime la esencia** | H.264, ProRes, DNxHD, JPEG 2000, PCM |
| **Contenedor** o encapsulado | **Cómo se empaqueta la esencia con sus metadatos** | **MXF**, MOV, MP4, AVI |
| **Metadatos** | **Los datos sobre el material**: código de tiempo, nombre, fecha, cámara | Van dentro del contenedor |
| **Proyecto** | **Las decisiones de montaje**, que no contienen esencia | **AAF**, EDL, XML |

**Las cuatro filas se preguntan en este cuadernillo**, y **la confusión entre ellas es el mecanismo de
tres de sus ocho preguntas**. La regla que las separa: **el códec dice cómo se comprime, el contenedor
cómo se empaqueta y el proyecto qué se hizo con ello.**

## 2. El AAF y los formatos de intercambio de proyecto

**Un archivo AAF es un formato de archivo multimedia que permite intercambiar medios digitales y
metadatos entre distintos sistemas, plataformas y aplicaciones.** Ésa es la respuesta oficial a la
pregunta 14.

**Para qué se usa realmente, que es lo que hace legible la definición**: **para sacar un montaje de un
programa y meterlo en otro**. Un montaje terminado en Avid se manda a la mezcla de sonido, o al
etalonaje, o a otro programa de edición, **y lo que viaja es el AAF**: qué clips, en qué orden, con
qué cortes, con qué niveles de audio y con qué efectos, **y opcionalmente la esencia misma**.

| Formato de proyecto | Qué lleva | Limitación |
|---|---|---|
| **EDL** | **Sólo la lista de cortes**, con códigos de tiempo | **Una sola pista de vídeo**; no lleva efectos ni audio complejo |
| **AAF** | **Cortes, pistas, niveles, efectos y metadatos**, y puede llevar la esencia | El más completo de los tres |
| **XML** | Lo mismo que el AAF, en la variante de cada fabricante | **No es universal**: cada casa tiene el suyo |

**Las tres opciones falsas de la pregunta 14 son la misma frase con el verbo cambiado**, y las tres
atribuyen al AAF una función que no tiene:

| Opción | Qué dice | Por qué no |
|---|---|---|
| a) | «Normalizar la señal para la edición» | **El AAF no normaliza ninguna señal**: transporta decisiones y metadatos |
| c) | «Normalizar la señal para la emisión» | **Lo mismo**, y además la emisión no es su ámbito |
| d) | «Ajustar niveles de una secuencia» | **Lleva los niveles, no los ajusta**: el ajuste se hace en el programa |

**La palabra que resuelve la pregunta es «intercambiar»**: **el AAF es un vehículo, no una
herramienta.**

## 3. El MXF y sus perfiles operacionales

**El MXF es el contenedor profesional de televisión**, normalizado por la SMPTE, y **no dice nada
sobre cómo está comprimido lo que lleva dentro**: puede envolver material de casi cualquier códec.

**Lo que sí distingue a unos ficheros MXF de otros es su perfil operacional**, que dice **cómo se
reparten las pistas dentro del fichero**:

| Perfil | Cómo empaqueta | Dónde se usa |
|---|---|---|
| **Op1a** | **Todo en un solo fichero**: vídeo y todas las pistas de audio multiplexadas juntas | **Emisión, intercambio y grabación en cámara**: es el fichero autónomo |
| **Op-Atom** | **Un fichero por pista**: uno de vídeo y uno por cada canal de audio | **El entorno de edición de Avid**, que trabaja mejor con pistas sueltas |

**El formato XDCAM HD 50i 4:2:2 está encapsulado en MXF Op1a.** Ésa es la respuesta oficial a la
pregunta 88, y es coherente con el reparto de arriba: **lo que sale de una cámara o de un grabador de
plató es un fichero autónomo**, no una colección de pistas sueltas.

**Las tres opciones falsas y su error, que vuelve sobre la distinción del epígrafe 1:**

| Opción | Por qué no |
|---|---|
| **DNxHR** | **Es un códec, no un encapsulado.** Confunde las dos categorías |
| **MXF Op1-Atom** | **Es un perfil real de MXF**, pero **es el de Avid**, no el del material de cámara |
| **IMX** | **Es un formato de grabación de definición estándar** de la misma casa, **anterior al XDCAM HD** |

**La opción b) es la trampa buena**: **nombra el contenedor correcto con el perfil equivocado**, y sólo
se descarta sabiendo para qué sirve cada perfil.

**Una declaración expresa**: **la documentación del fabricante que fija el encapsulado de ese formato
concreto no se ha consultado.** La distinción entre Op1a y Op-Atom es de norma SMPTE y de uso
corriente, **pero la atribución de Op1a a ese formato concreto descansa en la plantilla oficial.**

## 4. Los formatos de imagen fija

**Un montador maneja imágenes fijas a diario**: rótulos, logotipos, fondos, capturas. Y hay que saber
cuáles lo son y cuáles no.

| Formato | Qué es | Nota |
|---|---|---|
| **GIF** | **Imagen digital**, de hasta 256 colores, con animación y transparencia binaria | El de los gráficos animados de internet |
| **BMP** | **Imagen digital**, mapa de bits **sin compresión** | Pesado y sencillo |
| **PNG** | **Imagen digital**, comprimida **sin pérdida**, **con canal alfa completo** | **El de uso profesional para rótulos y logotipos** |
| **JPEG** | Imagen digital comprimida **con pérdida** | Fotografía; **no conviene para grafismo** |
| **TIFF** | Imagen digital sin pérdida, de mucha profundidad | Artes gráficas y cine |
| **OGG** | **NO es imagen: es un contenedor multimedia libre**, de audio y de vídeo | Es la respuesta de la pregunta 34 |

**El formato que NO es un tipo de imagen digital es OGG.** Ésa es la respuesta oficial a la pregunta
34, y el motivo es de categoría: **OGG no guarda imágenes fijas, guarda flujos de audio y de vídeo**,
normalmente con los códecs Vorbis y Theora.

**La razón de oficio para preferir el PNG en grafismo**, que va más allá de la pregunta: **es el único
de los cuatro que junta compresión sin pérdida y canal alfa de ocho bits**. El GIF tiene
transparencia, pero **binaria**: un píxel es opaco o transparente, **sin grados**, y por eso sus bordes
salen dentados sobre el vídeo. **El JPEG no tiene alfa y además degrada los bordes duros**, que es
justo lo que un rótulo tiene.

## 5. El XDCAM: el soporte óptico profesional

**El XDCAM es el sistema de grabación en disco óptico profesional de Sony**, y aparece nombrado en el
propio anexo del temario —«Equipos de almacenamiento en disco óptico (xd-cam) y disco duro»—. Es lo
que sustituyó a la cinta en informativos y en gran parte de la producción de televisión.

**Sus dos ventajas sobre la cinta**, que es lo que explica el cambio:

1. **Acceso no lineal**: se salta a cualquier punto sin rebobinar, **y se puede volcar mientras se
   sigue grabando**.
2. **Ficheros, no señal**: lo que hay en el disco **ya es un fichero MXF con sus metadatos**, así que
   la ingesta es una copia y no un volcado en tiempo real.

**Las dos preguntas de máquina concreta.** El examen cita **dos grabadores por su referencia** y **un
disco por su modelo**, y las dos respuestas descansan en la plantilla:

- **Pregunta 22.** En los grabadores citados, **para que al extraer el disco e insertar otro nuevo no
  se pierda nada de lo ocurrido en ese intervalo, el menú 150 —*rec mode*— debe ponerse en «D.exc»**.
  **Las tres opciones falsas** —«Normal», «C.rec» y «Continuous»— **son modos que el aparato tiene o
  que suenan a que los tiene**, y sólo la plantilla decide.
- **Pregunta 90.** El disco citado, **en el formato de grabación que la pregunta indica, tiene una
  capacidad de 4 horas.** **Las tres opciones falsas** —23 minutos, 8 horas y 95 minutos— **son
  duraciones plausibles de otros soportes o de otras tasas**.

**Lo que sí sostiene este tema sobre esas dos preguntas**, y es lo que las hace estudiables: **el
concepto de grabación en memoria intermedia durante el cambio de soporte** —el grabador sigue
escribiendo en una memoria interna mientras no hay disco, y vuelca cuando entra el nuevo— **y la regla
que gobierna la capacidad de cualquier soporte**: **capacidad en minutos = capacidad en bits partida
por la tasa de bits del formato**. Un mismo disco **da el doble de minutos a la mitad de tasa**, y por
eso la pregunta especifica el formato.

## 6. El audio en el XDCAM HD422

**En el formato XDCAM HD422 a 50i el audio es de 4 u 8 canales, con códec PCM y 24 bits.** Ésa es la
respuesta oficial a la pregunta 20.

**Qué significa cada parte:**

| Elemento | Qué dice |
|---|---|
| **4 u 8 canales** | **El formato admite las dos configuraciones**, y la elige el operador según la producción |
| **PCM** | **Modulación por impulsos codificados**: audio **sin comprimir** |
| **24 bits** | La profundidad de cuantificación: **unos 144 dB de rango dinámico** |

**Por qué PCM y no un códec comprimido**: **el audio de producción no se comprime**, porque va a pasar
por mezcla, ecualización y compresión de dinámica, **y cada paso sobre audio ya comprimido acumula
artefactos**. **La compresión de audio se hace al final de la cadena, en la emisión, no en la
captación.**

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «8 canales, PCM, 24 bits» | **La cifra de canales es incompleta**: deja fuera la configuración de cuatro |
| «16 canales, PCM, 32 bits» | **Ni la cifra de canales ni la profundidad** corresponden a este formato |
| «16 canales, PCM, 64 bits» | **64 bits no es una profundidad de audio de ningún formato de grabación** |

**La opción a) es la trampa buena**: **acierta el códec y la profundidad y falla en que el formato
admite dos configuraciones de canales, no una.** **La respuesta correcta es la más completa, no la más
concreta.**

**Una declaración expresa**: **la documentación del fabricante que fija estos parámetros no se ha
consultado**, así que **la respuesta descansa en la plantilla oficial**. Lo que este tema sostiene es
el porqué: qué es PCM, qué significan veinticuatro bits y por qué el audio de producción no se
comprime.

## 7. La LTO y el archivo a largo plazo

**Una LTO es una tecnología de almacenamiento en cinta magnética de alta capacidad, potente,
escalable y adaptable, que ayuda a abordar las crecientes demandas de protección de datos.** Ésa es la
respuesta oficial a la pregunta 21.

**Por qué una casa de televisión sigue usando cinta en pleno siglo XXI**, que es lo que hay que
entender:

| Ventaja | En qué consiste |
|---|---|
| **Coste por terabyte** | **El más bajo de todos los soportes** para volúmenes grandes |
| **Consumo** | **Una cinta guardada no consume nada**: un disco encendido, sí |
| **Vida útil** | **Décadas** en condiciones de archivo controladas |
| **Escalabilidad** | Se añaden cintas, no cabinas: **la capacidad crece por unidades baratas** |
| **Aislamiento** | **Una cinta fuera de la biblioteca no está en la red**, y por tanto no la alcanza un ataque |

**Y su desventaja, que es la que fija su uso**: **el acceso es secuencial y lento**. **Una LTO no es
almacenamiento de trabajo: es archivo.** El material vivo está en disco; **lo que ya no se toca, en
cinta**.

**Las tres opciones falsas de la pregunta 21 y su error:**

| Opción | Por qué no |
|---|---|
| «Cinta abierta desde un dispositivo de láser azul» | **Confunde la LTO con el disco óptico.** El láser azul es del XDCAM y del Blu-ray, **no de una cinta magnética** |
| «Al ser magnética su capacidad es baja y no son regrabables» | **Las dos mitades son falsas**: la capacidad es alta y **las LTO sí son regrabables** |
| «Anchura de más de 6 pulgadas y no escalable» | **Absurdo por magnitud** —la cinta LTO es de media pulgada— **y falso en lo de la escalabilidad**, que es una de sus señas |

**El aviso de vocabulario**: **«*linear tape open*» significa «cinta lineal abierta», y «abierta» no
se refiere al carrete** sino a que **es una norma abierta**, fabricada por varias casas, frente a los
formatos propietarios de cinta que la precedieron. **La opción a) juega con ese equívoco.**

## 8. La ingesta

**Ingestar es meter material en el sistema de edición**, y en una casa de televisión no es copiar
ficheros: es **un proceso programado, con metadatos y con vigilancia**.

**Las tres formas de ingesta**, que conviene distinguir:

| Forma | Qué es |
|---|---|
| **Ingesta de fichero** | Copiar material que ya viene en fichero —una tarjeta, un disco XDCAM, una entrega— **con su comprobación de integridad** |
| **Ingesta en directo** o *crash record* | **Grabar una señal que entra ahora**: una señal de agencia, un enlace, una cámara |
| **Ingesta programada** | **Grabar automáticamente en un horario previsto**, sin nadie delante |

**El sistema de ingesta que el examen cita ofrece cuatro opciones de recurrencia para una grabación
programada: None (sin recurrencia), Daily (diaria), Weekly (días específicos de la semana) y Monthly
(el mismo día de cada mes).** Ésa es la respuesta oficial a la pregunta 23.

**Las tres opciones falsas son la misma lista con una o dos entradas quitadas**, y ése es todo el
mecanismo de la pregunta: **hay que saber que son cuatro y no dos ni tres**.

**Una declaración expresa**: **el manual del sistema de ingesta citado no se ha consultado**, y **la
respuesta descansa en la plantilla oficial**.

**Lo que sí sostiene este tema, y es lo que hace la pregunta legible**: **por qué una programación de
grabación necesita recurrencia**. Una redacción graba **el mismo informativo de agencia todos los
días**, **la misma tertulia los martes y jueves** y **el mismo resumen mensual el primer lunes**. **Sin
recurrencia, alguien tendría que programar cada día a mano**, y **el día que se olvidase no habría
señal**. **Las cuatro opciones de recurrencia son las cuatro periodicidades de una parrilla**, y por
eso son ésas.

## 9. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 14 | Qué es y para qué se utiliza un archivo AAF | b) Intercambiar medios digitales y metadatos entre sistemas ✔ |
| 20 | Canales y codificación del audio en XDCAM HD422/50i | b) 4 u 8 canales, PCM, 24 bits ✔ **·** sólo con la plantilla |
| 21 | Qué es una LTO | b) Tecnología de cinta magnética de alta capacidad y escalable ✔ |
| 22 | Modo del menú 150 para no perder material al cambiar de disco | c) D.exc ✔ **·** sólo con la plantilla |
| 23 | Opciones de recurrencia en el sistema de ingesta citado | c) None / Daily / Weekly / Monthly ✔ **·** sólo con la plantilla |
| 34 | Cuál NO es un tipo de imagen digital | c) OGG ✔ |
| 88 | Encapsulado del formato XDCAM HD 50i 4:2:2 | c) MXF Op1a ✔ **·** sólo con la plantilla |
| 90 | Capacidad del disco XDCAM citado | b) 4 horas ✔ **·** sólo con la plantilla |

**Las ocho respuestas oficiales son correctas.**

**Y cinco de las ocho descansan sólo en la plantilla**: **las cinco que citan una máquina, un soporte o
un programa de un fabricante por su modelo o su referencia**. **Es el punto con más afirmaciones de
quinto nivel de toda la ocupación**, y el motivo es que **el propio anexo nombra una marca —«xd-cam»—
dentro del programa**, así que el tribunal se ha considerado autorizado a preguntar por catálogo.

**El aviso de estudio**: **las tres preguntas conceptuales de este punto —la 14, la 21 y la 34— se
contestan entendiendo la diferencia entre contenedor, códec, proyecto e imagen fija.** **Las cinco de
catálogo se memorizan.** Conviene separar el estudio de unas y otras, porque **no se preparan igual**.

## 10. Trazabilidad

**Este tema no cita ninguna norma del BOE.** Su materia son soportes, formatos y procesos de ingesta,
y **va como oficio**, salvo lo que descansa en la plantilla.

| Nivel | Fuente | Temas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Cinco afirmaciones**: el audio del formato de grabación, el modo del menú del grabador, las opciones de recurrencia del sistema de ingesta, el perfil de encapsulado y la capacidad del disco | Preguntas 20, 22, 23, 88 y 90 |

**Una declaración expresa sobre lo que no se ha podido contrastar**: **la documentación de los
fabricantes citados —los dos grabadores de disco óptico, el disco profesional, el formato de grabación
y el sistema de ingesta— no se ha consultado.** Son manuales de producto de casas comerciales, y este
proyecto no ha accedido a ellos. **Las cinco respuestas descansan en la plantilla oficial, que es el
quinto nivel de la jerarquía de fuentes.**

**Lo que este tema sí sostiene sobre esas cinco preguntas** es el vocabulario y el porqué: qué es un
perfil operacional de MXF y en qué se diferencian Op1a y Op-Atom, qué es PCM y por qué el audio de
producción no se comprime, cómo se calcula la capacidad en minutos de cualquier soporte, qué es una
memoria intermedia de grabación durante un cambio de disco y por qué una parrilla necesita cuatro
periodicidades de recurrencia. **La cifra se memoriza; el porqué se entiende.**

**El resto del tema va como oficio y así se declara**: la distinción entre esencia, códec, contenedor,
metadatos y proyecto; la comparación entre EDL, AAF y XML; las características de los formatos de
imagen fija; y el papel de la cinta LTO en el archivo. **Nada de eso está en un boletín oficial**, y el
tema no lo presenta como si lo estuviera.
