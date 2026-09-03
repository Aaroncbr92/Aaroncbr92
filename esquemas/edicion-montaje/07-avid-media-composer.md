# Esquema · Tema 7 del específico de Edición, Montaje y Procesos Audiovisuales · Edición de vídeo: Avid Media Composer

Telegrama. **Cada línea lleva delante de dónde sale**: `[plan]` = plantilla oficial, **sin
documentación de fabricante que la contraste** · `[of]` = oficio, para la arquitectura y el porqué.

**Cabecera.** Enunciado: «5.1 a 5.4 y 5.7. Edición lineal y A/B Roll · offline y online ·
postproducción en servidores · código de tiempo y multicámara · gestión de proyectos» · **13
preguntas** · **LAS TRECE DESCANSAN SÓLO EN LA PLANTILLA**: es el único punto del proyecto sin
ninguna fuente por encima del quinto nivel · **el anexo NO nombra el programa y el tribunal examina de
él punto por punto**.

<!-- indice -->

## Índice

- [El vocabulario de la casa](#el-vocabulario-de-la-casa)
- [Offline y online](#offline-y-online)
- [El bin y sus tres vistas](#el-bin-y-sus-tres-vistas)
- [Atajos y Command Palette](#atajos-y-command-palette)
- [El Match Frame](#el-match-frame)
- [El color de la barra](#el-color-de-la-barra)
- [Los grupos](#los-grupos)
- [Las herramientas de audio](#las-herramientas-de-audio)
- [Efectos y keyframes](#efectos-y-keyframes)
- [Dupe Detection y Dynamic Relink](#dupe-detection-y-dynamic-relink)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El vocabulario de la casa

| En el programa | Qué es |
|---|---|
| ***Bin*** | **La carpeta donde viven clips y secuencias** |
| **Secuencia** | **El montaje** guardado como objeto |
| ***Master clip*** | El clip original vinculado a su material |
| ***Media*** | **El material en disco, SEPARADO del proyecto** |
| ***Settings*** | **Las preferencias, que aquí son objetos** y se duplican y nombran |
| ***Command Palette*** | **El panel con todos los comandos** |

- **LA PARTICULARIDAD QUE EXPLICA MEDIA DOCENA DE PREGUNTAS**: **el proyecto y el material están
  SEPARADOS.** El proyecto guarda **decisiones**; el material vive aparte. **De ahí salen el Dynamic
  Relink, el Match Frame y la gestión de resoluciones.**

## Offline y online

| Fase | Qué es | Con qué material |
|---|---|---|
| ***Offline*** | **El montaje** | **Baja resolución**, ligero y rápido |
| ***Online*** | **El acabado**: efectos, grafismo, etalonaje | **Resolución completa** |

- **POR QUÉ EXISTIÓ**: cuando el disco era caro y lento, **montar con material ligero era la única
  forma**. **Hoy se mantiene** porque **el montaje se hace en una sala y el acabado en otra**.
- **Y ESTO EXPLICA LA PREGUNTA 15**: **el Dynamic Relink decide con qué resolución se trabaja en cada
  momento.**

## El bin y sus tres vistas

- **PREGUNTA 79** · `[plan]` · **Las tres vistas son TEXT, FRAME y SCRIPT.**

| Vista | Qué muestra | Para qué |
|---|---|---|
| **Text** | **Una tabla**: fila por clip, columna por dato | **Ordenar, buscar, ver metadatos** |
| **Frame** | **Un fotograma de cada clip** | **Reconocer material de un vistazo** |
| **Script** | **Fotogramas con espacio para escribir al lado** | **Ficción con guion**: qué dice cada toma |

- **LAS FALSAS MEZCLAN REAL E INVENTADO**: «Summary» e «Icon» **no son vistas de bin**; «Folder» y
  «Bin» **son objetos del proyecto, no vistas**.
- **LO QUE LO HACE MEMORABLE**: **las tres responden a tres formas de buscar** —**por dato, por imagen
  y por texto del guion**—, que son los tres modos de trabajar en una sala.

## Atajos y Command Palette

- **PREGUNTA 11** · `[plan]` · **El atajo de «IN» por defecto es la tecla «E».** Falsas: R, T, G.
- **DÓNDE ESTÁ**: **los comandos de marcado y edición van en la fila de la izquierda del teclado**,
  agrupados por función.
- **PREGUNTA 74** · `[plan]` · **Para editar desde la Command Palette hay que elegir «ACTIVE
  PALETTE».**
- **QUÉ HACE Y POR QUÉ SE LLAMA ASÍ**: **la paleta tiene dos modos**. En el normal **sus botones se
  ARRASTRAN** para asignarlos; **con «Active Palette», dejan de arrastrarse y se vuelven OPERATIVOS**:
  **pulsarlos ejecuta el comando desde la propia paleta**. **Ésa es la palabra: ACTIVA.**
- **LAS FALSAS SON HERRAMIENTAS REALES**: «Tool Palette» **no es el nombre de ésta** · **«Audio Tool»
  es el medidor** · **«Media Tool» es el gestor del material en disco**.

## El Match Frame

- **PREGUNTA 8** · `[plan]` · **Con MATCH FRAME, los puntos de entrada y salida del clip fuente SE
  ELIMINAN LOS DOS.**
- **QUÉ HACE LA FUNCIÓN**: **desde un cuadro de la secuencia, carga en el visor el CLIP ORIGINAL,
  posicionado exactamente en él.** Sirve para **alargar un plano cogiendo más material**.
- **POR QUÉ ELIMINA LOS PUNTOS**: **deja el clip abierto de par en par para que el montador marque
  desde ahí.** **Si conservase los puntos viejos, el material disponible quedaría acotado por una
  marca que no tiene nada que ver con lo que se busca ahora.**
- **LAS FALSAS**: «se mantienen» → contrario · «sólo el de salida» → **inventa una asimetría que no
  existe** · «se convierten en marcadores rojos» → **confunde los puntos con los *locators***.

## El color de la barra

- **PREGUNTA 56** · `[plan]` · **La barra de posición VERDE muestra, en el timeline, EL MATERIAL FUENTE
  CARGADO.**

| Color | Qué indica |
|---|---|
| **Azul** | **Se está en la SECUENCIA** |
| **Verde** | **Se está en el MATERIAL FUENTE** |

- **POR QUÉ EXISTE ESE CÓDIGO**: **el timeline puede mostrar la secuencia o el clip fuente**, y **sin
  distinguirlos un montador podría creer que edita cuando mira un clip**. **El color es el aviso.**
- **LAS FALSAS**: «nada, se personaliza» → **niega que signifique algo** · resolución distinta y audio
  par estéreo → **avisos reales del programa, pero no éste**.

## Los grupos

- **QUÉ ES UN GRUPO**: **varios clips sincronizados** —por código de tiempo, por marca o por sonido—
  **que se manejan como uno**. Es la herramienta de **multicámara**: **se salta de cámara sobre la
  marcha y el corte se hace donde se salta**.
- **PREGUNTA 54** · `[plan]` · **En el timeline, un grupo lleva «(G)» después del nombre.** Falsas:
  «(GP)», «(Grp)» y **«ninguna diferencia»**.
- **LO QUE SÍ SE PUEDE RAZONAR**: **la marca va DESPUÉS del nombre y ENTRE PARÉNTESIS**, que es la
  convención del programa. **Y «ninguna diferencia» se descarta sin saber la letra**, porque **un grupo
  y un clip se comportan distinto y el programa tiene que avisarlo.**

## Las herramientas de audio

| Herramienta | Qué hace |
|---|---|
| **Audio Mixer** | **Nivel y panorama**, por pista y por tramo |
| **Audio Tool** | **El MEDIDOR**, y **el GENERADOR DE TONO** |
| **Audio EQ Tool** | La ecualización |
| **Ganancia de clip** / **volumen** | **Dos capas distintas de nivel**: fija y automatizable |

- **PREGUNTA 36** · `[plan]` · **Panorama con SET PAN GLOBAL o SET PAN IN/OUT; nivel con SET LEVEL
  GLOBAL o SET LEVEL IN/OUT.**
- **LA CLAVE ES LA SIMETRÍA**: **panorama y nivel se comportan IGUAL**, y **cada uno tiene su versión
  global y su versión acotada**. **Las tres falsas ROMPEN esa simetría.**
- **PREGUNTA 81** · `[plan]` · **La herramienta que genera un tono junto a unas barras SMPTE es la
  AUDIO TOOL.**
- **POR QUÉ**: **es el medidor, y quien MIDE es quien genera la REFERENCIA.** **Barras y tono forman la
  cabecera técnica de una entrega**: **las barras calibran la imagen y el tono el sonido.** Falsas: el
  ecualizador, la Command Palette y el mezclador **no generan señal**.
- **PREGUNTA 52** · `[plan]` · **Para keyframes de audio en el timeline hay que tener activado el
  VOLUMEN.**
- **LA DISTINCIÓN**: **la GANANCIA DE CLIP es un valor FIJO para todo el clip; el VOLUMEN es una CURVA
  automatizable.** **Son dos capas y se suman.** «No se pueden marcar keyframes» **es falso de plano**
  y «forma de onda» **confunde la visualización con el parámetro**.

## Efectos y keyframes

- **PREGUNTA 48** · `[plan]` · **Para añadir un efecto a un clip que ya tiene otro, se mantiene pulsada
  «ALT».** **Sin la tecla, el nuevo efecto SUSTITUYE al que había; con ella, se APILA.**
- **LAS CUATRO OPCIONES DICEN QUE SÍ SE PUEDE**: **lo que se pregunta no es si se puede, sino CON QUÉ
  TECLA.**
- **PREGUNTA 82** · `[plan]` · **Los modos de interpolación son SPLINE, SHELF, LINEAR y BEZIER.**

| Modo | Cómo se comporta el valor entre dos claves |
|---|---|
| **Linear** | **En línea recta**: velocidad constante |
| **Bezier** | **Con tiradores** que el montador manipula |
| **Spline** | **Curva suave que pasa por todas las claves** |
| **Shelf** | **Sin interpolación: el valor SALTA y se mantiene** |

- **LAS TRES FALSAS SON LISTAS DE OTROS ÁMBITOS**: términos de valoración de montaje · **tipos de
  efecto de velocidad** (congelados, *timewarp*) · funciones de imagen sueltas. **Se descartan por
  coherencia interna**: **los cuatro nombres de la buena son todos términos de CURVAS.**

## Dupe Detection y Dynamic Relink

- **PREGUNTA 38** · `[plan]` · **Dupe Detection MUESTRA SI HAY ALGÚN CLIP DUPLICADO EN LA SECUENCIA.**
- **DE DÓNDE VIENE EL NOMBRE**: **en cine con copia en película, un mismo trozo de negativo NO se puede
  montar dos veces sin duplicarlo.**
- **LAS FALSAS**: clips en baja resolución → **eso es del Dynamic Relink** · llevar el cursor al
  principio → **navegación** · duplicar una selección → **lo contrario de DETECTAR duplicados**.
- **PREGUNTA 15** · `[plan]` · **El Dynamic Relink sirve para ELEGIR LA RESOLUCIÓN DE LA MEDIA (vídeo y
  audio) con la que se trabaja.**
- **POR QUÉ EXISTE**: en una casa de televisión **el mismo material está en el servidor en varias
  resoluciones a la vez**. **El Dynamic Relink dice cuál usa la sala en cada momento**, y permite
  **montar en ligera y enlazar a la completa para el acabado, sin recargar el proyecto**.
- **LA CONEXIÓN**: **es la herramienta que hace posible el flujo offline-online SIN RECONFORMAR A
  MANO.** Quien entienda esa relación **contesta sin haber tocado el programa.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 8 | Puntos de entrada y salida en MATCH FRAME | b) Ambos se eliminan ✔ **·** sólo con la plantilla |
| 11 | Atajo de «IN» | c) La tecla «E» ✔ **·** sólo con la plantilla |
| 15 | Función de «Dynamic Relink» | c) Elegir la resolución de la media ✔ **·** sólo con la plantilla |
| 36 | Panorama y nivel, a toda la pista o a un tramo | c) SET PAN / SET LEVEL, GLOBAL o IN/OUT ✔ **·** sólo con la plantilla |
| 38 | Qué hace Dupe Detection | c) Muestra clips duplicados ✔ **·** sólo con la plantilla |
| 48 | Añadir un efecto sobre otro | d) Con «Alt» ✔ **·** sólo con la plantilla |
| 52 | Qué activar para keyframes de audio | b) Volumen ✔ **·** sólo con la plantilla |
| 54 | Cómo se distingue un grupo | d) Llevan «(G)» ✔ **·** sólo con la plantilla |
| 56 | Barra de posición verde | b) Muestra el material fuente ✔ **·** sólo con la plantilla |
| 74 | Opción para editar desde la Command Palette | b) Active Palette ✔ **·** sólo con la plantilla |
| 79 | Las tres vistas de un bin | b) Text, Frame, Script ✔ **·** sólo con la plantilla |
| 81 | Herramienta que genera el tono | d) Audio Tool ✔ **·** sólo con la plantilla |
| 82 | Modos de interpolación de un keyframe | b) Spline, Shelf, Linear, Bezier ✔ **·** sólo con la plantilla |

**Las trece oficiales son correctas y LAS TRECE descansan sólo en la plantilla.** · **Aviso de
reparto**: **trece de noventa y seis salen de un programa que el anexo NO nombra: el 13,5 % del
examen.** · **Aviso de estudio**: **CINCO se contestan razonando** —las vistas del bin, la Active
Palette, el Match Frame, volumen frente a ganancia de clip y los modos de interpolación—. **Las otras
OCHO son memoria pura**: una tecla, una letra, un color, un nombre de orden. · **Y una advertencia de
método**: **este es el tema del proyecto que peor se estudia leyendo. Se aprende delante del
programa.**
