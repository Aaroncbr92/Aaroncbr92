# Esquema · Tema 12 del específico de Ingeniería Técnica · Telecomunicación · Sonido

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de sonido · `[exam]` = opciones
del propio cuadernillo · `[norma]` = norma o recomendación nombrada, sin cita literal. **Siglas**: el
decibelio (**dB**) y sus referencias —el milivatio (**dBm**), la tensión de 0,775 voltios (**dBu**) y
la escala digital (**dBFS**)—; la Sociedad de Ingeniería de Audio (**AES**) y la Unión Europea de
Radiodifusión (**UER**, en inglés **EBU**), que publican **AES/EBU** y **EBU R128**; la interfaz
digital de audio multicanal (**MADI**); la de Sony y Philips (**SPDIF**); la cinta digital de ocho
pistas de Alesis (**ADAT**); la interfaz digital de instrumentos musicales (**MIDI**); la modulación
por impulsos codificados (**PCM**); la de desplazamiento de fase en cuadratura (**QPSK**) y la de
amplitud en cuadratura (**QAM**); el par trenzado sin apantallar (**UTP**); el kilohercio (**kHz**);
la unidad de sonoridad referida a escala completa (**LUFS**); los formatos por su extensión (**WAV**,
**AIFF**, **FLAC**, **ALAC**, **MP3**, **AAC**); la Máquinas de Negocio Internacionales (**IBM**); las
tres técnicas de toma estéreo (**MS**, **XY**, **AB**); el atenuador de escucha de una mesa
(**DIM**); y **Dante**, **NICAM** y **Dolby**, que son nombres de sistema y no siglas.

**Cabecera.** Enunciado: punto 16 del anexo · **18 preguntas: el banco más grande de la ocupación,
empatado con el de redes** · **entre los dos, 36 de las 85 del específico: el 42 % del examen** ·
**reparto**: 4 de niveles y medida, 3 de audio sobre red, 3 de formatos de fichero, 3 de microfonía, 2
de mesa y monitores, 2 de interfaces, 1 de protocolo de instrumentos.

<!-- indice -->

## Índice

- [Los decibelios](#los-decibelios)
- [La sonoridad](#la-sonoridad)
- [La microfonía](#la-microfonía)
- [Las interfaces digitales](#las-interfaces-digitales)
- [El audio sobre red](#el-audio-sobre-red)
- [Los formatos de fichero](#los-formatos-de-fichero)
- [La mesa y la escucha](#la-mesa-y-la-escucha)
- [Dinámica y filtros](#dinámica-y-filtros)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los decibelios

- **LA IDEA MADRE** · `[of]` · **El decibelio no es una unidad absoluta: es una RELACIÓN.** **Por eso
  siempre lleva una letra detrás que dice respecto a qué.**

| Unidad | Referencia | Dónde |
|---|---|---|
| **dB** | **Ninguna: relación entre dos valores** | **Ganancias y atenuaciones** |
| **dBm** | **1 milivatio** ✔ | **Potencia** |
| **dBu** | **0,775 voltios** | **Tensión, audio profesional** |
| **dBV** | **1 voltio** | **Tensión, audio de consumo** |
| **dBFS** | **La escala digital completa** | **Digital: el máximo es 0 y el resto negativo** |
| **dBSPL** | **20 micropascales** | **Presión sonora en el aire** |

- **PREGUNTA 32** · `[exam]` · **El dBm mide potencia en relación a 1 milivatio.** **Las falsas cambian
  la referencia**: milivoltio, miliamperio, ohmio. **La «m» es de milivatio y el vatio es potencia.**
- **EL ERROR MÁS COMÚN DEL PUNTO** · `[of]` · **El dBm mide POTENCIA y el dBu mide TENSIÓN.** **No son
  convertibles sin conocer la impedancia.** **En 600 ohmios, 0 dBm y 0 dBu coinciden**, y de esa
  coincidencia histórica viene la confusión.
- **PREGUNTA 23** · `[exam]` · **Las barras de color en interfaz digital serie llevan audio a
  −18 dBFS.**

| Región | Nivel de alineación |
|---|---|
| **Europa** | **−18 dBFS** ✔ |
| **Estados Unidos** | **−20 dBFS** |

- **QUÉ ES EL NIVEL DE ALINEACIÓN** · `[of]` · **El punto de la escala digital al que corresponde el
  cero de un vúmetro analógico.** **Deja 18 decibelios de margen antes de la saturación.**
- **LA TRAMPA EVIDENTE** · `[exam]` · **«0 dBFS»**: en digital el cero es el máximo absoluto, **y una
  señal de alineación no se manda al máximo.**

## La sonoridad

- **PREGUNTA 24** · `[exam]` · **La recomendación EBU R128 trata de la normalización de la sonoridad y
  los máximos niveles.** · `[norma]`

| | **Antes: medida de pico** | **Después: medida de sonoridad** |
|---|---|---|
| **Qué se mide** | **El valor instantáneo más alto** | **Cuánto suena de verdad, integrado en el tiempo** |
| **Qué no ve** | **Cuánto suena**: mismo pico, sonoridad muy distinta | **Nada relevante** |
| **Qué produjo** | **La guerra del volumen** | **Que todos los programas suenen igual** |

| Magnitud | Valor |
|---|---|
| **Nivel objetivo del programa** | **−23 unidades referidas a escala completa** |
| **Tolerancia** | **± 0,5 unidades** |
| **Máximo de pico verdadero** | **−1 decibelio referido a escala completa** |

- **LAS FALSAS SON DE OTRO ÁMBITO** · `[exam]` · **Compresión de vídeo por satélite, protocolos de
  transporte, reducción de ruido analógica.**
- **LA CONSECUENCIA** · `[of]` · **La queja número uno del espectador es el salto de volumen entre
  programas y anuncios**, y esa recomendación existe para eliminarlo.
- **PREGUNTA 22** · `[exam]` · **El tiempo de reverberación se define como la caída de 60 dB tras
  desconectar la fuente.**
- **POR QUÉ 60** · `[of]` · **Es una reducción a la millonésima parte de la energía**: prácticamente el
  silencio, el momento en que el oído deja de percibir la cola.
- **LAS FALSAS ENGAÑAN PORQUE SIGNIFICAN ALGO** · `[exam]` · **3 decibelios es la mitad de la potencia,
  6 la mitad de la tensión y 12 no es un umbral notable.**

## La microfonía

| | **Dinámico** | **De condensador** |
|---|---|---|
| **Cómo funciona** | **Bobina en un campo magnético** | **Diafragma que cambia una capacidad** |
| **¿Alimentación?** | **No** | **Sí: fantasma de 48 voltios** ✔ |
| **Sensibilidad** | **Menor** | **Mayor** |
| **Detalle en agudos** | **Menor** | **Mayor** |
| **Presiones altas** | **Sí, muy bien** ✔ | **Peor, salvo modelos preparados** |
| **Robustez** | **Alta** | **Menor** |

- **PREGUNTA 51** · `[exam]` · **La fantasma de 48 voltios alimenta micrófonos de condensador.**
- **POR QUÉ SE LLAMA FANTASMA** · `[of]` · **Viaja por los mismos dos conductores que la señal, en modo
  común**, de modo que **un micrófono que no la necesita no la ve.**
- **EL AVISO DE OFICIO** · `[of]` · **Un micrófono de cinta antiguo SÍ puede dañarse con la fantasma**,
  sobre todo con el cable mal soldado. **Es la trampa fina de la pregunta**: no los alimenta, y además
  puede romperlos.
- **PREGUNTA 52** · `[exam]` · **Batería acústica con más de 90 decibelios: micrófonos dinámicos.**
  **Lo que decide es la PRESIÓN SONORA, no la calidad.**
- **EL MATIZ DECLARADO** · `[of]` · **En una batería real se combinan las dos familias**: **dinámicos en
  bombo y caja, condensadores en aéreos y charles**, porque los platos piden el detalle en agudos.
  **La respuesta es la correcta de las cuatro por la condición de los 90 decibelios.**
- **LAS FALSAS** · `[exam]` · **«Hipercardioides»**: es un patrón polar, no un tipo de micrófono.
  **«De condensador»**: más frágiles ante presión alta. **«Inalámbricos»**: es forma de transmisión, no
  tipo de cápsula.

| Patrón | De dónde capta | Para qué |
|---|---|---|
| **Omnidireccional** | **De todas partes** | **Ambiente, voz sin manejo** |
| **Cardioide** | **De delante, rechaza atrás** | **El de uso general** |
| **Hipercardioide** | **Más estrecho, lóbulo trasero pequeño** | **Aislar en ambiente ruidoso** |
| **Bidireccional o de ocho** | **Delante y detrás, rechaza los lados** | **Entrevista a dos, y la toma MS** |

- **PREGUNTA 91** · `[exam]` · **El sistema MS usa un cardioide y un bidireccional.**
- **CÓMO FUNCIONA** · `[of]` · **El cardioide apunta al frente —la media— y el bidireccional va
  perpendicular —el lateral—.** **Sumando y restando salen izquierdo y derecho.**
- **SU VENTAJA DECISIVA EN TELEVISIÓN** · `[of]` · **Es COMPATIBLE CON MONOFONÍA de forma perfecta**: al
  descartar el lateral queda el cardioide solo, sin cancelación. **Y la anchura del estéreo se cambia
  DESPUÉS de grabar**, subiendo o bajando el lateral.

| Técnica | Qué usa | Rasgo |
|---|---|---|
| **MS** | **Cardioide más bidireccional** ✔ | **Anchura ajustable después, compatible con monofonía** |
| **XY** | **Dos cardioides cruzados en el mismo punto** | **Buena imagen, compatible con monofonía** |
| **AB** | **Dos omnidireccionales separados** | **Mucha amplitud, problemas en monofonía** |

## Las interfaces digitales

| Interfaz | Canales | Conector y medio | Dónde |
|---|---|---|---|
| **AES/EBU (AES3)** · `[norma]` | **2** | **XLR de 110 ohmios** | **El estándar profesional de dos canales** |
| **SPDIF** | **2** | **Coaxial de 75 ohmios u óptico** | **Consumo y semiprofesional** |
| **ADAT** | **8** a 48 kHz | **Óptico** | **Grabación multipista** |
| **MADI (AES10)** · `[norma]` | **64** ✔ | **Coaxial u óptico** | **Troncales de estudio** |
| **Dante** | **Hasta 512** ✔ | **Red de datos corriente** | **Instalaciones sobre red** |

- **PREGUNTA 83** · `[exam]` · **El máximo de canales en MADI es 64.** **Es la cifra de la norma a la
  frecuencia de muestreo básica**: **a frecuencias dobles baja a la mitad.**
- **PREGUNTA 35, NEGATIVA** · `[exam]` · **La que NO sirve para sincronización es AES10**, porque **es
  MADI: transporte, no referencia.** **AES11, negro de barras y reloj de palabra sí lo son.**
- **LA REGLA** · `[of]` · **Tres opciones llevan sólo tiempo y una lleva audio.** **La que lleva audio
  es la intrusa.**

## El audio sobre red

- **PREGUNTA 10** · `[exam]` · **Un sistema Dante admite 512 canales bidireccionales a 24 bits y
  48 kHz.**
- **PREGUNTA 64, NEGATIVA** · `[exam]` · **Lo que NO es propio de ese protocolo es transmitir audio
  COMPRIMIDO.**

| Característica | ¿La tiene? |
|---|---|
| **Compatible con muchos dispositivos** | **Sí** |
| **Varios canales por un par trenzado** | **Sí** |
| **Audio comprimido de alta calidad** | **No: va sin comprimir** ✔ |
| **Latencia muy baja** | **Sí** |

- **LA RAZÓN DE SER** · `[of]` · **Calidad íntegra y latencia muy baja sobre red corriente.**
  **Comprimir añadiría retardo**, que es lo que no puede permitirse.
- **EL MATIZ DE LA CIFRA** · `[of]` · **512 es la del equipo de mayor capacidad de la familia**; **en la
  práctica el límite lo pone el equipo concreto y el ancho de banda del enlace**, no el protocolo.
- **LA RELACIÓN CON EL VÍDEO SOBRE RED** · `[of]` · **Este sistema es propietario y resuelve el audio**;
  **la familia de normas de vídeo sobre red resuelve vídeo, audio y datos con normas abiertas.** **Los
  dos conviven hoy.**

## Los formatos de fichero

| Formato | Compresión | Quién lo hizo |
|---|---|---|
| **WAV** | **Ninguna** ✔ | **Microsoft e IBM** |
| **AIFF** | **Ninguna** ✔ | **Apple** |
| **FLAC** y **ALAC** | **Sin pérdida** | **Libre y Apple** |
| **MP3** y **AAC** | **Con pérdida** | **El grupo de expertos en imágenes en movimiento** |

- **PREGUNTA 65** · `[exam]` · **WAV es un formato sin compresión.**
- **PREGUNTA 77** · `[exam]` · **AIFF es un formato sin compresión desarrollado por Apple.**
- **EL MATIZ QUE NINGUNA CUBRE** · `[of]` · **Los dos son CONTENEDORES que normalmente llevan modulación
  por impulsos codificados sin comprimir**, y **ninguno PROHÍBE llevar datos comprimidos dentro.** **Lo
  corriente es que no lo lleven**, y las respuestas describen ese uso corriente.
- **PREGUNTA 48** · `[exam]` · **NICAM 728 es un sistema de sonido digital**: **el que llevó el estéreo
  digital a la televisión analógica.** **728 es el caudal en kilobits por segundo.** **La palabra que
  decide es «sonido»**: las falsas son transmisión de vídeo, codificación de vídeo y reducción de ruido.
- **PREGUNTA 72** · `[exam]` · **MIDI es un protocolo para instrumentos musicales electrónicos.**
- **LO QUE HAY QUE TENER CLARO ES LO QUE NO ES** · `[of]` · **No transporta audio: transporta ÓRDENES**
  —qué nota, con qué fuerza, cuánto dura—, **y el sonido lo produce el instrumento que las recibe.**
  **Un fichero así ocupa unos kilobytes y suena distinto en cada aparato.**

## La mesa y la escucha

- **PREGUNTA 76** · `[exam]` · **El DIM atenúa el volumen de los monitores de control en una cantidad
  preestablecida.**
- **PARA QUÉ SIRVE DE VERDAD** · `[of]` · **Para hablar con alguien sin perder la referencia de
  escucha**: **baja una cantidad FIJA y conocida** —doce o veinte decibelios—, **y al soltarlo se vuelve
  exactamente al nivel de antes.** **Bajar el mando y volver a subirlo no garantiza eso.**

| Mando | Qué hace |
|---|---|
| **DIM** | **Atenúa la escucha una cantidad fija** ✔ |
| **Ganancia de entrada** | **Ajusta el nivel del previo, en el canal** |
| **Solo** | **Escucha únicamente el canal seleccionado** |
| **Mute** | **Silencia por completo** |

- **PREGUNTA 58** · `[exam]` · **Los monitores de campo cercano dan un sonido más preciso a corta
  distancia.**
- **LA RAZÓN FÍSICA** · `[of]` · **En campo cercano el sonido directo domina sobre el reflejado**: **se
  oye el altavoz y no la sala**, y por eso **una continuidad puede tener escucha fiable en una sala
  acústicamente mediocre.**
- **LAS FALSAS** · `[exam]` · **Hablan de tamaño, distancia y amplificación**: **hay monitores de campo
  cercano grandes y hay pasivos.** **Lo que los define es la distancia de escucha.**

## Dinámica y filtros

- **PREGUNTA 88** · `[exam]` · **Para actuar sobre una banda estrecha hay que usar un factor de calidad
  ALTO.**
- **QUÉ ES ESE FACTOR** · `[of]` · **La frecuencia central dividida entre el ancho de banda.** **Factor
  y ancho de banda son INVERSOS: si uno sube, el otro baja.**

| Factor | Ancho de banda | Para qué |
|---|---|---|
| **Alto** | **Estrecho** ✔ | **Quitar un zumbido o un acople sin tocar lo demás** |
| **Bajo** | **Ancho** | **Dar carácter, corregir una zona entera con suavidad** |

| Circuito | Qué hace | Cuándo actúa |
|---|---|---|
| **Compresor** | **Reduce la diferencia entre lo fuerte y lo flojo** | **Por encima del umbral** |
| **Limitador** | **Compresor de relación muy alta**: impide pasar del umbral | **Por encima del umbral** |
| **Puerta de ruido** | **Silencia lo que queda por debajo** | **Por debajo del umbral** |
| **Expansor** | **Aumenta la diferencia** | **Por debajo del umbral** |

- **LA REGLA EN UNA LÍNEA** · `[of]` · **Compresor y limitador miran hacia arriba; puerta y expansor,
  hacia abajo.**
- **LOS CUATRO PARÁMETROS COMUNES** · `[of]` · **Umbral, relación, tiempo de ataque y tiempo de
  relajación.** **Los dos tiempos deciden si el proceso se oye o no.**
- **PREGUNTA 39** · `[exam]` · **La microfonía inalámbrica digital usa QPSK**: **dos bits por símbolo y
  extraordinariamente robusta**, que es lo que un enlace de micrófono necesita.
- **LA REGLA QUE LO EXPLICA** · `[of]` · **Cuantos más bits por símbolo, más caudal y menos robustez.**
  **Un micrófono elige robustez; una televisión digital terrestre, caudal.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 10 | Canales bidireccionales del sistema de audio sobre red | **512** ✔ |
| 22 | En cuántos decibelios se define el tiempo de reverberación | **60 dB** ✔ |
| 23 | Nivel del audio de unas barras de color | **−18 dBFS** ✔ |
| 24 | Sobre qué recomienda la EBU R128 | **Sonoridad y máximos niveles** ✔ |
| 32 | Qué es el dBm | **Potencia respecto a 1 milivatio** ✔ |
| 39 | Modulación de la microfonía inalámbrica digital | **QPSK** ✔ |
| 48 | Qué es NICAM 728 | **Un sistema de sonido digital** ✔ |
| 51 | Para qué la fantasma de 48 voltios | **Micrófonos de condensador** ✔ |
| 52 | Qué micrófonos para una batería de más de 90 dB | **Dinámicos** ✔ **·** con matiz |
| 58 | Característica de los monitores de campo cercano | **Más precisos a corta distancia** ✔ |
| 64 | Cuál NO es propia de ese protocolo de audio | **Transmitir audio comprimido** ✔ |
| 65 | Qué es el formato WAV | **Audio sin compresión** ✔ |
| 72 | Qué es MIDI | **Protocolo para instrumentos musicales** ✔ |
| 76 | Qué es el DIM en una mesa | **Atenúa la escucha una cantidad fija** ✔ |
| 77 | Qué es el formato AIFF | **Sin compresión, de Apple** ✔ |
| 83 | Máximo de canales en MADI | **64** ✔ |
| 88 | Qué usar para una banda estrecha | **Factor de calidad alto** ✔ |
| 91 | Patrones del sistema MS | **Cardioide y bidireccional** ✔ |

- **LAS TRES CIFRAS QUE HAY QUE MEMORIZAR SÍ O SÍ** · `[of]` · **60, −18 y 64.**
