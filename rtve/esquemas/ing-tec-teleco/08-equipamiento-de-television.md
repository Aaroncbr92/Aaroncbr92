# Esquema · Tema 8 del específico de Ingeniería Técnica · Telecomunicación · Equipamiento de televisión

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de televisión · `[exam]` =
opciones del propio cuadernillo. **Siglas**: el dispositivo de carga acoplada (**CCD**) y el
semiconductor complementario de óxido metálico (**CMOS**); el rojo, verde y azul (**RGB**); las
componentes de luminancia y diferencia de color (**Y**, **Pb**, **Pr**); el multiplexado digital de
iluminación (**DMX512**); el monitor de forma de onda (**WFM**); la relación entre subportadora y
sincronismo horizontal (**SC/H**); la interfaz digital serie (**SDI**); los códecs que salen como
opciones falsas (**H264** y **MPEG2**); la grabación (**REC**); y la señal en forma de pajarita
(**BOWTIE**).

**Cabecera.** Enunciado: punto 10 del anexo, **el más largo de todos**: seis subpuntos y más de treinta
equipos · **7 preguntas** · **reparto**: 3 de cámara, 3 de equipos de medida, 1 de iluminación · **de
mezcladores, servidores, matrices y tituladores no ha caído ninguna** · **es el punto con peor relación
entre lo enunciado y lo preguntado de la ocupación.**

<!-- indice -->

## Índice

- [La cámara](#la-cámara)
- [Los equipos de medida](#los-equipos-de-medida)
- [Las señales de prueba](#las-señales-de-prueba)
- [La iluminación](#la-iluminación)
- [Lo enunciado que no ha caído](#lo-enunciado-que-no-ha-caído)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La cámara

- **PREGUNTA 37** · `[exam]` · **Un filtro dicroico separa las componentes de rojo, verde y azul en el
  bloque de sensores.** **Es un espejo que refleja una banda del espectro y deja pasar el resto**:
  **tres de ellos en un prisma reparten la luz entre tres sensores.**

| Arquitectura | Cómo separa el color | Rasgo |
|---|---|---|
| **Tres sensores con prisma dicroico** | **Ópticamente, antes de los sensores** ✔ | **Cada sensor recibe todos los píxeles de su color** |
| **Un sensor con matriz de filtros** | **Un filtro de color sobre cada píxel** | **Cada píxel ve un solo color; el resto se interpola** |

- **LA CONSECUENCIA** · `[of]` · **La primera da mejor separación de color; la segunda permite sensores
  mucho mayores**, que es lo que hoy se busca por la profundidad de campo. **Estudio: tres sensores.
  Cine: uno grande.**
- **LA PALABRA QUE DECIDE** · `[of]` · **«Dicroico» significa literalmente «de dos colores».** **Las
  falsas nombran cosas reales de la cámara**: conversión de temperatura de color, reductor de ruido,
  filtro del visor.
- **PREGUNTA 92** · `[exam]` · **El control de obturación modifica la velocidad de obturación.**

| Obturación | Qué produce |
|---|---|
| **Lenta**, la de por defecto | **La imagen integra todo el intervalo: estela natural** |
| **Rápida** | **Congela el movimiento: nítido y a saltos** |

- **PARA QUÉ SE USA DE VERDAD** · `[of]` · **Para repetir una jugada a cámara lenta con imagen nítida**
  y **para eliminar el parpadeo con iluminación de descarga o con pantallas.**
- **LA REGLA QUE SEPARA LOS CUATRO CONTROLES** · `[of]` · **La obturación es TIEMPO, la ganancia es
  AMPLIFICACIÓN y el equilibrio de blancos es COLOR.**
- **PREGUNTA 27** · `[exam]` · **La memoria caché graba con anterioridad a la pulsación del botón y
  permite cambiar de tarjeta sin perder información.**
- **CÓMO FUNCIONA** · `[of]` · **La cámara graba SIEMPRE en una memoria circular de unos segundos**: al
  pulsar, **lo que ya estaba se conserva y la toma empieza antes de que el operador reaccionara.**
- **POR QUÉ IMPORTA EN INFORMATIVOS** · `[of]` · **La reacción humana ante algo repentino son uno o dos
  segundos.** **Sin esa memoria se pierden.**
- **LAS FALSAS SON MEMORIAS REALES** · `[exam]` · **Colorimetría, metadatos y ajustes de usuario.**
  **Las tres existen y ninguna hace eso.**

## Los equipos de medida

| Instrumento | Qué mide | Qué se ve |
|---|---|---|
| **Monitor de forma de onda** | **La LUMINANCIA y los niveles** | **La señal de cada línea, en el tiempo** |
| **Vectorscopio** | **La CROMINANCIA: tono y saturación** ✔ | **Plano polar con los seis colores marcados** |
| **Rasterizador** | **Las dos cosas y más** | **Varias representaciones a la vez** |
| **Osciloscopio** | **Cualquier señal eléctrica** | **No tiene los patrones de vídeo** |

- **PREGUNTA 81** · `[exam]` · **Con un vectorscopio se mide la crominancia.**
- **LA REGLA GRABADA** · `[of]` · **Forma de onda para el BRILLO, vectorscopio para el COLOR.**
- **PREGUNTA 21** · `[exam]` · **La relación entre subportadora y sincronismo horizontal de un negro de
  barras se mide con un vectorscopio.**
- **POR QUÉ ESE INSTRUMENTO** · `[of]` · **Es una medida de FASE**, y **la fase es lo que un plano polar
  representa.** **El monitor de forma de onda muestra amplitud contra tiempo.**
- **EL AVISO** · `[of]` · **Es parámetro de instalación, no de operación**: se ajusta al montar la
  referencia y se comprueba **cuando dos fuentes que deberían estar bloqueadas dan un salto al
  mezclarlas.**

## Las señales de prueba

| Señal | Qué mide |
|---|---|
| **Pajarita** | **Retardo y ganancia relativos entre componentes** ✔ |
| **Multiráfaga** | **Distorsión de amplitud frente a frecuencia** |
| **Escalera modulada** | **Ganancia y fase diferenciales** |
| **Diagrama de ojo** | **Jitter y margen de una señal digital** |

- **PREGUNTA 84** · `[exam]` · **La pajarita mide problemas entre luminancia y diferencia de color.**
- **CÓMO FUNCIONA** · `[of]` · **Contiene dos frecuencias que coinciden en un punto exacto**: **con las
  tres componentes al mismo retardo el pico sale limpio y simétrico**; **si una llega antes o después,
  el pico se desplaza y se deforma.**
- **EL AVISO** · `[of]` · **Son señales del mundo de componentes analógicas.** **En digital serie el
  retardo relativo no existe**, porque las tres van multiplexadas en el mismo cable. **Siguen sirviendo
  para los caminos analógicos que quedan y para comprobar conversores.**

## La iluminación

- **PREGUNTA 28** · `[exam]` · **El protocolo más extendido para iluminación es el multiplexado digital
  de iluminación.** **Las falsas son dos códecs de vídeo y una sigla inventada**: de las cuatro, **sólo
  una nombra un protocolo de control.**
- **QUÉ ES** · `[of]` · **Protocolo serie de 512 canales por universo**, **cada canal de 0 a 255**, **por
  par trenzado en cadena.** **Cada foco ocupa tantos canales como parámetros tenga**: uno si sólo se
  regula la intensidad, más de veinte si es robotizado.

| Concepto | Qué es |
|---|---|
| **Universo** | **Un conjunto de 512 canales** |
| **Dirección** | **El primer canal que ocupa un aparato**, fijado en el propio aparato |
| **Terminación** | **La resistencia del final de cadena, que evita reflexiones** |

- **EL FALLO MÁS FRECUENTE** · `[of]` · **Una cadena sin terminación funciona a veces y falla a veces.**
  **El síntoma es un aparato que parpadea o responde a canales ajenos**, y cuesta relacionarlo con la
  causa.
- **LA EVOLUCIÓN** · `[of]` · **El protocolo sobre red envuelve el mismo mensaje en paquetes**: **una
  sola red lleva decenas de universos.** **Es el camino que el vídeo ya recorrió.**

## Lo enunciado que no ha caído

| Equipo | Qué hace |
|---|---|
| **Mezclador de vídeo** | **Elige qué fuente sale y cómo se pasa de una a otra** |
| **Matriz de conmutación** | **Encamina cualquier fuente a cualquier destino, sin transición** |
| **Generador de sincronismos** | **Produce la referencia de toda la instalación** |
| **Sincronizador de cuadro** | **Alinea una fuente que llega sin bloquear** |
| **Servidor de vídeo** | **Graba y reproduce como ficheros, con acceso inmediato** |
| **Titulador y grafismo** | **Genera los rótulos y las piezas** |
| **Generador de efectos digitales** | **Reduce, mueve y deforma la imagen en tiempo real** |
| **Multipantalla** | **Compone muchas fuentes en un monitor de control** |
| **Distribuidor** | **Reparte una señal en varias salidas** |
| **Incrustador y extractor de audio** | **Mete y saca el audio de la trama de vídeo** |

- **MEZCLADOR FRENTE A MATRIZ** · `[of]` · **El mezclador tiene una salida de programa y hace
  transiciones; la matriz tiene muchas salidas y conmuta sin transición.** **Uno es de realización, la
  otra de instalación.**
- **SINCRONIZADOR FRENTE A GENERADOR** · `[of]` · **El generador produce la referencia; el sincronizador
  adapta a ella una señal ajena**, guardando un cuadro entero y leyéndolo al ritmo de la casa.
- **EL AVISO** · `[of]` · **El sincronizador introduce un cuadro de retardo**: imperceptible en emisión
  y **un problema en un enlace de ida y vuelta con un corresponsal**, donde los retardos se suman.

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 21 | Con qué se mide la relación subportadora-sincronismo | **Un vectorscopio** ✔ |
| 27 | Qué es la memoria caché de una cámara | **La que graba antes de pulsar el botón** ✔ |
| 28 | Protocolo más extendido para iluminación | **DMX512** ✔ |
| 37 | Qué es un filtro dicroico | **El que separa las componentes en el bloque de sensores** ✔ |
| 81 | Qué se mide con un vectorscopio | **Crominancia** ✔ |
| 84 | Para qué sirve la señal en forma de pajarita | **Medir problemas entre componentes** ✔ |
| 92 | Para qué sirve el control de obturación | **Modificar la velocidad de obturación** ✔ |
