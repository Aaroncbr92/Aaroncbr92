# Esquema · Tema 8 del específico de Ingeniería Superior · Telecomunicación · Alta y ultraalta definición: estándares

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de televisión · `[plan]` =
enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo · `[norma]` = norma técnica
nombrada en la pregunta y confirmada por la plantilla. **Siglas**: la interfaz digital serie (**SDI**);
el alto rango dinámico (**HDR**) y el rango estándar (**SDR**); la tabla de consulta de color
(**LUT**); el bit por segundo con sus múltiplos **Mbit/s** y **Gbit/s**; y las sociedades y uniones que
publican las normas técnicas, que se nombran por su sigla en las citas de la plantilla.

**Cabecera.** Enunciado: punto 8 del anexo · **once preguntas: es el segundo punto más preguntado del
cuadernillo** · **sin norma del boletín**: los estándares son normas técnicas de sociedades de
ingeniería que este proyecto no tiene; **de ellas sólo se recoge lo que la plantilla confirma.**

**La idea que lo ordena** · `[of]` · **La ultraalta definición no se define por el número de píxeles.**
**El rango dinámico y la gama de color aportan más a igual tasa que duplicar la resolución**, y **casi
todas las preguntas de este punto viven ahí.**

<!-- indice -->

## Índice

- [La aritmética de los formatos](#la-aritmética-de-los-formatos)
- [Las interfaces](#las-interfaces)
- [Ultraalta definición por cuatro enlaces](#ultraalta-definición-por-cuatro-enlaces)
- [Rango dinámico y gama de color](#rango-dinámico-y-gama-de-color)
- [Las tablas de consulta](#las-tablas-de-consulta)
- [El intercambio de material](#el-intercambio-de-material)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La aritmética de los formatos

| Formato | Rejilla | Respecto al anterior |
|---|---|---|
| **alta definición** | **1920 × 1080** | — |
| **ultraalta, primer escalón** | **3840 × 2160** | **doble de líneas y doble de columnas: CUATRO veces más píxeles** |
| **ultraalta, segundo escalón** | **7680 × 4320** | **otras cuatro: dieciséis respecto a la alta definición** |

- **DONDE SE FALLA** · `[exam]` · **La comparación de píxeles POR CUADRO no depende de la cadencia.**
  **Dos mil ciento sesenta líneas progresivas a cincuenta cuadros tiene CUATRO veces más píxeles por
  cuadro que mil ochenta entrelazadas a cincuenta campos**, no ocho ni dieciséis. **Quien mezcle
  resolución con cadencia contesta ocho.**
- **el vocabulario comercial** · `[of]` · **«4K» y «8K» son nombres del cine y del mercado.** **Los
  formatos de difusión son de 3840 y de 7680 columnas**, y **el cinematográfico tiene 4096.** **En un
  pliego se escribe la rejilla, no el apodo.**

## Las interfaces

| Interfaz | Régimen aproximado | Para qué basta |
|---|---|---|
| **definición estándar** | **270 Mbit/s** | **definición estándar** |
| **alta definición** | **1,5 Gbit/s** | **1080i50 y 1080p25** |
| **3 gigabits** | **3 Gbit/s** | **1080p50** |
| **6 gigabits** | **6 Gbit/s** | **ultraalta con submuestreo y cadencia moderados** |
| **12 gigabits** | **12 Gbit/s** | **2160p50 por un solo cable** |

- **la cifra que se pregunta directamente** · `[exam]` · **Mil ochenta líneas entrelazadas a cincuenta
  campos sin comprimir van a unos 1,5 gigabits por segundo.** **No 270 megabits, que es definición
  estándar; ni 3 gigabits, que corresponde a mil ochenta progresivas a cincuenta.**
- **la regla que hace memorizables las dos normas de interfaz** · `[norma]` · **la serie 2081 es la de
  seis gigabits y la 2082, la de doce.** **De su contenido no se afirma nada más.**
- **los tres mapeados de la interfaz de tres gigabits** · `[norma]` · **nivel A, nivel B de enlace
  doble y nivel B de flujo doble.** **Ni dos ni cuatro.** **El nivel A lleva un flujo único a tres
  gigabits; los de nivel B, dos flujos de alta definición multiplexados**, lo que **da compatibilidad
  con equipamiento anterior.**

## Ultraalta definición por cuatro enlaces

| Método | Cómo reparte | Qué lleva cada enlace |
|---|---|---|
| **división en cuadrantes** | **parte la imagen en cuatro trozos** | **un cuarto de la imagen** |
| **entrelazado de dos muestras** | **muestras alternas en horizontal y en vertical** | **una imagen COMPLETA submuestreada** |

- **LA CONSECUENCIA QUE ES LA PREGUNTA** · `[exam]` · **Para obtener una copia en alta definición de la
  señal en cada uno de los cuatro enlaces sin equipamiento adicional, el método es el entrelazado de
  dos muestras.** **Con cuadrantes cada enlace lleva sólo un trozo y hay que recomponer los cuatro.**
- **las dos observaciones de oficio** · `[of]` · **1)** con cuatro enlaces hay que vigilar el
  **desfase**: cuatro cables de distinta longitud llegan en instantes distintos. **2)** distribuir por
  cuadrantes **multiplica el equipamiento**: cada señal necesita cuatro distribuidores, uno por
  cuadrante.

## Rango dinámico y gama de color

| Concepto | Qué es |
|---|---|
| **resolución** | **cuántos píxeles hay** |
| **gama de color** | **qué colores se pueden representar** |
| **rango dinámico** | **cuánta distancia hay entre el negro y el blanco más brillante** |

| | **Cuantificador perceptual** | **Gamma logarítmica híbrida** |
|---|---|---|
| **Cómo define el brillo** | **en valores ABSOLUTOS de luminancia** | **en valores RELATIVOS**, como toda la televisión anterior |
| **De dónde viene** | **del cine y del dominio del máster** | **de la radiodifusión** |
| **Compatibilidad con rango estándar** | **poca** | **ALTA**: la parte baja de su curva es la de siempre |
| **Dónde encaja** | **producción controlada y monitorado calibrado** | **DIRECTO**, donde hay que servir a los dos mundos |

- **LA RESPUESTA RAZONADA DEL DIRECTO** · `[exam]` · **La ventaja de la gamma logarítmica híbrida en
  una retransmisión es la COMPATIBILIDAD SIMULTÁNEA en el monitorado**: **el mismo flujo sirve a
  equipos de alto rango y de rango estándar.** **No comprime más, no usa ondículas —una función de
  transferencia no comprime nada—, no da más profundidad de color y el cuantificador perceptual no
  está limitado a la ultraalta definición.**
- **la norma de la función de transferencia** · `[norma]` · **La que define el cuantificador perceptual
  es de la sociedad de ingenieros de cine y televisión.** **Confundir la función de transferencia con
  el espacio de color es el error que la pregunta busca.**
- **lo que la plantilla confirma de las dos recomendaciones** · `[norma]` · **la de la gama amplia fija
  DOCE bits como profundidad máxima por componente**; **la del alto rango dinámico NO define ningún
  formato entrelazado —sólo progresivos— y NO define ningún espacio de color para rango estándar.**
- **las dos lecturas** · `[of]` · **1) la ultraalta definición nace PROGRESIVA**: el entrelazado es una
  herencia hacia atrás. **2) la recomendación del alto rango dinámico es de ALTO rango**: para rango
  estándar no define espacio de color porque no es lo suyo, y **la respuesta es «ninguno».**

## Las tablas de consulta

| Uso | Qué hace |
|---|---|
| **conversión entre rangos** | **su uso característico, y el que se pregunta** |
| **conversión entre gamas** | **adaptar el material de una cámara a la paleta del programa** |
| **monitorado** | **ver en rango estándar lo que se graba en alto rango** |
| **etalonaje** | **aplicar una intención estética repetible** |

- **LO QUE NO HACE** · `[exam]` · **No convierte de una norma de sesenta a una de cincuenta** —eso es
  interpolación temporal—, **no convierte progresivo en entrelazado** —eso es un entrelazador— **y no
  cambia la relación de aspecto.** **Trabaja sobre el VALOR de cada píxel, no sobre el tiempo ni sobre
  la geometría.**
- **el aviso de oficio** · `[of]` · **Una conversión de alto rango a rango estándar es una decisión
  creativa disfrazada de operación técnica.** **Ninguna manera de comprimir el rango es neutra**, así
  que **la tabla se elige, se aprueba, se documenta y se aplica igual en toda la producción.**

## El intercambio de material

| Qué se pacta | Por qué |
|---|---|
| **contenedor y su variante** | **decide si el fichero es autocontenido** |
| **códec y tasa** | **decide la calidad y si se puede editar directamente** |
| **muestreo y profundidad de bits** | **4:2:2 o 4:2:0, diez o doce bits** |
| **función de transferencia y espacio de color** | **rango estándar o alto rango, y con qué curva** |
| **cadencia y barrido** | **y si hay que convertir de norma** |
| **pistas de audio** | **cuántas, en qué orden y qué lleva cada una** |
| **código de tiempo y punto de inicio** | **para que el material encaje donde tiene que encajar** |
| **metadatos obligatorios** | **título, episodio, versión, subtítulos, audiodescripción** |

- **EL ORDEN DE UNA CONVERSIÓN** · `[of]` · **De ultraalta con alto rango a alta definición con rango
  estándar son tres operaciones y el orden importa**: **primero la tabla de consulta de rango**, porque
  **se decide sobre el material de más calidad**; **después el escalado**; **la transcodificación al
  final**, porque **es la que pierde y no conviene arrastrar sus pérdidas.**
- **la falsa que confunde tener información con saber qué hacer con ella** · `[of]` · **Un material de
  alto rango visto como rango estándar sin conversión sale lavado, no mejor.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 9 | Qué norma define la interfaz de seis gigabits | **La de la serie 2081** ✔ **·** la 2082 es la de doce |
| 13 | Formatos de mapeado de la interfaz de tres gigabits | **Tres: nivel A, nivel B de enlace doble y nivel B de flujo doble** ✔ |
| 25 | Método para tener una copia en alta definición en cada uno de cuatro enlaces | **Entrelazado de dos muestras** ✔ **·** con cuadrantes cada enlace lleva un trozo |
| 39 | Norma de codificación del alto rango dinámico en ultraalta definición | **La del cuantificador perceptual** ✔ **·** no la de gama de color ni la de transporte por red |
| 48 | Para qué sirve una tabla de consulta de color | **Convertir de alto rango a rango estándar y al revés** ✔ |
| 59 | Qué formato NO está definido en la recomendación del alto rango dinámico | **El entrelazado** ✔ **·** la ultraalta definición nace progresiva |
| 61 | Profundidad de bits máxima de la recomendación de gama amplia | **Doce bits** ✔ |
| 66 | Ventaja de la gamma logarítmica híbrida en un directo | **Compatibilidad simultánea en el monitorado** ✔ |
| 67 | Píxeles por cuadro de dos mil ciento sesenta progresivas frente a mil ochenta entrelazadas | **Cuatro veces más** ✔ **·** la cadencia no entra en la cuenta |
| 78 | Espacio de color que la recomendación del alto rango define para rango estándar | **Ninguno** ✔ |
| 84 | Tasa de una señal de alta definición entrelazada a cincuenta campos sin comprimir | **1,5 Gbit/s** ✔ |
