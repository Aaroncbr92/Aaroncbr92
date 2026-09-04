# Tema 6 del específico de Sonido · Señales de contribución

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Sonido · punto 4 |
| **Sirve para** | **Sonido** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el enlace de contribución y el retorno N-1, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Pregunta rota** | **La pregunta 44 tiene dos opciones idénticas**: la c) y la d) dicen exactamente lo mismo. **La respuesta oficial sigue siendo correcta** —Dante no es un algoritmo de codificación para una llamada por internet—, pero **el enunciado está mal construido y así se declara** |
| **Extensión** | **2.194 palabras** |

<!-- /portada -->

Las siglas y términos de este tema, presentados de entrada: la mezcla que devuelve todo menos la
propia señal del que escucha (**N-1**, o *mix-minus*); la red digital de servicios integrados
(**RDSI**, o **ISDN** en la documentación en inglés); el códec de audio para contribución; la
modulación por impulsos codificados (**PCM**, *pulse-code modulation*); el formato de fichero de onda
(**WAV**); el grupo de expertos de imágenes en movimiento (**MPEG**) y su capa II de audio; el
protocolo de red (**IP**); la fibra hasta el hogar (**FTTH**, *fibre to the home*, que el enunciado
del examen escribe «FFTH»); las generaciones de telefonía móvil (**3G**, **4G** y **5G**); los
sistemas de satélite de banda ancha global (**BGAN**) y **Thuraya**, y la **banda Ka**; la difusión
de audio digital (**DAB**); el estéreo (**ST**); y el múltiplex de una emisora, que es la matriz
desde la que se reparten las líneas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 4):
> «SEÑALES DE CONTRIBUCIÓN. Fuentes de reproducción sonora. Puestos de comentarista y multilaterales.
> RDSI.»

**Cuatro preguntas.** **Y el punto que separa a un técnico de radio de un aficionado**: **contribuir
no es emitir.** **Una señal de contribución es la que VIENE de fuera hacia la emisora**, con su
retorno de vuelta, y **todo el punto va de cómo se monta ese camino de ida y vuelta sin que se
realimente.**

**Un aviso sobre una de las cuatro**: **la pregunta 44 está rota.** **Sus opciones c) y d) son la
misma cadena repetida.** **Se contesta igual, y el defecto va declarado en el epígrafe 5.**

<!-- indice -->

## Índice

- [1. Qué es una señal de contribución](#1-qué-es-una-señal-de-contribución)
- [2. El N-1: la resta que hace posible un directo](#2-el-n-1-la-resta-que-hace-posible-un-directo)
- [3. Dos líneas, dos retornos: la pregunta 30](#3-dos-líneas-dos-retornos-la-pregunta-30)
- [4. La RDSI y lo que vino después](#4-la-rdsi-y-lo-que-vino-después)
- [5. Qué se puede mandar por IP y qué no](#5-qué-se-puede-mandar-por-ip-y-qué-no)
- [6. Las fuentes de reproducción sonora](#6-las-fuentes-de-reproducción-sonora)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Qué es una señal de contribución

**Las tres clases de señal que se manejan en una emisora, y que conviene no confundir:**

| Clase | De dónde a dónde | Calidad |
|---|---|---|
| **Contribución** | **Del exterior HACIA la emisora**: el enviado, el estadio, el estudio remoto | **La más alta posible**: va a sufrir proceso después |
| **Distribución** | **Entre centros de la propia cadena** | **Alta** |
| **Emisión** o difusión | **De la emisora HACIA el público** | **La que el sistema de difusión permita** |

**La regla que las ordena**: **una señal de contribución se comprime lo menos posible**, porque
**todavía va a pasar por la mesa, por el proceso de emisión y por el codificador de difusión.**
**Cada compresión con pérdida que se le añade antes de tiempo se paga al final.**

## 2. El N-1: la resta que hace posible un directo

**Una conexión en dúplex N-1 entre dos mezcladores es aquella que envía todas las señales a la mezcla
del envío excepto la que nos envían.** Ésa es la respuesta oficial a la pregunta 59.

**La aritmética del nombre lo explica entero**: **si hay N fuentes, al que está al otro lado se le
manda N MENOS UNA: todas menos la suya.**

**Por qué**: **porque el enlace tiene retardo.** **Si al enviado especial se le devuelve su propia voz
con doscientos milisegundos de retraso, se oye a sí mismo con eco y no puede hablar.** **La solución
no es bajarle el volumen —entonces no oiría el programa—: es quitarlo de su mezcla.**

**Las tres opciones falsas y por qué caen:**

| Opción | Qué falla |
|---|---|
| **«Sume dos señales o más restándole el primero de los canales»** | **Resta el PRIMER canal, no el del interlocutor**: la resta tiene que ser la de quien escucha |
| **«Envíe todas nuestras señales recibidas»** | **Eso es un retorno de programa completo**: es justo lo contrario del N-1 |
| **«Evite posibles retardos entre codificadores»** | **El N-1 no quita el retardo**: quita la señal que ese retardo haría insoportable |

**Y la distinción con el retorno de programa, que es la que la pregunta 30 lleva al límite:**

| Retorno | Qué lleva | Cuándo se usa |
|---|---|---|
| **De programa (ST)** | **Todo lo que sale al aire, en estéreo** | **Cuando el que escucha NO está en antena** |
| **N-1** | **Todo menos la propia señal del que escucha** | **Cuando el que escucha SÍ está en antena** |

## 3. Dos líneas, dos retornos: la pregunta 30

**Ésta es la mejor pregunta del punto y merece desmontarse entera.**

**El escenario**: **la emisora es cabecera y tiene una conexión con exteriores por dos caminos —una
línea principal y una de reserva— desde su múltiplex.** **Se pregunta qué retornos hay que enviar
para no devolver señal.**

**La respuesta oficial es la c)**: **retorno N-1 excluyendo la línea de reserva a la línea principal,
y retorno N-1 excluyendo la línea principal a la línea de reserva.**

**El razonamiento, y es el que hay que entender porque las cuatro opciones parecen razonables:**

1. **El exterior está en antena, así que su retorno tiene que ser N-1.** **Con eso caen las opciones
   que mandan programa estéreo por la línea principal**: la a) y la d).
2. **Pero hay DOS líneas y las dos traen la misma voz.** **Restar sólo «la línea principal» del
   retorno que va por la principal no basta**: **por la reserva sigue entrando esa misma voz, y
   volvería.** **Con eso cae la opción b), que deja la reserva con programa completo.**
3. **La única que cierra el lazo por los dos caminos es la c)**: **a cada línea se le devuelve la
   mezcla menos LA OTRA línea**, de modo que **ninguna de las dos vías puede devolverle al enviado su
   propia voz.**

**La lección que deja, y vale para cualquier montaje redundante**: **la redundancia duplica los
caminos de vuelta igual que los de ida.** **Un N-1 pensado para una sola línea deja de proteger en
cuanto se añade la de reserva.**

## 4. La RDSI y lo que vino después

**El enunciado del anexo nombra la RDSI expresamente y el examen no la pregunta.** **El tema la
desarrolla porque el programa la pide y porque explica de dónde viene el vocabulario del punto.**

**Qué es**: **la red digital de servicios integrados fue durante veinte años el enlace de
contribución de radio por excelencia.** **Sobre una línea telefónica digital daba dos canales de 64
kilobits por segundo**, que **combinados y con un códec adecuado permitían mandar audio de calidad de
radio desde cualquier sitio con teléfono.**

**Sus tres virtudes explican por qué duró tanto y por qué se echa de menos:**

1. **Establecía una LLAMADA**, no una conexión a una red compartida: **el ancho de banda estaba
   garantizado de extremo a extremo.**
2. **El retardo era bajo y CONSTANTE.**
3. **Funcionaba en cualquier sitio con línea telefónica.**

**Y su sustituto es el audio sobre IP del tema 16**, **que es más barato y más flexible y tiene el
problema que la RDSI no tenía: la red no garantiza nada.** **De ahí que los códecs modernos lleven
memorias intermedias adaptativas y corrección de errores.**

## 5. Qué se puede mandar por IP y qué no

**Dos preguntas del punto son negativas y las dos miden lo mismo: distinguir lo que viaja por una red
pública de lo que no.**

**La pregunta 44**: **de los algoritmos que enumera, el que NO se podría utilizar para una llamada por
IP a través de un códec de transmisión de audio es Dante a 48 kHz y 24 bits.** Ésa es la respuesta
oficial.

**El razonamiento tiene dos patas y las dos valen:**

1. **Dante no es un algoritmo de compresión.** **Es un protocolo de transporte de audio sin comprimir
   por red local**, así que **la pregunta lo saca de la categoría por definición.**
2. **Y aunque se le tomara por tal, no serviría**: **Dante está pensado para una red local
   controlada, con reloj compartido y latencia de microsegundos.** **No atraviesa internet pública.**

**Y aquí hay que declarar el defecto de la pregunta**: **sus opciones c) y d) son la misma cadena
repetida** —«MPEG-1 Layer II a 48 Khz, 384 Kbits/s»—. **Es un error de construcción del cuadernillo.**
**No cambia la respuesta**, porque **la opción marcada es la b) y las dos repetidas son igualmente
válidas como algoritmo de contribución**, pero **el temario lo dice en lugar de pasarlo por alto.**

**La pregunta 93**: **el enlace que NO se podría utilizar para una conexión IP bidireccional entre dos
códecs de audio es el enlace de microondas por transmisión DAB.** Ésa es la respuesta oficial.

**La palabra que decide es «bidireccional»**: **el DAB es un sistema de DIFUSIÓN.** **Va de un
transmisor a muchos receptores y no tiene camino de vuelta.** **Las otras tres opciones —fibra,
telefonía móvil y satélite— son enlaces de red y las tres permiten ida y vuelta.**

| Enlace | Bidireccional | Qué lo caracteriza |
|---|---|---|
| **Fibra FTTH a internet pública** | **Sí** | **El más barato y el menos garantizado** |
| **3G/4G/5G** | **Sí** | **Movilidad**: es la base de la mochila del tema 16 |
| **Satélite BGAN, Thuraya, banda Ka** | **Sí** | **Cobertura donde no hay nada**, con retardo alto |
| **Microondas por DAB** ✔ | **NO** | **Es difusión**: un emisor, muchos receptores |

## 6. Las fuentes de reproducción sonora

**El primer subpunto del enunciado tampoco se pregunta**, y **el tema lo cubre porque el programa lo
pide.**

**Lo que en una emisora se entiende por fuente de reproducción, y qué le pide cada una a la mesa:**

| Fuente | Qué exige |
|---|---|
| **Servidor de audio o sistema de automatización** | **Salidas a nivel de línea y arranque por orden**: es la fuente principal de una radio moderna |
| **Reproductores físicos** (disco compacto, giradiscos, cinta) | **Previo específico en el caso del giradiscos**: nivel muy bajo y la ecualización normalizada de disco de la asociación estadounidense de la industria discográfica (**RIAA**) |
| **Ordenador de redacción o de invitado** | **Caja de inyección o entrada de línea desbalanceada**: es la que más ruido de masa introduce |
| **Teléfono e híbrido telefónico** | **Un N-1 propio**: el híbrido separa la ida de la vuelta sobre una sola línea |
| **Códec de contribución** | **Su N-1 y su retorno**, que son los epígrafes 2 y 3 |

**Y el híbrido telefónico merece una línea, porque es el N-1 hecho aparato**: **su trabajo es separar
en una sola línea la voz que va de la que viene.** **Cuando ese aislamiento no es perfecto, lo que
vuelve es eco**, y **es el mismo problema que el N-1 resuelve en un enlace de dos direcciones.**

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 30 | Qué retornos enviar con línea principal y de reserva | c) N-1 cruzados, cada uno excluyendo la otra línea ✔ |
| 44 | Qué algoritmo NO sirve para una llamada por IP | b) Dante ✔ **·** la pregunta está rota: c) y d) son idénticas |
| 59 | En qué consiste una conexión dúplex N-1 | d) Todas las señales menos la que nos envían ✔ |
| 93 | Qué enlace NO sirve para una conexión IP bidireccional | d) Microondas por transmisión DAB ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Dos avisos de reparto:**

1. **Dos de las cuatro son negativas** —la 44 y la 93—: **se busca la que NO sirve.**
2. **Y una está mal construida** —la 44—, **con dos opciones idénticas.** **No cambia la respuesta.**

## 8. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son las señales de contribución, sus retornos y sus
enlaces, y **va entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | Las cuatro **van como oficio** |

**Tres declaraciones expresas:**

1. **La pregunta 44 está mal construida y el temario lo declara**: **sus opciones c) y d) son la misma
   cadena repetida.** **No es errata de plantilla** —la respuesta marcada, la b), es la correcta— sino
   **un defecto de redacción del cuadernillo.**
2. **Las características de Dante que este tema sostiene son de concepto, no de catálogo.** **La
   documentación de Audinate no se ha consultado en este proyecto**, y **lo que aquí se afirma —que es
   un transporte sin comprimir para red local y no un algoritmo de compresión— es lo que hace la
   pregunta contestable.** **El tema 16 desarrolla el sistema.**
3. **Las cifras de la RDSI del epígrafe 4 —dos canales de 64 kilobits— son las de la definición
   clásica del servicio básico**, y **no proceden de ninguna norma volcada en este proyecto.** **El
   tema las presenta como conocimiento común de la materia**, y **ninguna pregunta depende de ellas.**

**El resto del tema va como oficio y así se declara**: la distinción entre contribución, distribución
y emisión, la aritmética del N-1 y su diferencia con el retorno de programa, el razonamiento de los
retornos cruzados en un montaje redundante, y la tabla de fuentes de reproducción. **Nada de eso está
en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si
lo estuviera.
