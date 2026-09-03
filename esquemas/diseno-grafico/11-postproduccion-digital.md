# Esquema · Tema 11 del específico de Diseño Gráfico · Postproducción digital

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de postproducción · `[exam]` =
opciones del propio cuadernillo. **Siglas**: los formatos con transparencia, por su extensión
(**PNG**, **TGA**, **TIFF**, **MOV**, **ProRes**); y los fotogramas por segundo (**fps**).

**Cabecera.** Enunciado: punto 11 del anexo · **5 preguntas** · **ninguna lleva figura** · **las cinco
son de las tres primeras palabras del enunciado**: capas, transparencias e incrustaciones. **Del audio
y de las cortinillas no ha caído ninguna.**

<!-- indice -->

## Índice

- [La capa](#la-capa)
- [Transparencia y canal alfa](#transparencia-y-canal-alfa)
- [Incrustaciones](#incrustaciones)
- [Seguimiento de movimiento](#seguimiento-de-movimiento)
- [Interpolación](#interpolación)
- [Cortinillas y audio](#cortinillas-y-audio)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La capa

- **PREGUNTA 32** · `[exam]` · **Una capa es cada una de las subdivisiones en las que organizamos el
  diseño de un grafismo.**
- **LA OBSERVACIÓN, DECLARADA**: **dos de sus cuatro opciones dicen casi lo mismo.** **La marcada
  DESCRIBE lo que una capa es; la otra sólo dice que sirve para gestionar, que es más vago.** **Se
  marca la de la plantilla, con esa observación al lado.**
- **LAS DOS FALSAS RESTANTES SON DE CINE ANALÓGICO**: **la imagen impresa en el celuloide es el
  fotograma**, y el término inglés se refiere a él.
- **QUÉ HACE UNA CAPA**: **cada elemento vive en la suya** → **el orden de apilamiento decide qué tapa
  a qué** → **cada una lleva sus propiedades animables por separado.** **Poder tocar una cosa sin
  tocar las demás es toda la razón del modelo.**

## Transparencia y canal alfa

- **PREGUNTA 35** · `[exam]` · **Una transparencia alfa es un canal que almacena información de
  opacidad.**

| Valor del alfa | Qué ocurre |
|---|---|
| **Negro, o 0** | **Totalmente transparente** |
| **Blanco, o el máximo** | **Totalmente opaco** |
| **Gris intermedio** | **Semitransparente**: es lo que da el borde suave |

- **POR QUÉ LOS GRISES SON LO IMPORTANTE**: **un recorte con sólo negro y blanco daría un borde de
  sierra.** **Un canal alfa de un bit no sirve para vídeo.**
- **LAS TRES FALSAS SON COSAS REALES DE LA MISMA SALA**: una pista de sonido, una transición de
  barrido y un formato sin comprimir. **La palabra que decide es «alfa», que sólo significa
  opacidad.**

| Formato | ¿Alfa? | Para qué |
|---|---|---|
| **`PNG`** | **Sí** | **Imagen fija sobre fondo** |
| **`TGA`** | **Sí** | **Secuencias de fotogramas** |
| **`TIFF`** | **Sí** | **Artes gráficas** |
| **`MOV` con ProRes 4444** | **Sí** | **Vídeo con transparencia** ✔ |
| **`JPG`** | **No** | **Fotografía plana** |

- **EL AVISO DE ENTREGA**: **un grafismo en formato sin alfa llega al control con un fondo negro
  pegado.** **Es el error más frecuente, y no se ve hasta que el rótulo entra en emisión.**

## Incrustaciones

- **PREGUNTA 89** · `[exam]` · **La que NO es técnica de transparencia es el *time remapping*.**

| Técnica | Qué hace | ¿Transparencia? |
|---|---|---|
| **Chroma key** | **Hace transparente un color**, normalmente verde o azul | **Sí** |
| **Canal alfa** | **Lleva la opacidad en el propio fichero** | **Sí** |
| **Luma key** | **Hace transparente según la luminosidad** | **Sí** |
| **Time remapping** | **Cambia la velocidad de reproducción** | **No: es de tiempo** ✔ |

- **LA REGLA SIN CONOCER LAS CUATRO**: **tres nombres se refieren a QUÉ se ve y uno a CUÁNDO se ve.**
  **El que habla de tiempo es el intruso.**

| | **Por color** | **Por luminancia** |
|---|---|---|
| **Qué elimina** | **Un color concreto y sus vecinos** | **Lo más claro o lo más oscuro de un umbral** |
| **Cuándo se usa** | **Plató con fondo verde o azul** | **Rótulos blancos sobre negro, humo, fuego** |
| **Qué la estropea** | **Que el sujeto vista de ese color, o mal iluminado** | **Que el sujeto tenga el mismo brillo que el fondo** |

- **POR QUÉ EL FONDO ES VERDE** · `[of]` · **porque es el color más lejano al tono de piel** y **porque
  el sensor dedica más muestras al verde**, de modo que esa señal es la más limpia y da el recorte con
  menos ruido.

## Seguimiento de movimiento

- **PREGUNTA 41** · `[exam]` · **Seguir un objeto y aplicar efectos sincronizados es el *motion
  tracking*.**

| Término | Qué es |
|---|---|
| **Motion blur** | **El desenfoque que deja un objeto al moverse deprisa** |
| **Keying** | **La incrustación de arriba** |
| **Motion tracking** | **El seguimiento de un punto o de un plano en el tiempo** ✔ |
| **Time remapping** | **El cambio de velocidad de la 89** |

- **CÓMO FUNCIONA**: **el programa elige un rasgo con contraste suficiente y lo busca fotograma a
  fotograma**, generando una trayectoria que después se aplica a lo que se quiera.

| Grado | Qué recupera | Para qué |
|---|---|---|
| **De un punto** | **Posición** | **Pegar un elemento a algo que se mueve** |
| **De dos puntos** | **Posición, escala y rotación** | **Un rótulo que acompaña a algo que se acerca** |
| **De plano** | **La deformación de una superficie** | **Sustituir la pantalla de un móvil en mano** |
| **De cámara** | **El movimiento de la cámara en el espacio** | **Meter un objeto 3D en la escena** |

- **EL AVISO DE OFICIO**: **falla cuando el punto elegido no tiene contraste, se sale del cuadro o se
  desenfoca.** **Elegir bien el punto es el noventa por ciento del trabajo.**

## Interpolación

- **PREGUNTA 88** · `[exam]` · **Los fotogramas entre dos claves son la interpolación.** **Desarrollada
  en el tema 10**, porque la pregunta cita el programa de composición.
- **LA IDEA**: **se fijan dos posiciones en el tiempo y el programa calcula lo que va en medio.** **Sin
  ella habría que dibujar cada fotograma**, que es la animación tradicional del tema 4.

## Cortinillas y audio

- **LAS CORTINILLAS ESTÁN EN EL TEMA 9**, donde el examen sí las pregunta.

| Concepto de audio | Qué es |
|---|---|
| **Sincronía** | **Que el golpe de sonido caiga en el fotograma del golpe visual** |
| **Nivel** | **Que la pieza salga al mismo volumen que el resto** |
| **Sonido de marca** | **El logotipo sonoro que acompaña al visual** |
| **Silencio** | **Una pieza sin audio se entrega con pista muda, no sin pista** |

- **EL AVISO**: **una cabecera se juzga CON sonido.** **Montada muda parece bien y con música puede
  quedar medio fotograma corta, y medio fotograma se nota.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 32 | Qué es una capa | a) Cada una de las subdivisiones del diseño ✔ **·** con observación |
| 35 | Qué es una transparencia alfa | b) Un canal de opacidad ✔ |
| 41 | Seguir el movimiento y aplicar efectos | c) Motion tracking ✔ |
| 88 | Fotogramas entre dos claves | d) Interpolación ✔ |
| 89 | Cuál NO es técnica de transparencia | d) Time remapping ✔ |

**Las cinco oficiales son correctas** · **ninguna descansa en la plantilla** · **una lleva observación
declarada.** · **Aviso de estudio**: **la tabla de técnicas de transparencia contesta dos preguntas y
descarta los distractores de una tercera.**
