# Tema 13 del específico de Sonido · Radiofrecuencia

Las siglas y términos de este tema, presentados de entrada: la modulación de frecuencia (**FM**), la
de amplitud (**AM**) y la de fase (**PM**); la radiofrecuencia en general (**RF**); la difusión de audio digital (**DAB**) y su versión actual (**DAB+**); el
sistema de datos por radio (**RDS**, *radio data system*); la corrección de errores hacia adelante y,
en particular, el código **Reed-Solomon**; la red de frecuencia única (**SFN**, *single frequency
network*); el megahercio (**MHz**) y el kilohercio (**kHz**); las bandas de radiodifusión numeradas en
romanos (**banda I**, **II**, **III**, **IV** y **V**); y el códec **HE-AAC v2**, que es el que el DAB+
emplea.

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 11):
> «RADIOFRECUENCIA. Microfonía Inalámbrica. Antenas. Cableado. Tipos de modulaciones.»

**Tres preguntas.** **Y una particularidad que conviene señalar antes de estudiar**: **el enunciado
pide microfonía inalámbrica, antenas y cableado, y el examen preguntó por las tres cosas que NO
enumera**: **la banda de la FM, el sistema DAB+ y el tono piloto del estéreo.** **Las tres son de
radiodifusión, no de microfonía.**

**El tema desarrolla las dos cosas**: **lo que el examen preguntó y lo que el programa pide.**

<!-- indice -->

## Índice

- [1. Las bandas de radiodifusión](#1-las-bandas-de-radiodifusión)
- [2. El tono piloto de la FM estéreo](#2-el-tono-piloto-de-la-fm-estéreo)
- [3. El DAB+](#3-el-dab)
- [4. Los tipos de modulación](#4-los-tipos-de-modulación)
- [5. La microfonía inalámbrica](#5-la-microfonía-inalámbrica)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Las bandas de radiodifusión

**La emisión de radio FM corresponde a la banda II.** Ésa es la respuesta oficial a la pregunta 41.

**Las cinco bandas de radiodifusión, con lo que va en cada una:**

| Banda | Margen aproximado | Qué se emite |
|---|---|---|
| **I** | **47 a 68 MHz** | **Televisión analógica antigua**: ya no se usa para eso |
| **II** ✔ | **87,5 a 108 MHz** | **Radio FM** |
| **III** | **174 a 230 MHz** | **DAB y televisión digital en algunos países** |
| **IV** | **470 a 582 MHz** | **Televisión digital terrestre** |
| **V** | **582 a 862 MHz** | **Televisión digital terrestre**, y de aquí salió el dividendo digital |

**La que hay que fijar es la II, porque es la de la FM**, y **el número que la acompaña —de 87,5 a 108
megahercios— es el que todo el mundo conoce del dial.**

**Y el dato que enlaza con la microfonía inalámbrica del epígrafe 5**: **los micrófonos sin hilos
trabajan históricamente en huecos de las bandas IV y V**, es decir, **en el espectro de la televisión.**
**Cada vez que ese espectro se reasigna, los equipos de microfonía se quedan fuera de banda.**

## 2. El tono piloto de la FM estéreo

**El tono piloto de una transmisión FM en estéreo es un tono de 19 kHz.** Ésa es la respuesta oficial
a la pregunta 87.

**Para qué está ahí, que es lo que hace memorable la cifra**: **la FM estéreo tuvo que inventarse
siendo compatible con los receptores mono que ya existían.** **La solución fue mandar dos cosas:**

| Qué se manda | Dónde | Quién lo usa |
|---|---|---|
| **La suma L+R** | **En la banda base, de 30 Hz a 15 kHz** | **Todos los receptores**: es lo que oye un mono |
| **El tono piloto de 19 kHz** | **Justo encima de la banda base** | **El receptor estéreo**, para saber que hay estéreo y para reconstruir la portadora |
| **La diferencia L−R** | **Modulada en 38 kHz** | **El receptor estéreo**, que suma y resta para recuperar L y R |

**Y los 19 kilohercios no son arbitrarios**: **son exactamente la MITAD de 38.** **El receptor toma el
piloto, lo dobla, y con eso obtiene la portadora de 38 kHz que necesita para demodular la
diferencia**, en fase y sin ambigüedad.

**Las tres opciones falsas son frecuencias conocidas de otro terreno**: **44,1 y 48 kilohercios son
frecuencias de MUESTREO —del tema 9— y 24 no es nada en este contexto.** **La pregunta castiga
confundir el mundo de la radiodifusión con el del audio digital.**

**Y el dato que conviene añadir porque completa el cuadro**: **el RDS, que es lo que manda el nombre
de la emisora y el texto al dial, viaja en 57 kHz**, que **es tres veces el piloto.** **Toda la
multiplexación de la FM cuelga de esos 19 kilohercios.**

## 3. El DAB+

**De las afirmaciones sobre el Digital Audio Broadcasting, la cierta es que la corrección de errores
Reed-Solomon hace más robusta la señal de audio.** Ésa es la respuesta oficial a la pregunta 71.

**Qué es el DAB+ y en qué se diferencia de la FM:**

| | **FM** | **DAB+** |
|---|---|---|
| **Naturaleza** | **Analógica** | **Digital** |
| **Cuántos programas por frecuencia** | **Uno** | **Un múltiplex con VARIOS** |
| **Banda** | **II** | **III**, en la implantación europea |
| **Qué pasa al degradarse** | **Ruido creciente**: se sigue oyendo peor | **Funciona o se corta**: el precipicio digital |
| **Datos asociados** | **RDS**: texto corto | **Metadatos ricos**: título, carátula, guía de programas |

**Y la corrección de errores es la respuesta porque es lo que resuelve el problema de arriba**: **en
digital, un error de bit no degrada: rompe.** **Para que la señal aguante los desvanecimientos, los
ecos y el movimiento del receptor hay que poder RECONSTRUIR los bits perdidos**, y **eso es lo que
hace un código como el Reed-Solomon: añadir redundancia calculada para que el receptor rehaga lo que
falte.**

**Las tres opciones falsas, y las tres son falsas por razones distintas:**

1. **«Consigue mayor calidad utilizando el códec AC3+ v2»** **nombra un códec equivocado**: **el DAB+
   emplea HE-AAC v2**, no una variante de AC-3.
2. **«Por el momento NO transporta metadatos»** **es exactamente lo contrario de una de sus virtudes
   principales**: **el DAB+ transporta metadatos ricos, y es una de las razones por las que se
   implanta.**
3. **«Sólo se contemplan redes nacionales de frecuencia única»** **absolutiza**: **el DAB admite redes
   de frecuencia única, y también redes locales y regionales.** **Es la trampa del «sólo» que este
   cuadernillo repite en varios puntos.**

**Y la red de frecuencia única merece una línea porque es la ventaja estructural del DAB sobre la
FM**: **todos los transmisores de la red emiten en la MISMA frecuencia.** **En FM eso produciría
interferencia; en un sistema digital con intervalo de guarda, las señales de dos transmisores se suman
en vez de estorbarse.** **Por eso un receptor DAB no hay que resintonizarlo al cambiar de provincia.**

## 4. Los tipos de modulación

**El enunciado los pide expresamente y el examen no los pregunta.** **El tema los cubre porque el
programa lo pide.**

| Modulación | Qué varía de la portadora | Dónde se usa |
|---|---|---|
| **AM** | **La AMPLITUD** | **Onda media y corta**: mucho alcance, poca calidad, sensible al ruido eléctrico |
| **FM** | **La FRECUENCIA** | **Radiodifusión en banda II y microfonía inalámbrica analógica** |
| **PM** | **La FASE** | **Base de las modulaciones digitales** |
| **Digitales** (**QPSK**, **QAM**, **OFDM**) | **Combinan amplitud y fase**, y reparten en muchas portadoras | **DAB, televisión digital, redes** |

**Y la razón de que la FM ganara a la AM en calidad**: **el ruido eléctrico es sobre todo ruido de
AMPLITUD.** **Un receptor de FM puede recortar toda variación de amplitud sin perder información,
porque la información está en la frecuencia.** **Un receptor de AM no puede: ahí el ruido y la señal
son lo mismo.**

## 5. La microfonía inalámbrica

**Es el primer subpunto del enunciado y el examen no lo pregunta.** **Es, sin embargo, lo que un
técnico de sonido usa de radiofrecuencia todos los días.**

**Los cinco problemas que un montaje de inalámbricos plantea, y cómo se resuelven:**

| Problema | Solución |
|---|---|
| **Encontrar frecuencias libres** | **Explorar el espectro en el propio recinto y calcular un plan de frecuencias** |
| **Intermodulación** | **Las combinaciones de dos o más portadoras caen sobre otras**: el plan tiene que evitar esas combinaciones, no sólo los solapes |
| **Desvanecimiento** | **Diversidad**: dos antenas y el receptor toma la mejor en cada instante |
| **Reparto de antenas** | **Un distribuidor de antena** alimenta varios receptores desde un solo par |
| **Alcance** | **Antenas direccionales a la vista del escenario y cable de baja pérdida**, porque **la pérdida en el cable de RF es mucho mayor que en audio** |

**Y la diferencia con el cableado del tema 11 que hay que tener clara**: **un cable de audio largo
casi no pierde nivel; un cable de radiofrecuencia largo pierde mucho y a más frecuencia más pierde.**
**Por eso las antenas se acercan al escenario y no los receptores.**

## 6. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 41 | A qué banda corresponde la radio FM | b) Banda II ✔ |
| 71 | Qué afirmación sobre el DAB+ es cierta | c) Reed-Solomon hace más robusta la señal ✔ |
| 87 | Cuál es el tono piloto de la FM estéreo | b) 19 kHz ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Y el aviso de reparto**: **las tres preguntas son de radiodifusión y el enunciado pide microfonía,
antenas y cableado.** **Es la mayor divergencia entre programa y examen de toda la ocupación.**
**Quien estudie sólo por el examen se queda sin lo que el programa promete; quien estudie sólo por el
programa se pierde tres preguntas fáciles.** **Hay que hacer las dos cosas, y son pocas páginas.**

## 7. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es la radiofrecuencia aplicada al sonido, y **va
entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | Las tres **van como oficio** |

**Cuatro declaraciones expresas:**

1. **Los márgenes de frecuencia de las cinco bandas del epígrafe 1 son los de la atribución europea de
   espectro**, y **no proceden de ninguna norma volcada en este proyecto.** **Son cifras redondeadas
   de uso corriente**, y **lo que la pregunta 41 mide es la asignación de la FM a la banda II, que es
   inequívoca.**
2. **Las frecuencias de la multiplexación de la FM estéreo —19, 38 y 57 kilohercios— son las de la
   norma de radiodifusión**, que **tampoco se ha consultado.** **La relación entre ellas —el piloto es
   la mitad de la subportadora de diferencia— es una consecuencia del propio diseño del sistema**, y
   **el tema la presenta como conocimiento común de la materia.**
3. **La atribución del códec HE-AAC v2 al DAB+ no se ha contrastado en la especificación del
   sistema.** **La sostiene la respuesta oficial por descarte** —el enunciado ofrece «AC3+ v2», que no
   es el códec del DAB+— **y el temario declara que la especificación no se ha leído.**
4. **El plan de frecuencias y la intermodulación del epígrafe 5 son práctica de oficio**, y **el tema
   los presenta como tales.** **Ninguna pregunta depende de ellos.**

**El resto del tema va como oficio y así se declara**: la tabla de bandas, el mecanismo de la
multiplexación estéreo, la diferencia entre FM y DAB+ y por qué la corrección de errores es
imprescindible en digital, la tabla de modulaciones y por qué la FM resiste mejor el ruido, y los
cinco problemas de un montaje de inalámbricos. **Nada de eso está en un boletín oficial ni en una
norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
