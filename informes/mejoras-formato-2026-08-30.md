# Ocho mejoras del volumen, y las 65 respuestas que faltaban

**2026-08-30.** Encargo de ocho cambios sobre el volumen del bloque general, para
que sirva tal cual a quien estudia. Siete son de formato; una no lo era.

## 1. Fuera las referencias a ficheros del proyecto

El temario citaba en la ficha de cada tema dónde estaba guardado su esquema y
cómo se llamaba el informe que lo verificó, y por el cuerpo aparecían rutas de
volcados y nombres de herramientas. **A quien estudia no le dicen nada, y le
mandan a sitios a los que no puede ir.** Fuera de los nueve temas, los nueve
esquemas, el volumen impreso y el de Word: **70 líneas**.

Dos filas de la ficha desaparecen enteras —«Esquema de repaso» y
«Verificación»— y el generador de fichas **avisa** si alguna vuelve a colarse.
El rastro de la verificación no se pierde: vive en los informes, que es donde
toca.

## 2. Encabezado y pie

Encabezado **«TOAC – Temarios de Oposiciones»**; pie con **«Página X de Y»** a la
izquierda y **«Oposiciones RTVE – Temario General»** a la derecha. **La portada
va limpia**, sin uno ni otro.

En el PDF se dibujan encima de cada página, en una sola capa —hacerlo página a
página engordaba el fichero de 2 a 17 MB— y **recomprimiendo el contenido**, que
al fusionar se queda sin comprimir. En Word, con «primera página distinta» y
campos, así que el «de 254» lo cuenta Word y no hay que tocarlo cuando el
volumen crezca.

El logotipo queda para cuando haya fichero: llegó a la sesión como imagen dentro
de la conversación y desde ahí no se puede volcar a disco. La carpeta `marca/`
está preparada.

## 3. Índice con página y navegable

En **Word** es un campo de tabla de contenido: lo arma Word con los encabezados,
trae la página de verdad, se pincha para saltar y **se rehace solo** si el
documento crece al cambiarle el formato. El documento pide actualizarlo al
abrirse.

En **PDF** hubo que trabajarlo, porque **el motor que compone el PDF no sabe
contar páginas desde el documento**: no hay forma de escribir «este epígrafe
está en la página 47» antes de componerlo. Así que se compone, **se mira el PDF
para ver dónde ha caído cada ancla** —Chromium las guarda como destinos con
nombre— y se vuelve a componer con los números puestos. Como el índice crece al
llenarse y desplaza lo que viene detrás, **se repite hasta que los números dejan
de moverse**: bastan dos vueltas.

De regalo, los **marcadores** del panel de navegación del lector, con los tres
niveles.

**Una trampa que costó encontrar**: al reescribir el PDF para dibujarle el pie,
la tabla de destinos se pierde si se van añadiendo páginas sueltas. Hay que
**clonar el documento entero**; si no, el índice deja de poder pincharse.

## 4. Índice a tres niveles

`1.` el tema, `1.1` el epígrafe, `1.1.1` el subepígrafe, y sin recortes: **334
entradas** frente a las 8 × 14 de antes.

La numeración **se genera**, no se respeta la escrita. Los temas la traían a
medias —«1. Elaboración» la llevaba y «Artículo 1. Estado, soberanía» no—, así
que se quita la que venga y se pone entera. Cuerpo e índice dicen lo mismo
porque salen del mismo sitio.

## 5. Cuerpo justificado en el PDF

Ya lo estaba en Word. Ahora los dos formatos se ven igual.

## 6. El encabezado, con texto en vez de logotipo

Decisión del encargo mientras no haya fichero del logotipo.

## 7. Fuera la procedencia de cada pregunta

Debajo de cada pregunta se imprimía de qué cuadernillo salía y con qué número.
Fuera, por lo mismo que el punto 1.

Eso obligó a rehacer el apéndice: **las respuestas se identifican por el número
con el que la pregunta está impresa**, que además es como se lee. Y ha quedado
mejor de lo que estaba: en vez de una tabla de tres columnas y una fila por
pregunta, **una parrilla de diez en diez**, con las erratas de plantilla avisadas
debajo por su número.

## 8. Las 65 preguntas sin respuesta — la que no era de formato

Eran el único pendiente abierto del cuaderno. Venían de **tres plantillas
oficiales cuyo PDF no lleva tabla de caracteres**, y de las que ya se había
probado el OCR sin éxito: son tablas de dos columnas y el lector pierde la de
letras a partir de la segunda página.

**Lo que faltaba era dejar de leer la hoja y leer la celda.** Tres piezas:

1. **La geometría sale del propio PDF.** Los bordes de la tabla son dibujos
   vectoriales, así que da el rectángulo exacto de cada celda. No hay que
   adivinar dónde empieza una fila.
2. **Los códigos de la fuente son consistentes.** No sabemos qué letra es cada
   código, pero la misma letra lleva siempre el mismo. En la columna de
   respuestas hay **exactamente cuatro**. Consistentes **por página**, no por
   documento: en la plantilla de Iluminación cada página incrusta su propia
   fuente y los mismos códigos significan cosas distintas en la 2 y en la 3.
3. **El OCR solo tiene que nombrar esos cuatro**, sobre la celda recortada por
   dentro de sus bordes, ampliada y con margen blanco. Y por mayoría de varias
   celdas, no por una lectura suelta.

Se comprueba lo que se puede comprobar: que los cuatro códigos dan cuatro letras
**distintas**, que la columna de números lee **1..N sin huecos** y que el total
coincide con las preguntas del cuadernillo.

**Y se contrasta por fuera, que es lo que decide.** La lectura coincide **50 de
50** con las dos primeras páginas de la plantilla de Iluminación leídas a ojo
sobre la imagen. Y las **dos preguntas que se repiten** en cuadernillos con
plantilla legible dan la misma respuesta **aunque las opciones estén en distinto
orden**: en una, la «b» de Iluminación y la «c» de Realización A son el mismo
texto.

### Y por el camino, dos fallos que no eran del OCR

- **Ocho preguntas perdidas por un espacio.** El cuadernillo de Gestión escribe
  `101.-Seleccione`, sin espacio tras el guion, y el troceador lo exigía. Ahora
  en vez de exigir el espacio se exige que **lo que siga no sea un dígito**, que
  es lo que distingue la marca de una cifra como «1.000».
- **Diez preguntas sin respuesta por una errata en un nombre de fichero.** La
  plantilla de Ingeniero Superior Industrial se llama `..._iing_sup_industrial`,
  con una i de más, y el emparejamiento por nombre exacto la dejaba fuera. Ahora
  se acepta la más parecida **cuando el parecido es alto y no hay empate**: si
  dos se parecen lo mismo, no se elige ninguna.

## Dónde queda el volumen

| | Antes | Ahora |
|---|---|---|
| Preguntas del bloque general | 475 | **476** |
| Con respuesta oficial | 411 de 475 | **476 de 476** |
| Entradas del índice | 112 | **334** |
| Índice con número de página | no | **sí, y clicable** |
| Marcadores en el PDF | no | **sí, tres niveles** |
| Páginas | 273 | **254** |

Bajan las páginas porque el índice ya no recorta pero las preguntas ocupan
menos: la procedencia de cada una era un renglón, y eran 476.

**La pregunta que entró nueva pasó la prueba del apartado 7**: la 108 de Gestión
pregunta a partir de qué retraso hay falta grave, y el tema 5 dice **treinta
minutos, tres veces en 60 días consecutivos**.
