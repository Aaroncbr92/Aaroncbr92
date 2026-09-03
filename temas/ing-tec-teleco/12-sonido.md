# Tema 12 del específico de Ingeniería Técnica · Telecomunicación · Sonido

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 16 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son las normas de audio digital y la recomendación de sonoridad, **tras muro de pago**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Banco más grande** | **Dieciocho preguntas, empatado con el de redes.** Entre los dos se llevan **36 de las 85 del específico: el 42 % del examen** |
| **Extensión** | **4.368 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el decibelio (**dB**) y sus referencias —el
milivatio (**dBm**), la tensión de 0,775 voltios (**dBu**) y la escala digital (**dBFS**)—; la
Sociedad de Ingeniería de Audio (**AES**) y la Unión Europea de Radiodifusión (**UER**, en inglés
**EBU**), que publican juntas el formato **AES/EBU** y la recomendación **EBU R128**; la interfaz
digital de audio multicanal (**MADI**); la interfaz digital de Sony y Philips (**SPDIF**); la cinta
digital de ocho pistas de Alesis (**ADAT**); la interfaz digital de instrumentos musicales
(**MIDI**); la modulación por impulsos codificados (**PCM**); la modulación por desplazamiento de
fase en cuadratura (**QPSK**) y la de amplitud en cuadratura (**QAM**); el par trenzado sin
apantallar (**UTP**); el kilohercio (**kHz**); la unidad de sonoridad referida a escala completa
(**LUFS**); los formatos de fichero de audio, nombrados por su extensión (**WAV**, **AIFF**,
**FLAC**, **ALAC**, **MP3** y **AAC**); las dos casas que crearon los dos primeros —Microsoft y la
Máquinas de Negocio Internacionales (**IBM**)—; las tres técnicas de toma estéreo, que se nombran por
las letras de sus micrófonos (la de media y lateral, **MS**; la de dos cardioides cruzados, **XY**; y
la de dos micrófonos separados, **AB**); el atenuador de escucha de una mesa (**DIM**, de
*dimmer*); y **Dante**, **NICAM** y **Dolby**, que son nombres de sistema y no siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 16):
> «Sonido: Audio analógico y digital. Medida y control de la señal de audio. Niveles, dB, dBm, dBu y
> dBFS. Equipos de medida. Interfaces estándares en audio digital. Formatos AES/EBU, SPDIF y ADAT.
> Audio insertado en la señal de vídeo. Estándares de codificación y compresión. Microfonía.
> Mezcladores analógicos y digitales. Ecualizadores. Filtros. Circuitos de control de dinámica:
> limitadores, compresores, puertas de ruido, generadores de efectos. Procesadores de audio. Formatos
> analógicos y digitales de grabación y reproducción. Equipamiento auxiliar.»

**Dieciocho preguntas: el banco más grande de la ocupación, empatado con el de redes.** **Entre los
dos se llevan 36 de las 85 del específico: el 42 % del examen.**

**Su reparto**: **cuatro son de niveles y medida**, **tres de audio sobre red**, **tres de formatos de
fichero**, **tres de microfonía**, **dos de mesa y monitores**, **dos de interfaces** y **una de
protocolo de instrumentos.**

<!-- indice -->

## Índice

- [1. Los decibelios y sus referencias](#1-los-decibelios-y-sus-referencias)
- [2. La medida de la sonoridad](#2-la-medida-de-la-sonoridad)
- [3. La microfonía](#3-la-microfonía)
- [4. Las interfaces digitales](#4-las-interfaces-digitales)
- [5. El audio sobre red](#5-el-audio-sobre-red)
- [6. Los formatos de fichero](#6-los-formatos-de-fichero)
- [7. La mesa y la escucha](#7-la-mesa-y-la-escucha)
- [8. El control de dinámica y los filtros](#8-el-control-de-dinámica-y-los-filtros)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. Los decibelios y sus referencias

**El decibelio no es una unidad absoluta: es una relación.** **Por eso siempre lleva una letra detrás
que dice respecto a qué**, y **ésa es la tabla que el enunciado pide expresamente:**

| Unidad | Referencia | Dónde se usa |
|---|---|---|
| **dB** | **Ninguna: es una relación entre dos valores** | **Diferencias, ganancias, atenuaciones** |
| **dBm** | **1 milivatio** ✔ | **Potencia, en radiofrecuencia y en líneas** |
| **dBu** | **0,775 voltios** | **Tensión, en audio profesional** |
| **dBV** | **1 voltio** | **Tensión, en audio de consumo** |
| **dBFS** | **La escala digital completa** | **Audio digital: el máximo es 0 y todo lo demás es negativo** |
| **dBSPL** | **20 micropascales** | **Presión sonora en el aire** |

**La pregunta 32**: **el dBm es una medida de potencia eléctrica en relación a 1 milivatio.** Ésa es la
respuesta oficial.

---

**Y las tres opciones falsas cambian la referencia por otra magnitud**: **milivoltio, miliamperio y
ohmio.** **La regla que la contesta es que la «m» es de milivatio y el vatio es potencia**, que es
justo lo que el enunciado pregunta.

**El aviso que evita el error más común de todo el punto**: **el dBm mide POTENCIA y el dBu mide
TENSIÓN.** **Se parecen en la escritura y no son convertibles sin conocer la impedancia.** **En una
línea de 600 ohmios, 0 dBm y 0 dBu coinciden**, y de esa coincidencia histórica viene la confusión.

**La pregunta 23**: **unas barras de color en interfaz digital serie envían audio normalizado a un
nivel de −18 dBFS.** Ésa es la respuesta oficial.

---

**Y ése es el valor de alineación europeo**, que conviene aprender junto a su pareja:

| Región | Nivel de alineación |
|---|---|
| **Europa** | **−18 dBFS** ✔ |
| **Estados Unidos** | **−20 dBFS** |

**Qué significa «nivel de alineación», que es lo que hace útil el dato**: **el punto de la escala
digital al que corresponde el cero de un vúmetro analógico.** **Deja 18 decibelios de margen por
encima antes de la saturación**, y ese margen es lo que impide que un pico inesperado recorte.

**La opción «0 dBFS» es la trampa evidente**: **en digital, el cero es el máximo absoluto** y **una
señal de alineación no se manda al máximo**, porque no dejaría margen ninguno.

## 2. La medida de la sonoridad

**La pregunta 24**: **la recomendación EBU R128 recomienda sobre la normalización de la sonoridad y
los máximos niveles de audio.** Ésa es la respuesta oficial.

---

**Y es el cambio de mentalidad más importante del audio de televisión de las últimas dos décadas**,
así que conviene entenderlo y no memorizarlo:

| | **Antes: medida de pico** | **Después: medida de sonoridad** |
|---|---|---|
| **Qué se mide** | **El valor instantáneo más alto** | **Cuánto suena de verdad, integrado en el tiempo** |
| **Qué no ve** | **Cuánto suena**: dos programas con el mismo pico pueden sonar muy distinto | **Nada relevante** |
| **Qué produjo** | **La guerra del volumen**: comprimir hasta el límite para sonar más alto | **Que todos los programas suenen igual de alto** |

**Las tres cifras que la recomendación fija y que el examen puede pedir:**

| Magnitud | Valor |
|---|---|
| **Nivel objetivo de sonoridad del programa** | **−23 unidades referidas a escala completa** |
| **Tolerancia** | **± 0,5 unidades** |
| **Máximo de pico verdadero** | **−1 decibelio referido a escala completa** |

**Y las tres opciones falsas de la pregunta nombran tres cosas reales de otro ámbito**: **compresión
de vídeo por satélite, protocolos de transporte y reducción de ruido analógica.** **Ninguna es de
sonoridad.**

**La consecuencia práctica que este epígrafe deja**: **la queja número uno del espectador es el salto
de volumen entre programas y anuncios**, y **esa recomendación existe precisamente para eliminarlo.**

**La pregunta 22**: **el tiempo de reverberación se define como el tiempo de caída de una señal de
audio, cuando se desconecta de la fuente, en 60 dB.** Ésa es la respuesta oficial.

---

**Es una definición y hay que saberla exactamente**: **60 decibelios, no 3, ni 6, ni 12.** **De ahí
que se escriba con ese número al lado del símbolo del tiempo de reverberación.**

**Por qué 60 y no otra cifra**: **porque una caída de 60 decibelios es una reducción a la millonésima
parte de la energía**, y **eso equivale prácticamente al silencio**: es el momento en que el oído deja
de percibir la cola.

**Y las tres opciones falsas son cifras que sí significan algo en audio, y por eso engañan**: **3
decibelios es la mitad de la potencia, 6 es la mitad de la tensión y 12 no es un umbral notable.**

## 3. La microfonía

**Las dos familias que el examen distingue, y de las que sale una pregunta entera:**

| | **Dinámico** | **De condensador** |
|---|---|---|
| **Cómo funciona** | **Una bobina se mueve en un campo magnético** | **Un diafragma cambia la capacidad de un condensador** |
| **¿Necesita alimentación?** | **No** | **Sí: la fantasma de 48 voltios** ✔ |
| **Sensibilidad** | **Menor** | **Mayor** |
| **Detalle en agudos** | **Menor** | **Mayor** |
| **Aguanta presiones altas** | **Sí, muy bien** ✔ | **Peor, salvo modelos preparados** |
| **Robustez** | **Alta** | **Menor** |

**La pregunta 51**: **la alimentación fantasma de 48 voltios se usa para alimentar micrófonos de
condensador.** Ésa es la respuesta oficial.

---

**Por qué se llama fantasma**: **porque viaja por los mismos dos conductores que llevan la señal**,
en modo común, **de manera que un micrófono que no la necesita no la ve.** **Un dinámico conectado a
una entrada con fantasma no sufre**, y ésa es toda la gracia del invento.

**El aviso de oficio que sí importa**: **un micrófono de cinta antiguo SÍ puede dañarse con la
fantasma**, sobre todo si el cable está mal soldado. **La opción a de la pregunta nombra precisamente
los de cinta**, y es la trampa fina: **no los alimenta, y además puede romperlos.**

**La pregunta 52 plantea un caso**: **sonorizar una batería acústica en un concierto, con más de 90
decibelios que captar.** **La respuesta oficial es micrófonos dinámicos.**

---

**Y se razona con la tabla de arriba**: **lo que decide es la presión sonora, no la calidad.** **Un
bombo produce picos que saturan la cápsula de muchos condensadores**, mientras que **un dinámico los
aguanta sin inmutarse.**

**Las tres opciones falsas y por qué caen:**

| Opción | Por qué no |
|---|---|
| **Hipercardioides** | **Es un patrón polar, no un tipo de micrófono.** Responde a otra pregunta: a cuánto rechazo lateral, no a cuánta presión |
| **De condensador** | **Más sensibles y más frágiles ante presión alta** |
| **Inalámbricos** | **Es una forma de transmisión, no un tipo de cápsula** |

**El aviso que conviene añadir, porque el enunciado del punto pide microfonía entera**: **la respuesta
oficial simplifica.** **En una batería real se combinan las dos familias**: **dinámicos en bombo y
caja, y condensadores en aéreos y charles**, porque los platos piden el detalle en agudos que el
dinámico no da. **La respuesta es la correcta de las cuatro por la condición de los 90 decibelios**,
y el temario lo sostiene con ese matiz.

**Los patrones polares, que el examen puede pedir y que la opción falsa nombra:**

| Patrón | De dónde capta | Para qué |
|---|---|---|
| **Omnidireccional** | **De todas partes** | **Ambiente, voz sin manejo** |
| **Cardioide** | **De delante, rechaza atrás** | **El de uso general** |
| **Hipercardioide** | **Más estrecho, con un lóbulo trasero pequeño** | **Aislar una fuente en ambiente ruidoso** |
| **Bidireccional o de ocho** | **De delante y de detrás, rechaza los lados** | **Entrevista a dos, y la técnica del epígrafe siguiente** |

**La pregunta 91**: **el sistema de grabación estéreo llamado MS utiliza dos fuentes con un patrón
cardioide y otro bidireccional.** Ésa es la respuesta oficial.

---

**Qué es y por qué se usa en televisión**: **un micrófono cardioide apunta al frente —la señal
media— y uno bidireccional se coloca perpendicular —la señal lateral—.** **Sumando y restando las dos
se obtienen el canal izquierdo y el derecho.**

**Su ventaja decisiva, que es la razón de que esté en un temario de televisión**: **es
COMPATIBLE CON MONOFONÍA de forma perfecta.** **Si se descarta el lateral queda el cardioide solo, sin
ninguna cancelación.** **Y además la anchura del estéreo se puede cambiar DESPUÉS de grabar**,
subiendo o bajando el lateral.

**Las tres técnicas estéreo que conviene tener vistas:**

| Técnica | Qué usa | Rasgo |
|---|---|---|
| **MS** | **Cardioide más bidireccional** ✔ | **Anchura ajustable después, compatible con monofonía** |
| **XY** | **Dos cardioides cruzados en el mismo punto** | **Buena imagen, compatible con monofonía** |
| **AB** | **Dos omnidireccionales separados** | **Mucha amplitud, problemas en monofonía** |

## 4. Las interfaces digitales

**El cuadro que el enunciado pide expresamente, con los tres formatos que nombra y los dos que el
examen añade:**

| Interfaz | Canales | Conector y medio | Dónde se usa |
|---|---|---|---|
| **AES/EBU (AES3)** | **2** | **XLR de 110 ohmios** | **El estándar profesional de dos canales** |
| **SPDIF** | **2** | **Coaxial de 75 ohmios u óptico** | **Consumo y semiprofesional** |
| **ADAT** | **8** a 48 kHz | **Óptico** | **Grabación multipista** |
| **MADI (AES10)** | **64** ✔ | **Coaxial u óptico** | **Troncales de estudio** |
| **Dante** | **Hasta 512** ✔ | **Red de datos corriente** | **Instalaciones sobre red** |

**La pregunta 83**: **el número máximo de canales de audio digital en un sistema MADI es 64.** Ésa es
la respuesta oficial.

---

**Es memoria de una cifra**, y **el apoyo está en que 64 es la cifra de la norma a la frecuencia de
muestreo básica.** **A frecuencias dobles el número baja a la mitad**, y ése es el matiz que un
ingeniero debe saber aunque la pregunta no lo pida.

**La pregunta 35 es negativa**: **de las señales enumeradas, la que NO se utiliza para sincronización
es AES10.** Ésa es la respuesta oficial.

---

**Y ahí está la razón de que este tema y el de la señal audiovisual se estudien juntos**: **AES10 es
MADI, que es transporte de audio**, mientras que **las otras tres —AES11, negro de barras y reloj de
palabra— son señales de referencia.**

| Señal | Qué es |
|---|---|
| **AES11** | **La referencia de sincronismo digital de audio** |
| **Negro de barras** | **La referencia de vídeo analógica de toda la instalación** |
| **Reloj de palabra** | **El pulso que marca cada muestra de audio** |
| **AES10** | **MADI: transporte de 64 canales, no referencia** ✔ |

**La regla que la contesta sin memorizar los cuatro números**: **tres de las cuatro opciones sólo
llevan tiempo y una lleva audio.** **La que lleva audio es la intrusa.**

## 5. El audio sobre red

**Dos preguntas del punto son del mismo sistema**, y **conviene contestarlas con el mismo cuadro:**

**La pregunta 10**: **un sistema Dante admite 512 canales bidireccionales a 24 bits y 48 kHz.** Ésa es
la respuesta oficial.

**La pregunta 64 es negativa**: **de las características enumeradas, la que NO es propia de ese
protocolo es transmitir señales de audio comprimidas de alta calidad.** Ésa es la respuesta oficial.

---

**Y la segunda es la importante, porque explica el sistema entero**: **ese protocolo transmite audio
SIN COMPRIMIR.** **Ésa es precisamente su razón de ser**: **calidad íntegra y latencia muy baja sobre
una red de datos corriente.** **Comprimir añadiría retardo, que es lo que no puede permitirse.**

| Característica | ¿La tiene? |
|---|---|
| **Compatible con gran número de dispositivos** | **Sí** |
| **Varios canales por un cable de par trenzado** | **Sí** |
| **Audio comprimido de alta calidad** | **No: va sin comprimir** ✔ |
| **Latencia muy baja** | **Sí** |

**La cifra de 512 canales de la pregunta 10 corresponde al equipo de mayor capacidad de la familia**,
y **conviene decir que en la práctica el límite lo pone el equipo concreto y el ancho de banda del
enlace**, no el protocolo. **La respuesta oficial es la mayor de las cuatro cifras ofrecidas**, y
todas son potencias de dos.

**Y la relación con el tema 7, que es lo que ordena la ocupación**: **este sistema es propietario y
resuelve el audio**; **la familia de normas de vídeo sobre red del punto 8 resuelve vídeo, audio y
datos con normas abiertas**, y **su parte de audio se apoya en la norma de interoperabilidad de la
Sociedad de Ingeniería de Audio.** **Los dos conviven en las instalaciones de hoy.**

## 6. Los formatos de fichero

**Tres preguntas del punto son de aquí, y las tres se contestan con una tabla de dos columnas:**

| Formato | Compresión | Quién lo hizo |
|---|---|---|
| **WAV** | **Ninguna** ✔ | **Microsoft e IBM** |
| **AIFF** | **Ninguna** ✔ | **Apple** |
| **FLAC** y **ALAC** | **Sin pérdida** | **Libre y Apple** |
| **MP3** y **AAC** | **Con pérdida** | **El grupo de expertos en imágenes en movimiento** |

**La pregunta 65**: **el formato WAV es un formato de audio sin compresión.** Ésa es la respuesta
oficial.

**La pregunta 77**: **el formato AIFF es un formato de audio sin compresión desarrollado por Apple.**
Ésa es la respuesta oficial.

---

**Son la misma pregunta con el formato cambiado**, y **las dos tienen las mismas opciones falsas**:
con pérdida, sin pérdida y transmisión. **La distinción de las tres familias es la que hay que llevar,
y es la misma del tema 18 del específico de Técnica Informática.**

**El matiz que conviene añadir y que ninguna de las dos preguntas cubre**: **los dos formatos son
contenedores que normalmente llevan modulación por impulsos codificados sin comprimir**, pero
**ninguno de los dos PROHÍBE llevar datos comprimidos dentro.** **Lo corriente es que no lo lleven**,
y las respuestas oficiales describen ese uso corriente.

**La pregunta 48**: **NICAM 728 es un sistema de sonido digital.** Ésa es la respuesta oficial.

---

**Qué fue, para situarlo**: **el sistema que llevó el sonido estéreo digital a la televisión
analógica.** **Su nombre dice lo que hace**: multiplexado de casi instantánea compansión, y **728
es el caudal en kilobits por segundo.**

**Las tres opciones falsas son las tres categorías vecinas** —transmisión de vídeo, codificación de
vídeo y reducción de ruido—, **y la palabra que decide es «sonido».**

**La pregunta 72**: **el estándar MIDI es un protocolo de comunicación para instrumentos musicales
electrónicos.** Ésa es la respuesta oficial.

---

**Y el dato que hay que tener claro es lo que NO es**: **no transporta audio.** **Transporta órdenes**
—qué nota, con qué fuerza, cuánto dura—, **y el sonido lo produce el instrumento que las recibe.**
**Un fichero de ese tipo ocupa unos pocos kilobytes y suena distinto en cada aparato**, que es
exactamente lo contrario de un fichero de audio.

## 7. La mesa y la escucha

**La pregunta 76**: **el DIM en una mesa de sonido atenúa el volumen de los monitores de la sala de
control en una cantidad preestablecida.** Ésa es la respuesta oficial.

---

**Para qué sirve, que es lo que lo hace memorizable**: **para hablar con alguien sin perder la
referencia de escucha.** **Baja la escucha una cantidad fija y conocida** —doce o veinte decibelios
según la mesa—, **de modo que al soltarlo se vuelve exactamente al mismo nivel de antes.** **Bajar el
mando y volver a subirlo no garantiza eso.**

**Los cuatro mandos de la sección de escucha que las opciones mezclan:**

| Mando | Qué hace |
|---|---|
| **DIM** | **Atenúa la escucha una cantidad fija** ✔ |
| **Ganancia de entrada** | **Ajusta el nivel del previo, en el canal** |
| **Solo** | **Escucha únicamente el canal seleccionado** |
| **Mute** | **Silencia por completo** |

**La pregunta 58**: **la principal característica de los monitores de campo cercano frente a los de
campo lejano es que proporcionan un sonido más preciso a corta distancia.** Ésa es la respuesta
oficial.

---

**Y la razón física, que es lo que hay que entender**: **en campo cercano el sonido directo domina
sobre el reflejado.** **Eso significa que lo que se oye es el altavoz y no la sala**, y **por eso una
mesa de continuidad puede tener una escucha fiable en una sala acústicamente mediocre.**

**Las tres opciones falsas son afirmaciones sobre tamaño, distancia y amplificación**, y **ninguna es
la característica principal**: **hay monitores de campo cercano grandes y hay pasivos.** **Lo que los
define es la distancia de escucha, no su construcción.**

## 8. El control de dinámica y los filtros

**La pregunta 88**: **para actuar sobre una banda estrecha de frecuencias hay que usar un factor de
calidad alto.** Ésa es la respuesta oficial.

---

**Qué es el factor de calidad de un filtro**: **la frecuencia central dividida entre el ancho de
banda.** **De esa división sale la regla entera:**

| Factor de calidad | Ancho de banda | Para qué se usa |
|---|---|---|
| **Alto** | **Estrecho** ✔ | **Quitar un zumbido o un acople sin tocar lo demás** |
| **Bajo** | **Ancho** | **Dar carácter, corregir una zona entera con suavidad** |

**El apoyo que fija la respuesta**: **el factor de calidad y el ancho de banda son inversos.** **Si
uno sube, el otro baja**, exactamente igual que el número f y la apertura del diafragma.

**Los cuatro circuitos de control de dinámica que el enunciado nombra, porque son lo preguntable de lo
que no ha caído:**

| Circuito | Qué hace | Cuándo actúa |
|---|---|---|
| **Compresor** | **Reduce la diferencia entre lo fuerte y lo flojo**, con una relación | **Por encima del umbral** |
| **Limitador** | **Un compresor de relación muy alta**: impide pasar del umbral | **Por encima del umbral** |
| **Puerta de ruido** | **Silencia lo que está por debajo del umbral** | **Por debajo del umbral** |
| **Expansor** | **Aumenta la diferencia entre lo fuerte y lo flojo** | **Por debajo del umbral** |

**La regla que los ordena en una línea**: **compresor y limitador miran hacia arriba; puerta y
expansor, hacia abajo.**

**Y los cuatro parámetros que todos comparten**: **umbral, relación, tiempo de ataque y tiempo de
relajación.** **Los dos tiempos son los que deciden si el proceso se oye o no se oye.**

**La pregunta 39**: **la microfonía inalámbrica digital utiliza el modo de transmisión QPSK.** Ésa es
la respuesta oficial.

---

**Y las tres opciones falsas son tres modulaciones reales**, así que la pregunta exige saber cuál:
**la modulación por desplazamiento de fase en cuadratura lleva dos bits por símbolo y es
extraordinariamente robusta**, que es lo que un enlace de micrófono necesita: **prefiere aguantar sin
cortarse a llevar mucho caudal.**

**La regla que lo explica y que vale para todo el tema 5**: **cuantos más bits por símbolo, más caudal
y menos robustez.** **Un micrófono elige robustez; una televisión digital terrestre, caudal.**

## 9. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 10 | Canales bidireccionales de un sistema de audio sobre red | d) 512 ✔ |
| 22 | En cuántos decibelios se define el tiempo de reverberación | d) 60 dB ✔ |
| 23 | Nivel del audio normalizado de unas barras de color | d) −18 dBFS ✔ |
| 24 | Sobre qué recomienda la EBU R128 | c) Normalización de la sonoridad y máximos niveles ✔ |
| 32 | Qué es el dBm | a) Potencia en relación a 1 milivatio ✔ |
| 39 | Modo de transmisión de la microfonía inalámbrica digital | c) QPSK ✔ |
| 48 | Qué es NICAM 728 | d) Un sistema de sonido digital ✔ |
| 51 | Para qué se usa la alimentación fantasma de 48 voltios | b) Micrófonos de condensador ✔ |
| 52 | Qué micrófonos para una batería de más de 90 dB | c) Dinámicos ✔ **·** con matiz |
| 58 | Característica de los monitores de campo cercano | a) Sonido más preciso a corta distancia ✔ |
| 64 | Cuál NO es característica de ese protocolo de audio | c) Transmite audio comprimido ✔ |
| 65 | Qué es el formato WAV | c) Audio sin compresión ✔ |
| 72 | Qué es el estándar MIDI | b) Protocolo para instrumentos musicales electrónicos ✔ |
| 76 | Qué es el DIM en una mesa | b) Atenúa la escucha una cantidad preestablecida ✔ |
| 77 | Qué es el formato AIFF | b) Audio sin compresión desarrollado por Apple ✔ |
| 83 | Máximo de canales en MADI | a) 64 ✔ |
| 88 | Qué usar para una banda estrecha de frecuencias | d) Factor de calidad alto ✔ |
| 91 | Patrones del sistema MS | a) Cardioide y bidireccional ✔ |

**Las dieciocho respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **Una
lleva matiz declarado**: la 52, cuya respuesta simplifica lo que se hace en una batería real.

**El aviso de estudio**: **la tabla de referencias del decibelio y la de interfaces digitales
contestan cinco preguntas.** **Y las tres cifras que hay que memorizar sí o sí son 60, −18 y 64.**

## 10. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **Las normas AES3, AES10, AES11 y la recomendación EBU R128 no se han consultado**: su texto está
   tras un muro de pago. **Lo que el tema afirma de cada una es de uso universal en el sector**, y
   **coincide con las respuestas oficiales.** **Las tres cifras de la recomendación de sonoridad
   —−23, ±0,5 y −1— se dan como conocimiento común**, y **ninguna respuesta oficial depende de
   ellas**: la pregunta 24 sólo pide sobre qué recomienda.
2. **Dante es un sistema propietario y su documentación no se ha consultado.** **El temario afirma de
   él lo que las dos respuestas oficiales afirman** —que llega a 512 canales y que no comprime—, y
   **añade que en la práctica el límite lo pone el equipo concreto**, que es observación de oficio.
3. **La definición del tiempo de reverberación, los patrones polares, las técnicas estéreo y los
   circuitos de control de dinámica son teoría clásica de acústica y de audio**, presentadas como
   conocimiento común.
4. **El matiz de la pregunta 52 es del temario, no una impugnación**: **la respuesta oficial es la
   correcta de las cuatro por la condición de los 90 decibelios**, y **el temario señala que en una
   batería real se combinan las dos familias.**
5. **NICAM y MIDI son nombres de sistema**, citados por lo que la respuesta oficial dice de ellos.
   **Sus especificaciones no se han consultado**, y **el caudal de 728 kilobits por segundo se da como
   dato de uso corriente.**

**El resto del tema va como oficio y así se declara**: el aviso de que el dBm y el dBu no son
convertibles sin impedancia, la explicación del nivel de alineación, la razón de que la caída sean 60
decibelios, la explicación de por qué la alimentación se llama fantasma y el aviso sobre los
micrófonos de cinta, la ventaja de compatibilidad con monofonía del sistema MS, la razón de que el
audio sobre red no comprima, la explicación del uso del DIM, la razón física del campo cercano y la
regla inversa entre factor de calidad y ancho de banda. **Nada de eso está en un boletín oficial ni en
una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
