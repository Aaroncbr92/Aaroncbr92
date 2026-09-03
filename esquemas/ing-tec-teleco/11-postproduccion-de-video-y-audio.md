# Esquema · Tema 11 del específico de Ingeniería Técnica · Telecomunicación · Postproducción de vídeo y audio

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de postproducción · `[exam]` =
opciones del propio cuadernillo. **Siglas**: el código de tiempo (**TC**); los fotogramas por segundo
(**fps**); el código de tiempo longitudinal (**LTC**) y el vertical (**VITC**); la lista de decisiones
de edición (**EDL**); el formato de intercambio de material (**MXF**); la unidad central de proceso
(**CPU**) y la de proceso gráfico (**GPU**); y la Sociedad de Ingenieros de Cine y Televisión
(**SMPTE**).

**Cabecera.** Enunciado: punto 15 del anexo · **1 pregunta**, **y es de cálculo, no de equipamiento**:
una resta de códigos de tiempo · **el desajuste declarado**: el enunciado pide equipamiento y diagrama
a bloques, y lo que ha caído es **aritmética en base sesenta con un resto de veinticinco.**

<!-- indice -->

## Índice

- [El código de tiempo](#el-código-de-tiempo)
- [Cómo se opera](#cómo-se-opera)
- [El equipamiento](#el-equipamiento)
- [La interconexión](#la-interconexión)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El código de tiempo

- **QUÉ ES** · `[of]` · **Una etiqueta que identifica cada imagen de forma única**, en cuatro campos:
  **horas : minutos : segundos : fotogramas.**

| Campo | Base | Va de |
|---|---|---|
| **Horas** | **24** | **00 a 23** |
| **Minutos** | **60** | **00 a 59** |
| **Segundos** | **60** | **00 a 59** |
| **Fotogramas** | **La cadencia** | **00 a la cadencia menos uno** ✔ |

- **LA CLAVE** · `[of]` · **A 25 imágenes por segundo el campo de fotogramas va de 00 a 24**, y al
  llegar a 25 se convierte en un segundo. **Ésa es la única base que cambia**, y ahí están los errores.

| Formato de transporte | Cómo viaja | Cuándo se lee |
|---|---|---|
| **Longitudinal** | **Como señal de audio, por pista propia** | **Sólo con la cinta en movimiento** |
| **Vertical** | **Dentro del intervalo de borrado de la imagen** | **También con la imagen parada** ✔ |

- **EL QUE HOY SE USA** · `[of]` · **El incrustado en la trama digital**, evolución del segundo. **Los
  tres coexisten en el vocabulario porque las instalaciones conservan equipos de las tres épocas.**
- **EL AVISO** · `[of]` · **Con cadencias fraccionarias existe el código con salto de cuenta**, que
  **omite NÚMEROS —no imágenes— para que el reloj no derive del tiempo real.** **A 25 no ocurre**,
  porque la cadencia es exacta: por eso la pregunta de este examen es limpia.

## Cómo se opera

- **PREGUNTA 18** · `[exam]` · **01:13:56:15 menos 00:45:15:10, a 25 imágenes por segundo, da
  00:28:41:05.**

| Campo | Cuenta | Resultado |
|---|---|---|
| **Fotogramas** | **15 − 10** | **05** |
| **Segundos** | **56 − 15** | **41** |
| **Minutos** | **13 − 45**, prestando una hora → **73 − 45** | **28** |
| **Horas** | **1 − 0**, menos la prestada | **00** |

| Falsa | Qué error comete |
|---|---|
| **00:29:43:00** | **Restar mal los minutos y perder el préstamo** |
| **01:59:12:00** | **Sumar en vez de restar** |
| **00:27:36:05** | **Prestar dos veces, o usar base 100 en los minutos** |

- **LA REGLA QUE EVITA LOS TRES** · `[of]` · **Sólo el campo de fotogramas usa la cadencia; los otros
  dos usan sesenta.**
- **EL ATAJO DE COMPROBACIÓN** · `[of]` · **El resultado ha de ser menor que el minuendo y coherente en
  orden de magnitud.** **Una hora y catorce menos cuarenta y cinco minutos son algo menos de media
  hora**: **dos opciones rondan la media hora y dos no.** **La elección queda entre dos antes de hacer
  ninguna cuenta.**

## El equipamiento

| Bloque | Qué contiene |
|---|---|
| **Puestos de edición** | **Estación con proceso gráfico dedicado, monitor de referencia y superficie de control** |
| **Almacenamiento compartido** | **Varios montadores sobre el mismo material a la vez** |
| **Sala de sonido** | **Mesa, escucha calibrada y tratamiento acústico** |
| **Sala de etalonaje** | **Monitor de referencia calibrado y panel de color** |
| **Sala de gráficos** | **Estaciones de tres dimensiones y de composición** |
| **Cabina de sonorización** | **Locución y doblaje** |

- **LOS TRES PRINCIPIOS DE DISEÑO** · `[of]` · **El monitor de referencia manda**: lo que se decide de
  imagen se decide mirándolo a él, no la pantalla de trabajo · **la escucha ha de ser FIABLE antes que
  potente** · **el almacenamiento compartido es el cuello de botella**: varios montadores leyendo
  material sin comprimir piden un caudal que un almacenamiento corriente no da.
- **LA OBSERVACIÓN** · `[of]` · **Una sala de postproducción es una instalación de informática con
  requisitos de tiempo real.** **Lo que la distingue de una oficina no es el vídeo: es que no admite
  esperas.**

## La interconexión

| Vía | Qué lleva | Cuándo |
|---|---|---|
| **Almacenamiento compartido** | **Los ficheros de trabajo** | **Entre salas del mismo centro** ✔ |
| **Transferencia por red** | **Ficheros entregados o recibidos** | **Con productoras y otros centros** |
| **Señal por matriz o red** | **Vídeo y audio en tiempo real** | **Monitorizar y grabar de directo** |
| **Soporte físico** | **Discos y tarjetas** | **Lo que llega de rodaje** |

| Operación de frontera | Qué puede salir mal |
|---|---|
| **Transcodificación** | **Que el formato de entrega no sea el que la sala trabaja** |
| **Conformado** | **Que el código de tiempo de la baja resolución no case con el del original** |

- **EL FALLO MÁS CARO DE LA CADENA** · `[of]` · **La lista de decisiones es un fichero de texto con
  códigos de tiempo.** **Si no son los mismos en las dos copias, el conformado sale desplazado**, **el
  desplazamiento es constante y no salta a la vista**, y **se detecta al final.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 18 | Resta de dos códigos de tiempo a 25 imágenes por segundo | **00:28:41:05** ✔ |

- **EL AVISO DE ESTUDIO** · `[of]` · **Lo rentable es saber operar con códigos de tiempo**, que se
  aprende en cinco minutos y se olvida si no se practica; **lo enunciado se lee una vez.**
