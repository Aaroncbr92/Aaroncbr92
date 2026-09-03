# Esquema · Tema 10 del específico de Diseño Gráfico · Equipos y programas de diseño

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de diseño · `[exam]` = opciones
del propio cuadernillo · `[plan]` = plantilla oficial. **Siglas**: los formatos de fichero, por su
extensión (**PSD**, **TIFF**, **PNG**, **JPG**, **TGA**, **GIF**, **SVG**, **EPS**, **AI**); el modelo
de cian, magenta, amarillo y negro (**CMYK**) y el de rojo, verde y azul (**RGB**); los códecs de
vídeo (**H.264** y **H.265**); la ultraalta definición (**UHD**); la unidad de proceso gráfico
(**GPU**); y los gigabytes (**GB**).

**Cabecera.** Enunciado: punto 10 del anexo · **20 preguntas: casi una de cada cuatro del examen
específico y el banco más grande de la ocupación** · **una lleva figura** · **nueve son de un solo
programa de composición.** · **Este examen no pregunta teoría de informática: pregunta dónde está cada
cosa en el programa.**

<!-- indice -->

## Índice

- [Las familias de programa](#las-familias-de-programa)
- [Imagen fija](#imagen-fija)
- [Vectorial](#vectorial)
- [Composición y animación](#composición-y-animación)
- [Formatos, en un cuadro](#formatos-en-un-cuadro)
- [Tiempo real](#tiempo-real)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las familias de programa

| Familia | Con qué trabaja | Al ampliar | Programas del enunciado |
|---|---|---|---|
| **Mapa de bits** | **Rejilla de píxeles** | **Pierde calidad** | **Photoshop** |
| **Vectorial** | **Descripciones matemáticas de curvas** | **No pierde nada** | **Illustrator** |
| **Maquetación** | **Páginas con texto e imágenes** | **Según lo que coloque** | **InDesign** |
| **Composición y animación** | **Capas en una línea de tiempo** | **Según la capa** | **After Effects** |
| **Tres dimensiones** | **Geometría, materiales y luces** | **No pierde** | **Blender**, **Cinema 4D** |

- **PREGUNTA 78** · `[exam]` · **Se puede doblar el tamaño sin pérdida SÓLO si la imagen es
  vectorial.**
- **EL MATIZ QUE LA HACE DEFENDIBLE**: **el programa citado es de mapa de bits y admite objetos
  vectoriales dentro.** **Lo que no pierde al ampliarse es lo vectorial, esté donde esté.**
- **LA FALSA QUE MÁS ENGAÑA ES «SÍ, EN TODOS LOS CASOS»**: **una ampliación al doble con buen
  remuestreo casi no se nota**, y **«casi no se nota» no es «sin pérdida alguna».**
- **PREGUNTA 50** · `[exam]` · **El de 3D profesional es Blender.** **Las tres falsas son de otra
  familia**: maquetación, imagen fija y audio.

## Imagen fija

- **PREGUNTA 3** · `[exam]` · **Un trazado permite contornear con precisión un objeto irregular.**
- **QUÉ ES**: **una curva vectorial dentro de un documento de mapa de bits.** **No pinta píxeles:
  describe un contorno.**
- **PREGUNTA 28** · `[exam]` · **Para conservar capas, efectos y máscaras en menos de dos gigabytes,
  formato `PSD`.**
- **POR QUÉ EL ENUNCIADO DICE «DE MENOS DE 2GB»**: **el formato nativo tiene ese límite por fichero**;
  por encima hay que usar el formato grande. **Sin esa condición la respuesta sería discutible.**

| Formato | ¿Conserva capas? |
|---|---|
| **`PSD`** | **Sí: capas, efectos, máscaras, canales y trazados** ✔ |
| **`TIFF`** | **Puede llevarlas**, pero no es su cometido |
| **`TGA`** | **No.** Imagen plana con canal alfa |
| **`PNG`** | **No.** Imagen plana con transparencia |

- **PREGUNTA 82** · `[exam]` · **El máximo de canales es 56.** **Memoria pura**: **el apoyo es que 56
  es la única cifra no redonda de las cuatro, y las redondas suelen ser las inventadas.**
- **QUÉ ES UN CANAL**: **cada capa de información de color o de selección.** **Tres de color más el
  compuesto; cada máscara guardada añade un alfa.**
- **PREGUNTA 64** · `[exam]` · **El que NO admite CMYK es `PNG`.**

| Formato | Para qué nació | ¿CMYK? |
|---|---|---|
| **`PSD`** | **Trabajo en el propio programa** | **Sí** |
| **`JPG`** | **Fotografía, también imprenta** | **Sí** |
| **`TIFF`** | **Artes gráficas** | **Sí** |
| **`PNG`** | **La web**, donde todo es rojo, verde y azul | **No** ✔ |

- **LA REGLA**: **cian, magenta, amarillo y negro es el modelo de la TINTA; rojo, verde y azul el de
  la PANTALLA.** **Un formato de web no necesita el de la tinta.**

## Vectorial

- **PREGUNTA 48** · `[exam]` · **Lo que vectoriza una imagen es el calco de imagen.**

| Función | Qué hace |
|---|---|
| **Calco de imagen** | **Convierte un mapa de bits en vectores** ✔ |
| **Buscatrazos** | **Combina formas**: unir, restar, intersecar, excluir, dividir |
| **Fusión** | **Genera pasos intermedios entre dos objetos** |
| **Ajustar segmentos** | **Modifica un tramo de una curva ya dibujada** |

- **PREGUNTA 71** · `[plan]` · **La operación que da el resultado mostrado es RESTAR.** **Este esquema
  no ha visto la figura y no la describe.**

| Operación | Qué queda |
|---|---|
| **Unir** | **Una sola forma con el contorno exterior de todas** |
| **Restar** | **La de abajo menos lo que la de arriba tapaba** ✔ |
| **Intersecar** | **Sólo la zona común** |
| **Excluir** | **Todo menos la zona común**: el solape queda hueco |
| **Dividir** | **Tantas formas como trozos creen los cortes** |

- **CÓMO SE DECIDE MIRANDO**: **si desapareció un trozo de la de abajo, restar**; **si lo que
  desapareció es justo el solape, excluir**; **si lo que queda es sólo el solape, intersecar.**
- **PREGUNTA 69** · `[exam]` · **Las Bézier tienen nodo inicial, nodo final, punto de control y
  palanca de curva.** **Las cuatro opciones son la misma lista a la que le falta un elemento, salvo la
  correcta.**

## Composición y animación

- **PREGUNTA 6** · `[exam]` · **El área de trabajo es la sección de la línea de tiempo para
  previsualizar o renderizar.**
- **EL DISTRACTOR BUENO ES «EL ESPACIO DE TRABAJO PRINCIPAL»**, porque en castellano se llaman igual:
  **el área es un TRAMO DE TIEMPO, con dos asas sobre la línea; el espacio es la disposición de los
  paneles.**
- **PREGUNTA 10** · `[exam]` · **Para que dos capas trabajen como una: seleccionarlas y
  precomponer.** **Mete las capas elegidas en una composición nueva y deja una sola capa que la
  contiene.** **La falsa del atajo de duplicar hace lo contrario.**
- **PREGUNTA 18** · `[exam]` · **Con sólo capas 2D, la de primer término es la de numeración más
  baja.** **La lista se lee de arriba abajo y lo de arriba tapa a lo de abajo.**
- **LA CONDICIÓN «SÓLO CAPAS 2D» NO ES ADORNO**: **con capas 3D el orden lo decide la posición en
  profundidad**, no el número. **Ésa es la trampa que la pregunta evita al acotarlo.**
- **PREGUNTA 26** · `[exam]` · **Las luces virtuales afectan a las capas en 3D.** **Una luz es un
  objeto del espacio y una capa plana no está en el espacio.**
- **LA CONSECUENCIA PRÁCTICA**: **si se añade una luz y no pasa nada, falta activar la tercera
  dimensión en las capas.**
- **PREGUNTA 75** · `[exam]` · **El desenfoque de bordes de una máscara se anima con el calado.**

| Parámetro de máscara | Qué controla |
|---|---|
| **Trazado** | **La forma** |
| **Calado** | **Cuánto se difuminan sus bordes** ✔ |
| **Opacidad** | **Cuánto tapa** |
| **Expansión** | **Cuánto crece o encoge la forma** |

- **EL BUEN DISTRACTOR ES LA EXPANSIÓN**: **también modifica el borde, pero lo MUEVE, no lo
  difumina.**
- **PREGUNTA 88** · `[exam]` · **Los fotogramas entre dos claves son la interpolación.** **Las falsas
  son palabras parecidas de otras materias**: el interlineado es de tipografía, en el tema 5.
- **DOS TIPOS**: **espacial** —por dónde pasa el objeto— y **temporal** —a qué velocidad lo recorre—.
- **PREGUNTA 93** · `[exam]` · **El *wiggle* crea movimiento aleatorio.** **En rigor es una expresión,
  no un efecto**: se escribe sobre una propiedad y le añade una oscilación al azar, con dos números.
- **PREGUNTA 56** · `[exam]` · **«Recopilar archivos» busca los usados y crea una COPIA junto con el
  proyecto.** **La palabra que decide es COPIA**: **si los moviera, cualquier otro proyecto que los
  usara se rompería.** **Un programa serio no mueve lo que no es suyo.**
- **PARA QUÉ SIRVE**: **para llevarse un proyecto a otro equipo con todo lo que necesita.** **No
  hacerlo es la causa número uno de que un proyecto llegue con enlaces rotos.**
- **PREGUNTA 83** · `[exam]` · **Sí hay composiciones verticales, hasta 30.000 píxeles de alto.** **El
  límite es el mismo en las dos dimensiones**; **las falsas inventan una anchura mínima que no
  existe.**
- **POR QUÉ ESTÁ ESTA PREGUNTA**: **el vídeo vertical es hoy formato de trabajo corriente** en las
  piezas para redes.
- **PREGUNTA 63** · `[exam]` · **Un fotograma `TGA` SIN COMPRESIÓN ocupa lo mismo en todos los
  casos.** **El tamaño es el número de píxeles por los bytes de cada píxel, y nada más.** **Ni el
  entrelazado ni cuál sea el primer campo cambian cuántos píxeles hay.**
- **LAS TRES FALSAS SON LA MISMA IDEA EQUIVOCADA**: **creer que la organización de los datos cambia su
  volumen.** **Eso sólo ocurre con compresión, y el enunciado la excluye.**
- **PREGUNTA 81** · `[exam]` · **`H.265` admite UHD de 8K a tasas bajas y ahorra hasta el 50 % de la
  de `H.264`.** **Las tres falsas afirman lo contrario de lo cierto**: la generación nueva mejora, no
  empeora.
- **EL PRECIO QUE LAS OPCIONES NO DICEN**: **la eficiencia se paga en cálculo**, y por eso el formato
  viejo sigue siendo el compatible con todo.

## Formatos, en un cuadro

| Formato | Familia | Transparencia | Para qué |
|---|---|---|---|
| **`PSD`** | **Mapa de bits, nativo** | **Sí**, con capas | **Trabajo en curso** |
| **`AI`** | **Vectorial, nativo** | **Sí** | **Trabajo en curso** |
| **`TIFF`** | **Mapa de bits** | **Sí** | **Artes gráficas, archivo** |
| **`PNG`** | **Mapa de bits** | **Sí**, canal alfa | **Web y grafismo sobre fondo** |
| **`JPG`** | **Mapa de bits, con pérdida** | **No** | **Fotografía** |
| **`TGA`** | **Mapa de bits** | **Sí**, canal alfa | **Secuencias de fotogramas** |
| **`GIF`** | **256 colores** | **Sí**, de un solo valor | **Animaciones cortas** |
| **`SVG`** | **Vectorial** | **Sí** | **Web** |
| **`EPS`** | **Vectorial** | **Según el caso** | **Intercambio con imprenta** |

- **LA REGLA QUE DEJA**: **transparencia y web, `PNG`; capas, el nativo; secuencias renderizadas,
  `TGA`; fotografía comprimida, `JPG`.**

## Tiempo real

- **PREGUNTA 42** · `[exam]` · **Los *blueprints* son de Unreal**: **su sistema de programación
  visual**, en el que se programa uniendo nodos con cables.

| Programa | Qué es |
|---|---|
| **Unreal** | **Motor de videojuego**, hoy muy usado en televisión ✔ |
| **Unity** | **El otro motor grande**, con programación escrita |
| **Vizrt** | **Sistema de grafismo de televisión** |
| **Chyron** | **Sistema de grafismo y titulación** |

- **POR QUÉ UN MOTOR DE VIDEOJUEGO ESTÁ EN ESTE TEMARIO**: **la escenografía virtual y la realidad
  aumentada de los platós se calculan hoy con ellos.** **Lo que antes se renderizaba durante horas se
  calcula ahora en el mismo instante en que la cámara se mueve.**

| Modo | Cuándo se calcula | Ejemplos |
|---|---|---|
| **Renderizado diferido** | **Antes de emitir** | **Blender**, **Cinema 4D** |
| **Tiempo real** | **Mientras se emite** | **Unreal**, **Unity**, **Vizrt**, **Chyron** |

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 3 | Para qué sirve un trazado | a) Contornear con precisión ✔ |
| 6 | Qué es el área de trabajo | a) La sección de la línea de tiempo ✔ |
| 10 | Cómo anidar dos capas | b) Seleccionarlas y precomponer ✔ |
| 18 | Qué capa está en primer término con capas 2D | a) La de numeración más baja ✔ |
| 26 | A qué afectan las luces virtuales | b) A las capas en 3D ✔ |
| 28 | Formato que conserva capas | b) `PSD` ✔ |
| 42 | De qué programa son los *blueprints* | b) Unreal ✔ |
| 48 | Función que vectoriza | a) Calco de imagen ✔ |
| 50 | Programa profesional de 3D | b) Blender ✔ |
| 56 | Qué hace «recopilar archivos» | c) Copia los usados junto al proyecto ✔ |
| 63 | Tamaño de un `TGA` sin compresión | d) El mismo en todos los casos ✔ |
| 64 | Formato que NO admite CMYK | b) `PNG` ✔ |
| 69 | Características de las Bézier | c) Nodo inicial, final, punto de control y palanca ✔ |
| 71 | Operación de buscatrazos del resultado | a) Restar ✔ **·** figura |
| 75 | Parámetro que anima el desenfoque de una máscara | d) Calado ✔ |
| 78 | Si se puede doblar el tamaño sin pérdida | b) Sí, si es vectorial ✔ |
| 81 | Qué es `H.265` | d) Compresión que admite 8K y ahorra hasta el 50 % ✔ |
| 82 | Máximo de canales | b) 56 ✔ |
| 83 | Si hay composiciones verticales | a) Sí, hasta 30.000 píxeles ✔ |
| 93 | Qué es el *wiggle* | d) Movimiento aleatorio ✔ |

**Las veinte oficiales son correctas** · **una descansa en la plantilla**: la 71, que lleva figura. ·
**Aviso de estudio**: **nueve de las veinte son de un solo programa.** **Si el tiempo es escaso, ahí
está el rendimiento.**
