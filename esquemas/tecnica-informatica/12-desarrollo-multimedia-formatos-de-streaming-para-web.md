# Esquema · Tema 12 del específico de Técnica Informática · Desarrollo multimedia: formatos de difusión en continuo para web

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de vídeo por internet.
**Siglas**: la difusión en continuo sobre el protocolo de transferencia de hipertexto (**HLS**) y la
difusión adaptativa dinámica sobre ese mismo protocolo (**DASH**); el protocolo de transferencia de
hipertexto (**HTTP**); el de transporte en tiempo real (**RTP**), el de difusión en tiempo real
(**RTSP**) y el de mensajería en tiempo real (**RTMP**); el de control de transmisión (**TCP**) y el
de datagramas de usuario (**UDP**); el lenguaje de marcado extensible (**XML**); el códec de vídeo
avanzado (**AVC**), su sucesor de alta eficiencia (**HEVC**) y las alternativas abiertas (**VP9** y
**AV1**); el formato de transporte del grupo de expertos en imágenes en movimiento (**MPEG-TS**) y el
formato de fichero de medios de base (**fMP4**); y la red de distribución de contenidos (**CDN**).

**Cabecera.** Enunciado: punto 14 del anexo · **CERO preguntas** · **el tema se escribe igual, contra
el programa**: **un punto con cero preguntas en un llamamiento puede tener cuatro en el siguiente**, y
**quien sólo estudia lo preguntado estudia el examen pasado.** **Tercer caso del proyecto**, tras el
punto 11 de Información Gráfica y el 1.6 de Sonido. · **Es el punto donde la informática de RTVE se
encuentra con el negocio de RTVE.**

<!-- indice -->

## Índice

- [Difusión en continuo frente a descarga](#difusión-en-continuo-frente-a-descarga)
- [La difusión adaptativa](#la-difusión-adaptativa)
- [Lo que había antes](#lo-que-había-antes)
- [Los códecs](#los-códecs)
- [La latencia](#la-latencia)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Difusión en continuo frente a descarga

| | **Descarga** | **Difusión en continuo** |
|---|---|---|
| **Cuándo empieza a verse** | **Cuando el fichero llegó entero** | **A los pocos segundos** |
| **Qué queda en el equipo** | **El fichero completo** | **Sólo lo de la memoria intermedia** |
| **Si se abandona** | **Se descargó todo igualmente** | **Sólo se transmitió lo visto** |

- **LA TÉCNICA QUE LO HACE POSIBLE ES PARTIR EL CONTENIDO EN TROZOS**: **el vídeo se corta en
  fragmentos de pocos segundos** y **el reproductor los pide uno tras otro.**

## La difusión adaptativa

1. **El mismo contenido se codifica varias veces**, a distintas calidades y caudales.
2. **Cada versión se parte en fragmentos alineados en el tiempo**, para saltar de una a otra sin
   corte.
3. **Un manifiesto describe qué versiones hay y dónde están sus fragmentos.**
4. **El reproductor mide su ancho de banda y elige, fragmento a fragmento, qué versión pide.**

- **POR QUÉ LO CAMBIÓ TODO**: **el servidor deja de decidir la calidad.** **La decide el reproductor,
  que es el único que sabe cómo va la red del espectador en ese instante.**

| | **HLS** | **DASH** |
|---|---|---|
| **Quién la impulsó** | **Apple** | **Un consorcio de la industria; es norma internacional** |
| **Manifiesto** | **Lista de reproducción `m3u8`** | **Descripción de presentación de medios, en XML** |
| **Contenedor** | **MPEG-TS al principio, fMP4 hoy** | **fMP4** |
| **Dónde manda** | **El mundo Apple, y por extensión casi todo** | **Televisión conectada y Europa** |

- **LO QUE TIENEN EN COMÚN IMPORTA MÁS QUE LO QUE LAS SEPARA**: **las dos van sobre HTTP**, y eso
  **permite servirlas desde una red de distribución de contenidos corriente**, la misma que sirve
  páginas web.

## Lo que había antes

| Protocolo | Cómo funcionaba | Por qué cayó |
|---|---|---|
| **RTP con RTSP** | **Sesión con control aparte, sobre UDP** | **Los cortafuegos lo bloquean y no se puede almacenar en caché** |
| **RTMP** | **Conexión permanente, sobre TCP** | **Dependía de un complemento de navegador que desapareció** |

- **LA LECCIÓN PARA QUIEN ADMINISTRA SISTEMAS**: **lo que va por el 80 y el 443 atraviesa cualquier
  red corporativa; lo que necesita puertos propios, no.** **Ésa es la razón técnica —y no la calidad—
  de que la difusión en continuo se montara sobre el protocolo web.**
- **EL MATIZ**: **RTP sigue siendo el rey de la contribución en tiempo real** —el enlace desde el
  lugar de la noticia—, **porque ahí la latencia manda.** **Lo que perdió es la distribución al
  espectador.**

## Los códecs

| Códec | Generación | Dónde se usa |
|---|---|---|
| **H.264 / AVC** | **La que universalizó el vídeo por internet** | **Compatible con todo** |
| **H.265 / HEVC** | **La siguiente: la mitad de caudal para igual calidad** | **Alta y ultraalta definición** |
| **VP9** | **Alternativa abierta de la generación de HEVC** | **Plataformas de vídeo abiertas** |
| **AV1** | **La más reciente y abierta** | **Ganando terreno, con coste de proceso alto** |

- **LA REGLA QUE ORDENA LA TABLA**: **cada generación baja aproximadamente a la mitad el caudal y sube
  el coste de cálculo.** **Y la compatibilidad va al revés que la eficiencia**: **el más viejo es el
  que reproduce todo el mundo.**
- **POR ESO UNA PLATAFORMA SERIA PUBLICA VARIAS VERSIONES**: **la eficiente para quien pueda
  descodificarla y la compatible para el resto.** **Es la difusión adaptativa aplicada al códec.**

## La latencia

- **EL DATO QUE CONVIENE LLEVAR**: **la difusión adaptativa clásica introduce entre veinte y treinta
  segundos de retardo**, porque **el reproductor necesita varios fragmentos por delante para no
  cortarse.**
- **NO IMPORTA EN UNA PELÍCULA Y SÍ EN UN DIRECTO**: **el espectador se entera del gol por la calle
  antes que por la pantalla.**
- **LAS VARIANTES DE BAJA LATENCIA** bajan a unos pocos segundos **partiendo los fragmentos en trozos
  aún más pequeños**, a costa de más peticiones y menos margen frente a un tirón de la red.

## Lo que se ha preguntado

**Ninguna pregunta.**

**Aviso de estudio**: **es el punto de menor rendimiento por hora del temario y a la vez uno de los
más baratos de preparar.** **Con la idea de la difusión adaptativa, el par HLS y DASH y la escala de
códecs se cubre lo razonablemente preguntable.** **Media hora, y no más.**
