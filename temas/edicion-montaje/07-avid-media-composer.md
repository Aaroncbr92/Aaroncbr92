# Tema 7 del específico de Edición, Montaje y Procesos Audiovisuales · Edición de vídeo: Avid Media Composer

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 7 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el manejo de un programa comercial de montaje que **el anexo no nombra** y del que el tribunal examina punto por punto |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Las trece preguntas de este punto descansan en la plantilla oficial**: la documentación del fabricante no se ha consultado. **Es el único punto de todo el proyecto sin ninguna fuente por encima del quinto nivel**, y el tema lo declara en lugar de fingir lo contrario |
| **Extensión** | **3.578 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la lista de decisión de edición (**EDL**); el formato
avanzado de autoría (**AAF**); el formato de intercambio de material (**MXF**); la línea de tiempo
(***timeline***), la carpeta de clips (***bin***) y el fotograma clave (***keyframe***), que en este
tema se usan en su forma inglesa porque así los rotula el programa; la Sociedad de Ingenieros de Cine
y Televisión (**SMPTE**), cuyas barras se citan; el panorama entre izquierda, centro y derecha
(**L/M/R**); y las abreviaturas de grupo que el programa escribe, **(G)**, **(GP)** y **(Grp)**.

**Y una advertencia sobre el rótulo de las órdenes.** El cuadernillo escribe en mayúsculas los nombres
de las órdenes del programa, y este tema los reproduce tal cual porque **la respuesta oficial depende
de la orden exacta**: **MATCH FRAME**, la que recupera el clip de origen; **AUDIO MIXER**, el
mezclador; **IN**, el marcado del punto de entrada; **AUDIO EQ**, el ecualizador; y las cuatro órdenes
del mezclador —**SET PAN GLOBAL**, **SET PAN IN/OUT**, **SET LEVEL GLOBAL** y **SET LEVEL IN/OUT**—,
donde **SET** es «fijar», **PAN** el panorama, **LEVEL** el nivel, **GLOBAL** «toda la pista» e
**IN/OUT** «el tramo marcado entre entrada y salida». **No son siglas: son los rótulos del programa.**

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, puntos 5.1, 5.2, 5.3, 5.4 y 5.7):
> «Conceptos básicos de edición lineal, A/B Roll, mezcladores de video.»
> «Sistemas de edición offline y online.»
> «Sistemas de postproducción en servidores de video.»
> «Código de tiempo y edición multicámara.»
> «Gestión de proyectos e importación/exportación de archivos.»

**Trece preguntas**, y **las trece son de un programa concreto**: Avid Media Composer, que es la
herramienta de montaje de la casa. **El anexo no lo nombra**, pero el tribunal ha examinado de él
punto por punto, y por eso el temario le dedica un tema entero.

**Un aviso que gobierna todo el tema**: **la documentación de Avid no se ha consultado.** Es
documentación de producto de una casa comercial, y este proyecto no ha accedido a ella. **Las trece
respuestas descansan en la plantilla oficial**, y lo que este tema aporta es **el porqué de cada una y
el mapa del programa**, que es lo que las hace estudiables y recordables.

<!-- indice -->

## Índice

- [1. El vocabulario de Avid, que no es el de otros programas](#1-el-vocabulario-de-avid-que-no-es-el-de-otros-programas)
- [2. Offline y online](#2-offline-y-online)
- [3. El bin y sus vistas](#3-el-bin-y-sus-vistas)
- [4. Los atajos y la Command Palette](#4-los-atajos-y-la-command-palette)
- [5. Los puntos de entrada y salida, y el Match Frame](#5-los-puntos-de-entrada-y-salida-y-el-match-frame)
- [6. La línea de tiempo y sus colores](#6-la-línea-de-tiempo-y-sus-colores)
- [7. Los grupos y la edición multicámara](#7-los-grupos-y-la-edición-multicámara)
- [8. Las herramientas de audio](#8-las-herramientas-de-audio)
- [9. Los efectos y los keyframes](#9-los-efectos-y-los-keyframes)
- [10. Dupe Detection y Dynamic Relink](#10-dupe-detection-y-dynamic-relink)
- [11. Los datos que el examen ha preguntado](#11-los-datos-que-el-examen-ha-preguntado)
- [12. Trazabilidad](#12-trazabilidad)

<!-- /indice -->

## 1. El vocabulario de Avid, que no es el de otros programas

**Media Composer tiene nombres propios para cosas que otros programas llaman de otra manera**, y el
examen pregunta por los suyos. **Ésta es la tabla que hay que tener antes de nada:**

| En Avid | Qué es | Cómo se llama en otros programas |
|---|---|---|
| ***Bin*** | **La carpeta donde viven los clips y las secuencias** | Proyecto, carpeta, *media pool* |
| **Secuencia** | **El montaje**: la línea de tiempo guardada como objeto | Timeline, secuencia |
| ***Master clip*** | **El clip original** vinculado a su material | Clip de origen |
| ***Subclip*** | **Un trozo marcado de un master clip** | Subclip |
| ***Media*** | **El material en disco**, separado del proyecto | *Media*, *footage* |
| ***Settings*** | **Las preferencias**, que en Avid son objetos y se pueden duplicar y nombrar | Preferencias |
| ***Command Palette*** | **El panel con todos los comandos**, para asignarlos a teclas o botones | Editor de atajos |

**La particularidad que explica media docena de preguntas de este cuadernillo**: **en Avid el proyecto
y el material están separados.** El proyecto guarda **decisiones**; el material vive aparte, en
carpetas gestionadas por el programa. **De esa separación salen el Dynamic Relink, el Match Frame y
buena parte de la gestión de resoluciones.**

## 2. Offline y online

**Es la distinción que el punto 5.2 del anexo nombra**, y conviene fijarla porque el vocabulario ha
cambiado de sentido con los años:

| Fase | Qué es | Con qué material |
|---|---|---|
| ***Offline*** | **El montaje**: decidir qué va, en qué orden y con qué duración | **Material de baja resolución**, ligero y rápido |
| ***Online*** | **El acabado**: efectos, grafismo, etalonaje y salida | **El material de resolución completa** |

**Por qué existió la separación**: cuando el disco era caro y lento, **montar con material ligero era
la única forma de trabajar**, y al final se **reconformaba** la secuencia contra el material bueno.
**Hoy la separación se mantiene** en producciones grandes, no por el disco, sino porque **el montaje
se hace en una sala y el acabado en otra**.

**Y esto es lo que explica la pregunta 15**, la del *Dynamic Relink*: **es la función que decide con
qué resolución del material se está trabajando en cada momento.**

## 3. El bin y sus vistas

**Las tres vistas diferentes que se pueden elegir en un bin son Text, Frame y Script.** Ésa es la
respuesta oficial a la pregunta 79.

| Vista | Qué muestra | Para qué sirve |
|---|---|---|
| **Text** | **Una tabla**: una fila por clip y una columna por dato | **Ordenar, buscar y ver metadatos**: código de tiempo, duración, cámara |
| **Frame** | **Un fotograma de cada clip**, como contactos | **Reconocer material de un vistazo** |
| **Script** | **Los fotogramas con espacio para escribir texto al lado** | **Montaje de ficción con guion**: se anota qué dice cada toma |

**Las tres opciones falsas de la pregunta 79 mezclan nombres reales con nombres inventados**:
«Summary» y «Icon» **no son vistas de bin**, y «Folder» y «Bin» **son objetos del proyecto, no vistas
de un bin**.

**Lo que hace memorable la respuesta**: **las tres vistas responden a tres formas de buscar** —**por
dato**, **por imagen** y **por texto del guion**—, y esa terna cubre exactamente los tres modos de
trabajar en una sala.

## 4. Los atajos y la Command Palette

**El atajo de teclado de la función «IN» en una configuración por defecto de Media Composer es la
tecla «E».** Ésa es la respuesta oficial a la pregunta 11.

**El grupo de teclas del que forma parte**, que es lo que hace la respuesta recordable: **los
comandos de marcado y de edición están en la fila de la izquierda del teclado**, agrupados por
función. **«E» marca la entrada** y las teclas contiguas cubren la salida y los comandos de inserción
y solape. **Las tres opciones falsas —«R», «T» y «G»— son teclas del mismo teclado con otros
comandos.**

**En la Command Palette, la opción que hay que elegir para editar desde ella es «Active Palette».**
Ésa es la respuesta oficial a la pregunta 74.

**Qué hace, y por qué se llama así**: la Command Palette **tiene dos modos de uso**. En el modo normal
**sus botones se arrastran a un teclado o a una interfaz** para asignarlos. **Con «Active Palette»
marcado, los botones dejan de arrastrarse y se vuelven operativos**: **pulsarlos ejecuta el comando
desde la propia paleta**. **Ésa es la palabra: activa.**

**Las tres opciones falsas son herramientas reales del programa que hacen otra cosa**: «Tool Palette»
**no es el nombre de esta paleta**; **«Audio Tool» es el medidor de audio**; y **«Media Tool» es el
gestor del material en disco**.

## 5. Los puntos de entrada y salida, y el Match Frame

**Cuando se usa la función MATCH FRAME, los puntos de entrada y salida marcados en el clip fuente se
eliminan ambos.** Ésa es la respuesta oficial a la pregunta 8.

**Qué hace un Match Frame**: **desde un cuadro de la secuencia, carga en el visor de fuente el clip
original del que salió ese cuadro, posicionado exactamente en él**. Es la función que permite
**alargar un plano cogiendo más material del original** sin buscarlo a mano.

**Por qué elimina los puntos, que es lo que hay que entender**: **el Match Frame coloca el cursor en
el cuadro coincidente y deja el clip abierto de par en par**, precisamente para que el montador
**marque desde ahí lo que quiera**. **Si conservase los puntos anteriores, el material disponible
quedaría acotado por una marca vieja** que no tiene nada que ver con lo que se está buscando ahora.

**Las tres opciones falsas**: «se mantienen los puntos originales» **es lo contrario**; «sólo se
mantiene el punto de salida» **inventa una asimetría que no existe**; y «se convierten en marcadores
rojos» **confunde los puntos de entrada y salida con los marcadores o *locators***, que son otra cosa.

## 6. La línea de tiempo y sus colores

**Que la barra de posición en el timeline sea de color verde significa que se está mostrando, en el
timeline, el material fuente cargado.** Ésa es la respuesta oficial a la pregunta 56.

**El código de color de Media Composer**, que es lo que la pregunta mide:

| Color de la barra de posición | Qué indica |
|---|---|
| **Azul** | **Se está en la secuencia**: lo que se ve es el montaje |
| **Verde** | **Se está en el material fuente**: lo que se ve es el clip cargado en el visor de origen |

**Por qué existe ese código**: **el timeline de Avid puede mostrar la secuencia o el clip fuente**, y
**si no se distinguieran, un montador podría creer que está editando cuando está mirando un clip**.
**El color es el aviso.**

**Las tres opciones falsas**: «nada, el color se puede personalizar» **niega que el color signifique
algo**; «un clip con resolución distinta al proyecto» y «un clip con audio par estéreo» **son avisos
reales del programa, pero no son éste**.

## 7. Los grupos y la edición multicámara

**El punto 5.4 del anexo pide «código de tiempo y edición multicámara»**, y el grupo de clips es la
herramienta con la que Avid la hace.

**Qué es un grupo**: **varios clips sincronizados entre sí** —por código de tiempo, por marca o por
sonido— **que se manejan como uno solo**. Al cargarlo, **se puede saltar de una cámara a otra sobre la
marcha**, y **el corte se hace en el punto en que se salta**.

**En el timeline de una secuencia, un grupo de clips se distingue de un clip porque los grupos llevan
«(G)» después del nombre del clip.** Ésa es la respuesta oficial a la pregunta 54.

**Las tres opciones falsas son la misma respuesta con otra abreviatura**: «(GP)», «(Grp)» o **ninguna
diferencia**. **Es un distractor puro de memoria**: hay que saber que es una sola letra.

**Lo que sí se puede razonar**: **la marca va después del nombre y entre paréntesis**, que es la
convención del programa para todas sus anotaciones automáticas. **La opción que dice que no hay
ninguna diferencia se descarta sin saber la letra**, porque **un grupo y un clip se comportan de
manera distinta y el programa tiene que avisarlo**.

## 8. Las herramientas de audio

**Media Composer separa el audio en varias herramientas, y el examen pregunta por tres.**

| Herramienta | Qué hace |
|---|---|
| **Audio Mixer** | **Nivel y panorama** por pista y por tramo |
| **Audio Tool** | **El medidor**, y **el generador de tono de referencia** |
| **Audio EQ Tool** | **La ecualización** |
| **Ganancia de clip** y **volumen** | **Dos capas distintas de nivel**: una fija por clip y otra automatizable |

**Desde la herramienta AUDIO MIXER, los cambios de panorama y de nivel se pueden aplicar a toda la
pista o a un tramo concreto**: **el panorama con SET PAN GLOBAL o con SET PAN IN/OUT, y el nivel con
SET LEVEL GLOBAL o con SET LEVEL IN/OUT.** Ésa es la respuesta oficial a la pregunta 36.

**La simetría es la clave de esta pregunta**: **panorama y nivel se comportan igual**, y **cada uno
tiene su versión global y su versión acotada entre entrada y salida**. **Las tres opciones falsas
rompen esa simetría**: una dice que el panorama es global y el nivel local, otra que no hay forma de
enviar los cambios, y otra que las opciones existen para el panorama pero no para el nivel. **Quien
retenga que las cuatro órdenes son simétricas contesta sin dudar.**

**La herramienta que sirve para generar un clip con un tono de características determinadas y añadirlo
a unas barras SMPTE en el timeline es la Audio Tool.** Ésa es la respuesta oficial a la pregunta 81.

**Por qué la Audio Tool y no otra**: **es el medidor, y quien mide es quien genera la referencia**.
**Un tono de referencia acompaña siempre a unas barras de color**, y los dos juntos forman la cabecera
técnica de una cinta o de un fichero de entrega: **las barras calibran la imagen y el tono calibra el
sonido**. **Las tres opciones falsas** —el ecualizador, la Command Palette y el mezclador— **son
herramientas reales que no generan señal**.

**Para poder ajustar el nivel de audio con keyframes en el timeline hay que tener activado el
volumen.** Ésa es la respuesta oficial a la pregunta 52.

**La distinción que la pregunta mide**: **la ganancia de clip es un valor fijo para todo el clip**;
**el volumen es una curva automatizable con fotogramas clave**. **Son dos capas distintas y se suman.**
**La opción c) —«en el audio no se pueden marcar keyframes»— es falsa de plano**, y la d) —«forma de
onda»— **confunde la visualización con el parámetro**: **ver la onda no permite automatizar nada.**

## 9. Los efectos y los keyframes

**En Media Composer 2018 sí se puede añadir un nuevo efecto a un clip que ya tiene otro, manteniendo
pulsada la tecla «Alt» al añadir el nuevo efecto.** Ésa es la respuesta oficial a la pregunta 48.

**Lo que la tecla hace**: **sin ella, el nuevo efecto sustituye al que había**; **con ella, se
apila encima**. **Las tres opciones falsas son las otras tres teclas modificadoras** —Control, Shift y
la combinación de las dos—, y **las cuatro opciones afirman que sí se puede**: **lo que se pregunta no
es si se puede, sino con qué tecla.**

**Los modos de interpolación de un keyframe son Spline, Shelf, Linear y Bezier.** Ésa es la respuesta
oficial a la pregunta 82.

**Qué hace cada uno**, que es lo que permite reconocer la lista:

| Modo | Cómo se comporta el valor entre dos fotogramas clave |
|---|---|
| **Linear** | **En línea recta**: velocidad constante, con cambios bruscos en cada clave |
| **Bezier** | **Con tiradores que el montador manipula** a cada lado de la clave |
| **Spline** | **Con una curva suave que pasa por todas las claves**, calculada sola |
| **Shelf** | **Sin interpolación: el valor salta y se mantiene** hasta la clave siguiente |

**Las tres opciones falsas son listas de palabras de otros ámbitos**: una mezcla términos de
valoración de montaje —ritmo, estilo, continuidad—, otra nombra **tipos de efecto de velocidad**
—congelados, efectos de movimiento, *timewarp*—, y otra junta **funciones de imagen y conceptos
sueltos**. **Ninguna de las tres es una lista de modos de interpolación**, y **se descartan por
coherencia interna antes que por conocimiento del programa**: **los cuatro nombres de la buena son
todos términos de curvas**.

## 10. Dupe Detection y Dynamic Relink

**La función Dupe Detection muestra si hay algún clip duplicado en la secuencia.** Ésa es la respuesta
oficial a la pregunta 38.

**Para qué sirve de verdad**: **avisa de que el mismo material se ha usado dos veces en el mismo
montaje**. En ficción es un error de continuidad; **en publicidad y en cine con copia en película fue
durante décadas un problema físico**, porque **un mismo trozo de negativo no se puede montar dos veces
sin duplicarlo**, de ahí el nombre.

**Las tres opciones falsas describen otras funciones reales**: mostrar clips en baja resolución **es
cosa del Dynamic Relink**; llevar el cursor al principio de la secuencia **es un comando de
navegación**; y duplicar una selección **es lo contrario de detectar duplicados**.

**El setting «Dynamic Relink» sirve, cuando se trabaja en entornos Avid Interplay, para elegir la
resolución de la media —vídeo y audio— con la que trabajamos.** Ésa es la respuesta oficial a la
pregunta 15.

**Por qué existe**: en una casa de televisión **el mismo material está en el servidor en varias
resoluciones a la vez** —una ligera para montar y una completa para emitir—. **El Dynamic Relink es la
función que dice cuál de ellas usa la sala en cada momento**, y **permite pasar de una a otra sin
recargar el proyecto**: se monta en ligera y **se enlaza a la completa para el acabado**.

**Las tres opciones falsas nombran otros ajustes reales del proyecto**: el tipo de proyecto, la
frecuencia de cuadro y el espacio de color **se eligen en otro sitio y no cambian sobre la marcha**.

**La conexión con el epígrafe 2**: **el Dynamic Relink es la herramienta que hace posible el flujo
offline-online sin reconformar a mano.** Quien entienda esa relación **contesta la pregunta sin haber
tocado el programa.**

## 11. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 8 | Qué pasa con los puntos de entrada y salida al hacer MATCH FRAME | b) Ambos puntos se eliminan ✔ **·** sólo con la plantilla |
| 11 | Atajo de teclado de la función «IN» | c) La tecla «E» ✔ **·** sólo con la plantilla |
| 15 | Función del setting «Dynamic Relink» | c) Elegir la resolución de la media ✔ **·** sólo con la plantilla |
| 36 | Aplicar panorama y nivel a toda la pista o a un tramo | c) SET PAN / SET LEVEL, GLOBAL o IN/OUT ✔ **·** sólo con la plantilla |
| 38 | Qué hace la función Dupe Detection | c) Muestra si hay algún clip duplicado ✔ **·** sólo con la plantilla |
| 48 | Cómo añadir un efecto a un clip que ya tiene otro | d) Manteniendo pulsada «Alt» ✔ **·** sólo con la plantilla |
| 52 | Qué hay que tener activado para usar keyframes de audio | b) Volumen ✔ **·** sólo con la plantilla |
| 54 | Cómo se distingue un grupo de clips en el timeline | d) Llevan «(G)» después del nombre ✔ **·** sólo con la plantilla |
| 56 | Qué significa la barra de posición verde | b) Muestra el material fuente cargado ✔ **·** sólo con la plantilla |
| 74 | Opción de la Command Palette para editar desde ella | b) Active Palette ✔ **·** sólo con la plantilla |
| 79 | Las tres vistas de un bin | b) Text, Frame, Script ✔ **·** sólo con la plantilla |
| 81 | Herramienta para generar un tono junto a las barras SMPTE | d) Audio Tool ✔ **·** sólo con la plantilla |
| 82 | Modos de interpolación de un keyframe | b) Spline, Shelf, Linear, Bezier ✔ **·** sólo con la plantilla |

**Las trece respuestas oficiales son correctas**, y **las trece descansan sólo en la plantilla**: **es
el único punto de todo el proyecto en el que ninguna afirmación tiene fuente por encima del quinto
nivel**, y el motivo está declarado en la trazabilidad.

**El aviso de reparto**: **trece preguntas de noventa y seis salen de un programa que el anexo no
nombra.** **Quien prepare este bloque sin haber tocado Media Composer pierde el 13,5 % del examen**, y
**es el punto que más renta por hora de práctica**, no de lectura.

**El aviso de estudio**: **cinco de las trece se contestan razonando** —las vistas del bin, la Active
Palette, el Match Frame, el volumen frente a la ganancia de clip y los modos de interpolación—, porque
**su lógica se deduce de para qué sirve la función**. **Las otras ocho son memoria pura**: una tecla,
una letra, un color, un nombre de orden.

## 12. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es el manejo de un programa comercial de montaje, y
**va entera como oficio y como plantilla**.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Las trece afirmaciones del tema** | 8, 11, 15, 36, 38, 48, 52, 54, 56, 74, 79, 81, 82 |

**Una declaración expresa, y es la más amplia de todo el proyecto**: **la documentación de Avid
Technology sobre Media Composer no se ha consultado.** Son manuales de producto de una casa comercial,
**y este proyecto no ha accedido a ellos**. **Las trece respuestas de este punto descansan en la
plantilla oficial**, que es el quinto nivel de la jerarquía de fuentes.

**Lo que este tema sí sostiene, y es lo que lo hace un tema y no una lista**: **la arquitectura del
programa y el porqué de cada respuesta**. La separación entre proyecto y material, que explica el
Dynamic Relink y el Match Frame; el flujo offline-online, que explica para qué hay varias resoluciones
del mismo material; la simetría de las cuatro órdenes del mezclador; la diferencia entre ganancia de
clip y volumen; el sentido de los cuatro modos de interpolación; y el origen del nombre «Dupe
Detection». **Nada de eso está en la plantilla: la plantilla sólo da la letra.**

**Y una advertencia de método**: **este es el tema del proyecto que peor se estudia leyendo**. **Trece
preguntas sobre atajos, colores y nombres de orden se aprenden delante del programa**, y el temario lo
dice en lugar de fingir lo contrario.
