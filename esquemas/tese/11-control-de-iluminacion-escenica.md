# Esquema · Tema 11 del específico de Técnica de Equipos y Sistemas Electrónicos · Control de iluminación escénica

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de iluminación · `[conv]` =
enunciado de la convocatoria. **Siglas**: el multiplexado digital de la Asociación de Tecnología y
Producción de Espectáculos (**DMX**, y en su nombre completo **DMX512**); el diodo emisor de luz
(**LED**); el conector de tres o cinco contactos (**XLR**); y el protocolo de red para control de
iluminación (**Art-Net**).

**Cabecera.** Enunciado: punto 13 del anexo, el más corto de todos · **1 pregunta** · **el punto más
pequeño de la ocupación**, porque **la iluminación escénica tiene ocupación propia.**

<!-- indice -->

## Índice

- [Qué es un dimmer](#qué-es-un-dimmer)
- [La consola y la señal DMX](#la-consola-y-la-señal-dmx)
- [Diodos y robotizada](#diodos-y-robotizada)
- [Lo que el mantenimiento revisa](#lo-que-el-mantenimiento-revisa)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es un dimmer

- **PREGUNTA 79** · `[of]` · **Un dimmer es un dispositivo electrónico o mecánico cuya función es
  controlar la intensidad de una o varias fuentes de luz.**
- **LA PALABRA QUE DECIDE ES «INTENSIDAD».** **Las tres falsas nombran otras tres funciones reales:**

| Qué se quiere cambiar | Con qué se hace |
|---|---|
| **La intensidad** | **El atenuador** ✔ |
| **El color** | **Filtro, rueda de color o canales de un proyector de diodos** |
| **La temperatura de color** | **Cambio de lámpara, filtrado o mezcla de dos blancos** |
| **El momento del encendido** | **La memoria de la consola** |

- **POR QUÉ LA RESPUESTA DICE «O MECÁNICO»**: **el primer atenuador fue una resistencia variable movida
  a mano.** **El aparato es más viejo que la electrónica que hoy lo resuelve.**
- **EL AVISO QUE SEPARA DOS MUNDOS**: **una lámpara incandescente se atenúa recortando la onda de red;
  un diodo no.** **Enchufar un proyector de diodos a un canal de atenuador es la avería más frecuente
  del punto.**

## La consola y la señal DMX

- **LAS CIFRAS QUE HAY QUE LLEVAR**: **512 canales por universo · un byte por canal, de 0 a 255 · un
  solo sentido · cableado en cadena con terminador · conector de cinco contactos en la norma, de tres
  en la práctica.**
- **QUÉ ES UN UNIVERSO**: **una línea completa de 512 canales.** **Más canales piden más universos**, y
  de ahí que las instalaciones grandes encapsulen el DMX dentro de una red.
- **LA CUENTA DIARIA DEL ILUMINADOR**: **un aparato ocupa tantos canales como funciones tenga.** **Un
  atenuador, uno por circuito; un proyector de diodos de cuatro colores, cuatro; una luminaria
  robotizada, veinte o más.**
- **LA LIMITACIÓN DE FONDO DEL DMX**: **la consola habla y nadie contesta.** **No sabe si el foco
  recibió la orden.**

## Diodos y robotizada

| Ventaja del proyector de diodos | Consecuencia |
|---|---|
| **Consume mucho menos** | **Menos potencia contratada y menos sección de cable** |
| **Calienta mucho menos** | **Menos climatización y más confort en plató** |
| **Cambia de color sin filtros** | **Se acabaron las gelatinas** |

- **SUS TRES INCONVENIENTES**: **parpadeo con la cámara si la modulación bate con el obturador ·
  espectro incompleto en los blancos baratos · no se atenúa con el atenuador de sala.**
- **LA ROBOTIZADA AÑADE MOVIMIENTO**, y con él **una ventaja que enlaza con el tema 17**: **reenfocar
  un plató desde la consola convierte una tarea de altura en una tarea de sala.**

## Lo que el mantenimiento revisa

| Síntoma | Causa habitual |
|---|---|
| **Un aparato no responde y los demás sí** | **Dirección de inicio mal puesta** |
| **Parpadeo o respuesta a destiempo** | **Falta el terminador, o el cable no es el debido** |
| **Un aparato responde a órdenes de otro** | **Dos con la misma dirección de inicio** |
| **El canal sube y el foco no luce** | **Fallo en la potencia, no en los datos** |

- **LA REGLA DE DIAGNÓSTICO**: **separar siempre los datos de la potencia.** **Si recibe y no luce, el
  fallo está aguas abajo del atenuador; si no recibe, está en el cable de datos o en la dirección.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 79 | Qué es un dimmer | b) Dispositivo que controla la intensidad ✔ |

**La única oficial es correcta** y **no descansa sólo en la plantilla.** · **Aviso de estudio**: **con
una sola pregunta caída, el rendimiento está en lo que puede caer.** **Lo más preguntable son las
cifras del DMX y la incompatibilidad del diodo con el atenuador de sala.**
