# Tema 8 del específico de Información Gráfica y Captación de Imagen y Sonido · Control de cámara y ajuste de imagen

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Información Gráfica y Captación de Imagen y Sonido · punto 8 |
| **Sirve para** | **Información Gráfica y Captación de Imagen y Sonido** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los circuitos de ajuste de una cámara, el reparto de tareas entre operador y control de imagen y el puesto de técnico de imagen digital, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Aviso de vocabulario** | **Un enunciado usa dos expresiones de plató que no están en ningún diccionario técnico** —«abrir la focal» por «ir al angular» y «cachear» por «asomar en el encuadre»—. **El temario las traduce** |
| **Extensión** | **3.525 palabras** |

<!-- /portada -->

Las siglas y rótulos de este tema, presentados de entrada: la unidad de control de cámara (**CCU**);
el técnico de imagen digital (**DIT**, *digital imaging technician*); el decibelio (**dB**); los tres
primarios (**RGB**); la luminancia (**Y**); el paso de diafragma (***f stop***); la
intercomunicación (***intercom***); y la captación electrónica de noticias (**ENG**) frente a la
producción electrónica en campo (**EFP**).

**Y una advertencia sobre los rótulos de los circuitos de cámara.** El cuadernillo escribe en
mayúsculas los nombres de los ajustes tal como están rotulados en el panel de control, y este tema los
reproduce igual porque **la respuesta oficial depende del rótulo exacto**: **BLACK STRETCH**, que
levanta las sombras y que el examen escribe **BLACK STRECH**; **BLACK GAMMA**, que curva la parte baja;
**LEVEL DEPEND**, que hace depender del nivel el recorte del detalle; **FREQUENCY**, que fija la banda
del realce de detalle y que el examen escribe **FREQUENCY** sin la «u»; **KNEE**, que comprime las
altas luces; y **FRENCH FLAG**, la bandera francesa. **No son siglas: son los rótulos del panel.**

> Enunciado de la convocatoria (Anexo 2, temario específico de Información Gráfica y Captación de
> Sonido, puntos 3.10 y 4.1):
> «Control de cámaras: Métodos de medición para el ajuste de cámara EFP y ENG.»
> «Cámara de video: Ajustes básicos de la cámara y óptica.»

**Siete preguntas.** Y es el punto que separa **al operador de cámara del que sólo sabe encuadrar**:
todo lo que pregunta son **circuitos de la cámara que un operador tiene que saber nombrar cuando el
control de imagen se lo pide por la intercomunicación.**

<!-- indice -->

## Índice

- [1. Quién ajusta qué](#1-quién-ajusta-qué)
- [2. La bandera francesa](#2-la-bandera-francesa)
- [3. La parte baja de la curva: las sombras](#3-la-parte-baja-de-la-curva-las-sombras)
- [4. El realce de detalle y sus dependencias](#4-el-realce-de-detalle-y-sus-dependencias)
- [5. La parte alta de la curva: el knee](#5-la-parte-alta-de-la-curva-el-knee)
- [6. La ganancia y su equivalencia en pasos](#6-la-ganancia-y-su-equivalencia-en-pasos)
- [7. El balance de blancos](#7-el-balance-de-blancos)
- [8. El técnico de imagen digital](#8-el-técnico-de-imagen-digital)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. Quién ajusta qué

**En una producción multicámara el ajuste de imagen no lo hace el operador**: lo hace **el control de
imagen**, desde la unidad de control de cámara. **El operador ejecuta lo que se le pide por la
intercomunicación**, y para eso **tiene que conocer el vocabulario**.

| Puesto | De qué responde |
|---|---|
| **Operador de cámara** | **El encuadre, el foco y el movimiento.** Y **ejecutar en la cámara lo que el control le pide** |
| **Control de imagen** | **Que todas las cámaras casen**: nivel, color, sombras, altas luces, detalle |
| **Técnico de imagen digital** | **En producciones de un solo sistema**: configuración, calidad, calibración y gestión de ficheros |

**La diferencia entre reportaje y multicámara, que es lo que este punto presupone**: **en reportaje el
operador es también el control de imagen**, y **hace los ajustes él mismo en el menú**. **En
multicámara los hace otro**, y el operador **sólo tiene que entender la orden**.

## 2. La bandera francesa

**Si un control de cámaras indica por la intercomunicación que hay que ajustar la bandera francesa de
la cámara, un operador deberá abrir a la máxima apertura de focal y rectificar la sujeción si cachea
el encuadre.** Ésa es la respuesta oficial a la pregunta 11.

**Qué es una bandera francesa**: **una pantalla opaca montada en un brazo articulado sobre la propia
cámara**, que **hace sombra al objetivo** para **evitar que una luz directa entre en el frontal y
produzca velo o destellos**. **Es una visera de quita y pon**, más grande y más orientable que el
parasol.

**Por qué el ajuste consiste en abrir el zoom al máximo**, que es la lógica de la respuesta: **el
ángulo de visión más amplio es el del extremo angular**. **Si la bandera no entra en el cuadro en el
angular, no entra en ninguna focal.** Así que **el ajuste se comprueba en el peor caso**: **se abre el
zoom todo lo que da y se mira si la bandera se ve en el borde**. Si **cachea** —si asoma en el
encuadre—, **se rectifica su posición**.

**Las tres opciones falsas y su error:**

| Opción | Qué describe |
|---|---|
| «Buscar un color azul o rojo saturado y ocupar el 80 % del encuadre» | **Un procedimiento real de ajuste de saturación y matriz**, pero **no tiene nada que ver con una bandera** |
| «Comunicarlo al equipo de iluminación para que corrijan la sombra del proyector más lejano» | **Confunde la bandera de cámara con una bandera de iluminación**: **la de cámara la ajusta el operador, no el iluminador** |
| «Seleccionar la señal de diente de sierra en la cámara» | **Es un procedimiento de ajuste de nivel con señal de prueba**, y **no interviene ninguna bandera** |

**El aviso de vocabulario que esta pregunta impone**: **«cachear» es el verbo de plató para «asomar en
el encuadre»**, y **no aparece en ningún diccionario técnico**. **Quien no lo conozca no entiende la
opción correcta.** **La misma frase usa «abrir la focal» con el significado de «ir al angular»**, que
es el uso de plató del tema 4 y **no tiene nada que ver con abrir el diafragma.**

## 3. La parte baja de la curva: las sombras

**Dos circuitos distintos actúan sobre las zonas oscuras de la imagen**, y el examen pregunta por los
dos. **Confundirlos es el error clásico.**

| Circuito | Sobre qué actúa | Qué hace | ¿Bidireccional? |
|---|---|---|---|
| **Levantado de negros** | **La señal de luminancia (Y)** | **Sólo LEVANTA las zonas de sombra** | **No: sólo en un sentido** |
| **Gamma de negros** | **Los tres canales RGB** | **Levanta o comprime la parte baja de la curva** | **Sí** |

**El circuito de levantado de negros actúa sobre la señal de luminancia y sólo funciona levantando las
zonas de sombras.** Ésa es la respuesta oficial a la pregunta 24.

**Las cuatro opciones se construyen combinando dos variables**, y hay que acertar las dos:

| Variable | Las dos posibilidades |
|---|---|
| **Sobre qué actúa** | **La luminancia (Y)** frente a **los tres canales RGB** |
| **En qué sentido** | **Sólo levanta** frente a **bidireccional** |

**La respuesta correcta es «luminancia» y «sólo levanta»**, y las tres falsas fallan en una de las
dos:

| Opción | Qué falla |
|---|---|
| «RGB y bidireccional» | **Las dos** |
| «RGB y sólo levanta» | **Sobre qué actúa** |
| «Luminancia y bidireccional» | **En qué sentido**. **Es la trampa buena**, porque acierta la mitad más difícil |

**Para qué sirve, y es lo que hace la respuesta razonable**: **levantar los negros abre las sombras y
deja ver lo que hay en ellas**, a cambio de **perder contraste** y **hacer visible el ruido que en
negro no se veía**. **Y por eso sólo levanta**: **comprimir los negros por debajo del nivel de negro
no tiene sentido**, porque **no hay nada por debajo del negro**. **Ésa es la razón física de que este
circuito sea unidireccional y el otro no.**

## 4. El realce de detalle y sus dependencias

**El realce de detalle es un circuito que aumenta el contraste local en los bordes** para que la
imagen se perciba más nítida. **Su problema es que también realza el ruido**, y **de ahí salen sus
controles.**

| Control | Qué hace |
|---|---|
| **Nivel de detalle** | **Cuánto realce se aplica** |
| **Frecuencia** | **En qué banda de detalle actúa**: bordes finos o gruesos |
| **Dependencia del nivel** | **Reduce o suprime el realce EN LAS ZONAS OSCURAS**, donde el ruido es peor |
| **Recorte** o *crispening* | Ignora las diferencias pequeñas, que suelen ser ruido |

**En una imagen diafragmada correctamente en la que hay una zona oscura y ruidosa, el parámetro de
control de cámara que puede ayudar a limpiar ese ruido es la dependencia del nivel.** Ésa es la
respuesta oficial a la pregunta 16.

**Por qué funciona**: **el ruido de una imagen bien expuesta está sobre todo en las sombras**, y **el
realce de detalle lo amplifica ahí más que en ningún sitio**. **La dependencia del nivel apaga el
realce en la parte baja de la escala**, así que **el ruido de las sombras deja de realzarse y se
disimula**, mientras **el detalle de las zonas bien iluminadas se mantiene**.

**Las tres opciones falsas y por qué se caen:**

| Opción | Qué hace en realidad |
|---|---|
| **Frecuencia** | **Cambia la banda del realce**, no lo apaga en las sombras. **Puede aliviar, no resolver** |
| **Gamma de negros** | **Curva la parte baja**: **cambia cómo se ven las sombras, no cuánto ruido tienen** |
| **Levantado de negros** | **Levanta las sombras**: **hace el ruido MÁS visible, no menos** |

**La opción d) es la trampa mejor puesta y la más instructiva**: **levantar los negros es lo primero
que se le ocurre a alguien que quiere ver mejor una sombra**, y **es exactamente lo contrario de lo que
conviene si la sombra es ruidosa**. **Levantar el negro sube el ruido con él.**

**La regla de oficio**: **el ruido de las sombras no se arregla iluminando la imagen desde el menú. Se
arregla iluminando la escena, o quitándole realce a esa parte de la escala.**

## 5. La parte alta de la curva: el knee

**El *knee* es el circuito que comprime las altas luces** para que **la información por encima del
blanco de referencia quepa dentro del margen de la señal** en lugar de recortarse de golpe.

**El efecto que tiene el ajuste del control del *knee* sobre la imagen es controlar cómo se comprimen
las altas luces para evitar la sobreexposición.** Ésa es la respuesta oficial a la pregunta 64.

**Cómo funciona, con la curva delante**: **la respuesta de la cámara es aproximadamente recta hasta un
punto —el codo, que es lo que significa la palabra— y a partir de ahí se tumba.** **Todo lo que hay
por encima del codo se representa con muchos menos niveles**, así que **cabe más margen de luz en la
señal a cambio de menos matiz en las luces.**

| Ajuste | Qué controla |
|---|---|
| **Punto del codo** | **A qué nivel empieza la compresión** |
| **Pendiente del codo** | **Cuánto se tumba la curva** a partir de ahí |
| **Recorte de blancos** | **El techo absoluto**: por encima, todo es blanco |

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «Aumenta la sensibilidad de la cámara para captar más detalle en altas luces» | **El *knee* no cambia la sensibilidad**: **reparte de otra manera lo que ya se captó** |
| «Elimina el parpadeo en las altas luces causado por la sobreexposición» | **El parpadeo tiene otras causas** —frecuencia de la red, obturación— **y no lo arregla el *knee*** |
| «Reduce la luminancia de las altas luces para oscurecer la imagen» | **LA TRAMPA BUENA**: el *knee* **sí reduce el nivel de las altas luces**, pero **no para oscurecer la imagen**: para **meter dentro del margen lo que se saldría**. **La imagen general no se oscurece** |

**La opción c) merece detenerse**, porque **describe correctamente el efecto sobre los valores y
atribuye mal el propósito**. **El enunciado pregunta por el efecto sobre la imagen**, y el efecto es
**conservar información en las luces**, no oscurecer.

**La pareja que ordena los epígrafes 3, 4 y 5**: **el levantado y la gamma de negros trabajan en la
parte baja de la curva; el *knee* en la parte alta; y el realce de detalle sobre los bordes de toda
ella.** **Un operador que tenga ese mapa entiende cualquier orden que le llegue del control.**

## 6. La ganancia y su equivalencia en pasos

**La ganancia es una amplificación electrónica de la señal**, y se mide en decibelios. **No añade luz:
amplifica lo que hay, con su ruido incluido.**

**Si se activan 6 dB de ganancia en la cámara, la equivalencia en pasos de diafragma es un paso.** Ésa
es la respuesta oficial a la pregunta 53.

**De dónde sale la equivalencia, y es una cuenta que conviene saber hacer**: **un paso de diafragma
duplica la luz**. **En decibelios de tensión, duplicar es +6 dB**, porque **20 por el logaritmo
decimal de 2 es aproximadamente 6**. **Por tanto, 6 dB de ganancia equivalen a un paso.**

| Ganancia | **Pasos de diafragma** | Precio en ruido |
|---|---|---|
| **+3 dB** | **Medio paso** | Poco |
| **+6 dB** | **1 paso** | Apreciable |
| **+12 dB** | **2 pasos** | **Mucho** |
| **+18 dB** | **3 pasos** | **La imagen ya es ruidosa** |

**Las tres opciones falsas** —medio paso, dos pasos y tres pasos— **son las equivalencias de otros
valores de ganancia**: **medio paso son 3 dB, dos pasos son 12 dB y tres pasos son 18 dB**. **La tabla
las contiene todas**, y por eso conviene aprenderla entera y no la cifra sola.

**El aviso de oficio que va con la ganancia**: **es el último recurso, no el primero.** **El orden
correcto es: abrir el diafragma, bajar la obturación si el movimiento lo permite, añadir luz y, sólo
entonces, subir ganancia.** **Cada paso de ganancia es un paso de ruido**, y **el ruido de una toma no
se quita después.**

## 7. El balance de blancos

**El balance de blancos es el ajuste de la temperatura de color de los sensores de la cámara a la
existente en la escena.** Ésa es la respuesta oficial a la pregunta 67.

**Qué hace la cámara al hacerlo**: **mide una superficie que se le presenta como blanca** y **ajusta
la ganancia relativa de los canales rojo y azul** hasta que **los tres canales dan el mismo valor**.
**A partir de ahí, lo que era blanco en la escena sale blanco en la señal**, y **todo lo demás cae en
su sitio**.

**Las tres opciones falsas y su error, que es de precisión y no de bulto:**

| Opción | Por qué no |
|---|---|
| «Ajustar la temperatura de color a la escena del rodaje» | **LA TRAMPA MEJOR PUESTA**: **es casi la respuesta, y le falta decir QUÉ se ajusta.** **No se ajusta la temperatura de color de la escena: se ajusta la de la cámara a la de la escena.** La opción, tal como está escrita, se puede leer como que se cambia la escena |
| «Equilibrar la iluminación de la escena para evitar dominantes» | **Eso lo hace el iluminador con filtros** —tema 7—, **no la cámara** |
| «Ajustar la sensibilidad de la cámara a la luz de la escena» | **Eso es la exposición y la ganancia**, no el balance |

**La opción a) es la que más gente marca**, y conviene ver exactamente por qué la d) es mejor: **la d)
dice las dos mitades** —**la temperatura de color de los sensores** y **la existente en la escena**— y
**dice en qué dirección va el ajuste**. **La a) sólo dice una mitad.** **Es el mismo mecanismo de la
pregunta 20 del tema 5 de Edición y Montaje**: **la respuesta correcta es la más completa, no la más
corta.**

**Los tres caminos para hacerlo, que es oficio de reportaje:**

| Camino | Cuándo |
|---|---|
| **Balance automático sobre una carta blanca** | **Siempre que haya tiempo**: es el fiable |
| **Preajuste de 3.200 K o 5.600 K** | **Cuando no hay tiempo** y se sabe qué luz hay |
| **Balance automático continuo** | **Cuando la luz cambia sin control**, a cambio de que **los tonos deriven en plano** |

**El aviso de oficio**: **el balance automático continuo es el enemigo del montaje.** **Dos tomas de la
misma escena salen de distinto color**, y **el montador no puede casarlas.** **En reportaje se hace
balance fijo y se rehace cuando cambia la luz.**

## 8. El técnico de imagen digital

**Entre las labores profesionales de un técnico de imagen digital está la configuración técnica de la
cámara, el control de calidad de la imagen, la calibración de monitores y la gestión de archivos y
formatos.** Ésa es la respuesta oficial a la pregunta 56.

**Qué es este puesto y de dónde ha salido**: **es el que apareció cuando la cámara dejó de ser una
máquina que se ajusta con tres mandos y se convirtió en un ordenador con menús, curvas, tablas de
consulta y formatos de fichero.** **Su trabajo está entre la cámara y la posproducción**: **garantiza
que lo que se graba es lo que el director de fotografía quiere y que llega íntegro al montaje.**

**Sus cuatro tareas, que son las cuatro de la respuesta:**

| Tarea | En qué consiste |
|---|---|
| **Configuración técnica de la cámara** | Resolución, cadencia, curva, muestreo, códec, tablas de consulta |
| **Control de calidad de la imagen** | **Vigilar exposición, foco y color con instrumentos**, no a ojo |
| **Calibración de monitores** | **Que lo que se ve en el plató sea lo que se está grabando** |
| **Gestión de archivos y formatos** | **Volcado, comprobación de integridad, copias y entrega** |

**Las tres opciones falsas atribuyen al puesto trabajo de otros:**

| Opción | De quién es en realidad |
|---|---|
| «La coordinación del equipo de producción en grandes eventos» | **De producción** |
| «La planificación de planos y su composición» | **De realización o dirección de fotografía** |
| «Diseño gráfico y digitalización de documentos del archivo histórico» | **De grafismo y de documentación** |

**La forma de contestarla**: **de las cuatro opciones, tres describen puestos que existen con otro
nombre y una describe un trabajo técnico sobre la imagen y sus ficheros.** **El nombre del puesto
—técnico de imagen— ya orienta.**

## 9. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 11 | Qué hace el operador si le piden ajustar la bandera francesa | a) Abrir al máximo el angular y rectificar si cachea ✔ |
| 16 | Qué parámetro limpia el ruido de una zona oscura | a) Dependencia del nivel ✔ |
| 24 | Cómo actúa el circuito de levantado de negros | b) Sobre la luminancia y sólo levantando ✔ |
| 53 | Equivalencia de 6 dB de ganancia en pasos | a) 1 paso ✔ |
| 56 | Labores del técnico de imagen digital | c) Configuración, calidad, calibración y gestión de ficheros ✔ |
| 64 | Qué efecto tiene el ajuste del *knee* | d) Controla cómo se comprimen las altas luces ✔ |
| 67 | Qué es el balance de blancos | d) Ajuste de la temperatura de color de los sensores a la de la escena ✔ |

**Las siete respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla**: las
siete son circuitos de cámara y vocabulario de oficio, verificables en cualquier manual de operación y
en la práctica del control de imagen.

**Tres avisos de estudio.** **La pregunta 24 combina dos variables** —sobre qué actúa y en qué
sentido— **y hay que acertar las dos**. **La 16 tiene como trampa el ajuste que empeora el problema**:
levantar los negros sube el ruido con ellos. **Y la 67 tiene una opción que dice media verdad**: la
respuesta correcta es la que dice qué se ajusta y a qué.

**Un aviso de vocabulario**: **el enunciado de la pregunta 11 usa dos expresiones de plató que no están
en ningún diccionario técnico** —«abrir la focal» por «ir al angular» y «cachear» por «asomar en el
encuadre»—. **Quien no las conozca no entiende la opción correcta**, y el temario las traduce en su
epígrafe.

## 10. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los circuitos de ajuste de una cámara, el reparto
de tareas entre operador y control de imagen y el puesto de técnico de imagen digital, y **va entera
como oficio**.

**Ninguna de sus siete respuestas descansa sólo en la plantilla.** El comportamiento de los circuitos
de sombras, del realce de detalle y del *knee*, la equivalencia entre decibelios de ganancia y pasos de
diafragma, la definición de balance de blancos y las tareas del técnico de imagen digital **son
conocimiento asentado del oficio**, y **la equivalencia de los 6 dB es además una cuenta comprobable**:
**veinte veces el logaritmo decimal de dos son aproximadamente seis.**

**Dos declaraciones expresas:**

1. **Los nombres de los circuitos varían de un fabricante a otro.** **El levantado de negros, la gamma
   de negros, la dependencia del nivel y el codo de altas luces se rotulan con nombres distintos según
   la casa**, y **lo que este tema fija es qué hace cada circuito**, no cómo se llama en un modelo
   concreto. **La documentación de ningún fabricante se ha consultado**, y **ninguna respuesta depende
   de una especificación de catálogo**: lo que se pregunta es **el comportamiento**, que es común.
2. **El vocabulario de plató que el examen usa no está normalizado.** **«Bandera francesa», «cachear» y
   «abrir la focal» son expresiones de oficio**, transmitidas en la práctica y **con variantes según el
   equipo**. **El tema las traduce y advierte de ello**, porque **una pregunta que se contesta con
   vocabulario no escrito en ninguna parte es una pregunta que hay que explicar antes de responder.**
