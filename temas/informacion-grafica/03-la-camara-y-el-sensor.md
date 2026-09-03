# Tema 3 del específico de Información Gráfica y Captación de Imagen y Sonido · La cámara de vídeo y el sensor

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Información Gráfica y Captación de Imagen y Sonido · punto 3 |
| **Sirve para** | **Información Gráfica y Captación de Imagen y Sonido** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la tecnología del sensor, la óptica aplicada y el manejo de una cámara, y **va como oficio**, salvo cuatro datos de menú y de catálogo |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Cuatro preguntas** —el rótulo del modo de pregrabación, el formato de menor calidad de una familia de fabricante, el rótulo del modo de red y el procedimiento completo de sincronización de dos cámaras— **citan producto de fabricante y no se han podido contrastar** |
| **Extensión** | **4.041 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la captación electrónica de noticias (**ENG**,
*electronic news gathering*) y la producción electrónica en campo (**EFP**, *electronic field
production*); el dispositivo de acoplamiento de carga (**CCD**) y el semiconductor complementario de
óxido metálico (**CMOS**); el conversor analógico-digital (**ADC**, *analog-to-digital converter*);
la tabla de consulta (**LUT**, *look-up table*); el código de tiempo (**TC**, *time code*); la
sincronización externa de la cámara (***genlock***); la interfaz digital serie (**SDI**) y el conector
de vídeo *Bayonet Neill-Concelman* (**BNC**); la red de área local (**LAN**) y la comunicación de
campo cercano (**NFC**); la tarjeta de memoria (**SD**); la ultra alta definición (**UHD**); y el
formato de grabación en disco óptico de la casa Sony (**XDCAM**), con sus perfiles **Proxy AV**,
**MPEG IMX**, **MPEG HD** y **DVCAM**, que el examen escribe **DVCA**.

**Y una advertencia sobre los rótulos de menú.** El cuadernillo escribe los nombres de las opciones de
cámara tal como aparecen en el menú, y este tema los reproduce igual porque **la respuesta oficial
depende del rótulo exacto**: **Picture Cache**, la pregrabación; **Free Run** y **Clock**, los dos
modos de código de tiempo; **Ext. Link**, el enlace externo; **Simul Rec**, la grabación simultánea;
**Scene** y **Paint**, los ajustes de imagen; **Access Point Mode**, el modo de punto de acceso; y
**S-Log3**, una curva logarítmica de fabricante. **No son siglas: son los rótulos de la máquina.**

> Enunciado de la convocatoria (Anexo 2, temario específico de Información Gráfica y Captación de
> Sonido, puntos 3.1, 3.4, 3.5, 3.12, 3.13, 4.1 y 4.4):
> «Cámara de video: ENG, EFP y cinematografía digital.»
> «Sensores y señal: CCDs y CMOS. Tamaños. Resolución espacial y temporal. Rango.»
> «Sistemas de grabación: formatos, muestreo, compresión, codificación y soportes.»
> «Ajustes de la cámara en producción ligera PEL.»
> «Cámara de video: Ajustes básicos de la cámara y óptica, cuidados, mantenimiento.»

**Ocho preguntas.** Y es el punto de la ocupación con más **mezcla de teoría y menú**: cuatro se
contestan con física del sensor y de la óptica, y cuatro con el menú de una cámara concreta.

<!-- indice -->

## Índice

- [1. Las familias de cámara](#1-las-familias-de-cámara)
- [2. Del fotón al número: la cadena del sensor](#2-del-fotón-al-número-la-cadena-del-sensor)
- [3. CCD y CMOS](#3-ccd-y-cmos)
- [4. La máscara de Bayer](#4-la-máscara-de-bayer)
- [5. El tamaño del sensor y la profundidad de campo](#5-el-tamaño-del-sensor-y-la-profundidad-de-campo)
- [6. Las curvas logarítmicas y el visor](#6-las-curvas-logarítmicas-y-el-visor)
- [7. Los formatos de grabación](#7-los-formatos-de-grabación)
- [8. La pregrabación](#8-la-pregrabación)
- [9. El envío desde la cámara](#9-el-envío-desde-la-cámara)
- [10. Dos cámaras grabando a la vez](#10-dos-cámaras-grabando-a-la-vez)
- [11. Los datos que el examen ha preguntado](#11-los-datos-que-el-examen-ha-preguntado)
- [12. Trazabilidad](#12-trazabilidad)

<!-- /indice -->

## 1. Las familias de cámara

**El anexo nombra tres familias, y cada una tiene su forma de trabajar:**

| Familia | Dónde | Cómo trabaja |
|---|---|---|
| **ENG** | **Reportaje e informativos** | **Autónoma**: batería, tarjeta, un operador. **Al hombro** |
| **EFP** | **Retransmisiones y producción en exteriores** | **En cadena**: cuelga de una unidad de control por triax o fibra |
| **Cinematografía digital** | **Ficción** | Autónoma, con registro propio y flujo de etalonaje |

**La distinción que ordena el resto del tema**: **una cámara ENG lo lleva todo dentro y decide sola;
una EFP delega el control de imagen en el control de cámara.** **Este punto del temario es
mayoritariamente de ENG**, porque el puesto lo es.

## 2. Del fotón al número: la cadena del sensor

**Cuatro pasos separan la luz de un fichero**, y el examen pregunta por el tercero.

1. **El fotosito convierte fotones en carga eléctrica.** Cada fotosito es un pozo que acumula carga
   en proporción a la luz que recibe.
2. **La carga se convierte en tensión** y se amplifica.
3. **El conversor analógico-digital traduce esa tensión en un número binario.**
4. **El procesador aplica la ganancia, el balance de blancos, la curva de transferencia y la
   compresión**, y escribe el fichero.

**El dispositivo que convierte las tensiones eléctricas almacenadas en cada píxel en valores digitales
de código binario es el ADC o conversor analógico-digital.** Ésa es la respuesta oficial a la pregunta
30.

**Las tres opciones falsas son piezas reales de la cadena que hacen otro paso:**

| Opción | Qué hace en realidad |
|---|---|
| «El sensor CMOS» | **El paso 1**: convierte luz en carga. **No digitaliza** |
| «El sensor CCD» | **El paso 1**, igual |
| «El circuito amplificador integrado en cada fotosito» | **El paso 2**: convierte carga en tensión y la amplifica |

**La opción d) es la trampa mejor puesta**, porque **describe una pieza que sí existe y que sí está en
cada fotosito** de un sensor de tecnología CMOS: **el amplificador**. Lo que la descarta es que
**amplifica, no digitaliza**. **La palabra que decide es «binario»**: sólo un conversor
analógico-digital produce números.

## 3. CCD y CMOS

**Son las dos tecnologías de sensor, y la diferencia está en dónde se hace la conversión.**

| | **CCD** | **CMOS** |
|---|---|---|
| **Dónde se lee la carga** | **Se transporta pozo a pozo hasta un conversor común** | **Cada fotosito tiene su propio amplificador** |
| **Obturación** | **Global**: toda la imagen a la vez | **Normalmente por barrido de líneas** |
| **Defecto característico** | ***Smear***: una raya vertical bajo una luz muy fuerte | ***Rolling shutter***: verticales inclinadas en movimiento rápido |
| **Consumo** | Mayor | **Menor** |
| **Dónde se usa hoy** | Cámaras de estudio antiguas | **Prácticamente todo** |

**El defecto que hay que saber reconocer de cada una**: **el *smear* del CCD es una columna vertical
clara que atraviesa la imagen** cuando entra una luz intensa en el cuadro; **el *rolling shutter* del
CMOS inclina las líneas verticales** cuando la cámara panea rápido o el sujeto se mueve deprisa,
**porque la imagen no se lee de golpe sino de arriba abajo**.

## 4. La máscara de Bayer

**Una máscara de Bayer es una superposición de microfiltros para sensores de imagen que permiten que
los píxeles registren las longitudes de onda de la luz.** Ésa es la respuesta oficial a la pregunta 59.

**Por qué hace falta**: **un fotosito no distingue color**. **Cuenta fotones y da un número**, sin
saber de qué longitud de onda venían. **Para que un sensor único capte color hay que poner delante de
cada fotosito un filtro que sólo deje pasar una banda del espectro.**

**Cómo está construida**: **un mosaico de filtros rojo, verde y azul en el que la mitad de los
elementos son verdes** y una cuarta parte rojos y otra cuarta parte azules. **Se pone el doble de
verdes porque el ojo humano obtiene del verde la mayor parte de la información de brillo**, como
demuestran los coeficientes de luminancia del tema 2.

**La consecuencia, que es lo que distingue un sensor con máscara de un bloque de tres sensores con
prisma dicroico**: **cada píxel conoce sólo uno de los tres colores y los otros dos hay que
interpolarlos** a partir de sus vecinos. **Ese proceso se llama *demosaicing***, y es la razón de que
un mismo sensor pueda dar imágenes distintas según el procesado.

**Las tres opciones falsas de la pregunta 59 y su error:**

| Opción | Por qué no |
|---|---|
| «Permiten que los píxeles registren SÓLO la intensidad de la luz» | **Es lo que hace un sensor SIN máscara**: eso es blanco y negro. **La máscara existe justamente para que registren color** |
| «Un filtro que consigue alta sensibilidad y alta resolución en un solo sensor» | **La máscara REDUCE la sensibilidad y la resolución de color**, no las aumenta: cada fotosito recibe sólo un tercio del espectro |
| «Un filtro destinado a limitar el tamaño mínimo de los detalles para que no se generen patrones de muaré» | **Es el filtro ÓPTICO PASO BAJO**, otra pieza real que va delante de la máscara y que hace exactamente eso |

**La opción d) es la trampa mejor puesta**, porque **describe una pieza que existe y que está justo al
lado de la máscara en el mismo bloque óptico**. **La distinción**: **la máscara de Bayer da color; el
filtro paso bajo evita el muaré.**

## 5. El tamaño del sensor y la profundidad de campo

**Las cámaras con sensores de imagen de formato completo dan menores profundidades de campo que las de
sensores de dos tercios de pulgada, partiendo de la misma resolución y a la misma distancia, porque
los sensores más grandes capturan un área mayor de la escena y por tanto requieren distancias focales
mayores para dar el mismo encuadre.** Ésa es la respuesta oficial a la pregunta 54.

**El razonamiento completo, que es el que hay que tener y no la frase:**

1. **La profundidad de campo depende de tres cosas**: **la distancia focal**, **la apertura del
   diafragma** y **la distancia de enfoque**. **El tamaño del sensor no aparece en esa lista.**
2. **Pero un sensor grande abarca más escena con la misma óptica**, así que **para conseguir el mismo
   encuadre desde el mismo sitio hay que poner una focal más larga**.
3. **Y a más focal, menos profundidad de campo**, manteniendo la distancia de enfoque.

**Por tanto: el sensor grande no reduce la profundidad de campo por sí mismo. La reduce la focal más
larga que obliga a usar.** **Ésa es la distinción que la pregunta mide**, y es la razón de que la
respuesta oficial hable de distancias focales y no de sensores.

**Las tres opciones falsas y por qué se caen:**

| Opción | Por qué no |
|---|---|
| «Los sensores más grandes son menos luminosos y se usan diafragmas más abiertos» | **Al contrario**: a igual número de píxeles, **un sensor grande tiene fotositos mayores y es MÁS sensible**. Y **un diafragma más abierto sí reduce la profundidad**, pero la premisa es falsa |
| «Los sensores más grandes multiplican la distancia focal de las ópticas» | **Es lo contrario del factor de recorte**: **son los sensores PEQUEÑOS los que "multiplican" la focal equivalente** |
| «Tienen píxeles más grandes, lo que reduce la profundidad de campo» | **El tamaño del píxel afecta al círculo de confusión aceptable, y por tanto a la profundidad**, pero **no es la causa principal ni la que la pregunta busca**: la causa es la focal |

**La consecuencia de oficio, que es lo que un operador maneja a diario**: **con una cámara de sensor
grande cuesta mucho más mantener el foco**, y **por eso los informativos han trabajado durante décadas
con sensores de dos tercios de pulgada**: **su mayor profundidad de campo perdona el error de foco en
una situación en la que no hay tiempo de medir.**

## 6. Las curvas logarítmicas y el visor

**Una curva logarítmica reparte los valores disponibles a lo largo de todo el rango dinámico del
sensor**, en lugar de concentrarlos donde quedarían bien a la vista. **El resultado es una imagen de
bajo contraste y baja saturación que conserva información en luces y sombras**, y que **exige
etalonaje**.

**Si se usa una curva logarítmica durante la grabación en 4K o UHD, sí afecta a la imagen que el
operador ve en su visor: la imagen parecerá lavada, plana, blanquecina y sin contraste, y para
previsualizar el aspecto final en el visor se debe aplicar una LUT.** Ésa es la respuesta oficial a la
pregunta 40.

**Por qué es un problema de operación y no una curiosidad**: **el operador de cámara juzga la
exposición, el foco y el encuadre por lo que ve en el visor**. **Con una imagen lavada, el contraste
no dice nada**: **no se ve si una zona está quemada ni si un rostro está bien expuesto**. **La LUT de
monitorización es la que devuelve al visor un contraste juzgable sin tocar lo que se graba.**

**La distinción que hay que tener clara**, porque es la clave de la pregunta:

| | Lo que se graba | Lo que se ve en el visor |
|---|---|---|
| **Sin LUT** | **Logarítmico** | **Logarítmico: lavado** |
| **Con LUT de monitorización** | **Logarítmico**, sin cambios | **Con el contraste aplicado: juzgable** |

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «No afectará, se visualiza correctamente» | **Sí afecta**: el visor muestra la señal tal como sale |
| «No afectará, pero en 4K y UHD sobreexponemos» | **La resolución no tiene nada que ver con la exposición**: son dos ejes independientes |
| «Sí afectará, pero conectando la cámara a un monitor por SDI se verá correctamente» | **LA TRAMPA BUENA**: **la salida por interfaz digital serie lleva la MISMA señal logarítmica**. **Un monitor conectado ahí verá exactamente la misma imagen lavada**, salvo que **el monitor aplique su propia LUT**, que es lo que la opción no dice |

**La opción c) merece detenerse**, porque **contiene un error de concepto muy extendido**: **la
interfaz digital no "corrige" nada**. **Es un transporte, no un procesador.** **Lo que sale por ella es
lo que la cámara le da.**

## 7. Los formatos de grabación

**Un mismo sistema de grabación puede escribir en varios formatos**, y **cada uno tiene su tasa de
bits y su calidad**. **El formato de menor calidad de los que el examen enumera es el Proxy AV.** Ésa
es la respuesta oficial a la pregunta 62.

| Formato | Qué es | Calidad |
|---|---|---|
| **Proxy AV** | **Una copia ligera y de baja resolución**, escrita a la vez que la buena | **La menor con diferencia** |
| **MPEG IMX** | Formato de definición estándar de tasa alta | Media |
| **MPEG HD** | Formato de alta definición | Alta |
| **DVCAM** | Formato de cinta de definición estándar | Media-baja |

**Por qué el *proxy* es el de menor calidad, y por qué eso es una virtud y no un defecto**: **no está
para verse, está para trabajar**. Una copia ligera **se transmite por una línea estrecha**, **se
visiona desde la redacción sin ocupar el material bueno** y **permite montar en baja resolución
mientras el original espera**. **Es el mismo principio del flujo *offline*-*online***.

**Las tres opciones falsas son formatos reales de mayor calidad**, y **la trampa está en «DVCA»**, que
es **una grafía incompleta de DVCAM**: quien no lo reconozca puede pensar que es un formato inventado
y descartarlo por eso, **acertando por el motivo equivocado**.

## 8. La pregrabación

**Con una cámara ENG, el modo de grabación especial que hay que activar en el menú para tener una
pregrabación antes de pulsar el botón de grabación es Picture Cache.** Ésa es la respuesta oficial a
la pregunta 57.

**Qué hace, y por qué existe**: **la cámara graba continuamente en una memoria intermedia circular
aunque no se esté grabando en el soporte**. **Al pulsar el botón, lo que se escribe en la tarjeta
incluye los segundos anteriores** que estaban en esa memoria. **El operador recupera lo que ya había
pasado.**

**El caso de uso es exactamente el del enunciado**: **una salida de juzgados, una puerta por la que va
a salir alguien en un momento que nadie controla**. **Sin pregrabación, el operador tiene dos
opciones**: grabar durante horas, **llenando la tarjeta y la batería**, o **arriesgarse a pulsar tarde
y perder el momento**. **Con pregrabación, pulsa cuando ve salir a alguien y tiene los segundos de
antes.**

**Las tres opciones falsas son modos de grabación reales que hacen otra cosa:**

| Opción | Qué hace en realidad |
|---|---|
| **Clip continuo** | **Escribe todo en un solo fichero** en lugar de cortar por tomas |
| **Grabación simultánea** | **Escribe en dos soportes a la vez**, para tener copia |
| ***Timelapse*** | **Graba un cuadro cada cierto tiempo**: es lo contrario de la pregrabación |

**La palabra que resuelve la pregunta es «antes»**: **sólo un modo escribe lo que pasó antes de
pulsar**, y **su nombre —memoria de imagen— lo dice.**

## 9. El envío desde la cámara

**En una cámara ENG con conexión a red, para poder enviar archivos grabados en la cámara por internet
a través de un teléfono móvil hay que activar el modo de punto de acceso.** Ésa es la respuesta
oficial a la pregunta 90.

**Cómo funciona el envío, en tres pasos**, que es lo que da sentido a la respuesta:

1. **La cámara no tiene línea propia a internet.** Tiene red inalámbrica, pero **necesita algo que la
   saque a la calle**.
2. **El teléfono móvil sí tiene línea**, y **puede compartirla**.
3. **El modo de punto de acceso es el que hace que la cámara se comporte como cliente de una red
   ajena** —la del teléfono— **en lugar de crear su propia red**.

**Las tres opciones falsas son ajustes reales del menú de red de la cámara**, y ahí está la
dificultad:

| Opción | Qué es en realidad |
|---|---|
| **Network** | **El menú que contiene todos los ajustes de red.** Es el contenedor, no la opción |
| **Wireless LAN** | **El interruptor general de la radio.** Enciende la red inalámbrica, **pero no decide si la cámara crea red o se une a una ajena** |
| **NFC** | **Comunicación de campo cercano**: sirve para **emparejar dos aparatos acercándolos**, no para transmitir ficheros |

**La distinción que la pregunta mide**: **encender la radio no es lo mismo que decidir a qué red se
conecta.** **Las opciones a) y c) hay que activarlas también**, pero **la que responde a lo que el
enunciado pregunta es la del modo.**

## 10. Dos cámaras grabando a la vez

**Ésta es la pregunta más larga del cuadernillo, y es un procedimiento entero de montaje.** Se
contesta con dos ideas de oficio: **cómo se sincroniza el código de tiempo** y **cómo se igualan los
ajustes de imagen**.

**El material y los ajustes necesarios para que dos cámaras ENG graben de forma idónea para el montaje
son: poner el código de tiempo de las dos cámaras en Free Run; conectar un cable de vídeo desde la
salida de vídeo de la cámara 1 a la entrada de sincronización externa de la cámara 2, y un segundo
cable desde la salida de código de tiempo de la cámara 1 a la entrada de código de tiempo de la cámara
2, hasta que aparezca en las cámaras el enlace externo y se vea que tienen el mismo código de tiempo;
y grabar en la cámara 1 la configuración de escena en una tarjeta y cargarla en la cámara 2 para
igualar sus ajustes de imagen.** Ésa es la respuesta oficial a la pregunta 101.

**Las tres cosas que la respuesta hace, y por qué cada una:**

| Qué se hace | Para qué |
|---|---|
| **Código de tiempo en marcha libre** | **Que el código siga corriendo aunque no se grabe.** Es lo que permite que las dos cámaras compartan la misma cuenta |
| **Sincronización externa desde la cámara 1** | **Que las dos cámaras vayan al mismo compás de cuadro**, sin lo cual el montaje multicámara salta |
| **Misma configuración de escena** | **Que las dos imágenes se parezcan**: mismo balance, misma gamma, mismo tratamiento. **Sin esto, el corte entre cámaras se ve** |

**Por qué las otras tres opciones se caen**, y conviene verlo porque las cuatro son largas y
parecidas:

| Opción | Qué falla |
|---|---|
| a) | **Conecta la salida de vídeo de la cámara 1 a la ENTRADA DE VÍDEO de la 2**, que **no sincroniza nada**, y **activa la grabación simultánea**, que es escribir en dos soportes de la misma cámara y no tiene nada que ver |
| b) | **Pone el código de tiempo en «Clock»** —en reloj de hora del día, que **no se puede enlazar entre dos cámaras**— y usa la **salida de interfaz digital serie** para la sincronización |
| d) | **Conecta la salida de sincronización de la cámara 1**, que **una cámara ENG normalmente no tiene**, y **omite comprobar que las dos tengan el mismo código de tiempo** |

**La regla que resuelve la pregunta sin memorizar el párrafo**: **la buena es la única que hace las
tres cosas y las hace por el camino que existe en una cámara ENG**: **marcha libre**, **la salida de
vídeo entrando por la sincronización externa** y **el archivo de escena copiado por tarjeta**.

**Y el aviso de estudio**: **es la pregunta con más letra del cuadernillo**, y **se contesta buscando
los dos errores de bulto de las otras tres** —una entrada de vídeo donde debía ir una de
sincronización, y un modo de código de tiempo que no se enlaza—, **no leyendo las cuatro de arriba
abajo.**

## 11. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 30 | Qué convierte las tensiones en código binario | b) El conversor analógico-digital ✔ |
| 40 | Si una curva logarítmica afecta al visor | d) Sí: se ve lavada y hace falta una LUT ✔ |
| 54 | Por qué un sensor grande da menos profundidad de campo | c) Requiere focales mayores para el mismo encuadre ✔ |
| 57 | Modo para tener pregrabación antes del botón | c) Picture Cache ✔ **·** sólo con la plantilla |
| 59 | Qué es una máscara de Bayer | a) Microfiltros que permiten registrar las longitudes de onda ✔ |
| 62 | Formato de grabación de menor calidad | a) Proxy AV ✔ **·** sólo con la plantilla |
| 90 | Qué activar para enviar por internet con un móvil | b) Access Point Mode ✔ **·** sólo con la plantilla |
| 101 | Material y ajustes para dos cámaras ENG simultáneas | c) Marcha libre, sincronización externa y archivo de escena ✔ **·** sólo con la plantilla |

**Las ocho respuestas oficiales son correctas**, y **cuatro descansan sólo en la plantilla**: **las
cuatro que dependen del rótulo exacto de un menú de cámara o del nombre de un formato de fabricante**.

**Las cuatro que no**: la del conversor analógico-digital, la de la curva logarítmica, la del tamaño
del sensor y la de la máscara de Bayer. **Las cuatro son física del sensor y de la óptica**, y se
sostienen en cualquier manual.

**El aviso de estudio**: **la pregunta 101 es la más larga del cuadernillo** y **se contesta por
descarte de dos errores de bulto**, no leyendo las cuatro opciones enteras. **Y la 40 castiga un error
de concepto muy extendido**: **creer que una interfaz digital corrige la señal que transporta.**

## 12. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es la tecnología del sensor, la óptica aplicada y el
manejo de una cámara, y **va como oficio**, salvo cuatro datos de menú y de catálogo que descansan en
la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Cuatro afirmaciones**: el rótulo del modo de pregrabación, el formato de menor calidad de una familia de fabricante, el rótulo del modo de red y el procedimiento completo de sincronización de dos cámaras | 57, 62, 90, 101 |

**Una declaración expresa sobre lo que no se ha podido contrastar**: **la documentación de los
fabricantes de las cámaras y de los formatos de grabación citados no se ha consultado.** Son manuales
de producto de casas comerciales, y este proyecto no ha accedido a ellos. **Las cuatro respuestas
señaladas descansan en la plantilla oficial**, que es el quinto nivel de la jerarquía de fuentes.

**Lo que este tema sí sostiene sobre esas cuatro preguntas** es el porqué: qué es una memoria
intermedia circular de grabación y por qué existe; qué es un fichero *proxy* y para qué sirve una copia
deliberadamente mala; qué diferencia hay entre encender una radio y decidir a qué red se conecta un
aparato; y qué tres cosas hay que igualar entre dos cámaras para que su material se pueda montar
—compás de cuadro, código de tiempo y ajustes de imagen—. **El rótulo lo da la plantilla; el porqué lo
da el tema.**

**El resto va como oficio y así se declara**: la cadena que va del fotón al número, la diferencia entre
las dos tecnologías de sensor y sus defectos característicos, la construcción y las consecuencias de
la máscara de Bayer, la relación entre tamaño de sensor, distancia focal y profundidad de campo, y el
comportamiento de una curva logarítmica en el visor. **Nada de eso está en un boletín oficial ni en
una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
