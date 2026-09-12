# Esquema · Realización (Asistencia) 16: realidad aumentada y producción online

Esqueleto para repasar. Todo desarrollado y verificado en el tema.

**Siglas**: el diodo emisor de luz (**LED**).

<!-- indice -->

## Índice

- [Tres técnicas que se confunden](#tres-técnicas-que-se-confunden)
- [Iluminar un croma](#iluminar-un-croma)
- [Seguimiento de cámara](#seguimiento-de-cámara)
- [Motor de representación](#motor-de-representación)
- [Retardo con realidad aumentada](#retardo-con-realidad-aumentada)
- [Efectos visuales y 360°](#efectos-visuales-y-360)
- [Distribución por red](#distribución-por-red)
- [Videoconferencia](#videoconferencia)

<!-- /indice -->

## Tres técnicas que se confunden

| Técnica | Qué es real | Cómo se junta |
|---|---|---|
| **Decorado virtual** | Sólo las personas y lo que tocan | Incrustación de crominancia |
| **Realidad aumentada** | **El plató entero** | Objetos superpuestos con llave |
| **Producción en pared de LED** | Personas y decorado próximo | **No hay incrustación**: se filma la pantalla |

*Las tres necesitan **saber dónde está la cámara** y las tres **añaden retardo**.*

## Iluminar un croma

**Dos trabajos, no uno**: iluminar al personaje **como si estuviera en el decorado virtual** y,
además, **iluminar el fondo uniformemente**.
*Separar al personaje del croma, no pegarlo: pegado recibe rebote verde y recorta peor.*

## Seguimiento de cámara

Familias: **mecánica por codificadores · óptica por marcas de referencia · óptica sin marcas · por
ultrasonidos · inercial**.
La ficha del **Mo-Sys StarTracker Max** documenta **marcas retrorreflectantes en techo, pared o
suelo**, y que **FreeD** es uno de los formatos de salida de esos datos hacia el motor.

**ERRATA DE PLANTILLA · pregunta 46 del primer llamamiento.** La opción marcada —«postes de croma
colocados en el techo»— **describe un montaje de croma y no mide nada**. **La correcta es la a)**:
«sensores que permiten establecer la posición de la cámara mediante la lectura de pequeñas marcas de
referencia».

## Motor de representación

**Unreal Engine**: motor de **render en tiempo real** para televisión, cine y videojuegos.
*Es la herramienta, no el resultado ni el sitio.*

## Retardo con realidad aumentada

Dos cámaras con realidad aumentada (2 fotogramas de retardo) y cinco sin ella; se hacen transiciones
**entre una cámara con RA y la misma sin RA**.
→ Las entradas al mezclador son **nueve, no siete**: siete directas y dos aumentadas.
→ **Retardo de 2 fotogramas en las siete señales directas** y **80 ms en todas las fuentes de
sonido** del plató.
*A 25 fps: 1 fotograma = 40 ms; 2 = 80 ms; 4 = 160 ms.*

## Efectos visuales y 360°

***Plate***: **el plano grabado que sirve de fondo o punto de partida** para integrar efectos.
***Stitching***: **empalmar las imágenes que forman una de 360°**. *El cuadernillo escribe
«Steaching».*

## Distribución por red

**Streaming** = consumo **al mismo tiempo que la descarga**, sin descargarlo previamente.
Para directo, **transmisión por secuencias**: trocea y sirve segmento a segmento, y se adapta.
*La descarga progresiva no sirve para el directo: lo que va a venir aún no existe.*

## Videoconferencia

El mayor desafío es **la diversidad de dispositivos y sistemas operativos de los participantes**:
es lo único que no se controla. *Se prueba antes con cada uno, en su equipo y en su sitio.*
