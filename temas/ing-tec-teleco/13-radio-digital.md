# Tema 13 del específico de Ingeniería Técnica · Telecomunicación · Radio digital

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 17 |
| **Sirve para** | **Ing. Técnica Telecomunicación** y **Ing. Superior Telecomunicación** |
| **Punto compartido con Ing. Superior** | **Este mismo enunciado es el punto 24 del anexo de Ingeniería Superior · Telecomunicación**, palabra por palabra, así que **el tema se comparte y sirve a las dos ocupaciones** |
| **Fuente** | **Sin norma del boletín.** Su materia son las normas de radio digital y las recomendaciones de radiodifusión, **no consultadas**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Único punto de radio** | **Es el único punto del anexo dedicado enteramente a la radio**, y **el examen no ha entrado**. Una corporación que es de radio y televisión tiene la mitad de su nombre aquí |
| **Extensión** | **1.652 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la radiodifusión digital de audio (**DAB**) y su
versión mejorada (**DAB+**); la radio mundial digital (**DRM**); la Unión Internacional de
Telecomunicaciones (**UIT**); la multiplexación por división de frecuencias ortogonales codificada
(**COFDM**) del tema 5; la modulación de amplitud (**AM**) y la de frecuencia (**FM**); la
codificación de audio avanzada (**AAC**); el megahercio (**MHz**); y la red de frecuencia única
(**RFU**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 17):
> «Radio digital: Sistema DAB: características generales, mecanismos de transporte, información de la
> configuración del múltiplex, codificación de canal y señal de transmisión. Sistema DRM. Propagación.
> Bandas de frecuencia utilizadas. Normativa, recomendaciones de la UIT sobre radiodifusión.»

**Este tema sirve a DOS ocupaciones**: **el enunciado de arriba es también, palabra por palabra, el
punto 24 del anexo de Ingeniería Superior · Telecomunicación**, así que **el tema se comparte con
aquella ocupación**, como se comparte el de prevención de riesgos laborales. **Nada de lo que sigue
está escrito para una sola de las dos.**

**Cero preguntas.** **Este punto del anexo no ha dado ni una en el cuadernillo**, y **el tema se
escribe igual, contra el programa.**

**Y hay una razón añadida para escribirlo**: **es el único punto del anexo dedicado enteramente a la
radio.** **Una corporación que es de radio y televisión tiene la mitad de su nombre aquí**, y **el
examen no ha entrado.**

<!-- indice -->

## Índice

- [1. Por qué la radio digital no repitió la historia de la televisión](#1-por-qué-la-radio-digital-no-repitió-la-historia-de-la-televisión)
- [2. El sistema de radiodifusión digital de audio](#2-el-sistema-de-radiodifusión-digital-de-audio)
- [3. El múltiplex y su configuración](#3-el-múltiplex-y-su-configuración)
- [4. El otro sistema: la radio mundial digital](#4-el-otro-sistema-la-radio-mundial-digital)
- [5. Las bandas y la propagación](#5-las-bandas-y-la-propagación)
- [6. Lo que el examen ha preguntado](#6-lo-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Por qué la radio digital no repitió la historia de la televisión

**Conviene empezar por ahí porque explica el punto entero**: **la televisión analógica se apagó y la
radio analógica sigue emitiendo.**

| | **Televisión** | **Radio** |
|---|---|---|
| **Qué obligó al cambio** | **El espectro valía mucho y la digitalización lo liberaba** | **La banda de frecuencia modulada no vale lo mismo** |
| **Qué ganaba el oyente** | **Muchos más canales y mejor imagen** | **Algo más de calidad y algo más de oferta** |
| **Coste del receptor** | **Se cambió el televisor por otras razones** | **Hay que cambiar TODOS los receptores, incluido el del coche** |
| **Resultado** | **Apagón analógico** | **Convivencia indefinida** |

**La lección de ingeniería que deja**: **una norma técnica mejor no se impone sola.** **Hace falta que
alguien gane algo con el cambio**, y **en radio el que tenía que pagarlo —el oyente— no ganaba lo
suficiente.**

**Y el dato que lo confirma**: **en España la radio digital terrestre se licenció, se emitió y
prácticamente se apagó**, mientras que **en el Reino Unido, en Noruega y en Alemania se desplegó y en
algún caso sustituyó a la analógica.** **La diferencia no fue técnica: fue de política y de mercado.**

## 2. El sistema de radiodifusión digital de audio

**Sus características generales, que es lo primero que el enunciado pide:**

| Característica | Qué es |
|---|---|
| **Modulación** | **Multiportadora con intervalo de guarda**, la misma familia que la televisión terrestre del tema 5 |
| **Banda de trabajo** | **La banda III de televisión y la banda L** |
| **Ancho de bloque** | **1,536 megahercios** |
| **Codificación de audio** | **La original usaba una capa del grupo de expertos; la versión mejorada usa codificación avanzada** |
| **Red** | **De frecuencia única: todos los emisores en la misma frecuencia** |

**Y el rasgo que lo hace atractivo, que es el mismo que la televisión terrestre**: **la red de
frecuencia única.** **Un solo canal cubre un país entero y el receptor no tiene que resintonizar al
viajar**, que es exactamente lo contrario de lo que ocurre con la frecuencia modulada.

**La codificación de canal, que el enunciado nombra expresamente:**

| Mecanismo | Qué hace |
|---|---|
| **Codificación convolucional** | **Añade redundancia para corregir errores** |
| **Entrelazado en tiempo y en frecuencia** | **Reparte los bits para que una interferencia corta no dañe bits contiguos** |
| **Protección desigual** | **Da más protección a los bits que más importan** |

**El entrelazado merece una línea propia porque es la clave de la recepción en movimiento**: **un coche
que pasa bajo un puente pierde la señal durante un instante.** **Sin entrelazado, ese instante se lleva
un trozo entero de audio; con él, se lleva bits sueltos repartidos que la corrección reconstruye.**

## 3. El múltiplex y su configuración

**El enunciado pide expresamente «información de la configuración del múltiplex», y eso es lo más
propio del sistema:**

**Qué es el múltiplex**: **un bloque de capacidad que se reparte entre varios programas.** **A
diferencia de la frecuencia modulada, donde una frecuencia es una emisora, aquí una frecuencia lleva
varias.**

| Componente del múltiplex | Qué lleva |
|---|---|
| **Canal de servicio principal** | **Los programas de audio y los datos asociados** |
| **Canal de información rápida** | **La configuración: qué programas hay, cómo se llaman y dónde están** ✔ |
| **Canal de sincronización** | **La estructura de trama** |

**Y ahí está la diferencia de mentalidad respecto a la radio analógica**: **el receptor no busca
frecuencias: lee una lista.** **La información de configuración le dice qué servicios hay, con su
nombre y su tipo**, y **el usuario elige por nombre, no por número.**

**La consecuencia práctica que un ingeniero tiene que prever**: **la capacidad del múltiplex es fija y
se reparte.** **Añadir un programa quita caudal a los demás**, y **decidir ese reparto es una decisión
editorial disfrazada de técnica**: más programas con menos calidad, o menos con más.

## 4. El otro sistema: la radio mundial digital

**El enunciado lo nombra en segundo lugar, y resuelve otro problema:**

| | **Radiodifusión digital de audio** | **Radio mundial digital** |
|---|---|---|
| **Para qué banda nació** | **Bandas altas: banda III y banda L** | **Las bandas bajas: onda larga, media y corta** ✔ |
| **A quién sustituye** | **A la frecuencia modulada** | **A la amplitud modulada** |
| **Ancho de canal** | **1,536 megahercios** | **El de un canal de amplitud modulada: 9 o 10 kilohercios** |
| **Alcance** | **Local o regional** | **Continental, por reflexión ionosférica** |

**Y su virtud principal**: **cabe en el hueco de un canal analógico existente.** **Eso permite
digitalizar una emisión de onda media sin pedir espectro nuevo**, que era el gran obstáculo.

**Su versión para bandas altas** existe y **compite con el otro sistema**, lo que **es parte de la
razón de que ninguno de los dos se impusiera del todo**: **dos normas que resuelven lo mismo dividen
al mercado de receptores.**

## 5. Las bandas y la propagación

**El enunciado pide las dos cosas juntas, y van juntas porque la propagación depende de la banda:**

| Banda | Frecuencias | Cómo se propaga | Alcance |
|---|---|---|---|
| **Onda larga** | **Hasta 300 kilohercios** | **Onda de superficie** | **Cientos de kilómetros, estable** |
| **Onda media** | **De 526 a 1606 kilohercios** | **Superficie de día, ionosfera de noche** | **Regional de día, continental de noche** |
| **Onda corta** | **De 3 a 30 megahercios** | **Reflexión ionosférica** | **Miles de kilómetros, variable** |
| **Frecuencia modulada** | **De 87,5 a 108 megahercios** | **Línea de vista** | **Local** |
| **Banda III** | **Alrededor de 200 megahercios** | **Línea de vista** | **Local o regional** ✔ |
| **Banda L** | **Alrededor de 1,5 gigahercios** | **Línea de vista, muy limitada** | **Urbano** |

**Los tres fenómenos de propagación que el enunciado da por sabidos:**

| Fenómeno | Qué produce |
|---|---|
| **Onda de superficie** | **La señal sigue la curvatura del suelo**: alcance estable y previsible |
| **Reflexión ionosférica** | **La señal rebota en las capas altas**: alcance enorme y variable con la hora y la estación |
| **Propagación por línea de vista** | **La señal llega si no hay obstáculo**: alcance limitado por el horizonte |

**Y la observación que lo une todo**: **cuanto más alta la frecuencia, más se parece la radio a la
luz.** **Baja, rodea obstáculos y sigue el suelo; alta, va recta y se detiene en una pared.** **Ésa es
la razón de que la onda media entre en un sótano y la frecuencia modulada no.**

**Las recomendaciones que el enunciado nombra**: **la Unión Internacional de Telecomunicaciones
publica las de radiodifusión sonora y las de planificación de frecuencias**, y **son las que fijan las
condiciones técnicas de cada servicio en cada región.** **No se han consultado y así se declara.**

## 6. Lo que el examen ha preguntado

**Ninguna pregunta.**

**El aviso de estudio**: **es el único punto del anexo dedicado a la radio y no ha caído nada.** **Lo
razonablemente preguntable son las dos normas y para qué banda es cada una, la idea del múltiplex y la
tabla de propagación por bandas.** **Media hora bien empleada, y no más.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **no tiene ninguna respuesta oficial que
sostener**, porque el punto no ha dado preguntas.

**Cuatro declaraciones expresas:**

1. **Las normas de los dos sistemas de radio digital no se han consultado**: su texto está en
   organismos de normalización de acceso restringido. **Sus características generales, sus bandas y
   sus mecanismos de codificación son de uso corriente en el sector**, y **se presentan como
   conocimiento común de la materia.**
2. **Las recomendaciones de la Unión Internacional de Telecomunicaciones sobre radiodifusión tampoco
   se han consultado**, y **el temario sólo dice qué clase de contenido tienen.**
3. **Las cifras del epígrafe 5 —los límites de cada banda— son las de uso universal**, dadas como
   referencia. **Ninguna respuesta oficial depende de ellas**, porque el punto no ha dado preguntas.
4. **El epígrafe 1 contiene una interpretación del temario** —por qué la radio digital no siguió el
   camino de la televisión—, **presentada como tal y no como dato.** **Los despliegues que menciona en
   otros países son de conocimiento común.**

**El tema entero va como oficio y así se declara**, porque **su punto del anexo no tiene norma volcada
detrás ni preguntas que contestar**: se ha escrito contra el programa, que es lo que el manual de este
proyecto manda hacer con un punto sin banco.
