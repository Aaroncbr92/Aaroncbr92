# Tema 12 del específico de Técnica Informática · Desarrollo multimedia: formatos de difusión en continuo para web

Las siglas de este tema, presentadas de entrada: la difusión en continuo sobre el protocolo de
transferencia de hipertexto (**HLS**, *HTTP live streaming*) y la difusión adaptativa dinámica sobre
ese mismo protocolo (**DASH**, *dynamic adaptive streaming over HTTP*); el protocolo de transferencia
de hipertexto (**HTTP**); el protocolo de transporte en tiempo real (**RTP**), el de difusión en
tiempo real (**RTSP**) y el de mensajería en tiempo real (**RTMP**); el protocolo de control de
transmisión (**TCP**) y el de datagramas de usuario (**UDP**); el lenguaje de marcado extensible
(**XML**); el códec de vídeo avanzado (**AVC**), su sucesor de alta eficiencia (**HEVC**)
y las alternativas abiertas (**VP9** y **AV1**); el formato de transporte de la norma del grupo de
expertos en imágenes en movimiento (**MPEG-TS**) y el formato de fichero de medios de base
(**fMP4**); y la red de distribución de contenidos (**CDN**, *content delivery network*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 14):
> «Desarrollo multimedia: formatos de streaming para web.»

**Cero preguntas.** **Este punto del anexo no ha dado ni una en el cuadernillo**, y **el tema se
escribe igual, contra el programa**, por la razón que el manual de este proyecto fija: **un punto con
cero preguntas en un llamamiento puede tener cuatro en el siguiente**, y **quien sólo estudia lo
preguntado estudia el examen pasado.**

**Es el tercer caso del proyecto**, después del punto 11 de Información Gráfica y del punto 1.6 de
Sonido.

**Y hay una razón añadida para escribirlo bien en esta ocupación**: **es el punto donde la informática
de RTVE se encuentra con el negocio de RTVE.** **Un técnico informático de una televisión pública
trabaja con vídeo, y este punto es el único del anexo que lo dice.**

<!-- indice -->

## Índice

- [1. Qué es la difusión en continuo y en qué se diferencia de una descarga](#1-qué-es-la-difusión-en-continuo-y-en-qué-se-diferencia-de-una-descarga)
- [2. La difusión adaptativa](#2-la-difusión-adaptativa)
- [3. Lo que había antes, y por qué se abandonó](#3-lo-que-había-antes-y-por-qué-se-abandonó)
- [4. Los códecs](#4-los-códecs)
- [5. La latencia, que es el problema abierto](#5-la-latencia-que-es-el-problema-abierto)
- [6. Lo que el examen ha preguntado](#6-lo-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Qué es la difusión en continuo y en qué se diferencia de una descarga

| | **Descarga** | **Difusión en continuo** |
|---|---|---|
| **Cuándo empieza a verse** | **Cuando el fichero ha llegado entero** | **A los pocos segundos** |
| **Qué queda en el equipo** | **El fichero completo** | **Sólo lo que está en la memoria intermedia** |
| **Qué pasa si se abandona** | **Se ha descargado todo igualmente** | **Sólo se transmitió lo visto** |

**Y la técnica que lo hace posible es partir el contenido en trozos**: **el vídeo se corta en
fragmentos de unos pocos segundos**, y **el reproductor los va pidiendo uno tras otro.**

## 2. La difusión adaptativa

**Es la idea que domina hoy el vídeo por internet**, y **la que hay que entender de este punto:**

1. **El mismo contenido se codifica varias veces**, a distintas calidades y caudales.
2. **Cada versión se parte en fragmentos alineados en el tiempo**, de modo que se pueda saltar de una
   a otra sin corte.
3. **Un fichero de manifiesto describe qué versiones hay y dónde están sus fragmentos.**
4. **El reproductor mide su propio ancho de banda y elige, fragmento a fragmento, qué versión pide.**

**Por qué eso lo cambió todo**: **el servidor deja de decidir la calidad.** **La decide el
reproductor, que es el único que sabe cómo va la red del espectador en ese instante.**

**Las dos familias que se reparten el mundo:**

| | **HLS** | **DASH** |
|---|---|---|
| **Quién la impulsó** | **Apple** | **Un consorcio de la industria, y es norma internacional** |
| **Manifiesto** | **Lista de reproducción `m3u8`** | **Descripción de presentación de medios, en XML** |
| **Contenedor de los fragmentos** | **MPEG-TS al principio, fMP4 hoy** | **fMP4** |
| **Dónde manda** | **El mundo Apple, y por extensión casi todo** | **Televisión conectada y Europa** |

**Lo que las dos tienen en común es más importante que lo que las separa**: **las dos van sobre HTTP**,
y **eso es lo que permite servirlas desde una red de distribución de contenidos corriente**, con la
misma infraestructura que sirve páginas web. **Ahí está la razón de que hayan desplazado a los
protocolos anteriores.**

## 3. Lo que había antes, y por qué se abandonó

| Protocolo | Cómo funcionaba | Por qué cayó |
|---|---|---|
| **RTP con RTSP** | **Sesión con control aparte, sobre UDP** | **Los cortafuegos lo bloquean y no se puede almacenar en caché** |
| **RTMP** | **Conexión permanente, sobre TCP** | **Dependía de un complemento de navegador que desapareció** |

**La lección que se lleva quien administra sistemas**: **lo que va por el puerto 80 y el 443 atraviesa
cualquier red corporativa.** **Lo que necesita puertos propios, no.** **Ésa es la razón técnica —y no
la calidad— de que la difusión en continuo se montara sobre el protocolo web.**

**Y el matiz que hay que hacer**: **RTP sigue siendo el rey de la contribución en tiempo real** —el
enlace desde el lugar de la noticia hasta la casa, del que hablan los temas de las ocupaciones
técnicas—, **porque ahí la latencia manda sobre todo lo demás.** **Lo que perdió es la distribución al
espectador.**

## 4. Los códecs

| Códec | Generación | Dónde se usa |
|---|---|---|
| **H.264 / AVC** | **La que universalizó el vídeo por internet** | **Compatible con todo** |
| **H.265 / HEVC** | **La siguiente: la mitad de caudal para la misma calidad** | **Alta definición y ultraalta** |
| **VP9** | **Alternativa abierta de la misma generación que HEVC** | **Plataformas de vídeo abiertas** |
| **AV1** | **La más reciente y abierta** | **Ganando terreno, con coste de proceso alto** |

**La regla que ordena la tabla**: **cada generación baja aproximadamente a la mitad el caudal
necesario y sube el coste de cálculo.** **Y la compatibilidad va al revés que la eficiencia**: **el
más viejo es el que reproduce todo el mundo.**

**Por eso una plataforma seria publica varias versiones**: **la eficiente para quien pueda
descodificarla y la compatible para el resto.** **Es la misma lógica de la difusión adaptativa,
aplicada al códec en vez de a la calidad.**

## 5. La latencia, que es el problema abierto

**Un dato que conviene llevar**: **la difusión adaptativa clásica introduce entre veinte y treinta
segundos de retardo**, porque **el reproductor necesita tener varios fragmentos por delante para no
cortarse.**

**Eso no importa en una película y sí en un directo**: **el espectador se entera del gol por la calle
antes que por la pantalla.** **Las variantes de baja latencia de las dos familias reducen el retardo a
unos pocos segundos partiendo los fragmentos en trozos aún más pequeños**, a costa de más peticiones y
menos margen frente a un tirón de la red.

## 6. Lo que el examen ha preguntado

**Ninguna pregunta.**

**El aviso de estudio**: **es el punto de menor rendimiento por hora del temario y a la vez uno de los
más baratos de preparar.** **Con la idea de la difusión adaptativa, el par HLS y DASH y la escala de
códecs se cubre lo razonablemente preguntable.** **Media hora, y no más.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **no tiene ninguna respuesta oficial que
sostener**, porque el punto no ha dado preguntas.

**Cuatro declaraciones expresas:**

1. **Las especificaciones de HLS, DASH, RTP, RTSP y RTMP no se han consultado.** **Lo que el tema
   afirma de cada una es de uso corriente en el sector**, y **se presenta como conocimiento común de
   la materia.**
2. **Las normas que definen los códecs H.264, H.265, VP9 y AV1 tampoco se han consultado.** **La
   regla de que cada generación reduce aproximadamente a la mitad el caudal es un orden de magnitud
   del uso corriente**, no una cifra tomada de ninguna norma.
3. **Las cifras de latencia del epígrafe 5 —entre veinte y treinta segundos en la difusión adaptativa
   clásica y unos pocos segundos en las variantes de baja latencia— son órdenes de magnitud**, y **así
   se presentan.**
4. **Apple y los consorcios que impulsan cada familia se nombran por ser quienes las publican**, dato
   de uso corriente. **No se ha consultado documentación de ninguno.**

**El tema entero va como oficio y así se declara**, porque **su punto del anexo no tiene norma detrás
ni preguntas que contestar**: se ha escrito contra el programa, que es lo que el manual de este
proyecto manda hacer con un punto sin banco.
