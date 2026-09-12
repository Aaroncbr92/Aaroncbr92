# Tema 8 del específico de Ingeniería Técnica · Telecomunicación · Equipamiento de televisión

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 10 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia son las cámaras, los instrumentos de medida y la iluminación, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Desajuste declarado** | **El enunciado es el más largo del anexo**: seis subpuntos y más de treinta equipos, **de los que sólo cuatro han dado pregunta** |
| **Extensión** | **2.586 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el dispositivo de carga acoplada (**CCD**) y el
semiconductor complementario de óxido metálico (**CMOS**), que son los dos sensores; el rojo, el verde
y el azul (**RGB**); las componentes de luminancia y diferencia de color (**Y**, **Pb** y **Pr**); el
multiplexado digital de iluminación (**DMX512**); el monitor de forma de onda (**WFM**); la relación
entre la subportadora y el sincronismo horizontal (**SC/H**); la interfaz digital serie (**SDI**) del
tema 3; los códecs que aparecen como opciones falsas (**H264** y **MPEG2**); la grabación
(**REC**), como la marca el propio botón; y la señal de prueba en forma de pajarita, que el sector
llama por su nombre inglés (**BOWTIE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 10):
> «Equipamiento de televisión: 10.1. Cámaras de Estudio. Diagrama a bloques. Procesado. Transmisión
> cableada (Triax y Fibra) y transmisión inalámbrica. Ópticas. 10.2. Camcorders. Tipología. Ópticas.
> 10.3. Mezcladores de video. Magnetoscopios. Editores no lineales. Equipos de grafismo. Generadores
> de efectos digitales. Tituladores. Mesa de Sonido. Matrices de conmutación. Generadores de
> sincronismos. Sincronizadores. 10.4. Servidores de video. Sistemas de Multipantalla. Sistemas de
> producción para Redacción Digital. Equipos de monitorado de vídeo. Monitores y medidores de vídeo.
> 10.5. Mesas de iluminación, dimmers, iluminación robotizada. 10.6. Equipos de medida y control (WFM,
> rasterizadores, medida de audio, etc.) Equipamiento auxiliar de vídeo (distribuidores, embebedores,
> etc.)»

**Siete preguntas.** **Y el enunciado es, con diferencia, el más largo del anexo**: **seis subpuntos y
más de treinta equipos nombrados.**

**Su reparto**: **tres preguntas son de cámara**, **tres de equipos de medida** y **una de
iluminación.** **De mezcladores, servidores, matrices y tituladores no ha caído ninguna**, aunque el
enunciado los nombra.

<!-- indice -->

## Índice

- [1. La cámara](#1-la-cámara)
- [2. Los equipos de medida](#2-los-equipos-de-medida)
- [3. Las señales de prueba](#3-las-señales-de-prueba)
- [4. La iluminación](#4-la-iluminación)
- [5. Lo que el enunciado nombra y no ha caído](#5-lo-que-el-enunciado-nombra-y-no-ha-caído)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. La cámara

**La pregunta 37**: **un filtro dicroico en una cámara es un filtro que separa las componentes de rojo,
verde y azul en el bloque de sensores.** Ésa es la respuesta oficial.

---

**Qué es y por qué está ahí**: **un espejo que refleja una banda del espectro y deja pasar el
resto.** **Tres de ellos, montados en un prisma, reparten la luz que entra por el objetivo entre tres
sensores**, uno por color primario.

**Y de ahí sale la distinción que ordena las cámaras profesionales:**

| Arquitectura | Cómo separa el color | Rasgo |
|---|---|---|
| **De tres sensores, con prisma dicroico** | **Ópticamente, antes de los sensores** ✔ | **Cada sensor recibe todos los píxeles de su color** |
| **De un sensor, con matriz de filtros** | **Con un filtro de color sobre cada píxel** | **Cada píxel ve un solo color, y el resto se interpola** |

**La consecuencia práctica**: **la primera da mejor separación de color y la segunda permite sensores
mucho mayores**, que es lo que hoy se busca por la profundidad de campo. **Las cámaras de estudio
siguen siendo mayoritariamente de tres sensores; las de producción cinematográfica, de uno grande.**

**Las tres opciones falsas nombran tres cosas reales de una cámara**: **un filtro de conversión de
temperatura de color, un reductor de ruido y un filtro del visor.** **La palabra que decide es
«dicroico», que significa literalmente «de dos colores».**

**La pregunta 92**: **el control de obturación de una cámara de vídeo sirve para modificar la velocidad
de obturación.** Ésa es la respuesta oficial.

---

**Es casi una traducción**, y **lo que conviene entender es qué hace esa velocidad:**

| Obturación | Qué produce |
|---|---|
| **Lenta**, la de por defecto | **Cada imagen integra todo el intervalo: el movimiento sale con estela natural** |
| **Rápida** | **Cada imagen congela el movimiento: se ve nítida y a saltos** |

**Para qué se usa de verdad en televisión**: **para poder repetir una jugada a cámara lenta con la
imagen nítida**, y **para eliminar el parpadeo con iluminación de descarga o con pantallas.**

**Las tres opciones falsas son los otros tres controles de la cámara**: **la ganancia, la temperatura
de color y la resolución.** **La regla que las separa: la obturación es TIEMPO, la ganancia es
AMPLIFICACIÓN y el equilibrio de blancos es COLOR.**

**La pregunta 27**: **la memoria caché de una cámara es la memoria que graba con anterioridad a la
pulsación del botón de grabación y permite cambiar de disco o tarjeta sin pérdida de información.**
Ésa es la respuesta oficial.

---

**Y ésta es una pregunta de oficio puro**, de las que **sólo contesta bien quien ha usado el equipo.**

**Qué hace**: **la cámara está grabando SIEMPRE en una memoria circular de unos segundos.** **Al pulsar
el botón, lo que ya estaba en esa memoria se conserva**, de modo que **la toma empieza unos segundos
ANTES de que el operador reaccionara.**

**Por qué importa en informativos**: **la reacción humana ante algo que ocurre de pronto son uno o dos
segundos.** **Sin esa memoria, esos segundos se pierden**; **con ella, se recuperan.**

**Y la segunda mitad de la respuesta oficial es igual de práctica**: **al cambiar de tarjeta, lo que
está en la memoria no se pierde**, y **la grabación continúa en la nueva sin hueco.**

**Las tres opciones falsas nombran tres memorias reales de la cámara**: **la de ajustes de
colorimetría, la de metadatos y la de ajustes de usuario.** **Las tres existen y ninguna hace eso.**

## 2. Los equipos de medida

**Dos preguntas del punto son del mismo instrumento**, y **conviene contestarlas con la misma tabla:**

| Instrumento | Qué mide | Qué se ve |
|---|---|---|
| **Monitor de forma de onda** | **La LUMINANCIA y los niveles** | **La señal de cada línea, en el tiempo** |
| **Vectorscopio** | **La CROMINANCIA: tono y saturación** ✔ | **Un plano polar con los seis colores de barras marcados** |
| **Rasterizador** | **Las dos cosas y más, en pantalla de ordenador** | **Varias representaciones a la vez** |
| **Osciloscopio** | **Cualquier señal eléctrica** | **No está pensado para vídeo: no tiene los patrones** |

**La pregunta 81**: **con un vectorscopio se puede medir la crominancia.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son medidas de los otros instrumentos**: **el jitter se mide en el
diagrama de ojo del tema 3**, y **la componente de luminancia y la luminancia misma se miden en el
monitor de forma de onda.**

**La regla que separa los dos instrumentos y que conviene llevar grabada**: **forma de onda para el
BRILLO, vectorscopio para el COLOR.**

**La pregunta 21**: **para medir la relación entre la subportadora y el sincronismo horizontal de una
señal de negro de barras se usa un vectorscopio.** Ésa es la respuesta oficial.

---

**Qué es esa relación, para que la pregunta signifique algo**: **la fase de la subportadora de color
en el instante del sincronismo horizontal.** **Es un parámetro de la referencia analógica del tema 3**,
y **si está mal, las señales de dos fuentes distintas no casan al mezclarlas.**

**Por qué se mide en ese instrumento y no en el otro**: **porque es una medida de FASE**, y **la fase
es exactamente lo que un plano polar representa.** **El monitor de forma de onda muestra amplitud
contra tiempo y no puede mostrar una relación de fase.**

**El aviso de oficio que este epígrafe deja**: **es un parámetro de instalación, no de operación.**
**Se ajusta al montar la referencia y se comprueba cuando dos fuentes que deberían estar bloqueadas
producen un salto al mezclarlas.**

## 3. Las señales de prueba

**La pregunta 84**: **la señal en forma de pajarita sirve para medir problemas entre las componentes de
luminancia y de diferencia de color.** Ésa es la respuesta oficial.

---

**Cómo funciona, que es lo que la hace ingeniosa**: **la señal contiene dos frecuencias distintas que
coinciden en un punto exacto.** **Si las tres componentes llegan con el mismo retardo, ese punto
aparece como un pico limpio y simétrico**; **si una llega antes o después, el pico se desplaza y se
deforma.**

**Qué mide, dicho con precisión**: **errores de RETARDO relativo y de GANANCIA relativa entre
componentes.** **Es la señal con la que se comprueba que un camino de tres cables está bien igualado.**

**Y las tres opciones falsas son medidas reales de otras señales de prueba:**

| Señal de prueba | Qué mide |
|---|---|
| **Pajarita** | **Retardo y ganancia entre componentes** ✔ |
| **Multiráfaga** | **Distorsión de amplitud frente a frecuencia** |
| **Escalera modulada** | **Ganancia y fase diferenciales** |
| **Diagrama de ojo** | **El jitter y el margen de una señal digital**, del tema 3 |

**El aviso que conviene añadir**: **estas señales son del mundo de componentes analógicas.** **En una
instalación digital serie el problema del retardo relativo no existe**, porque **las tres componentes
van multiplexadas en el mismo cable.** **Siguen usándose en los caminos analógicos que quedan y en
la comprobación de conversores.**

## 4. La iluminación

**La pregunta 28**: **el protocolo más extendido en difusión para iluminación es el multiplexado digital
de iluminación.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son dos códecs de vídeo y una sigla inventada**, lo que **hace la
pregunta contestable sin saber nada de iluminación**: **de las cuatro, sólo una nombra un protocolo de
control.**

**Qué es, en tres líneas**: **un protocolo serie de 512 canales por universo**, **cada canal con un
valor de 0 a 255**, **que viaja por un par trenzado en cadena de un aparato a otro.** **Cada foco
ocupa tantos canales como parámetros tenga**: uno si sólo se le regula la intensidad, y más de veinte
si es robotizado con color, posición y efectos.

**Los tres conceptos que un examen puede pedir:**

| Concepto | Qué es |
|---|---|
| **Universo** | **Un conjunto de 512 canales**: una instalación grande tiene varios |
| **Dirección** | **El primer canal que ocupa un aparato**, y se fija en el propio aparato |
| **Terminación** | **La resistencia al final de la cadena**, que evita reflexiones |

**Y el aviso de instalación, que es el fallo más frecuente**: **una cadena sin terminación funciona a
veces y falla a veces.** **El síntoma es un aparato que parpadea o responde a canales que no son
suyos**, y **cuesta mucho relacionarlo con la causa.**

**La evolución que conviene conocer**: **el protocolo sobre red envuelve ese mismo mensaje en
paquetes**, de modo que **una sola red lleva decenas de universos.** **Es el mismo camino que el vídeo
recorrió en el tema 7.**

## 5. Lo que el enunciado nombra y no ha caído

**El subpunto 10.3 nombra nueve equipos y el 10.4 otros cinco, y ninguno ha dado pregunta.** **Lo
mínimo que conviene llevar visto, agrupado por lo que hace cada uno:**

| Equipo | Qué hace |
|---|---|
| **Mezclador de vídeo** | **Elige qué fuente sale y cómo se pasa de una a otra** |
| **Matriz de conmutación** | **Encamina cualquier fuente a cualquier destino, sin transición** |
| **Generador de sincronismos** | **Produce la referencia de toda la instalación** |
| **Sincronizador de cuadro** | **Alinea una fuente que llega sin bloquear a la referencia local** |
| **Servidor de vídeo** | **Graba y reproduce material como ficheros, con acceso inmediato** |
| **Titulador y equipo de grafismo** | **Genera los rótulos y las piezas del tema 9 de Diseño Gráfico** |
| **Generador de efectos digitales** | **Reduce, mueve y deforma la imagen en tiempo real** |
| **Sistema de multipantalla** | **Compone muchas fuentes en un solo monitor de control** |
| **Distribuidor** | **Reparte una señal en varias salidas** |
| **Incrustador y extractor de audio** | **Mete y saca el audio de la trama de vídeo** |

**Las dos distinciones que un examen puede pedir de esa lista:**

1. **Mezclador frente a matriz.** **El mezclador tiene una salida de programa y hace transiciones; la
   matriz tiene muchas salidas y conmuta sin transición.** **Uno es de realización, la otra es de
   instalación.**
2. **Sincronizador de cuadro frente a generador de sincronismos.** **el generador produce la
   referencia y el sincronizador adapta a ella una señal ajena**, guardando un cuadro entero en memoria
   y leyéndolo al ritmo de la casa.

**Y el aviso de oficio que ordena el subpunto**: **el sincronizador de cuadro introduce un cuadro de
retardo.** **Es imperceptible en emisión y es un problema en un enlace de ida y vuelta con un
corresponsal**, donde los retardos se suman.

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 21 | Con qué se mide la relación de subportadora y sincronismo | d) Un vectorscopio ✔ |
| 27 | Qué es la memoria caché de una cámara | d) La que graba antes de pulsar el botón ✔ |
| 28 | Protocolo más extendido para iluminación | c) DMX512 ✔ |
| 37 | Qué es un filtro dicroico | b) El que separa las componentes en el bloque de sensores ✔ |
| 81 | Qué se mide con un vectorscopio | d) Crominancia ✔ |
| 84 | Para qué sirve la señal en forma de pajarita | a) Medir problemas entre componentes ✔ |
| 92 | Para qué sirve el control de obturación | b) Modificar la velocidad de obturación ✔ |

**Las siete respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la regla de que la forma de onda mide brillo y el vectorscopio mide color
contesta dos preguntas.** **Y el enunciado nombra más de treinta equipos de los que sólo han caído
cuatro**: **es el punto con peor relación entre lo enunciado y lo preguntado de toda la ocupación.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **No se ha consultado la documentación de ningún fabricante de cámaras, de instrumentos de medida
   ni de equipos de iluminación.** **Lo que el tema afirma de cada uno es de uso corriente en el
   oficio**, y **coincide con las respuestas oficiales.**
2. **La norma del protocolo de iluminación no se ha consultado**: **su texto está tras un muro de
   pago.** **Los 512 canales por universo, el rango de 0 a 255 y la necesidad de terminación son de
   uso universal**, y **la respuesta oficial de la pregunta 28 sólo pide el nombre del protocolo.**
3. **Las señales de prueba del epígrafe 3 y lo que mide cada una son de uso corriente en la medida de
   vídeo.** **La respuesta oficial de la pregunta 84 procede del propio enunciado**, que nombra las
   tres componentes.
4. **La lista de equipos del epígrafe 5 desarrolla los subpuntos 10.3 y 10.4 del anexo, que no han
   dado ninguna pregunta.** **Se escribe contra el programa**, y **su contenido es oficio de
   instalación.**

**El resto del tema va como oficio y así se declara**: la comparación entre las dos arquitecturas de
sensor, para qué se usa de verdad la obturación rápida, la explicación de la memoria previa a la
grabación, la razón de que la relación de fase se mida en un plano polar, el funcionamiento de la
señal en forma de pajarita, el aviso sobre la terminación de la cadena de iluminación, las dos
distinciones del epígrafe 5 y la advertencia sobre el retardo del sincronizador. **Nada de eso está en
un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
