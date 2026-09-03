# Tema 12 del específico de Producción · Transporte de la señal

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Producción · punto 12 |
| **Sirve para** | **Producción** |
| **Fuente** | **Sin norma en el enunciado.** Se apoya en la **Recomendación UIT-R SNG.770-2** —segundo nivel— y en la **ficha del fabricante del LiveU LU800** —cuarto nivel— |
| **Identificador** | `UIT-R SNG.770-2` · ficha del **LiveU LU800** |
| **Redacción que se estudia** | La recomendación, en su edición de 01/2012; la ficha, **tal como estaba el 03/09/2026** |
| **Aviso sobre las fuentes** | **La documentación de Avid sobre el iNEWS Command sigue cerrada**: ocho rutas probadas con agente de navegador. La respuesta a la pregunta 2 se sostiene porque **los otros tres términos sí transportan señal** |
| **Extensión** | **2.331 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la fibra hasta el hogar (**FTTH**, del inglés *fiber
to the home*); el periodismo electrónico digital por satélite (**DSNG**, del inglés *digital satellite
news gathering*) y su versión analógica (**SNG**); el enlace ascendente (***uplink***) y el descendente
(***downlink***); la cuarta y la quinta generación de telefonía móvil (**4G** y **5G**); la producción
remota multicámara (**MCRP**, del inglés *multi-camera remote production*); la línea de abonado
digital asimétrica (**ADSL**); la interfaz digital serie (**SDI**); el protocolo de internet (**IP**);
la alta definición (**HD**); y la Unión Internacional de Telecomunicaciones (**UIT**) con su Sector de
Radiocomunicaciones (**UIT-R**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Producción, punto 12):
> «TRANSPORTE DE LA SEÑAL.»

**Cuatro preguntas**, y todas sobre el mismo problema: **cómo llega la señal desde donde se produce
hasta donde se emite**.

<!-- indice -->

## Índice

- [1. Contribución y distribución](#1-contribución-y-distribución)
- [2. Las vías de transporte](#2-las-vías-de-transporte)
- [3. Qué NO es un sistema de transmisión de imágenes](#3-qué-no-es-un-sistema-de-transmisión-de-imágenes)
- [4. El enlace por satélite](#4-el-enlace-por-satélite)
- [5. Las mochilas de agregación celular](#5-las-mochilas-de-agregación-celular)
- [6. La producción remota multicámara](#6-la-producción-remota-multicámara)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Contribución y distribución

**Es la distinción que ordena el tema entero:**

| | **Contribución** | **Distribución** o emisión |
|---|---|---|
| Qué es | El transporte **hacia el centro de producción**, para seguir trabajando la señal | El transporte **hacia el espectador** |
| Calidad | **Alta**: la señal se va a manipular después | La que el sistema de emisión permita |
| Compresión | Poca o ninguna | La del sistema de emisión |
| Retardo | El menor posible | Menos crítico |
| Quién la ve | El equipo técnico | El público |

**Este punto del temario trata la contribución**: cómo se trae la señal. La distribución es materia
del tema 13, que es el que la encamina y la emite.

---

## 2. Las vías de transporte

| Vía | Cómo funciona | Ventaja | Límite |
|---|---|---|---|
| **Fibra óptica** | Circuito contratado o instalado hasta el recinto | **Capacidad y calidad**; retardo mínimo | **Hay que tenerla puesta**: no vale para lo imprevisto |
| **Enlace de microondas** | Vano de radio hasta un repetidor o hasta el centro | Rápido de montar | **Necesita visión directa** y coordinación de frecuencias |
| **Satélite (DSNG)** | Antena en el vehículo, ascendente al satélite y descendente al centro | **Llega desde cualquier sitio** | Coste, licencia y **retardo** |
| **Agregación de redes móviles** | Varias tarjetas de telefonía sumadas en una mochila | **Ligerísimo y barato** | Depende de la cobertura; latencia variable |
| **Redes de datos** (**FTTH**, líneas dedicadas) | Transporte sobre red de datos, con protocolos de contribución | Barato donde hay red | Depende de la red de un tercero |

**Y una tendencia que atraviesa las cinco: la señal viaja cada vez más sobre redes de datos y menos
sobre circuitos dedicados.** Eso abarata y complica a la vez: abarata porque la red ya existe, y
complica porque **una red compartida no garantiza por sí sola ni el ancho de banda ni el retardo**.

---

## 3. Qué NO es un sistema de transmisión de imágenes

**La pregunta 2 ofrece cuatro términos y pide el que no transmite.** La respuesta oficial es **«Avid
comand»**, que es la grafía con que el cuadernillo escribe **Avid iNEWS Command**.

| Término | Qué es | ¿Transmite? |
|---|---|---|
| **Avid Command** | **Un sistema de automatización de emisión de informativos** de Avid: dispara la escaleta y controla los equipos del control | **No** |
| **FTTH** | Fibra óptica hasta el domicilio | Sí |
| **Mochila 4G** | Unidad de agregación de redes móviles | Sí |
| **DSNG** | Periodismo electrónico digital por satélite | Sí |

**Lo que distingue al primero de los otros tres es que no mueve señal de un sitio a otro: la
gobierna.** Un sistema de automatización decide **qué se pone al aire y cuándo**; el transporte es
cosa de los otros tres.

**Y este tema declara lo que no ha podido contrastar.** La documentación de **Avid** sobre el iNEWS
Command **está cerrada**: este proyecto probó **ocho rutas con agente de navegador** y todas
respondieron «prohibido» o «no encontrado». Lo que aquí se dice de ese producto **no está verificado
en su fabricante**; lo que sí sostiene la respuesta es que **los otros tres términos sí son sistemas
de transmisión**, y eso basta para responder una pregunta formulada en negativo.

**El cuadernillo escribe «Avid comand»**, con una sola eme y en minúscula. Es una errata de grafía y
no afecta a la respuesta.

---

## 4. El enlace por satélite

**Un enlace por satélite tiene dos mitades y cada una tiene su nombre:**

| Mitad | Nombre | Qué hace |
|---|---|---|
| **Ascendente** | ***Uplink*** | **Sube la señal** de la estación terrena al satélite, con antena parabólica de gran ganancia |
| **Descendente** | ***Downlink*** | **El satélite retransmite** hacia su zona de cobertura, **en una banda de frecuencias distinta** |

**El enlace de subida de una señal a satélite se denomina *uplink*.** Ésa es la respuesta oficial a la
pregunta 34, y las tres opciones falsas son: el ***downlink***, que es **la mitad contraria**; la
**modulación en fase**, que es una técnica de modulación y no un tramo del enlace; y el **símplex**,
que es un modo de comunicación en un solo sentido.

**Por qué las dos mitades usan bandas distintas**: si el satélite reemitiera en la misma frecuencia en
la que recibe, **se realimentaría a sí mismo**. El transpondedor recibe en una banda, traslada la
señal a otra y la reemite.

**Y lo que la producción tiene que gestionar de un enlace por satélite**, que es lo que lo hace caro:
**reservar segmento espacial** —tiempo de transpondedor, que se contrata por horas—, **coordinar la
frecuencia**, **obtener la licencia** del país desde el que se sube y **comprobar que el punto de
recepción está dentro de la huella**.

**La Recomendación UIT-R SNG.770-2** describe para qué existe esta técnica: el periodismo electrónico
por satélite es **temporal y ocasional**, y a menudo **su activación no puede determinarse con gran
antelación**; se hace con **estaciones terrenas de enlace ascendente portátiles o fácilmente
transportables**. **Ésa es su razón de ser y también la razón de su precio.**

---

## 5. Las mochilas de agregación celular

**Una mochila de agregación suma varias conexiones de telefonía móvil para conseguir un canal
estable.** Es la vía que ha cambiado el directo en la última década: **pesa dos kilos, cuesta una
fracción de un enlace y llega donde hay cobertura**.

**Cómo funciona**: la unidad reparte el flujo de vídeo entre varias tarjetas —de operadores
distintos—, más red de área local y red inalámbrica si las hay, y el receptor del centro **reordena
los trozos y reconstruye la señal**. Si una conexión cae, las demás la absorben.

**Sus dos límites** son los de la red que usa: **la cobertura**, que no se controla, y **la latencia**,
que varía con la carga de la red.

**La pregunta 38 pide con qué modelo de mochilas de la marca LiveU se pueden enviar hasta cuatro
señales de alta resolución sincronizadas, y la respuesta oficial es el LU800.**

**Y la ficha del fabricante lo dice con esas palabras.** La página del producto describe el LU800 como
«the first multi-camera production-level field unit for live news and sports coverage» y precisa:

> Up to four high-res, fully frame-synced feeds from a single portable unit.

—«hasta cuatro señales de alta resolución, completamente sincronizadas fotograma a fotograma, desde
una sola unidad portátil»—, y añade que la unidad se convierte en multicámara **con la licencia
correspondiente**. La misma ficha da sus cifras de conexión: agrega **hasta catorce conexiones** con
**hasta ocho módems internos de doble tarjeta**, y soporta **hasta 60 Mbps**.

**Las tres opciones falsas se descartan así:**

- **El LU600** es un modelo anterior de la misma familia, **de una sola señal**.
- **El LU900** no corresponde a un modelo de esa gama.
- **«Con ninguno, en la actualidad es imposible»** es falso, y la ficha del fabricante lo desmiente.

**Y la pieza que hace posible la respuesta es la sincronización.** Enviar cuatro señales por una
mochila es cuestión de ancho de banda; **enviarlas sincronizadas fotograma a fotograma es lo
difícil**, porque cada una viaja por caminos distintos y llega con retardos distintos. Sin esa
sincronía, un mezclador no puede conmutar entre ellas.

---

## 6. La producción remota multicámara

**En una producción remota, las cámaras están en el acontecimiento y la realización está en el centro
de producción.** Lo que viaja no es un programa terminado: **viajan todas las señales de cámara**, y
el control las mezcla a cientos de kilómetros.

| | **Producción tradicional** | **Producción remota (MCRP)** |
|---|---|---|
| Dónde está el control | **En una unidad móvil**, en el recinto | **En el centro de producción** |
| Qué viaja | El programa ya realizado | **Todas las señales de cámara**, y los retornos hacia el recinto |
| Personal desplazado | Todo el equipo | **Sólo cámaras, sonido y técnicos de campo** |
| Coste de desplazamiento | Alto | **Mucho menor** |
| Exigencia de red | Un enlace | **Muchos, con muy baja latencia** |

**La respuesta oficial a la pregunta 41 dice que el MCRP permite la centralización de las cámaras,
facilitando la coordinación de los operadores desde un control remoto, pero que su implementación
requiere enlaces de fibra óptica de baja latencia, lo que puede generar dificultades en ubicaciones
donde la infraestructura de red no es adecuada o no existe.**

**Es correcta, y su acierto está en la segunda mitad: el problema del MCRP es la red.** Mover una
señal ya realizada necesita un enlace; mover ocho, diez o veinte señales **más los retornos, el
intercomunicador y los datos de control** necesita capacidad y, sobre todo, **latencia baja y
estable**. Sin eso, el realizador corta con retardo y los operadores de cámara reciben las órdenes
tarde.

**Las tres opciones falsas fallan cada una en un punto técnico:**

- **La a)** dice que las cámaras llevan **unidades de grabación autónomas** y que eso **reduce la
  necesidad de conectividad**. Es lo contrario: en producción remota la señal viaja **en directo**, y
  grabar en la cámara no ahorra red.
- **La b)** dice que el control remoto se hace **por ADSL** y que el problema es la congestión por
  afluencia de público. **El ADSL no da ni la capacidad ni la latencia** que esto exige, y la
  congestión de la red móvil del público no afecta a un enlace dedicado.
- **La d)** dice que las cámaras remotas **no pueden hacer ajustes manuales en tiempo real**. Es falso:
  el control de imagen ajusta las cámaras a distancia desde sus unidades de control, que es
  precisamente lo que hace posible la producción remota.

**Y la regla de lectura que este examen repite en sus preguntas largas**, ya vista en los temas 4 y 7:
**la opción correcta es la que reconoce a la vez la ventaja y el límite real**; las falsas afirman
imposibilidades o atribuyen el problema a la causa equivocada.

---

## 7. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 2 | Cuál NO es un sistema de transmisión de imágenes | a) Avid Command ✔ |
| 34 | Cómo se denomina el enlace de subida a satélite | b) *Uplink* ✔ |
| 38 | Modelo de LiveU para cuatro señales sincronizadas | c) LU 800 ✔ |
| 41 | Efecto del MCRP en la logística y sus dificultades técnicas | c) Centraliza cámaras, pero exige fibra de baja latencia ✔ |

**Las cuatro respuestas oficiales son correctas**, y **la 38 es la única de todo este examen que se
puede contrastar en la ficha del fabricante**: la página del LU800 dice literalmente «up to four
high-res, fully frame-synced feeds».

**Una anotación de grafía**: la pregunta 2 escribe **«Avid comand»** por **Avid Command**. No afecta a
la respuesta.

**Y un aviso de estudio.** Las cuatro preguntas de este punto se reparten entre **las cuatro vías del
epígrafe 2**, y ninguna repite materia: una descarta un sistema que no transporta, otra pregunta por
el satélite, otra por la agregación celular y la última por la producción remota sobre fibra. **Es de
los puntos que hay que estudiar enteros.**

---

## 8. Trazabilidad

**Dos fuentes sostienen este tema, de dos niveles distintos de la jerarquía:**

| Fuente | Nivel | Qué sostiene | Leída |
|---|---|---|---|
| **Recomendación UIT-R SNG.770-2** (01/2012), «Procedimientos operacionales uniformes para el periodismo electrónico digital por satélite (DSNG)» | Segundo: organismo de normalización | Que el periodismo por satélite es **temporal y ocasional**, que se activa **con escaso tiempo de aviso** y que se hace con **estaciones terrenas de enlace ascendente portátiles o fácilmente transportables** | Edición en español |
| **Ficha del producto LiveU LU800** | Cuarto: documentación de fabricante | Que el LU800 entrega **hasta cuatro señales de alta resolución sincronizadas fotograma a fotograma desde una sola unidad portátil**, que agrega **hasta catorce conexiones** con **ocho módems internos de doble tarjeta** y que soporta **hasta 60 Mbps** | 03/09/2026 |

**La ficha del LU800 se ha conseguido con la regla del proyecto**: ruta corta del sitio del
fabricante y agente de navegador. Es la misma casa cuya ficha del LU300S ya estaba guardada.

**Lo que va como oficio y así se declara**: la distinción entre contribución y distribución, la tabla
de vías de transporte, el funcionamiento de la agregación celular, la comparación entre producción
tradicional y remota y las gestiones que exige un enlace por satélite.

**Y una declaración expresa sobre lo que no se ha podido contrastar**: la documentación de **Avid**
sobre el **iNEWS Command** sigue cerrada —ocho rutas probadas con agente de navegador—, de modo que
lo que este tema dice de ese producto **no está verificado en su fabricante**. La respuesta a la
pregunta 2 se sostiene igual, porque lo que hay que saber para contestarla es que **los otros tres
términos sí transportan señal**.
