# Esquema · Tema 6 del específico de Sonido · Señales de contribución

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de contribución · `[plan]` =
plantilla oficial. **Siglas**: el protocolo de internet (**IP**); la red digital de servicios
integrados (**RDSI**); la radiodifusión digital de audio (**DAB**); el menos uno de los retornos
(**N-1**); y **Dante**, que es un nombre comercial y no unas siglas.

**Cabecera.** Enunciado: «1.7. Señales de contribución» · **4 preguntas** · **dos son del N-1 y dos son
de qué enlace sirve para qué.**

<!-- indice -->

## Índice

- [Qué es una señal de contribución](#qué-es-una-señal-de-contribución)
- [El N-1: la resta que hace posible un directo](#el-n-1-la-resta-que-hace-posible-un-directo)
- [Dos líneas, dos retornos](#dos-líneas-dos-retornos)
- [Qué se puede mandar por IP y qué no](#qué-se-puede-mandar-por-ip-y-qué-no)
- [La RDSI y lo que vino después](#la-rdsi-y-lo-que-vino-después)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es una señal de contribución

- **LA DEFINICIÓN**: **la que va del sitio donde ocurre la noticia a la casa**, frente a la de difusión,
  que va de la casa al espectador.
- **QUÉ LA CARACTERIZA**: **calidad alta, latencia baja y, casi siempre, ida y vuelta.**

## El N-1: la resta que hace posible un directo

- **PREGUNTA 59** · `[of]` · **Una conexión dúplex N-1 es aquella en la que se envían todas las señales
  del envío excepto la que nos envían.**
- **POR QUÉ EXISTE**: **si al enviado se le devuelve su propia voz con el retardo del enlace, se oye a
  sí mismo con eco y no puede hablar.** **Restándose a sí mismo del retorno, el problema desaparece.**
- **CÓMO SE LLAMA POR AHÍ FUERA**: **«mix menos», «clean feed» y «N-1» son la misma cosa.**

## Dos líneas, dos retornos

- **PREGUNTA 30** · `[of]` · **Con línea principal y línea de reserva hay que enviar dos N-1 cruzados,
  cada uno excluyendo la otra línea.**
- **EL RAZONAMIENTO**: **si la vuelta del retorno viene por la línea principal, lo que hay que restar
  es la principal; si viene por la de reserva, la de reserva.** **Cruzarlos es lo que evita el eco
  cualquiera que sea la línea que quede en pie.**
- **QUÉ PASA SI NO SE CRUZAN**: **el día que se cae la principal, el enviado se oye a sí mismo**, que
  es el momento peor posible.

## Qué se puede mandar por IP y qué no

- **PREGUNTA 93** · `[of]` · **El enlace que NO sirve para una conexión IP bidireccional entre dos
  códecs es el de microondas por transmisión DAB.**
- **LA PALABRA QUE DECIDE ES «BIDIRECCIONAL»**: **el DAB es un sistema de difusión, de uno a muchos y
  en un solo sentido.** **No tiene camino de vuelta.**
- **PREGUNTA 44** · `[plan]` · **De los algoritmos enumerados, el que NO serviría para una llamada por
  IP es Dante.**
- **AVISO: LA PREGUNTA ESTÁ ROTA** · **sus opciones c) y d) son idénticas**, y **el temario lo
  declara.** **La respuesta oficial sigue siendo correcta**: **Dante es un transporte de audio para red
  local, no un algoritmo de codificación para una llamada por internet.**

## La RDSI y lo que vino después

- **LA SECUENCIA HISTÓRICA**: **línea telefónica, RDSI, y después códecs sobre IP.**
- **LO QUE CAMBIÓ**: **la RDSI daba un canal reservado y una latencia previsible; la IP da mucho más
  ancho de banda y ninguna garantía**, y de ahí que se protejan con los mecanismos del audio sobre
  redes del tema 16.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 30 | Qué retornos enviar con línea principal y de reserva | c) N-1 cruzados ✔ |
| 44 | Qué algoritmo NO sirve para una llamada por IP | b) Dante ✔ **·** la pregunta está rota |
| 59 | En qué consiste una conexión dúplex N-1 | d) Todas las señales menos la que nos envían ✔ |
| 93 | Qué enlace NO sirve para una conexión IP bidireccional | d) Microondas por DAB ✔ |

**Las cuatro oficiales son correctas** · **una viene de una pregunta mal construida y así se
declara.** · **Aviso de estudio**: **el N-1 es la idea más rentable del punto**: **contesta dos
preguntas y explica la mitad de las averías de un directo.**
