# Esquema · Tema 15 del específico de Ingeniería Superior · Telecomunicación · Postproducción de vídeo y audio

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de postproducción · `[plan]` =
enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: la tabla de
consulta de color (**LUT**); el alto rango dinámico (**HDR**) y el rango estándar (**SDR**).

**Cabecera.** Enunciado: punto 17 del anexo · **una pregunta** · **sin norma del boletín**.

**La idea que lo ordena** · `[of]` · **El orden de las operaciones no es una costumbre: es lo que
decide si el trabajo se pierde.** **Etalonar un plano que después se cae es tiempo tirado**, y
**conformar al final es lo que impide que el resultado dependa de la copia ligera.**

<!-- indice -->

## Índice

- [El flujo de trabajo](#el-flujo-de-trabajo)
- [El equipamiento](#el-equipamiento)
- [Etalonaje y conversión de rango](#etalonaje-y-conversión-de-rango)
- [Mezcla y masterizado de audio](#mezcla-y-masterizado-de-audio)
- [La interconexión](#la-interconexión)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El flujo de trabajo

| Etapa | Qué produce |
|---|---|
| **1 · ingesta y copias ligeras** | **el proyecto poblado** |
| **2 · montaje** | **la lista de decisiones, sobre copia ligera** |
| **3 · conformado** | **la secuencia en calidad de máster** |
| **4 · etalonaje** | **la imagen ya ajustada** |
| **5 · grafismo y efectos** | **los elementos incrustados** |
| **6 · mezcla de audio** | **la banda sonora** |
| **7 · masterizado y entrega** | **el máster y sus versiones** |

- **las tres reglas del orden** · `[of]` · **1)** el montaje **se cierra antes de etalonar**, y un
  cambio posterior obliga a revisar los planos vecinos. **2)** la mezcla se hace **sobre imagen
  cerrada**: un cambio de duración desplaza todo lo que va detrás. **3)** el conformado va **antes** del
  acabado: **etalonar sobre copia ligera y confiar en que el original responda igual es como se
  descubre, al final, que no responde.**
- **lo que ata copia y original** · `[of]` · **El CÓDIGO DE TIEMPO.** **Si no lo comparten, el
  conformado no cuadra**, y **ése es el fallo más caro de una postproducción mal preparada.**

## El equipamiento

| Vídeo | Qué hace |
|---|---|
| **estación de edición** | **el programa de montaje y su máquina** |
| **almacenamiento compartido** | **que varios puestos trabajen sobre el mismo material: tema 18** |
| **monitor de referencia calibrado** | **es lo que hace posible el etalonaje** |
| **panel de etalonaje** | **mandos y bolas de control para el color** |
| **forma de onda y vectorscopio** | **la medida objetiva que acompaña al ojo: tema 12** |

| Audio | Qué hace |
|---|---|
| **estación de trabajo de audio** | **el programa de mezcla** |
| **superficie de control** | **faders y mandos físicos** |
| **monitorado calibrado** | **cajas y sala tratada acústicamente** |
| **medidores de nivel y sonoridad** | **lo que decide la entrega: tema 12** |
| **sala de locución** | **grabación de voz** |
| **biblioteca de efectos y músicas** | **con sus derechos documentados** |

- **las dos condiciones que no salen en ninguna lista de equipos** · `[of]` · **1) LA SALA**: **un
  monitor de referencia en una sala con luz de ventana no sirve, y unas cajas en una sala sin tratar
  tampoco.** **La sala es parte del instrumento.** **2) LA CALIBRACIÓN CON FECHA**: **sin ella, dos
  salas de la misma casa entregan cosas distintas y nadie sabe cuál está bien.**

## Etalonaje y conversión de rango

| Herramienta | Qué hace |
|---|---|
| **primarios** | **actúan sobre toda la imagen** |
| **secundarios** | **sobre una parte: un rango de color, una zona, un objeto seguido** |
| **máscaras y seguimiento** | **delimitan dónde actúa cada ajuste** |
| **tablas de consulta** | **conversiones de espacio y de curva, y aspectos guardados** |

- **EL CASO COMPLETO Y SU ORDEN** · `[exam]` · **De ultraalta definición con alto rango y códec de
  producción a alta definición con rango estándar y códec de emisión, son tres operaciones**:
  **1) aplicar la tabla de consulta de rango** —se decide sobre el material con más información—;
  **2) reducir la resolución**; **3) transcodificar al final** —es la operación que pierde y no
  conviene arrastrar sus pérdidas—.
- **la opción que hay que descartar** · `[exam]` · **Decir que no hace falta tabla porque el material
  «tiene más información de color» confunde tener información con saber qué hacer con ella.** **Un
  material de alto rango codificado como rango estándar sin conversión sale lavado**, no mejor. **Y
  decir que la conversión no es posible es sencillamente falso.**
- **el aviso de método** · `[of]` · **Una conversión de rango es una decisión creativa disfrazada de
  operación técnica.** **Se elige una tabla, se aprueba, se documenta y se aplica la misma a toda la
  producción**, porque **dos tablas distintas en el mismo programa se ven.**

## Mezcla y masterizado de audio

| Etapa | Qué se hace |
|---|---|
| **edición y limpieza** | **quitar ruidos, cuadrar sincronía, reparar** |
| **equilibrio** | **niveles relativos entre diálogo, ambiente, efectos y música** |
| **procesado** | **ecualización, dinámica y reverberación** |
| **espacialización** | **reparto entre canales** |
| **masterizado** | **ajustar a la norma de entrega y comprobarlo** |

- **la regla que ordena una mezcla de televisión** · `[of]` · **Manda el DIÁLOGO.** **Todo lo demás se
  coloca respecto a él**, porque **el espectador que no entiende lo que se dice apaga.**

| Magnitud de entrega | Qué es |
|---|---|
| **sonoridad integrada** | **cuán fuerte suena el programa entero**: es lo que se normaliza |
| **rango de sonoridad** | **cuánto varía entre lo más flojo y lo más fuerte** |
| **pico verdadero** | **el máximo real de la señal reconstruida**, que puede superar al de las muestras |

- **las dos cosas que hay que saber decir** · `[of]` · **1)** la normalización moderna es **por
  sonoridad, no por pico**: ajustar al pico dejaba niveles percibidos muy distintos, **y eso producía
  el salto de volumen entre programa y publicidad.** **2)** el pico verdadero **no es el de las
  muestras**: al reconstruir la señal entre muestras pueden aparecer valores más altos, **y por eso se
  deja margen.**
- **lo que el temario NO da** · `[of]` · **Ningún valor objetivo de sonoridad ni de pico**: **están en
  las recomendaciones de entrega, que no se han consultado.**

## La interconexión

| Con quién | Para qué |
|---|---|
| **almacenamiento compartido** | **de donde lee y a donde escribe: tema 18** |
| **gestión de medios y archivo** | **buscar material y devolver el máster catalogado** |
| **ingesta** | **recibir el material rodado** |
| **salas de grafismo** | **intercambiar elementos y composiciones: tema 16** |
| **continuidad y emisión** | **entregar el máster listo para su hora: tema 13** |

- **las dos reglas de intercambio** · `[of]` · **1)** el proyecto se intercambia **con un formato de
  PROYECTO, no con un vídeo**: lleva cortes, pistas, niveles y referencias, y permite seguir
  trabajando. **2)** se pacta **la entrega antes de empezar**: **descubrir al final que pedía otra
  estructura de audio cuesta rehacer la mezcla.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 28 | Orden correcto de los procesos para entregar en alta definición y rango estándar un material de ultraalta definición con alto rango | **Tabla de consulta primero, escalado después y transcodificación al final** ✔ |
