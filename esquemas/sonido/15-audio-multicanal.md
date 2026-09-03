# Esquema · Tema 15 del específico de Sonido · Audio multicanal

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de sonido envolvente · `[plan]`
= plantilla oficial. **Siglas**: el canal de efectos de baja frecuencia (**LFE**, *low frequency
effects*); la mezcla reducida compatible con matriz (**Lt/Rt**, *left total / right total*) y la
reducida estéreo simple (**Lo/Ro**, *left only / right only*); y **Dolby Atmos** y **Dolby E**, que son
nombres comerciales y no siglas.

**Cabecera.** Enunciado: «1.15. Audio multicanal» · **4 preguntas** · **dos son de notación, una de
concepto y una de mezcla reducida.**

<!-- indice -->

## Índice

- [Cómo se lee un formato multicanal](#cómo-se-lee-un-formato-multicanal)
- [Canales frente a objetos](#canales-frente-a-objetos)
- [El bed](#el-bed)
- [Las mezclas reducidas](#las-mezclas-reducidas)
- [El Dolby E](#el-dolby-e)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Cómo se lee un formato multicanal

- **LA NOTACIÓN TIENE TRES CIFRAS Y CADA UNA ES UN PLANO**: **la primera son los canales del plano
  horizontal; la segunda, los de baja frecuencia; la tercera, los de altura.**
- **PREGUNTA 54** · `[of]` · **5.1.4 son 5 canales horizontales, 1 de efectos de baja frecuencia y 4
  en vertical.**
- **LOS FORMATOS CORRIENTES**: **2.0 estéreo · 5.1 envolvente clásico · 7.1 envolvente ampliado ·
  5.1.4 y 7.1.4 con altura.**
- **POR QUÉ EL «.1» NO CUENTA COMO CANAL ENTERO**: **el canal de efectos de baja frecuencia lleva sólo
  la parte grave del espectro**, y por eso se escribe como una décima parte.

## Canales frente a objetos

- **PREGUNTA 81** · `[of]` · **Lo que caracteriza a Dolby Atmos es un enfoque basado en objetos de
  audio.**
- **LA DIFERENCIA DE FONDO**: **en un formato de canales se decide en la mezcla por qué altavoz sale
  cada cosa; en uno de objetos se guarda dónde está cada sonido y el reproductor decide por qué
  altavoces lo saca**, según la sala que tenga.
- **QUÉ GANA**: **la misma mezcla vale para una sala de doce altavoces y para unos auriculares.**

## El bed

- **PREGUNTA 10** · `[plan]` · **El tamaño máximo del bed en Dolby Atmos es 7.1.2.**
- **QUÉ ES EL BED**: **la cama de canales fijos sobre la que se colocan los objetos.** **Lo que no
  necesita moverse va ahí**: ambientes, música, coros.
- **POR QUÉ DESCANSA EN LA PLANTILLA**: **es una cifra de especificación de un producto comercial**, y
  **el temario declara que no ha consultado esa especificación.**

## Las mezclas reducidas

- **PREGUNTA 96** · `[of]` · **Para poder decodificar después la trasera y la central hay que hacer un
  downmix Lt/Rt.**
- **LAS DOS REDUCCIONES, UNA FRENTE A OTRA:**

| Reducción | Qué hace | Se puede volver atrás |
|---|---|---|
| **Lo/Ro** | **Suma los canales a estéreo sin más** | **No** |
| **Lt/Rt** | **Codifica en matriz la trasera y la central dentro del estéreo** | **Sí, con un decodificador de matriz** ✔ |

- **LA LETRA QUE LO DICE TODO**: **la «t» es de *total***: lleva dentro más de lo que se oye en
  estéreo.

## El Dolby E

- **PARA QUÉ SIRVE**: **meter una señal multicanal completa dentro de un par de canales de audio
  digital**, para que viaje por una infraestructura pensada para estéreo.
- **SU RASGO CRÍTICO**: **va alineado al cuadro de vídeo.** **Un corte fuera de cuadro parte una trama
  y produce un chasquido**, que es la avería característica del formato.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 10 | Tamaño máximo del bed en Dolby Atmos | a) 7.1.2 ✔ **·** sólo con la plantilla |
| 54 | Qué significa una escucha 5.1.4 | a) 5 horizontales, 1 de baja frecuencia y 4 en vertical ✔ |
| 81 | Qué caracteriza a Dolby Atmos | b) Un enfoque basado en objetos de audio ✔ |
| 96 | Downmix del que se puedan decodificar trasera y central | b) Lt/Rt ✔ |

**Las cuatro oficiales son correctas** · **una descansa sólo en la plantilla.** · **Aviso de
estudio**: **leer la notación de tres cifras contesta una pregunta y evita equivocarse en las otras
tres.**
