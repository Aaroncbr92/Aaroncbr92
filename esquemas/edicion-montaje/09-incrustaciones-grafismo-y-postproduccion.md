# Esquema · Tema 9 del específico de Edición, Montaje y Procesos Audiovisuales · Incrustaciones, grafismo y postproducción

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, sin norma detrás · `[plan]` =
plantilla oficial, **sin documentación de fabricante que la contraste**.

**Cabecera.** Enunciado: «5.5. Incrustaciones canal alpha, chromakey, e integración con aplicaciones
de diseño gráfico · 5.6. Colorización» · **8 preguntas** · **SEIS son de un programa concreto y
descansan sólo en la plantilla; DOS se contestan con teoría de la imagen.**

<!-- indice -->

## Índice

- [Las cuatro familias de incrustación](#las-cuatro-familias-de-incrustación)
- [Las tres señales](#las-tres-señales)
- [El canal alfa](#el-canal-alfa)
- [La máscara de capa](#la-máscara-de-capa)
- [Los tipos de capa](#los-tipos-de-capa)
- [La precomposición](#la-precomposición)
- [El recorte de trazado](#el-recorte-de-trazado)
- [El degradado](#el-degradado)
- [Los keyframes y su asistente](#los-keyframes-y-su-asistente)
- [Los plugins](#los-plugins)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las cuatro familias de incrustación

| Familia | De dónde sale el recorte |
|---|---|
| ***Chroma key*** | **DEL COLOR**: un color del fondo se vuelve transparente |
| ***Luma key*** | **DEL BRILLO**: por encima o por debajo de un nivel |
| **Canal alfa** | **DE UN CUARTO CANAL** que viene con la imagen |
| **Máscara** o *roto* | **DE UNA FORMA DIBUJADA**, fija o animada |

- **POR QUÉ EL FONDO ES VERDE O AZUL**: **son los más alejados del tono de la piel**, así que **el
  recorte no se come la cara del presentador**. **El verde se ha impuesto porque los sensores tienen el
  DOBLE de fotositos verdes** y entregan ese canal **con menos ruido**.

## Las tres señales

- **PREGUNTA 62** · **En una composición por efecto *key* intervienen TRES señales.**

| Señal | Qué es |
|---|---|
| **FONDO** (*background*) | **Lo que se ve por el agujero** |
| **RELLENO** (*fill*) | **Lo que se ve dentro de la forma** |
| **RECORTE** (*key*) | **La señal que define la FORMA del agujero** |

- **POR QUÉ TRES Y NO DOS**: **con dos imágenes no hay composición**, porque **falta decir DÓNDE acaba
  una y empieza la otra**. **En un mezclador, *key* y *fill* entran por conectores distintos.**
- **POR QUÉ NO CUATRO**: **el canal alfa NO es una cuarta señal**: es **la forma de llevar el recorte
  pegado al relleno**. **Con alfa siguen siendo tres**, sólo que dos comparten fichero.
- **LAS FALSAS SE DESCARTAN CON EL MISMO RAZONAMIENTO**: **una no compone, dos no dicen dónde, cuatro
  sobra.**

## El canal alfa

| Valor | Qué significa |
|---|---|
| **0** | **Totalmente transparente**: se ve el fondo |
| **Intermedios** | **SEMITRANSPARENTE**: se mezclan fondo y relleno |
| **Máximo** | **Totalmente opaco**: se ve el relleno |

- **LOS VALORES INTERMEDIOS SON LA RAZÓN DE SER DEL ALFA**: **sin ellos los bordes serían escalones**;
  con ellos **un borde puede estar medio dentro y medio fuera**, que es como se ve un recorte bueno.
- **DE AQUÍ SALE LA NOTACIÓN 4:4:4:4** del tema 4: **la cuarta cifra es el alfa.**

## La máscara de capa

- **PREGUNTA 31** · **Su función principal es OCULTAR O MOSTRAR PARTES ESPECÍFICAS DE UNA CAPA SIN
  ELIMINAR PERMANENTEMENTE EL CONTENIDO.**
- **LAS TRES PALABRAS QUE PESAN**: **ocultar**, **mostrar** y **sin eliminar permanentemente**. **Una
  máscara NO BORRA: TAPA.** Por eso **se puede rehacer en cualquier momento**.
- **CÓMO FUNCIONA**: **es una imagen en escala de grises pegada a la capa.** **Blanco = se ve · negro =
  no · gris = a medias.** **Es un canal alfa dibujado a mano.**
- **LAS FALSAS SON FUNCIONES REALES QUE HACEN OTRA COSA**: efectos de color · cambiar el tamaño ·
  brillo y contraste. **Ninguna oculta ni muestra.**
- **AVISO DE OFICIO**: **es la razón por la que un fichero de grafismo se puede retocar meses después.**
  **Quien recorte BORRANDO píxeles entrega un trabajo que no se puede corregir**, y en televisión los
  rótulos se corrigen siempre.

## Los tipos de capa

- **PREGUNTA 78** · `[plan]` · **Capa de FORMA, capa de AJUSTE, capa de TEXTO y OBJETO NULO.**

| Tipo | Qué es |
|---|---|
| **Texto** | Texto vectorial editable |
| **Forma** | Formas vectoriales del programa |
| **Sólido** | **Un rectángulo de color plano**, base para efectos |
| **Ajuste** | **Capa SIN contenido que aplica sus efectos a TODO lo que tiene debajo** |
| **Objeto nulo** | **Capa INVISIBLE que sirve de padre**: mueve a las enlazadas sin verse |

- **LAS FALSAS MEZCLAN REAL E INVENTADO**: **«capa de relleno manual»** y **«capa inversa»** **NO
  EXISTEN**; **«capa de fusión»** **confunde una CAPA con un MODO DE FUSIÓN**.
- **LA REGLA**: **basta reconocer los dos inventos para descartar tres de las cuatro listas.**

## La precomposición

- **PREGUNTA 35** · `[plan]` · **Para anidar dos capas y que trabajen como una: SELECCIONAR LAS DOS Y
  ELEGIR «PRECOMPONER» con el botón derecho.**
- **QUÉ HACE**: **mete las capas seleccionadas dentro de una composición nueva**, que **ocupa el sitio
  de todas ellas**. A partir de ahí **se comporta como UNA capa**.
- **PARA QUÉ**: **aplicar un efecto al conjunto y no a cada pieza**, y **ordenar**. **Es agrupar, con
  la diferencia de que se puede abrir y editar por dentro.**
- **LAS FALSAS**: «no lo permite» → **sí** · «Ctrl + D» → **eso DUPLICA** · «precomponer una y luego la
  otra» → **LA TRAMPA BUENA**: **daría DOS composiciones separadas**, y **el enunciado pide UNA SOLA**.

## El recorte de trazado

- **PREGUNTA 30** · `[plan]` · **Se aplica en TEXTOS, LÍNEAS Y RELLENOS.**
- **QUÉ ES**: **dibuja progresivamente el TRAZADO de un elemento vectorial**: anima la aparición de una
  línea o de un texto **como si se escribiera**.
- **POR QUÉ AHÍ Y NO EN OTRO SITIO**: **necesita un TRAZADO, y sólo lo tienen los elementos
  vectoriales.** **Una imagen de mapa de bits no tiene trazado.**
- **LAS FALSAS**: «capa de ajuste» → **no tiene trazado** · «modificar formas poligonales» → **el
  recorte NO CAMBIA la forma: la REVELA poco a poco** · «rotoscopia» → **usa máscaras animadas**.

## El degradado

- **PREGUNTA 75** · `[plan]` · **Las dos formas de pendiente son LINEAL y RADIAL.**

| Forma | Cómo va |
|---|---|
| **Lineal** | **De un punto a otro en recta**: bandas paralelas |
| **Radial** | **Desde un centro hacia fuera**, en círculos |

- **LAS FALSAS MEZCLAN LA BUENA CON FORMAS QUE EXISTEN EN OTROS PROGRAMAS**: **«de ángulo»** —barre
  girando— y **«de reflejado»** —se espeja a los dos lados—.
- **AVISO**: **tres de las cuatro opciones contienen «lineal» o «radial».** **Lo que hay que saber es
  que son ÉSAS DOS y sólo ésas.**

## Los keyframes y su asistente

- **PREGUNTA 95** · `[plan]` · **La interpolación se denomina DESACELERACIÓN / ACELERACIÓN SUAVE.**
- **QUÉ HACE**: **suaviza la ENTRADA Y LA SALIDA de la clave**, de modo que **el valor no arranca ni se
  detiene de golpe**. Convierte **un movimiento mecánico en uno que parece natural**.

| Opción | Qué hace |
|---|---|
| **Suavizado de entrada** | **Sólo frena a la llegada** |
| **Suavizado de salida** | **Sólo arranca despacio** |
| **De entrada y salida** | **LAS DOS COSAS**: es la respuesta |
| **Lineal** | **Sin suavizado** |

- **LAS FALSAS**: «desaceleración suave» = **SÓLO LA MITAD** · «lineal» = **lo contrario** · «escala
  exponencial» = **otra orden del asistente, que no es una interpolación de suavizado**.
- **LA REGLA**: **la buena nombra LAS DOS MITADES; la mala nombra UNA.** Es el mismo mecanismo de la
  pregunta 20 del tema 5.

## Los plugins

- **PREGUNTA 73** · `[plan]` · **Mocha, Saber y Boris Sapphire.**

| Complemento | Para qué |
|---|---|
| **Mocha** | **Seguimiento planar** y máscaras asistidas |
| **Saber** | **Efectos de luz y energía** |
| **Boris Sapphire** | **Un paquete grande de efectos** |

- **LAS TRES FALSAS MEZCLAN TRES MUNDOS**: una mete **un complemento de etalonaje de OTRO programa de
  montaje** · otra mete **DOS complementos de AUDIO** (reverberación y saturación) · otra mete **un
  banco de imágenes, un complemento de audio y una transición**.
- **CÓMO CONTESTARLA SIN CONOCER LOS PRODUCTOS**: **buscar la lista en la que los TRES nombres
  pertenecen al MISMO MUNDO.** **Sólo una es homogénea.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 30 | Dónde se aplica el recorte de trazado | d) Textos, líneas y rellenos ✔ **·** sólo con la plantilla |
| 31 | Función de una máscara de capa | b) Ocultar o mostrar sin eliminar ✔ |
| 35 | Cómo anidar dos capas | b) Seleccionarlas y «precomponer» ✔ **·** sólo con la plantilla |
| 62 | Cuántas señales en una composición por *key* | c) Tres ✔ |
| 73 | Complementos de After Effects | a) Mocha, Saber, Boris Sapphire ✔ **·** sólo con la plantilla |
| 75 | Formas de pendiente del degradado | a) Lineal y radial ✔ **·** sólo con la plantilla |
| 78 | Tipos de capa | d) Forma, ajuste, texto y objeto nulo ✔ **·** sólo con la plantilla |
| 95 | Interpolación del asistente de keyframes | b) Desaceleración / aceleración suave ✔ **·** sólo con la plantilla |

**Las ocho oficiales son correctas y SEIS descansan sólo en la plantilla.** · **Aviso de estudio**:
**CUATRO de las seis de programa se contestan por COHERENCIA INTERNA de las opciones** —los tipos de
capa inventados, la lista que mezcla audio con vídeo, la opción que hace dos composiciones en lugar de
una y la interpolación que nombra media función—. **Sólo DOS son memoria pura**: dónde se aplica el
recorte de trazado y cuáles son las dos formas de pendiente.
