# Esquema · Tema 15 del específico de Realización Televisión · El mezclador

**Siglas y marcas**: el nombre de una plataforma de grafismo (**Brainstorm IPF**), al que **este
esquema no atribuye forma larga porque no la ha verificado**.

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de control · `[fab]` =
documentación de fabricante, citada literal · `[plan]` = plantilla oficial.

**Siglas**: el efecto digital de vídeo con que se reduce y coloca una imagen
dentro de otra (**DVE**, *digital video effect*).

**Cabecera.** Enunciado: «4.3. Conceptos generales del mezclador» —**el enunciado más corto del anexo:
seis palabras**— · **7 preguntas** · **CUATRO son de incrustación y TRES de automatización.**

<!-- indice -->

## Índice

- [Qué hace un mezclador](#qué-hace-un-mezclador)
- [El chroma key: CUALQUIER color](#el-chroma-key-cualquier-color)
- [Directo contra postproducción](#directo-contra-postproducción)
- [Incrustar sin key en el mezclador](#incrustar-sin-key-en-el-mezclador)
- [El timeline lanzado](#el-timeline-lanzado)
- [La macro](#la-macro)
- [El software que programa una emisión entera](#el-software-que-programa-una-emisión-entera)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué hace un mezclador

| Función | Qué significa |
|---|---|
| **Conmutar** | **Pasar de una entrada a otra**: el corte |
| **Transicionar** | **Encadenado, cortinilla, fundido** |
| **Incrustar** | **Meter una imagen dentro de otra** |
| **Componer** | **Reducir, colocar y superponer**: es el DVE |
| **Automatizar** | **Guardar una secuencia y lanzarla con un botón**: la macro |

- **VOCABULARIO QUE EL EXAMEN DA POR SABIDO**: **«GAFA» = composición de varias ventanas en
  pantalla.** **Una gafa 50/50 es la pantalla partida en dos; una 20/60/20, tres ventanas con la central
  más ancha.** **No es término normalizado.**

## El chroma key: CUALQUIER color

- **PREGUNTA 77** · `[of]` · **Un *chroma key* se puede hacer CON CUALQUIER COLOR.**
- **EL MECANISMO**: **el mezclador no reconoce «el verde»: reconoce EL COLOR QUE SE LE DIGA**, con una
  tolerancia.
- **POR QUÉ SE USA VERDE Y AZUL, QUE ES LO QUE HACE VEROSÍMILES LAS FALSAS**: **ni el verde ni el azul
  saturados están en la piel** · **el canal verde tiene más resolución en el sensor** · **se elige azul
  si el vestuario lleva verde y al revés.** **Es COSTUMBRE, no limitación.**
- **LAS TRES FALSAS EMPIEZAN POR «SOLO».**

## Directo contra postproducción

- **PREGUNTA 6** · `[of]` · **El equipo que hace croma en TIEMPO REAL es INFINITY SET.**
- **LA REGLA QUE SEPARA LA COLUMNA**: **DaVinci, After Effects y Nuke son herramientas de
  POSTPRODUCCIÓN**, y **una herramienta de postproducción se define por trabajar sobre material QUE YA
  EXISTE.** **En directo el material no existe todavía.**
- **PREGUNTA 28** · `[plan]` · **NEGATIVA. El que NO es generador de caracteres es MISTIKA**, sistema de
  acabado de sala. **Chyron, Brainstorm IPF y Ventuz sí lo son.**
- **ES LA MISMA FRONTERA PREGUNTADA DOS VECES**: **equipos de directo contra equipos de sala.**

## Incrustar sin key en el mezclador

- **PREGUNTA 31** · `[of]` · **SÍ se puede trabajar en decorado virtual en tiempo real sin *key* en el
  mezclador: TENIENDO LA SEÑAL DE CÁMARA EN EL MOTOR DE RENDER y un software que incruste.**
- **EL RAZONAMIENTO**: **la incrustación NO tiene que hacerla el mezclador.** **Si se hace aguas arriba,
  el mezclador recibe una sola señal ya montada y se limita a conmutarla.**
- **⚠ LA OPCIÓN d) DA LA RESPUESTA CORRECTA POR UNA RAZÓN FALSA**: **«sí, el chroma no se realiza por
  key» — el croma ES una clase de key.** **Quien marque «sí» sin leer entero acierta el sí y falla la
  pregunta.**

## El timeline lanzado

- **PREGUNTA 29** · `[of]` · **NO se puede reposicionar la señal dentro de la gafa: es un EFECTO
  PREPROGRAMADO EN UN TIMELINE y no se puede una vez lanzado.**
- **LO QUE LA RESPUESTA AFIRMA, CON PRECISIÓN**: **no es que un DVE no se pueda mover** —se mueve
  siempre—: **es que las posiciones que forman parte de un timeline en marcha ESTÁN ESCRITAS EN EL
  EFECTO.**
- **EL CONCEPTO QUE VALE PARA TODA LA AUTOMATIZACIÓN**: **un efecto programado se comporta como una
  GRABACIÓN, no como un mando.** **Se prepara antes o se cancela; mientras corre, manda él.**

## La macro

- **PREGUNTA 72** · `[fab]` · **Son LAS INSTRUCCIONES que le solicitamos a un mezclador PARA HACER UNA
  SERIE DE PASOS CON SOLO APRETAR UN BOTÓN.**
- **EL MANUAL EN ESPAÑOL DEL ATEM DE BLACKMAGIC LO DEFINE ASÍ, LITERAL**: **«Una macro es una secuencia
  de instrucciones que se llevan a cabo automáticamente al presionar un botón.»**
- **LAS TRES FALSAS**: **un mezclador ligero** = confunde la macro con el aparato · **el botón que
  amplía una imagen** = **confunde la macro del mezclador con el OBJETIVO MACRO de fotografía** · **el
  aparato donde se almacenan los efectos** = **el propio manual dice que se almacenan EN EL
  MEZCLADOR.**
- **MACRO Y TIMELINE SON LA MISMA IDEA**: **una secuencia guardada.** **Y comparten la limitación: se
  editan PARADAS.**

## El software que programa una emisión entera

- **PREGUNTA 102** · `[plan]` · **Es LIVE EDIT.**
- **QUÉ ES**: **la macro llevada al extremo**: **guarda la escaleta entera de un programa** y **el
  control pasa de ejecutar a supervisar.** **Es la tecnología de los grandes eventos musicales y
  deportivos.**
- **EL SISTEMA QUE CONVIENE ASOCIAR**: **CuePilot**, del tema 12: **realización programada contra
  tiempo.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 6 | Con qué equipo se hace un croma en tiempo real | b) Infinity Set ✔ |
| 28 | Qué equipo NO es generador de caracteres | a) Mistika ✔ |
| 29 | Si se puede reposicionar en un *timeline* lanzado | a) No, es preprogramado ✔ |
| 31 | Decorado virtual sin *key* en el mezclador | a) Sí, con la señal en el motor de render ✔ |
| 72 | Qué es un macro | d) Instrucciones para hacer varios pasos con un botón ✔ |
| 77 | Con qué colores se puede hacer un *chroma key* | a) Cualquier color ✔ |
| 102 | Qué software programa cada cambio de plano | d) Live Edit ✔ **·** sólo con la plantilla |

**Las siete oficiales son correctas.** · **Aviso de estudio**: **CUATRO se razonan** —la frontera entre
directo y sala, y la trampa del «sólo»— **y TRES exigen conocer un nombre o un comportamiento
concreto** —la 29, la 72 y la 102—. **Sólo esas tres hay que memorizarlas.**
