# Esquema · Tema 5 del específico de Ingeniería Superior · Telecomunicación · La señal de televisión

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de televisión · `[plan]` =
enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: el hercio (**Hz**);
el milisegundo (**ms**); el bit por segundo con sus múltiplos **Mbit/s** y **Gbit/s**; y las notaciones
de formato **1080i50**, **1080p25**, **1080p50** y **2160p50**, que se leen en el primer epígrafe.

**Cabecera.** Enunciado: punto 5 del anexo · **tres preguntas** · **sin norma**: el punto no nombra
ninguna y el tema va como oficio.

**La idea que lo ordena** · `[of]` · **Casi todas las preguntas de este punto son de ARITMÉTICA**, y
**se fallan por leer mal la unidad**: campos por cuadros, cuadro por campo, línea por imagen entera.

<!-- indice -->

## Índice

- [Barrido y notación](#barrido-y-notación)
- [Las dos familias de cadencia](#las-dos-familias-de-cadencia)
- [Sincronismo y borrado](#sincronismo-y-borrado)
- [El color](#el-color)
- [El submuestreo](#el-submuestreo)
- [Las tres cuentas](#las-tres-cuentas)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Barrido y notación

| | **Progresivo** | **Entrelazado** |
|---|---|---|
| **Cómo recorre** | **todas las líneas en orden** | **impares y pares en dos campos** |
| **Por cuadro** | **un cuadro entero** | **dos campos de medio cuadro** |
| **Banda a igual cadencia** | **el doble** | **la mitad** |
| **Qué gana** | **nitidez en movimiento y detalle vertical** | **ancho de banda** |
| **Qué pierde** | **nada, salvo banda** | **peine y parpadeo de línea** |

- **la lectura histórica** · `[of]` · **El entrelazado se inventó para engañar al ojo con la mitad de
  información**: **refresca al doble de frecuencia de la que manda imágenes completas.** **Fue un
  compromiso genial cuando el problema era la banda**, y **hoy complica comprimir, escalar, convertir
  de norma y congelar un cuadro.**
- **LA TRAMPA DE LA NOTACIÓN** · `[exam]` · **La cifra que va detrás de la letra no significa lo mismo
  en las dos.** **En entrelazado son CAMPOS; en progresivo, CUADROS.** **Por eso 1080i50 y 1080p25
  mandan las mismas imágenes completas por segundo, y 1080p50 ocupa el doble.**

## Las dos familias de cadencia

| Familia | Cadencia | Dónde |
|---|---|---|
| **de 50** | **50 campos o 25 cuadros** | **Europa y buena parte del mundo** |
| **de 60** | **60 campos o 30 cuadros, con la variante de 59,94** | **América y Japón** |

- **por qué la red eléctrica** · `[of]` · **Si la luz del plató parpadea a la frecuencia de la red y la
  cámara explora a otra cadencia, aparece una banda que recorre la imagen.** **Sincronizar la cadencia
  con la red la elimina.**
- **LA CONSECUENCIA QUE SE PREGUNTA** · `[exam]` · **Una señal que llega de América es, con mucha mayor
  probabilidad, de la familia de sesenta.** **Ante opciones que mezclan las dos familias, la de sesenta
  es la que corresponde.**
- **la variante de 59,94** · `[of]` · **Es la de sesenta bajada en una parte por mil**, **herencia de
  la introducción del color sobre un sistema que ya emitía en blanco y negro.** **Su rastro es el
  código de tiempo con salto de cuadro, que descarta NÚMEROS de cuadro y no cuadros.**

## Sincronismo y borrado

| Parte | Qué es |
|---|---|
| **línea activa** | **la parte con imagen** |
| **borrado horizontal** | **el hueco entre líneas** |
| **borrado vertical** | **el hueco entre imágenes** |
| **sincronismos** | **las marcas de dónde empieza cada línea y cada imagen** |

- **por qué el borrado sigue existiendo en digital** · `[of]` · **En analógico daba tiempo al haz a
  volver; en digital no hay haz.** **Se conserva por compatibilidad de estructura y, sobre todo,
  porque es DONDE CABEN LOS DATOS AUXILIARES**: **audio embebido, código de tiempo, subtítulos y
  metadatos.** **El hueco se convirtió en el canal de servicio de la señal.**
- **las referencias de una instalación** · `[of]` · **negro con ráfaga** para definición estándar ·
  **sincronismo de tres niveles** para alta definición · **reloj de palabra** para el audio digital ·
  **referencia de precisión por red** para una instalación sobre paquetes, tema 19.
- **LA REGLA DE INSTALACIÓN** · `[of]` · **Una instalación tiene UNA referencia maestra y todo lo demás
  se engancha a ella.** **Dos referencias independientes producen deslizamiento**, y **el
  deslizamiento se ve como un salto o se oye como un clic.**

## El color

- **por qué no se transmiten los tres primarios** · `[of]` · **1) compatibilidad**: un receptor de
  blanco y negro sólo necesita la luminancia. **2) economía**: **el ojo distingue mucho menos detalle
  en color que en brillo.**

| Parámetro | Qué es |
|---|---|
| **espacio de color** | **qué colores puede representar el sistema** |
| **función de transferencia** | **cómo se reparten los códigos entre lo oscuro y lo claro** |
| **profundidad de bits** | **cuántos escalones tiene cada componente** |
| **niveles de referencia** | **qué código es el negro y cuál el blanco** |

- **EL AVISO QUE UN EXAMEN PREMIA** · `[of]` · **En televisión el negro y el blanco no son el cero y el
  máximo del código**: **se dejan márgenes arriba y abajo.** **Tratar esa señal como si fuera de margen
  completo aplasta los negros y quema los blancos**, y **es el error de conversión más frecuente entre
  el mundo de la televisión y el de la informática.**

## El submuestreo

| Estructura | Qué hace |
|---|---|
| **4:4:4** | **sin submuestreo** |
| **4:2:2** | **mitad de color en horizontal, todas las líneas** |
| **4:2:0** | **mitad en horizontal Y mitad en vertical** |
| **4:1:1** | **un cuarto en horizontal, todas las líneas** |

- **LA CUENTA QUE SE PREGUNTA** · `[exam]` · **En 4:2:0, por cada cien muestras de luminancia de la
  imagen ENTERA, cada diferencia de color tiene VEINTICINCO**: **se divide por dos en horizontal y por
  dos en vertical, o sea por cuatro.** **La trampa es hacer la cuenta sobre una línea suelta y
  contestar cincuenta.**
- **las tres reglas de oficio** · `[of]` · **1)** cada escalón se paga después: **una incrustación por
  color sobre 4:2:0 tiene los bordes sucios.** **2)** el submuestreo **no se recupera**: convertir a
  4:4:4 interpola, inventa. **3)** **la cadena vale lo que su eslabón más pobre.**

## Las tres cuentas

| Cuenta | Regla |
|---|---|
| **Régimen binario** | **muestras por línea × líneas × imágenes por segundo × bits por muestra × componentes** |
| **Píxeles entre formatos** | **2160 tiene el doble de líneas y el doble de columnas que 1080: CUATRO veces más píxeles por cuadro** |
| **Retardo en milisegundos** | **cuadros × duración de cuadro**, y **la duración sale de la cadencia de CUADROS** |

| Cadencia | Dura un cuadro |
|---|---|
| **25 cuadros por segundo** | **40 ms** |
| **50 cuadros por segundo** | **20 ms** |
| **30 cuadros por segundo** | **33,3 ms** |

- **DONDE SE FALLA** · `[exam]` · **En una señal entrelazada de cincuenta CAMPOS el cuadro dura
  cuarenta milisegundos, no veinte.** **Y en la cuenta de píxeles la cadencia no entra**: **quien la
  mezcle contesta ocho o dieciséis.**
- **la lectura de oficio del desajuste** · `[of]` · **El oído tolera mucho peor el audio ADELANTADO que
  el retrasado**, porque **en la naturaleza el sonido siempre llega después de la imagen.** **Por eso
  las tolerancias no son simétricas**, y **el temario no da sus cifras porque no las ha leído en su
  fuente.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 8 | Con qué formato es más probable que llegue una señal procedente de América | **Mil ochenta líneas entrelazadas a sesenta campos** ✔ **·** la familia de sesenta |
| 16 | Cinco cuadros de retraso de sonido en una señal de dos mil ciento sesenta líneas progresivas a cincuenta cuadros | **100 ms** ✔ **·** cinco por veinte milisegundos |
| 24 | Muestras de una diferencia de color por cada cien de luminancia en 4:2:0, imagen entera | **25** ✔ **·** dividido por dos en horizontal y por dos en vertical |
