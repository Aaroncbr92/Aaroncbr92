# Tema 11 del específico de Diseño Gráfico · Técnicas digitales de postproducción de audio y vídeo

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Diseño Gráfico · punto 11 |
| **Sirve para** | **Diseño Gráfico** |
| **Fuente** | **Sin norma: no la hay.** Su materia son las capas, las transparencias y las incrustaciones, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Observación declarada** | **Dos de las cuatro opciones de la pregunta 32 son defendibles.** El temario dice cuál es mejor y por qué, en vez de fingir que sólo hay una |
| **Extensión** | **1.976 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: los formatos de fichero que admiten transparencia,
nombrados por su extensión (**PNG**, **TGA**, **TIFF**, **MOV**, **ProRes**); y los fotogramas por
segundo (**fps**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Diseño Gráfico, punto 11):
> «Técnicas digitales de postproducción de audio y vídeo. Capas, transparencias, incrustaciones,
> cortinillas.»

**Cinco preguntas.** **Y las cinco son de las tres primeras palabras del enunciado**: **capas,
transparencias e incrustaciones.** **Del audio y de las cortinillas no ha caído ninguna.**

**Ese desajuste conviene decirlo**: **el enunciado pide audio y el examen no lo ha preguntado nunca en
este punto**, así que **el tema lo desarrolla sin gastar en él más de lo que merece.**

<!-- indice -->

## Índice

- [1. La capa, que es la unidad de trabajo](#1-la-capa-que-es-la-unidad-de-trabajo)
- [2. La transparencia y el canal alfa](#2-la-transparencia-y-el-canal-alfa)
- [3. Las incrustaciones](#3-las-incrustaciones)
- [4. El seguimiento de movimiento](#4-el-seguimiento-de-movimiento)
- [5. La interpolación](#5-la-interpolación)
- [6. Las cortinillas y el audio, que el enunciado pide](#6-las-cortinillas-y-el-audio-que-el-enunciado-pide)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. La capa, que es la unidad de trabajo

**La pregunta 32**: **una capa es cada una de las subdivisiones en las que organizamos el diseño de un
grafismo.** Ésa es la respuesta oficial.

---

**Y hay que señalar una cosa de esta pregunta, porque el temario no puede callársela**: **dos de sus
cuatro opciones dicen casi lo mismo.** **La marcada habla de «subdivisiones en las que organizamos el
diseño» y la última de «un elemento de gestión del diseño de un grafismo».** **Las dos son
defendibles.**

**Lo que hace mejor a la marcada es que DESCRIBE lo que una capa es** —una subdivisión del trabajo—
**mientras la otra sólo dice que sirve para gestionarlo**, que es más vago. **La respuesta oficial es
la de la plantilla y se marca**, con esa observación al lado.

**Las dos opciones falsas restantes son de cine analógico**: **la imagen impresa en el celuloide es el
fotograma**, y **el término inglés que se refiere a él es *frame*.** **Ninguna de las dos es una
capa.**

**Qué hace una capa, en tres líneas, para que la definición signifique algo**: **cada elemento del
grafismo vive en su propia capa**; **el orden de apilamiento decide qué tapa a qué**; y **cada capa
lleva sus propias propiedades —posición, escala, rotación, opacidad— que se pueden animar por
separado.** **Ésa es la razón de ser del modelo: poder tocar una cosa sin tocar las demás.**

## 2. La transparencia y el canal alfa

**La pregunta 35**: **una transparencia alfa es un canal que almacena información de opacidad.** Ésa
es la respuesta oficial.

---

**Y la definición precisa es ésa**: **un cuarto canal, junto a los tres de color, que para cada píxel
dice cuánto se ve.**

| Valor del canal alfa | Qué ocurre con el píxel |
|---|---|
| **Negro, o 0** | **Totalmente transparente** |
| **Blanco, o el máximo** | **Totalmente opaco** |
| **Gris intermedio** | **Semitransparente**: es lo que hace posible un borde suave |

**Por qué los grises son lo importante y no los extremos**: **un recorte que sólo tuviera negro y
blanco daría un borde de sierra.** **Los valores intermedios son los que dan el borde limpio**, y por
eso **un canal alfa de un bit no sirve para vídeo.**

**Las tres opciones falsas son tres cosas reales de la misma sala**: **una pista de sonido, una
transición de barrido y un formato sin comprimir.** **La palabra que decide es «alfa»**, que **sólo
significa opacidad.**

**Los formatos que llevan canal alfa, que es lo que hay que saber al exportar:**

| Formato | ¿Alfa? | Para qué se usa |
|---|---|---|
| **`PNG`** | **Sí** | **Imagen fija sobre fondo** |
| **`TGA`** | **Sí** | **Secuencias de fotogramas** |
| **`TIFF`** | **Sí** | **Artes gráficas** |
| **`MOV` con ProRes 4444** | **Sí** | **Vídeo con transparencia** ✔ |
| **`JPG`** | **No** | **Fotografía plana** |

**El aviso de oficio que este cuadro deja**: **un grafismo entregado en un formato sin alfa llega al
control con un fondo negro pegado.** **Es el error de entrega más frecuente**, y no se ve hasta que
el rótulo entra en emisión.

## 3. Las incrustaciones

**La pregunta 89 es negativa**: **de las enumeradas, la que NO es una técnica de transparencia en
vídeo es el *time remapping*.** Ésa es la respuesta oficial.

---

**Las cuatro opciones, con lo que hace cada una:**

| Técnica | Qué hace | ¿Es transparencia? |
|---|---|---|
| **Chroma key** | **Hace transparente un color determinado**, normalmente verde o azul | **Sí** |
| **Canal alfa** | **Lleva la opacidad guardada en el propio fichero** | **Sí** |
| **Luma key** | **Hace transparente según la luminosidad**, no el color | **Sí** |
| **Time remapping** | **Cambia la velocidad de reproducción de una capa** | **No: es de tiempo** ✔ |

**La regla que la contesta sin conocer las cuatro**: **tres de los cuatro nombres se refieren a QUÉ se
ve y uno a CUÁNDO se ve.** **El que habla de tiempo es el intruso.**

**Y la distinción entre las dos incrustaciones por clave, que es lo preguntable de lo que no ha
caído:**

| | **Por color** | **Por luminancia** |
|---|---|---|
| **Qué elimina** | **Un color concreto y sus vecinos** | **Todo lo más claro o lo más oscuro de un umbral** |
| **Cuándo se usa** | **Plató con fondo verde o azul** | **Rótulos blancos sobre negro, humo, fuego** |
| **Qué la estropea** | **Que el sujeto vista de ese color, o que el fondo esté mal iluminado** | **Que el sujeto tenga el mismo brillo que el fondo** |

**Por qué el fondo es verde y no de otro color**: **porque es el color más lejano al tono de la piel**
y **porque el sensor de la cámara dedica más muestras al verde que a los otros dos**, de modo que **la
señal verde es la más limpia y la que da un recorte con menos ruido.**

## 4. El seguimiento de movimiento

**La pregunta 41**: **el proceso de seguir el movimiento de un objeto en un vídeo y aplicar efectos
sincronizados con él se llama *motion tracking*.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son tres términos reales de la misma sala:**

| Término | Qué es |
|---|---|
| **Motion blur** | **El desenfoque que deja un objeto al moverse deprisa** |
| **Keying** | **La incrustación del epígrafe anterior** |
| **Motion tracking** | **El seguimiento de un punto o de un plano a lo largo del tiempo** ✔ |
| **Time remapping** | **El cambio de velocidad de la pregunta 89** |

**Cómo funciona, en una línea**: **el programa elige un rasgo de la imagen con contraste suficiente y
lo busca fotograma a fotograma**, generando **una trayectoria** que después se aplica a lo que se
quiera.

**Los cuatro grados que conviene distinguir, porque el enunciado del punto los da por sabidos:**

| Grado | Qué recupera | Para qué sirve |
|---|---|---|
| **De un punto** | **Posición** | **Pegar un elemento a algo que se mueve** |
| **De dos puntos** | **Posición, escala y rotación** | **Un rótulo que acompaña a un objeto que se acerca** |
| **De plano** | **La deformación de una superficie entera** | **Sustituir la pantalla de un móvil en mano** |
| **De cámara** | **El movimiento de la cámara en el espacio** | **Meter un objeto tridimensional en la escena** |

**El aviso de oficio**: **el seguimiento falla cuando el punto elegido no tiene contraste, se sale del
cuadro o se desenfoca.** **Elegir bien el punto es el noventa por ciento del trabajo**, y **es lo que
distingue a quien lo ha hecho de quien lo ha leído.**

## 5. La interpolación

**La pregunta 88**: **el proceso de creación de fotogramas intermedios entre dos fotogramas clave se
denomina interpolación.** Ésa es la respuesta oficial.

---

**Está desarrollada en el tema 10, epígrafe 4**, porque **la pregunta cita expresamente el programa de
composición**; **aquí se recoge por pertenecer también a este punto.**

**La idea, en una línea**: **se fijan dos posiciones en el tiempo y el programa calcula todo lo que
va en medio.** **Sin ella habría que dibujar cada fotograma**, que es exactamente lo que hace la
animación tradicional del tema 4.

## 6. Las cortinillas y el audio, que el enunciado pide

**El enunciado nombra las cortinillas y el audio, y el examen no ha preguntado por ninguno de los dos
en este punto.** **Lo mínimo que conviene llevar visto:**

**Las cortinillas**: **son las piezas de transición entre bloques de emisión**, y **su desarrollo
está en el tema 9**, donde el examen sí las pregunta como parte de la continuidad.

**El audio en una pieza de grafismo, con los cuatro conceptos que un diseñador necesita:**

| Concepto | Qué es |
|---|---|
| **Sincronía** | **Que el golpe de sonido caiga en el fotograma del golpe visual** |
| **Nivel** | **Que la pieza salga al mismo volumen que el resto de la emisión** |
| **Sonido de marca** | **El logotipo sonoro que acompaña al visual** |
| **Silencio** | **Que una pieza sin audio se entregue con pista muda, no sin pista** |

**El aviso que resume el epígrafe**: **una cabecera se juzga con sonido.** **Montada muda parece bien
y con música puede quedar medio fotograma corta**, y **medio fotograma se nota.**

## 7. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 32 | Qué es una capa | a) Cada una de las subdivisiones en las que organizamos el diseño ✔ **·** con observación |
| 35 | Qué es una transparencia alfa | b) Un canal que almacena información de opacidad ✔ |
| 41 | Cómo se llama seguir el movimiento y aplicar efectos sincronizados | c) Motion tracking ✔ |
| 88 | Creación de fotogramas entre dos claves | d) Interpolación ✔ |
| 89 | Cuál NO es una técnica de transparencia | d) Time remapping ✔ |

**Las cinco respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **Una lleva
observación declarada**: la 32, cuyas opciones a y d son las dos defendibles.

**El aviso de estudio**: **la tabla de técnicas de transparencia contesta dos preguntas y descarta los
distractores de una tercera.** **Es lo más rentable del punto.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La documentación de los programas de postproducción no se ha consultado.** **Lo que el tema
   afirma del canal alfa, de las incrustaciones y del seguimiento de movimiento es de uso corriente
   en el oficio**, y **coincide con las respuestas oficiales.**
2. **La respuesta oficial de la pregunta 32 se sostiene con observación declarada**: **dos de sus
   cuatro opciones son defendibles**, y **el temario dice cuál es mejor y por qué**, en vez de fingir
   que sólo hay una.
3. **La explicación de por qué el fondo de una incrustación es verde** —lejanía del tono de piel y
   mayor densidad de muestras en ese canal— **es de uso corriente en el sector**, y **ninguna
   respuesta oficial depende de ella.**
4. **La tabla de formatos con canal alfa recoge el uso corriente de cada uno.** **Las
   especificaciones no se han consultado**, y **la misma tabla, más completa, está en el tema 10.**

**El resto del tema va como oficio y así se declara**: la razón de ser del modelo de capas, la
explicación de por qué los grises del canal alfa son lo importante, el aviso del fondo negro pegado en
la entrega, la regla del intruso que habla de tiempo, los cuatro grados de seguimiento, el consejo
sobre la elección del punto y la advertencia de juzgar una cabecera con sonido. **Nada de eso está en
un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
