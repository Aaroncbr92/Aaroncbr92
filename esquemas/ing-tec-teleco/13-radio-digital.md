# Esquema · Tema 13 del específico de Ingeniería Técnica · Telecomunicación · Radio digital

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de radiodifusión · `[plan]` =
enunciado del propio anexo · `[norma]` = norma o recomendación nombrada, sin cita literal. **Siglas**:
la radiodifusión digital de audio (**DAB**) y su versión mejorada (**DAB+**); la radio mundial digital
(**DRM**); la Unión Internacional de Telecomunicaciones (**UIT**); la multiplexación por división de
frecuencias ortogonales codificada (**COFDM**); la modulación de amplitud (**AM**) y la de frecuencia
(**FM**); la codificación de audio avanzada (**AAC**); el megahercio (**MHz**); y la red de frecuencia
única (**RFU**).

**Cabecera.** Enunciado: punto 17 del anexo · **cero preguntas** · **es el ÚNICO punto del anexo
dedicado enteramente a la radio**: una corporación que es de radio y televisión tiene la mitad de su
nombre aquí, **y el examen no ha entrado.**

**Tema compartido.** **El enunciado de este punto es también, palabra por palabra, el punto 24 del
anexo de Ingeniería Superior · Telecomunicación**, así que **este esquema sirve a las dos
ocupaciones.**

<!-- indice -->

## Índice

- [Por qué la radio no repitió la historia de la televisión](#por-qué-la-radio-no-repitió-la-historia-de-la-televisión)
- [El sistema de radiodifusión digital de audio](#el-sistema-de-radiodifusión-digital-de-audio)
- [El múltiplex](#el-múltiplex)
- [La radio mundial digital](#la-radio-mundial-digital)
- [Bandas y propagación](#bandas-y-propagación)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Por qué la radio no repitió la historia de la televisión

| | **Televisión** | **Radio** |
|---|---|---|
| **Qué obligó al cambio** | **El espectro valía mucho y digitalizar lo liberaba** | **La banda de frecuencia modulada no vale lo mismo** |
| **Qué ganaba el usuario** | **Muchos más canales y mejor imagen** | **Algo más de calidad y algo más de oferta** |
| **Coste del receptor** | **El televisor se cambió por otras razones** | **Hay que cambiar TODOS los receptores, el del coche incluido** |
| **Resultado** | **Apagón analógico** | **Convivencia indefinida** |

- **LA LECCIÓN DE INGENIERÍA** · `[of]` · **Una norma técnica mejor no se impone sola.** **Hace falta
  que alguien gane algo con el cambio**, y **en radio el que tenía que pagarlo —el oyente— no ganaba
  lo suficiente.**
- **EL DATO QUE LO CONFIRMA** · `[of]` · **En España se licenció, se emitió y prácticamente se apagó**;
  **en el Reino Unido, Noruega y Alemania se desplegó y en algún caso sustituyó a la analógica.** **La
  diferencia no fue técnica: fue de política y de mercado.**

## El sistema de radiodifusión digital de audio

| Característica | Qué es |
|---|---|
| **Modulación** | **Multiportadora con intervalo de guarda**, la familia de la televisión terrestre |
| **Banda de trabajo** | **Banda III de televisión y banda L** |
| **Ancho de bloque** | **1,536 megahercios** |
| **Codificación de audio** | **La original, una capa del grupo de expertos; la mejorada, codificación avanzada** |
| **Red** | **De frecuencia única: todos los emisores en la misma frecuencia** |

- **EL RASGO ATRACTIVO** · `[of]` · **Un solo canal cubre un país entero y el receptor no resintoniza al
  viajar**, que es lo contrario de la frecuencia modulada.

| Codificación de canal · `[plan]` | Qué hace |
|---|---|
| **Codificación convolucional** | **Añade redundancia para corregir errores** |
| **Entrelazado en tiempo y frecuencia** | **Reparte los bits para que una interferencia corta no dañe bits contiguos** |
| **Protección desigual** | **Más protección a los bits que más importan** |

- **POR QUÉ EL ENTRELAZADO ES LA CLAVE EN MOVIMIENTO** · `[of]` · **Un coche que pasa bajo un puente
  pierde la señal un instante.** **Sin entrelazado ese instante se lleva un trozo entero de audio; con
  él, bits sueltos repartidos que la corrección reconstruye.**

## El múltiplex

- **QUÉ ES** · `[of]` · **Un bloque de capacidad que se reparte entre varios programas.** **En
  frecuencia modulada una frecuencia es una emisora; aquí una frecuencia lleva varias.**

| Componente | Qué lleva |
|---|---|
| **Canal de servicio principal** | **Los programas de audio y sus datos** |
| **Canal de información rápida** | **La configuración: qué programas hay, cómo se llaman, dónde están** ✔ |
| **Canal de sincronización** | **La estructura de trama** |

- **EL CAMBIO DE MENTALIDAD** · `[of]` · **El receptor no busca frecuencias: LEE UNA LISTA.** **El
  usuario elige por nombre, no por número.**
- **LA CONSECUENCIA QUE UN INGENIERO HA DE PREVER** · `[of]` · **La capacidad del múltiplex es fija y se
  reparte**: **añadir un programa quita caudal a los demás**, y **decidir ese reparto es una decisión
  editorial disfrazada de técnica.**

## La radio mundial digital

| | **Radiodifusión digital de audio** | **Radio mundial digital** |
|---|---|---|
| **Para qué banda nació** | **Bandas altas: III y L** | **Bandas bajas: onda larga, media y corta** ✔ |
| **A quién sustituye** | **A la frecuencia modulada** | **A la amplitud modulada** |
| **Ancho de canal** | **1,536 megahercios** | **9 o 10 kilohercios** |
| **Alcance** | **Local o regional** | **Continental, por reflexión ionosférica** |

- **SU VIRTUD PRINCIPAL** · `[of]` · **Cabe en el hueco de un canal analógico existente**: digitaliza
  una emisión de onda media **sin pedir espectro nuevo**, que era el gran obstáculo.
- **POR QUÉ NINGUNO SE IMPUSO DEL TODO** · `[of]` · **Su versión para bandas altas compite con el otro
  sistema**, y **dos normas que resuelven lo mismo dividen al mercado de receptores.**

## Bandas y propagación

| Banda | Frecuencias | Cómo se propaga | Alcance |
|---|---|---|---|
| **Onda larga** | **Hasta 300 kHz** | **Onda de superficie** | **Cientos de kilómetros, estable** |
| **Onda media** | **De 526 a 1606 kHz** | **Superficie de día, ionosfera de noche** | **Regional de día, continental de noche** |
| **Onda corta** | **De 3 a 30 MHz** | **Reflexión ionosférica** | **Miles de kilómetros, variable** |
| **Frecuencia modulada** | **De 87,5 a 108 MHz** | **Línea de vista** | **Local** |
| **Banda III** | **Alrededor de 200 MHz** | **Línea de vista** | **Local o regional** ✔ |
| **Banda L** | **Alrededor de 1,5 GHz** | **Línea de vista muy limitada** | **Urbano** |

| Fenómeno | Qué produce |
|---|---|
| **Onda de superficie** | **La señal sigue la curvatura del suelo**: alcance estable y previsible |
| **Reflexión ionosférica** | **Rebota en las capas altas**: alcance enorme y variable con hora y estación |
| **Línea de vista** | **Llega si no hay obstáculo**: alcance limitado por el horizonte |

- **LA OBSERVACIÓN QUE LO UNE TODO** · `[of]` · **Cuanto más alta la frecuencia, más se parece la radio
  a la luz.** **Baja: rodea obstáculos y sigue el suelo. Alta: va recta y se detiene en una pared.**
  **Por eso la onda media entra en un sótano y la frecuencia modulada no.**
- **LAS RECOMENDACIONES DEL ENUNCIADO** · `[norma]` · **La Unión Internacional de Telecomunicaciones
  publica las de radiodifusión sonora y las de planificación de frecuencias**: fijan las condiciones
  técnicas de cada servicio en cada región. **No se han consultado y así se declara.**

## Lo que se ha preguntado

- **NINGUNA PREGUNTA.**
- **LO RAZONABLEMENTE PREGUNTABLE** · `[of]` · **Las dos normas y para qué banda es cada una**, **la
  idea del múltiplex** y **la tabla de propagación por bandas.** **Media hora bien empleada, y no más.**
