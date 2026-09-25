# Tema 9 del específico de Operador/a de Sonido · Grabación, edición y postproducción

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 9 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Recomendaciones técnicas: EBU R 128 s1 (sonoridad de las piezas cortas: anuncios, promociones), EBU Tech 3343 (producción conforme a la R 128), EBU Tech 3285 (formato BWF); documento técnico AES TD1008 (sonoridad en internet). Documentación de fabricante: iZotope, manual de RX 11 (reducción de ruido); Avid, *Pro Tools Reference Guide* 2025.12 (tipos de pista, *dither* y conversión de frecuencia de muestreo). Manual universitario: J. O. Smith (Stanford), teorema del muestreo. Lo demás, oficio y cálculo |
| **Redacción que se estudia** | La vigente el 24/09/2026: EBU R 128 s1 V3 (agosto de 2020), EBU Tech 3343-2023 (noviembre de 2023), EBU Tech 3285 versión 2.0 (mayo de 2011), AES TD1008.1.21-9 (septiembre de 2021); de fabricante, *Pro Tools Reference Guide* versión 2025.12 |
| **Extensión** | 11.600 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de
Radiodifusión (**UER**, en inglés **EBU**, *European Broadcasting Union*), que publica sus
recomendaciones (**R**) y sus documentos técnicos (**Tech**); Sociedad de Ingeniería de Audio
(**AES**, *Audio Engineering Society*) y sus documentos técnicos (**TD**, *technical document*);
Sociedad de Ingenieros de Cine y Televisión (**SMPTE**, *Society of Motion Picture and Television
Engineers*); la estación de trabajo de audio digital (**DAW**, *digital audio workstation*); el
tamaño de la memoria intermedia de la interfaz, medido en muestras (*buffer*); la modulación por
impulsos codificados (**PCM**, *pulse code modulation*); el formato de fichero de onda (**WAV**) y
su versión para radiodifusión (**BWF**, *broadcast wave format*); el identificador único de
material (**UMID**, *unique material identifier*); el códec libre de compresión sin pérdida
(**FLAC**, *free lossless audio codec*); la codificación avanzada de audio (**AAC**, *advanced
audio coding*); el códec **Opus**; el sistema de codificación **AC-3** de Dolby; el formato
**MP3**; el bit y el byte (**b** y **B**) y el megabyte (**MB**, un millón de bytes); los
fotogramas o cuadros por segundo (**fps**); el decibelio a escala completa (**dBFS**) y el de pico
verdadero (**dBTP**, *decibels true peak*); la unidad de sonoridad referida a la escala completa
(**LUFS**, *loudness units relative to full scale*) y la unidad de diferencia de sonoridad (**LU**,
*loudness unit*); el rango de sonoridad (**LRA**, *loudness range*); el código de tiempo (**TC**,
*timecode*), longitudinal (**LTC**, *longitudinal timecode*) o en el intervalo vertical
(**VITC**, *vertical interval timecode*), con salto de cuadros (**DF**, *drop frame*) o sin él
(**NDF**, *non-drop frame*); la lista de decisiones de edición (**EDL**, *edit decision list*); el amplificador controlado por
tensión (**VCA**, *voltage-controlled amplifier*), que da nombre a un tipo de canal y de pista; la
interfaz digital de instrumentos musicales (**MIDI**, *Musical Instrument Digital Interface*); la
regrabación automática de diálogos (**ADR**, *automated dialogue replacement*), también llamada
*looping*; los efectos de sonido creados en sala (*Foley*); la banda internacional sin diálogos
(**M&E**, *music and effects*); los sistemas de climatización (**HVAC**, *heating, ventilation and
air conditioning*), que el manual de iZotope nombra como fuente de ruido; las entradas y salidas de propósito general (**GPIO**, *general purpose input/output*), por las que un equipo recibe o da órdenes; el control de calidad (**QC**, *quality control*). Los fabricantes se citan
por su nombre comercial: iZotope, Avid (Pro Tools es su estación de trabajo) y Dolby.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 9):
>
> Grabación, edición y postproducción: Músicas, cuñas, ráfagas y continuidad, DAW, pistas,
> sincronía, doblaje, limpieza, mezcla y entrega.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué procesos forman la postproducción de sonido; qué tres parámetros
definen un audio digital sin comprimir y cuánto ocupa un minuto de estéreo; qué códec es sin
pérdida; en qué fase trabaja el ambientador musical; qué es una pieza corta para la UER y qué
sonoridad máxima a corto plazo admite una cuña o una promoción según la EBU R 128 s1; por qué no
se mide el LRA de un anuncio; cómo se calcula la latencia de una memoria intermedia; qué es una
EDL; qué tipos de pista tiene una DAW y para qué sirve una auxiliar o una VCA; en qué capas se ordena una banda sonora y por qué se separan; qué diferencia hay entre
sincronizar la posición, la velocidad y la muestra; qué es el código de tiempo, el LTC y el VITC,
y cuándo importa el *drop frame*; cuántas muestras dura un cuadro a 48 kHz y 25 fps; qué es el
ADR; qué lleva una pista internacional; cómo trabaja una reducción de ruido por perfil y qué
artefactos produce; qué tolerancia de sonoridad se pide a un programa postproducido; qué es un
BWF, qué añade la UER al WAV y qué metadatos de sonoridad lleva su versión 2;
para qué sirve el *dither* y en qué orden se cambian frecuencia y resolución. En la prueba
práctica: montar y limpiar un corte, medir y corregir la sonoridad de una cuña o de un programa,
sincronizar un sonido grabado aparte, preparar las pistas de un máster y rellenar sus datos.

<!-- indice -->

## Índice

- [Grabación, edición y postproducción](#grabación-edición-y-postproducción)
  - [Qué es la postproducción](#qué-es-la-postproducción)
  - [La cadena de la postproducción de sonido](#la-cadena-de-la-postproducción-de-sonido)
  - [De qué está hecho un fichero de audio](#de-qué-está-hecho-un-fichero-de-audio)
  - [La cuenta del tamaño](#la-cuenta-del-tamaño)
  - [Con pérdida y sin pérdida](#con-pérdida-y-sin-pérdida)
  - [Los equipos de grabación](#los-equipos-de-grabación)
- [Músicas](#músicas)
  - [La ambientación musical](#la-ambientación-musical)
  - [Las piezas musicales de un programa](#las-piezas-musicales-de-un-programa)
  - [La música bajo la voz](#la-música-bajo-la-voz)
  - [Los derechos](#los-derechos)
- [Cuñas, ráfagas y continuidad](#cuñas-ráfagas-y-continuidad)
  - [Las piezas de continuidad](#las-piezas-de-continuidad)
  - [Por qué hay una norma para las piezas cortas](#por-qué-hay-una-norma-para-las-piezas-cortas)
  - [Lo que fija la R 128 s1](#lo-que-fija-la-r-128-s1)
  - [Un caso práctico: la cuña que no pasa](#un-caso-práctico-la-cuña-que-no-pasa)
  - [Las piezas cortas en internet](#las-piezas-cortas-en-internet)
  - [La continuidad: que todo suene igual](#la-continuidad-que-todo-suene-igual)
- [DAW](#daw)
  - [Qué es una estación de trabajo de audio digital](#qué-es-una-estación-de-trabajo-de-audio-digital)
  - [La latencia de una estación de trabajo](#la-latencia-de-una-estación-de-trabajo)
  - [La edición: cortar, fundir, encadenar](#la-edición-cortar-fundir-encadenar)
  - [La lista de decisiones de edición](#la-lista-de-decisiones-de-edición)
  - [La automatización](#la-automatización)
- [Pistas](#pistas)
  - [Las capas de la banda sonora](#las-capas-de-la-banda-sonora)
  - [Una fuente, una pista](#una-fuente-una-pista)
  - [Los tipos de pista de una estación de trabajo](#los-tipos-de-pista-de-una-estación-de-trabajo)
  - [Las pistas de un programa terminado](#las-pistas-de-un-programa-terminado)
- [Sincronía](#sincronía)
  - [Posición, velocidad y muestra](#posición-velocidad-y-muestra)
  - [El código de tiempo](#el-código-de-tiempo)
  - [La aritmética del código de tiempo](#la-aritmética-del-código-de-tiempo)
  - [Muestras y fotogramas](#muestras-y-fotogramas)
  - [La marca de tiempo del BWF](#la-marca-de-tiempo-del-bwf)
- [Doblaje](#doblaje)
  - [El ADR](#el-adr)
  - [Doblaje a otro idioma](#doblaje-a-otro-idioma)
  - [Lo que el doblaje pide a la grabación y a la mezcla](#lo-que-el-doblaje-pide-a-la-grabación-y-a-la-mezcla)
- [Limpieza](#limpieza)
  - [Qué se limpia](#qué-se-limpia)
  - [La reducción de ruido por perfil](#la-reducción-de-ruido-por-perfil)
  - [Los artefactos](#los-artefactos)
  - [Limpieza de los diálogos, paso a paso](#limpieza-de-los-diálogos-paso-a-paso)
- [Mezcla](#mezcla)
  - [Qué es mezclar en postproducción](#qué-es-mezclar-en-postproducción)
  - [Mezclar de oído, con la escucha fija](#mezclar-de-oído-con-la-escucha-fija)
  - [La sonoridad del programa terminado](#la-sonoridad-del-programa-terminado)
  - [Lo que se revisa antes de dar la mezcla por buena](#lo-que-se-revisa-antes-de-dar-la-mezcla-por-buena)
- [Entrega](#entrega)
  - [El máster](#el-máster)
  - [Reducir la resolución y cambiar la frecuencia](#reducir-la-resolución-y-cambiar-la-frecuencia)
  - [El fichero de entrega de audio: el BWF](#el-fichero-de-entrega-de-audio-el-bwf)
  - [Lo que lleva la extensión «bext»](#lo-que-lleva-la-extensión-bext)
  - [Archivo y distribución](#archivo-y-distribución)
  - [Un caso práctico: la entrega de una cuña de radio](#un-caso-práctico-la-entrega-de-una-cuña-de-radio)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Grabación, edición y postproducción

### Qué es la postproducción

La postproducción es todo lo que se le hace al material después de registrarlo y antes de
entregarlo. Su lista:

| Proceso | Qué hace |
|---|---|
| Volcado e ingesta | Meter el material en el sistema, con sus metadatos |
| Montaje | Elegir y ordenar: qué se ve y cuánto dura |
| Grafismo | Rótulos, cabecera, cortinillas, infografía |
| Efectos visuales | Composición, borrados, elementos generados |
| Etalonaje | Ajustar la imagen y darle su aspecto |
| Montaje y mezcla de sonido | Diálogo, ambientes, efectos y música |
| Máster | El fichero o la cinta final, con sus especificaciones |

La grabación es, por tanto, la fase anterior: lo que se capta en el estudio o en exteriores (temas 6,
7 y 8) llega a la postproducción como ficheros, y lo que no se grabó bien no siempre se puede
arreglar después (oficio). La edición es la parte del montaje que elige, corta y ordena; la
postproducción de sonido engloba la edición y todo lo demás hasta la entrega.

### La cadena de la postproducción de sonido

Dentro de la postproducción, el sonido tiene su propia cadena:

| Proceso | Qué hace |
|---|---|
| Montaje de diálogos | Limpiar, ajustar y elegir las tomas de voz |
| ADR o *looping* | Volver a grabar diálogo en sala, en sincronía con la imagen |
| Foley | Grabar en sala los efectos que se ven: pasos, roces, objetos |
| Efectos de biblioteca | Los que no se graban: motores, disparos, ambientes |
| Ambientes | La capa de fondo del lugar |
| Ambientación musical | Elegir y colocar la música |
| Mezcla | Equilibrar las capas y entregar en el formato de destino |
| Pista internacional | La mezcla sin la voz que hay que traducir, para vender fuera |

Cada fila tiene su epígrafe en este tema: la música en «Músicas», las capas en «Pistas», el ADR y
la pista internacional en «Doblaje», la limpieza de los diálogos en «Limpieza», la mezcla y la
entrega en los dos últimos. En radio la cadena es más corta —no hay imagen que seguir—, pero el
orden es el mismo: grabar, editar, limpiar, mezclar, medir y entregar (oficio).

### De qué está hecho un fichero de audio

Tres números definen un audio digital sin comprimir, y de ellos sale todo lo demás:

| Parámetro | Qué fija | Valores corrientes |
|---|---|---|
| Frecuencia de muestreo | Cuántas veces por segundo se mide la señal | 44,1 kHz —disco compacto—, 48 kHz —vídeo y difusión—, 96 y 192 kHz |
| Profundidad de bits | Con cuánta finura se mide cada muestra | 16 bits —disco—, 24 bits —producción—, 32 en coma flotante |
| Canales | Cuántas señales paralelas | 1 mono, 2 estéreo, más en multicanal |

Dos reglas los gobiernan. La del muestreo: una señal se puede reconstruir sin error a partir de sus
muestras si no tiene contenido a la mitad de la frecuencia de muestreo ni por encima (teorema del
muestreo, en el manual de J. O. Smith, de la Universidad de Stanford); dicho de otro modo, hay que
muestrear a más del doble de la frecuencia más alta, y lo que queda por encima se pliega como
frecuencias que no estaban (el *aliasing*). La de los bits, desarrollada en el tema 1: cada bit
añade unos 6 dB de rango dinámico teórico (16 bits, unos 96 dB; 24 bits, unos 144 dB).
Por eso el audio de producción se graba a 24 bits: el margen sobra y el ruido de cuantificación
queda muy por debajo del de la electrónica (oficio).

### La cuenta del tamaño

Un fichero PCM sin comprimir ocupa, sin contar la cabecera, lo que dicen sus tres números por su
duración. La
cuenta, y conviene hacerla siempre en el mismo orden, para un estéreo a 44,1 kHz, 16 bits y 5
minutos:

1. Bytes por muestra y canal: 16 bits son 2 bytes.
2. Bytes por segundo: 44.100 × 2 × 2 canales = 176.400.
3. Segundos: 5 minutos son 300.
4. Total: 176.400 × 300 = 52.920.000 bytes, que son unos 53 megabytes.

Y el atajo que conviene tener en la cabeza para no hacer la cuenta entera: un minuto de estéreo a
44,1 kHz y 16 bits ocupa unos 10 megabytes. Cinco minutos, unos 50.

Un minuto de estéreo en los formatos corrientes (cálculo, con el megabyte de un millón de bytes):

| Formato | Bytes por segundo | Un minuto de estéreo |
|---|---|---|
| 44,1 kHz · 16 bits | 44.100 × 2 × 2 = 176.400 | 10.584.000 B ≈ 10,6 MB |
| 48 kHz · 24 bits | 48.000 × 3 × 2 = 288.000 | 17.280.000 B ≈ 17,3 MB |
| 96 kHz · 24 bits | 96.000 × 3 × 2 = 576.000 | 34.560.000 B ≈ 34,6 MB |

Con el megabyte binario (1.048.576 bytes) las cifras salen algo menores (el primer renglón, unos
10,1); la cuenta es la misma. Un caso de entrega: un programa de 30 minutos en estéreo a 48 kHz y
24 bits ocupa 288.000 × 1.800 = 518.400.000 bytes, unos 518 MB; si se entregan además cuatro pistas
mono (dos de diálogo, una de música y efectos y una de reserva), cada una ocupa la mitad del
estéreo: las cuatro juntas, el doble que el estéreo, y el total se triplica, unos 1.555 MB
(cálculo).

### Con pérdida y sin pérdida

Los códecs de audio se reparten en dos familias:

| Familia | Qué hace | Ejemplos |
|---|---|---|
| Sin pérdida | Comprime como un fichero comprimido cualquiera: al descomprimir sale el original bit a bit | FLAC, Apple Lossless, WavPack |
| Con pérdida | DESCARTA lo que el oído no va a notar, apoyándose en el enmascaramiento | AAC, Opus, AC-3, MP3 |

Cada códec con pérdida tiene su terreno: AAC es el sucesor del MP3 y el estándar de la
distribución; Opus es el de las comunicaciones en tiempo real por red; AC-3 es el de Dolby Digital,
el del cine y la televisión multicanal.

La regla de familia: un códec sin pérdida no puede garantizar el caudal de datos. Comprime lo que
el material le deje, y el resultado varía de un material a otro. Un códec con pérdida sí garantiza
el caudal, porque tira lo que haga falta para cumplirlo.

La consecuencia para la postproducción: una señal de contribución no se comprime con pérdida si se
puede evitar, porque todavía va a pasar por más procesos. Las pérdidas se acumulan y no se
recuperan. Se graba, se edita y se mezcla en PCM (WAV o BWF), y el códec con pérdida se deja para el
último paso, la distribución (oficio). Por qué tras un códec con pérdida hace falta un techo de
pico más bajo se explica en el tema 13.

### Los equipos de grabación

| Equipo | Para qué |
|---|---|
| Grabador de mano | Ambientes, efectos, entrevistas rápidas: autonomía y micrófonos incorporados |
| Grabador multipista de campo | Sonido directo de rodaje: entradas con previo de calidad, código de tiempo y alimentación fantasma |
| Estación de trabajo con interfaz | Estudio: grabación, edición y mezcla (epígrafe «DAW») |
| Grabador de estado sólido de emisora | Continuidad y archivo: redundancia y arranque por orden |

Qué se exige a una grabación que va a postproducción (oficio): cada fuente en su pista (tema 6), a
24 bits y a la frecuencia del proyecto (48 kHz en televisión), con nivel que deje margen (la
alineación a −18 dBFS de la EBU R 68, en los temas 4 y 5), con el mismo código de tiempo que la
imagen si se graba aparte, y con un nombre de fichero y unos datos que permitan encontrarla.

## Músicas

### La ambientación musical

El ambientador musical elige y coloca la música de un programa: la sintonía, las ráfagas, los
fondos y los cortes musicales que subrayan.

La música se decide en preproducción y se coloca en postproducción. En preproducción se acuerda el
estilo, se encarga la composición y se gestionan los derechos; pero la música no se puede colocar
hasta que el montaje existe, porque va pegada a la duración y al ritmo de los planos. De ahí que su
fase sea la posproducción.

Lo que no es trabajo del ambientador (oficio): el etalonaje es una parte de la postproducción, y de
imagen; lanzar las piezas durante la emisión es trabajo de continuidad, no de ambientación; y en
preproducción la música se decide y se contrata, pero no se ambienta.

### Las piezas musicales de un programa

| Pieza | Qué es (oficio) |
|---|---|
| Sintonía | La pieza musical que identifica un programa o una emisora; una sola |
| Careta | La entrada del programa: sintonía con la voz o los elementos que lo presentan |
| Ráfaga | Fragmento musical breve que separa bloques o noticias y marca el ritmo |
| Fondo | Música bajo la voz, a nivel de acompañamiento |
| Corte musical | Fragmento de una obra que se oye en primer plano |

Estos términos son vocabulario de oficio, sin definición normativa leída. La ambientación sonora es
la que se compone con efectos, ráfagas y fondos musicales (tema 6).

### La música bajo la voz

Cuando la música va de fondo, manda la voz: la música se baja lo bastante para que se entienda la
palabra, y se sube en los huecos (oficio). Se hace a mano, con el fader o con la automatización del
DAW (tema 4), o de forma automática con un atenuador gobernado por la voz, el *ducker* del tema 5.

La edición de la música también tiene sus reglas de oficio: se corta a compás y en un punto en que
la frase musical cierra, no a mitad; si hay que acortar una pieza se quita un fragmento entero
(una frase, una repetición) y se encadena en el mismo punto del compás; y un final se resuelve con
la cadencia de la obra o con un fundido, no con un corte seco.

Cuánto más alta que la voz puede sonar la música en distribución por internet lo dice un documento
de la AES: si es operativamente viable, **«the listener experience can be improved by normalizing
music 2 or 3 LU higher than speech»** (AES TD1008), porque la voz normalizada a la misma sonoridad
integrada que la música se percibe unos 2 o 3 dB más fuerte. En emisión, la EBU R 128 mide el programa entero y no normaliza por
elementos (tema 13).

### Los derechos

La música lleva derechos, y usarla exige tenerlos: en preproducción se gestionan (epígrafe «La
ambientación musical»). La gestión de derechos musicales de CSRTV, sus bibliotecas y sus
procedimientos de declaración no constan en un documento publicado leído (véase «Lo que este tema
no da»).

## Cuñas, ráfagas y continuidad

### Las piezas de continuidad

La continuidad es lo que se emite entre programa y programa, y las piezas cortas que la forman
(oficio; ninguna definición normativa leída):

| Pieza | Qué es | Dónde va |
|---|---|---|
| Cuña | Anuncio breve de radio, publicitario o institucional | En los bloques de publicidad |
| Ráfaga | Pieza musical corta con la identidad de la emisora o del programa | Entre bloques o entre noticias |
| Careta | La entrada de un programa | Al empezar |
| Promoción | Anuncio de un programa propio | En los bloques |
| Indicativo | Identificación de la emisora | A las horas, entre programas |

La UER no usa esas palabras: agrupa estas piezas como **«advertisements (commercials) and promos
(as well as interstitials etc.)»** y las piezas de muy pocos segundos como **«interstitials,
stingers, bumpers and similar very short items»** (EBU R 128 s1). A efectos técnicos, una cuña, una
ráfaga o una promoción son contenido corto, y cada una cuenta como un programa.

### Por qué hay una norma para las piezas cortas

Una cuña puede cumplir la sonoridad integrada de −23 LUFS (tema 13) y aun así molestar: si es muy
dinámica, su promedio cumple, pero su pasaje más fuerte salta sobre el programa que la rodea. La
EBU R 128 s1 existe por eso: **«Especially for short-form content like advertisements
(commercials) and promos (as well as interstitials etc.) there is a need to give guidance using the
parameter Maximum Short-term Loudness in addition to the basic parameters Programme Loudness and
Maximum True Peak Level.»** Su fin es evitar **«overly dynamic short-form programmes, which would
lead to audience complaints»**.

Qué es contenido corto: **«A programme of short duration (up to approximately 2 minutes),
typically shorter than 30 seconds; In addition to advertisements (commercials) and promotional
items also interstitials, stingers, bumpers and similar very short items belong to that
category.»**

Y que cada pieza es un programa: **«An advertisement (commercial), trailer, promotional item
(‘promo’), interstitial or similar item shall be considered to be a programme in this context.»**
La definición de programa de la R 128 s1 dice **«audio-visual or audio-only»**: vale para
televisión y para radio.

### Lo que fija la R 128 s1

| Punto | Lo que dice |
|---|---|
| b) Sonoridad del programa | **«the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS»**; **«a tolerance of ±0.2 LU is allowed»**, en la implantación de los flujos de trabajo (por ejemplo, en control de calidad) y para tener en cuenta los errores de medida |
| c) Objetivo más bajo | **«In special cases»** (en casos especiales) se puede normalizar por debajo de −23 **«on purpose. This exception shall be clearly indicated to ensure that such a lower Programme Loudness Level is not compensated»** |
| d) Sonoridad máxima a corto plazo | **«the Short-term Loudness Level (measured in compliance with EBU Tech 3341) shall not exceed −18.0 LUFS (+5.0 LU on the relative scale)»**; **«a tolerance of +0.2 LU is allowed»**, con la misma salvedad |
| f) Todo el programa | **«the audio signal shall generally be measured in its entirety, without emphasis on specific foreground elements such as speech, music or sound effects»** |
| g) Pico verdadero | **«the True Peak Level of the programme shall not exceed −1 dBTP»** para audio lineal (la nota remite a la EBU Tech 3344 para los máximos de cada sistema de distribución); **«The measurement tolerance is ±0.3 dB»** para señales de banda limitada a 20 kHz |

Las tres cifras de una cuña, por tanto: −23 LUFS integrada, −18 LUFS como máximo a corto plazo
(+5 LU en la escala relativa, cuyo 0 es −23) y −1 dBTP en audio lineal. La sonoridad a corto plazo es la que se
mide con una ventana de 3 segundos (tema 13).

Lo que no se mide en una pieza corta: **«The measure ‘Loudness Range’ is not useful for
short-form content. [...] Therefore, a maximum and/or minimum value for Loudness Range shall not be
specified for programmes of this length/genre.»** La R 128 general ya desaconseja el LRA en
programas de menos de un minuto (tema 13).

Las versiones: la primera edición es de noviembre de 2014; la V2, de enero de 2016, **«removed
alternative Maximum Momentary Loudness limit»**; la V3, de agosto de 2020, es la **«Addition of
tolerances (for QC and True-peak)»**. La vigente es la V3.

### Un caso práctico: la cuña que no pasa

Una cuña de 20 segundos mide −23,1 LUFS integrada, −1,5 dBTP de pico verdadero y −15,5 LUFS de
máxima a corto plazo. Integrada y pico cumplen; la máxima a corto plazo supera en 2,5 LU el límite
de −18 LUFS (y en 2,3 LU el límite con tolerancia, −17,8). Bajarla entera 2,5 dB no sirve: la
integrada caería a −25,6 LUFS, fuera de la tolerancia de ±0,2 LU (y la salvedad c) exige declararlo
a propósito). Hay que reducir la dinámica del pasaje fuerte —con un compresor o bajando ese tramo
con la automatización— y volver a medir hasta que la máxima a corto plazo quede en −18 o por debajo
con la integrada en −23 (cálculo sobre las cifras de la R 128 s1).

### Las piezas cortas en internet

Para la distribución por internet, el documento técnico AES TD1008 da una cifra para el mismo tipo
de pieza: en su tabla 1, la fila **«Interstitial»** da una sonoridad de distribución de −18 LUFS
con una tolerancia superior de +0,2 LU, y el documento define ese contenido como **«Interstitial Content such as commercial advertising,
public service announcements, promotional material»**. No es la emisión: en emisión rige la
R 128 s1, a −23 LUFS. La sonoridad del *streaming* y del pódcast es materia del tema 7.

### La continuidad: que todo suene igual

La continuidad encadena piezas de orígenes distintos, y el oyente sólo nota una cosa: si el nivel
salta (oficio). Si cada pieza llega normalizada a −23 LUFS, se encadenan sin retocar. La Tech 3343
describe cómo se protege la salida sin estropear lo que ya cumple: el sistema de emisión **«shall
signal to the Loudness Processor when loudness-compliant content is played [...]. The processor
should then switch to Bypass Mode or to a preset that only applies safety True-peak limiting. Such
signalling may be performed via GPIO or control data network systems.»** (§ 2.4). Es decir: el
procesador de sonoridad de la salida se aparta cuando entra material conforme, o se queda sólo en
limitador de seguridad de pico verdadero.

Lo que el operador comprueba de cada pieza antes de cargarla en continuidad (oficio sobre las
cifras de la R 128 s1): sonoridad integrada, máxima a corto plazo y pico verdadero; que no lleve
silencio de más al principio ni al final, porque en continuidad las piezas se lanzan una detrás de
otra; y que su duración y su nombre coincidan con lo que dice la pauta. El sistema de continuidad
de CSRTV y sus requisitos de entrega de publicidad no constan en un documento publicado leído.

## DAW

### Qué es una estación de trabajo de audio digital

Una DAW es un ordenador con un programa de grabación, edición y mezcla y una interfaz de audio que
hace las conversiones y da las entradas y salidas (oficio). En ella se hace todo lo del tema: se
graba, se edita, se limpia, se mezcla, se mide y se exporta el fichero de entrega. Por dentro se
organiza como una mesa (tema 4): pistas que hacen de canales, envíos, buses, inserciones y un bus
de salida, más una línea de tiempo en la que se colocan los fragmentos de audio.

La edición en una DAW es no destructiva (oficio): los fragmentos de la línea de tiempo apuntan al
fichero grabado, y cortar, mover o fundir un fragmento no cambia ese fichero; sólo lo cambia un
proceso que se aplica y se escribe sobre él, o la exportación final. Por eso conviene conservar
siempre los ficheros originales de la grabación.

### La latencia de una estación de trabajo

Toda DAW trabaja por bloques de muestras: la interfaz llena una memoria intermedia (*buffer*) y el
programa la procesa entera. Mientras se llena, el sonido espera, y esa espera es la latencia.

El razonamiento: la latencia en segundos es el número de muestras dividido entre las muestras por
segundo. 128 ÷ 44.100 = 0,0029 segundos. Para pasarlo a milisegundos se multiplica por mil: 2,9
milisegundos.

La fórmula, por tanto: latencia en milisegundos = muestras × 1.000 ÷ frecuencia de muestreo, con la
frecuencia en hercios (44.100, no 44,1). La comprobación que despeja cualquier duda es el orden de
magnitud: una memoria intermedia de 128 muestras es la configuración de trabajo de baja latencia de
cualquier estación. Su latencia es de unos pocos milisegundos; si la cuenta da miles, la frecuencia
se ha escrito en kilohercios.

| Buffer | Latencia a 44,1 kHz | Cuándo se usa |
|---|---|---|
| 64 muestras | 1,5 ms | Grabar con monitorización por el DAW: lo más ajustado |
| 128 muestras | 2,9 ms | Trabajo normal de grabación |
| 512 muestras | 11,6 ms | Mezcla: no hay que tocar en directo |
| 2.048 muestras | 46 ms | Mezclas muy cargadas de proceso |

A 48 kHz, la frecuencia de televisión, las mismas memorias dan (cálculo): 64 muestras, 1,33 ms; 128,
2,67 ms; 256, 5,33 ms; 512, 10,67 ms; 1.024, 21,33 ms.

La regla de oficio: buffer pequeño para grabar, buffer grande para mezclar. Con memoria pequeña el
ordenador tiene menos tiempo para procesar cada bloque y, si no le da tiempo, se oyen chasquidos o
cortes; con memoria grande procesa con holgura, pero quien graba se oye con retraso (oficio).

La latencia real de un sistema es mayor que la del búfer: hay que sumar la de los conversores y la
del proceso. Los procesos con anticipación (*look-ahead*, tema 5) o de análisis añaden su propio
retardo; las estaciones de trabajo suelen compensarlo retrasando las demás pistas para que todo
siga alineado (oficio; cómo lo hace cada programa no se ha leído).

### La edición: cortar, fundir, encadenar

Las operaciones básicas de edición y sus cuidados (oficio):

| Operación | Qué es | El cuidado |
|---|---|---|
| Corte | Separar o quitar un fragmento | Cortar en silencio o en un punto en que la onda pase por cero; un corte en mitad de la onda produce un chasquido |
| Fundido de entrada o de salida | Subir o bajar el nivel al principio o al final de un fragmento | Da un arranque y un final limpios, sin chasquido |
| Encadenado | Fundir la salida de un fragmento con la entrada del siguiente, solapados | Es la forma de unir dos tomas o dos ambientes sin que se note la unión |
| Ajuste de nivel del fragmento | Subir o bajar un fragmento entero | Igualar tomas antes de mezclar |

En una edición de voz se corta en las pausas y en las respiraciones, y el ritmo del habla tiene que
seguir sonando natural: quitar todas las respiraciones hace una voz que no respira (oficio). Bajo un
corte, el ambiente del lugar tapa las uniones (tema 6: «el ambiente se graba siempre»).

Para los cortes de voz de un informativo de radio, el Manual de estilo de RTVE (capítulo 3, de RNE)
da dos criterios de oficio:

Su duración no se fija en segundos, sino por el sentido: **«El corte debe durar el tiempo
imprescindible para que el mensaje emitido sea congruente, desarrolle una idea con principio y final
y resulte radiofónicamente aceptable.»**

Cómo se corta: **«Salvo excepciones, debe evitarse cortar un testimonio en alto; existen recursos como
el de bajar el sonido cuando se considera que el oyente ya se ha formado una idea de lo que estaba
expresando el personaje en cuestión. En todos los casos, el oyente debe entender qué dicen todas y cada
una de las voces que intervienen en el boletín»**.

Son referencia de oficio, no norma de CSRTV: no se ha localizado un libro de estilo de radio
publicado de Canal Sur.

### La lista de decisiones de edición

Una EDL es la lista de las decisiones de un montaje: para cada corte, de qué fuente sale, con qué
código de tiempo de entrada y de salida, en qué posición del montaje se coloca y con qué transición
entra. Es el documento que permite rehacer un montaje en otro sistema y con el material original.

Una EDL no lleva todos los parámetros de una edición: lleva las fuentes, los códigos de tiempo, el
orden y el tipo de transición, y deja fuera la corrección de color, los niveles de audio, la
posición de los rótulos y los ajustes de los efectos.

Para el sonido eso importa: una EDL permite recomponer los cortes, pero no la mezcla. Los formatos
de intercambio de sesiones entre estaciones de trabajo y montaje, que sí llevan más datos, no se han
leído en fuente (véase «Lo que este tema no da»).

### La automatización

La automatización guarda los movimientos de la mezcla —nivel, panorama, silencios, envíos, ajustes
de los procesos— sobre la línea de tiempo, y los repite en cada reproducción. Sus modos (Off, Read,
Write, Touch, Latch y Trim, con los nombres de Pro Tools, de Avid) están en el tema 4. En postproducción es la herramienta que hace posible una mezcla que cambia con el
programa: bajar la música cuando entra una voz, subir un ambiente en una transición, corregir un
tramo concreto (oficio).

## Pistas

### Las capas de la banda sonora

Las cinco capas de una banda sonora de ficción, que son las que se montan por separado y se mezclan
al final:

| Capa | Qué contiene |
|---|---|
| Diálogos | La voz de los actores: directo, y lo que haya que sustituir en sala |
| Ambientes | El fondo del lugar: la calle, el bar, el bosque |
| Efectos de sala (*Foley*) | Lo que los cuerpos hacen: pasos, ropa, objetos, todo grabado mirando la imagen |
| Efectos de biblioteca | Lo que no se puede hacer en sala: disparos, motores, explosiones |
| Música | Original y no original |

El tema 6 las agrupa en cuatro (diálogo, ambientes, efectos y música), con los dos tipos de efectos
en una sola; es la misma clasificación, más o menos desglosada. En un informativo o un documental
las capas son las mismas con otros nombres: la voz en off y los totales hacen de diálogo (oficio).

Y la razón de que se separen no es estética: es comercial. Manteniendo los diálogos en su propia
capa, la mezcla puede entregarse también sin ellos —es la banda internacional, la M&E— y con ella
se dobla la obra a cualquier idioma sin volver a montar nada. El doblaje que el enunciado nombra
depende enteramente de que esa separación se haya respetado.

### Una fuente, una pista

La regla de la sesión de postproducción es la misma que la de la captación (tema 6): cada fuente
en su pista, para poder tratarla aparte (oficio). En la práctica:

- Cada micrófono de la grabación llega en su pista; no se mezclan dos voces en una.
- Las pistas se agrupan por capa y cada capa sale por su propio bus (submezcla): diálogos,
  ambientes, efectos, música. La mezcla final es la suma de esos buses.
- Una fuente mono va en pista mono; un ambiente o una música estéreo, en pista estéreo. Poner en
  estéreo una fuente mono sólo duplica la señal.
- Las pistas llevan nombre, y la sesión un orden fijo (voz arriba, música abajo, o el que marque la
  casa), para que otro técnico pueda abrirla y entenderla.

Separar por capas es lo que permite luego las entregas del epígrafe «Entrega»: la mezcla completa,
la pista internacional y, si se piden, las capas por separado.

### Los tipos de pista de una estación de trabajo

Las pistas de una DAW no son todas iguales. Se toman aquí de Pro Tools, de Avid, porque es la
documentación que se ha leído; otras estaciones usan nombres parecidos. Su guía de referencia
enumera **«audio, Auxiliary Input, Master Fader, VCA Master, MIDI, Instrument, Folder, and video
tracks»**:

| Tipo | Para qué sirve, según la guía |
|---|---|
| Audio | **«record to disk and play back from disk recorded or imported audio files»**: grabar y reproducir ficheros |
| Auxiliar (*Auxiliary Input*) | **«effects sends, destinations for submixes, as a bounce destination, as inputs to monitor or process audio»**: el retorno de un efecto, la submezcla de una capa |
| Máster (*Master Fader*) | **«control the overall level of audio paths that are routed to physical output paths»**; también el nivel de una submezcla |
| VCA (*VCA Master*) | Imita los canales VCA de una mesa analógica para **«control, group, or offset the signal levels of other channels»**; **«do not pass audio»**: no tienen entradas, salidas, inserciones ni envíos, y gobiernan las pistas de un grupo de mezcla |
| MIDI | **«record, store, and playback MIDI data»**; no pasa audio |
| Instrumento | MIDI y audio en una misma tira de canal, para instrumentos virtuales o externos |
| Carpeta (*Folder*) | Contenedor de otras pistas; la de encaminamiento (*Routing Folder*) además pasa audio **«similarly to an Auxiliary Input track»** |
| Vídeo | Añadir o importar vídeo; en postproducción, la imagen de referencia sobre la que se monta y se mezcla (oficio) |

Las pistas de audio, auxiliares, de carpeta de encaminamiento, máster y de instrumento pueden ser
mono, estéreo o multicanal (en Pro Tools, de 3 a 8 canales en las versiones Ultimate y Studio).
Aplicado a una sesión de postproducción (oficio): las voces y los ambientes en pistas de audio; cada
capa sumada en una auxiliar, que es su submezcla; la reverberación en una auxiliar alimentada por
envíos; una VCA para subir o bajar toda una capa sin tocar sus pistas; y una pista máster al final,
que es donde va el *dither* de la entrega (epígrafe «Reducir la resolución y cambiar la
frecuencia»).

### Las pistas de un programa terminado

Qué lleva cada pista de audio del máster lo fija su destino: la especificación de un máster incluye
la configuración de pistas de audio —qué lleva cada una: mezcla, pista internacional,
audiodescripción— (epígrafe «Entrega»). El reparto de pistas que exige CSRTV en sus másteres de
emisión no consta en un documento publicado leído.

## Sincronía

### Posición, velocidad y muestra

Sincronizar no es una sola cosa. Las tres cosas que una estación de trabajo tiene que sincronizar,
y que no son la misma:

| Qué se sincroniza | Con qué | Si falla |
|---|---|---|
| La POSICIÓN: por dónde va | Código de tiempo (LTC o MTC) | La imagen y el sonido no cuadran |
| La VELOCIDAD: a qué ritmo avanza | Word clock o referencia de vídeo | Deriva lenta: cuadra al principio y no al final |
| La MUESTRA: cuándo cae cada una | Word clock | Chasquidos y ruido digital |

El MTC es el código de tiempo transmitido por MIDI (la interfaz digital de instrumentos musicales,
*musical instrument digital interface*); el *word clock* es la señal de reloj que marca a todos los
equipos digitales el instante de cada muestra (oficio). En una instalación de audio sobre IP ese
reloj común lo da la red, con el protocolo de tiempo de precisión (tema 15).

Y un error de concepto que hay que evitar: el código de tiempo NO sincroniza el reloj de muestreo. Dice en
qué punto se está, no a qué velocidad se avanza. Un montaje que lleve código de tiempo y no lleve
reloj común deriva igualmente.

Un ejemplo de deriva (cálculo): si el reloj de un grabador va un 0,01 % más deprisa que el de la
cámara, en una hora de grabación el sonido acaba 3.600 × 0,0001 = 0,36 segundos desplazado, que a
25 fps son 9 cuadros: la toma cuadra al principio y al final se ve hablar antes de oírse. Por eso,
en doble sistema (tema 6), además de código común se enclavan los relojes o se vuelve a
sincronizar de vez en cuando (oficio).

### El código de tiempo

El código de tiempo es la etiqueta que numera cada cuadro en horas, minutos, segundos y cuadros
(HH:MM:SS:CC), y es el instrumento de sincronización de toda la cadena (oficio). Viaja de dos
formas:

| Forma | Cómo viaja | Dónde se usa |
|---|---|---|
| LTC, longitudinal | Como una señal de audio, por un cable o canal propio | Entre equipos: cámara, grabador de sonido, generador |
| VITC, vertical | Dentro de la propia señal de vídeo, en el intervalo vertical | Dentro de la cadena de vídeo |

Una palabra de LTC ocupa 80 bits por cuadro; de ellos, 32 son bits de usuario (oficio; la norma
SMPTE que lo fija no se ha leído).

- DF o NDF sólo importa a 29,97 y 59,94: como esa cadencia no es entera, un código que cuente 30
  cuadros por segundo se adelanta al reloj, y el *drop frame* salta números de cuadro para
  corregirlo (no salta imágenes). A 25 y 50 cuadros no hay nada que corregir.

En la estación de trabajo, el código de tiempo es la regla sobre la que se coloca todo: la sesión
empieza en el mismo código que el vídeo del programa, y cada fichero grabado con código se puede
colocar en su sitio exacto (oficio). Cómo se sincroniza en rodaje un sonido grabado aparte —sistema
único o doble, claqueta— está en el tema 6.

### La aritmética del código de tiempo

La duración entre dos códigos se calcula restando campo a campo, de derecha a izquierda, con
acarreos, y sabiendo a qué cadencia va el material (cálculo). Ejemplo a 25 cuadros por segundo, de
00:47:17:23 a 01:23:54:00:

| Campo | Operación | Resultado |
|---|---|---|
| Cuadros | 00 − 23 no se puede: se toma prestado un segundo (25 cuadros) | 25 − 23 = 2 |
| Segundos | 54 − 1 prestado = 53; 53 − 17 | 36 |
| Minutos | 23 − 47 no se puede: se toma prestada una hora | 83 − 47 = 36 |
| Horas | 1 − 1 prestada = 0; 0 − 0 | 0 |

La resta da 00:36:36:02. Si el último código se cuenta como parte del plano (duración inclusiva), se
suma un cuadro: 00:36:36:03. A 24 o a 30 cuadros el campo de cuadros saldría distinto, porque el
préstamo es de 24 o de 30.

### Muestras y fotogramas

Cuando el sonido va con imagen, hay que pasar de muestras a cuadros. Cuánto duran 13.440 muestras
en un sistema a 48 kHz con vídeo a 25 fotogramas por segundo; la cuenta, en dos pasos y sin
atajos:

1. De muestras a segundos: 13.440 ÷ 48.000 = 0,28 segundos.
2. De segundos a fotogramas: 0,28 × 25 = 7.

Y el atajo: a 48 kHz y 25 fotogramas por segundo, cada fotograma dura exactamente 1.920 muestras.
13.440 ÷ 1.920 = 7.

| Cadencia | Muestras por fotograma a 48 kHz |
|---|---|
| 25 fps —Europa— | 1.920 |
| 24 fps —cine— | 2.000 |
| 30 fps | 1.600 |
| 29,97 fps, la cadencia del sistema americano | No es entero: de ahí el código de tiempo con salto |

A 50 fps, 960 muestras por cuadro (cálculo: 48.000 ÷ 50). En Europa las cuentas salen redondas; a
29,97 no (oficio). Un desfase de un cuadro a 25 fps son 40 milisegundos (1.000 ÷ 25), y de 1.920
muestras a 48 kHz (cálculo).

### La marca de tiempo del BWF

El fichero BWF (epígrafe «Entrega») lleva escrita su posición en el tiempo. La EBU Tech 3285, del
campo TimeReference: **«These fields shall contain the time-code of the sequence. It is a 64-bit value
which contains the first sample count since midnight. The number of samples per second depends on
the sample frequency»**. Es decir, no guarda horas y minutos, sino el número de muestras
transcurridas desde la medianoche hasta la primera muestra del fichero.

Un caso (cálculo): una grabación a 48 kHz que empieza a las 10:00:00 lleva como referencia
10 × 3.600 × 48.000 = 1.728.000.000 muestras. Al importarla, la estación de trabajo la coloca en
el código 10:00:00:00 de la sesión. Si la cámara y el grabador llevaban el mismo código de tiempo,
sonido e imagen caen juntos sin claqueta; si no, hace falta la claqueta del tema 6.

## Doblaje

### El ADR

El ADR es la creación y sustitución de diálogo en sincronía labial, en postproducción de sonido.

Se hace en una sala de doblaje, con el intérprete viendo su propia imagen, y sirve para tres cosas:

1. Sustituir diálogo que se grabó mal: con ruido, con viento, con un avión encima.
2. Cambiar una interpretación sin volver a rodar.
3. Añadir diálogo que no se rodó: reacciones, murmullos, voces de fondo.

Su nombre inglés lo explica: *automated dialogue replacement*, sustitución automatizada de diálogo.
Y *looping* viene del método antiguo: se montaba un bucle de película con la escena y se repetía
sin parar hasta que el intérprete encajaba.

Lo que no es ADR, aunque sea de la misma fase (oficio): el proceso por el que se combinan varias
pistas es la mezcla; el sonido del entorno que se ve en la imagen es el ambiente; y la ventana que
muestra la disposición cronológica del montaje es la línea de tiempo.

### Doblaje a otro idioma

El doblaje, en sentido amplio, es sustituir la voz original por otra grabada en sala; el ADR lo hace
con la voz del mismo intérprete y en el mismo idioma, y el doblaje a otro idioma, con la de un
actor de doblaje (oficio). Los dos se graban igual: mirando la imagen, frase a frase, buscando la
sincronía labial.

Para doblar a otro idioma hace falta la banda internacional (epígrafe «Las capas de la banda
sonora»): toda la mezcla menos la voz que se sustituye. En un documental, la pista internacional
lleva músicas, ambientes y los totales de los entrevistados en su idioma original, y deja fuera la
voz en off, que se vuelve a locutar (tema 6).

### Lo que el doblaje pide a la grabación y a la mezcla

Qué cuida el técnico en una sesión de ADR o de doblaje (oficio):

- Sala seca y silenciosa, y el micrófono a una distancia fija durante toda la sesión, para que
  todas las frases suenen igual.
- El mismo tipo de micrófono y una distancia parecida a la del rodaje, si la voz nueva tiene que
  casar con frases de directo que se quedan.
- Cada toma en su pista, con el código de tiempo de la sesión, para colocarla y elegir después.
- En la mezcla, la voz de sala se lleva al plano de la imagen —con ecualización y reverberación
  (tema 5)— y se le pone debajo el ambiente del lugar: una voz de sala sin ambiente suena pegada
  al oído en un plano general (los planos de sonido, en el tema 6).
- La sincronía labial se comprueba mirando la imagen, y se corrige moviendo la toma o editándola
  por sílabas. La medida de referencia es el cuadro: 40 ms a 25 fps (epígrafe «Muestras y
  fotogramas»); el desfase máximo tolerable entre sonido e imagen no se ha leído en fuente.

## Limpieza

### Qué se limpia

Limpiar es quitar de una grabación lo que sobra sin tocar lo que sirve (oficio). Los defectos
corrientes y la herramienta que se usa contra cada uno:

| Defecto | Qué es | Contra él (oficio) |
|---|---|---|
| Ruido de fondo constante | Soplido, climatización, ventiladores, motores | Reducción de ruido por perfil |
| Zumbido de red | La frecuencia de la red eléctrica y sus armónicos | Filtros de ranura en la fundamental y sus armónicos, o un reductor de zumbido |
| Chasquidos y crepitaciones | Impulsos cortos: un mal corte, un contacto, un disco | Reductor de chasquidos, o edición de la muestra |
| Recorte | La onda saturada, con la cresta plana | Reconstrucción de la forma de onda; si es grave, no tiene arreglo |
| Oclusivas | El golpe de aire de la p y la b en el micrófono | Filtro paso alto en ese tramo o reductor de oclusivas |
| Sibilantes | La s demasiado brillante | Reductor de sibilantes (tema 5) |
| Viento y roces | Golpes de graves, roce de la ropa con un corbata | Filtro paso alto, reductores específicos o edición |
| Reverberación de la sala | La voz lejana, con cola | Reductor de reverberación, con límites |

El fabricante del programa de restauración cuyo manual se ha leído, iZotope, tiene un módulo para
casi cada fila: **«De-click»**, **«De-clip»**, **«De-crackle»**, **«De-ess»**, **«De-hum»**,
**«De-plosive»**, **«De-reverb»**, **«De-rustle»**, **«De-wind»**, además del **«Spectral
De-noise»** del epígrafe siguiente. Son nombres de un producto comercial: sirven para ver qué
familias de herramientas existen, no como norma. Los filtros (paso alto, ranura) y el reductor de
sibilantes están explicados en el tema 5.

La regla de oficio que va antes que todas: lo que no se graba no hay que limpiarlo. Toda limpieza
fuerte deja huella, y lo que se recorta en la grabación no se recupera (temas 5 y 6).

### La reducción de ruido por perfil

El principio lo explica el manual de iZotope RX 11: **«Spectral De-noise is designed to remove
stationary or slowly changing tonal noise and broadband hiss by learning a profile of the offending
noise and then subtracting it from the signal. It can be useful for tape hiss, HVAC systems,
outdoor environments, line noise, ground loops, camera motors, fans, wind, and complex buzz with
many harmonics.»** Es decir: el programa aprende cómo es el ruido y lo resta del conjunto.

Cómo se trabaja:

1. Se busca un trozo con sólo ruido: **«Make a selection of the longest section of noise you can
   find in your file (ideally a few seconds in length).»** Por eso se graba un minuto de ambiente
   sin nadie hablando (tema 6): sin trozo de ruido limpio no hay perfil.
2. Se aprende el perfil. El perfil aprendido a mano sirve para el ruido fijo: **«Manually learned
   noise profiles are best suited to removing or reducing noise that is constant and continuous»**.
   Para el ruido que cambia —**«recordings in outdoor environments, traffic noise, or ocean
   waves»**— el programa tiene un modo adaptativo, que sigue al ruido.
3. Se ajusta el umbral: **«Higher threshold settings reduce more noise, but also suppress low-level
   signal components.»**
4. Se ajusta la reducción, que puede ser distinta para las partes tonales y las aleatorias del
   ruido: **«tonal parts (such as hum, buzz or interference) and random parts (such as hiss)»**.

Y el aviso del fabricante: **«Strong suppression of noise can also degrade low-level signals, so
it is recommended to apply only as much suppression as needed»**.

### Los artefactos

Una limpieza excesiva se oye, y el manual nombra dos artefactos, uno en cada extremo del mismo
ajuste:

- La sustracción espectral fuerte **«can produce musical noise artifacts, resulting in a “chirpy”
  or “watery” sound during heavy processing»**: el ruido que queda suena a gorjeo o a agua.
- Y si, para evitarlo, el proceso se apoya más en la puerta de banda ancha, tiene menos ruido
  musical pero suena a puerta y deja **«bursts of noise right after the signal falls below the
  threshold»**: ráfagas de ruido justo cuando la voz se calla. Es un compromiso entre los dos
  artefactos, que el módulo regula con un control propio (*Artifact Control*).

Cómo se evitan (oficio): reducir poco y en varias pasadas mejor que mucho en una; escuchar el
resultado y también lo que se ha quitado; y comparar con el original a igual nivel. Una voz algo
ruidosa se entiende; una voz con artefactos, peor.

### Limpieza de los diálogos, paso a paso

El orden de trabajo habitual sobre una pista de diálogo (oficio):

1. Edición: quitar golpes, toses y ruidos sueltos cortando o sustituyendo el trozo por ambiente
   del mismo lugar.
2. Filtro paso alto contra los graves que no son voz (tema 5).
3. Zumbido, si lo hay.
4. Reducción de ruido por perfil, suave.
5. Sibilantes y oclusivas, si hace falta.
6. Después, la ecualización y la compresión de la mezcla (tema 5).

Y el relleno: donde se ha cortado algo, debajo tiene que seguir sonando el ambiente del lugar; si no,
el silencio digital delata el corte (tema 6).

## Mezcla

### Qué es mezclar en postproducción

La mezcla equilibra las capas y entrega en el formato de destino (epígrafe «La cadena de la
postproducción de sonido»). A diferencia del directo (tema 8), se hace sobre material grabado: se
puede repetir, automatizar y medir el programa entero antes de entregarlo (oficio).

El orden de trabajo habitual (oficio):

1. Los diálogos primero: limpios, igualados entre tomas y en su plano. Son la referencia del resto.
2. Los ambientes, que dan continuidad y tapan los cortes.
3. Los efectos, a la medida de la imagen.
4. La música, que deja sitio a la voz (epígrafe «La música bajo la voz»).
5. El conjunto: el bus de salida, la medida de sonoridad y el pico verdadero.

Los procesos de la mezcla (ecualización, compresión, limitación, reverberación) son los del tema 5;
la mesa, sus buses y la automatización, los del tema 4; la mezcla multicanal y su mezcla
descendente a estéreo, las del tema 14.

### Mezclar de oído, con la escucha fija

La normalización por sonoridad cambia la forma de mezclar. La Tech 3343: **«Loudness levelling
encourages to mix ‘only by ear’ - after setting levels and a fixed monitor gain.»** Se fija el nivel
de escucha una vez y no se toca: si con la escucha fija el programa suena bien, estará cerca del
objetivo. El nivel de escucha de referencia de la UER y su ajuste están en el tema 8.

### La sonoridad del programa terminado

Un programa postproducido no tiene la excusa del directo. La Tech 3343: en postproducción **«a
general tolerance of ±0.2 LU around the Target Level of −23 LUFS is acceptable»**, para no rechazar
programas por la suma de las tolerancias de medida, mientras que el directo tiene ±1 LU (tema 13).
Dentro de la tolerancia no hay que hacer nada; fuera de ella, se corrige con **«a simple corrective static gain
calculation»** (§ 3.2), un cambio de ganancia fijo para todo el programa; **«Typically, offline loudness
meters perform both the measurement as well as the correction.»** (§ 3.1).

Un cambio de ganancia de X dB mueve la sonoridad integrada X LU y el pico verdadero X dB (tema 13).
Dos casos (cálculo):

| Programa medido | Corrección | Resultado |
|---|---|---|
| −21,4 LUFS, pico −2,5 dBTP | Bajar 1,6 dB | −23,0 LUFS, pico −4,1 dBTP: cumple |
| −24,5 LUFS, pico −1,8 dBTP | Subir 1,5 dB | −23,0 LUFS, pero pico −0,3 dBTP: no cumple el −1 dBTP |

En el segundo caso hay que limitar antes de subir: el limitador tiene que rebajar los picos al
menos 0,7 dB (de −1,8 a −2,5 dBTP), para que tras subir 1,5 dB no pasen de −1,0 dBTP (con 0,8 dB
de reducción quedan en −1,1, con algo de margen); y medir de nuevo,
porque limitar baja un poco la integrada (oficio y cálculo).

### Lo que se revisa antes de dar la mezcla por buena

Oficio, sobre las cifras de las recomendaciones citadas y del tema 13:

- Integrada del programa entero en −23 LUFS (±0,2 LU en postproducción); en una pieza corta,
  además, máxima a corto plazo no mayor de −18 LUFS.
- Pico verdadero no mayor de −1 dBTP.
- La voz se entiende en todo el programa, también sobre la música y los efectos.
- Fase: la suma en mono no pierde la voz (tema 13).
- Sin chasquidos en los cortes, sin silencios digitales bajo los cortes y sin saltos de ambiente.
- Sincronía con la imagen al principio y al final del programa.

## Entrega

### El máster

El máster es el resultado final del que salen todas las copias, y lo que lo define no es su soporte
sino sus especificaciones:

| Especificación | Qué fija |
|---|---|
| Formato y códec | Cómo está escrito el vídeo |
| Resolución y cadencia | Cuántos píxeles y cuántos fotogramas por segundo |
| Espacio de color y niveles | Que la señal esté dentro del rango legal |
| Configuración de pistas de audio | Qué lleva cada pista: mezcla, pista internacional, audiodescripción |
| Nivel de sonoridad | El volumen medio normalizado que el destino exige |
| Estructura | Cabecera con barras y tono, claqueta, cuenta atrás, programa |
| Subtítulos | Incrustados o en fichero aparte |

Y la regla que ordena todo: el máster se hace para su destino. Una misma pieza tiene un máster de
emisión, uno de plataforma y uno de venta internacional, y los tres se diferencian sobre todo en las
pistas de audio y en los subtítulos.

Al técnico de sonido le tocan tres filas: las pistas, la sonoridad (−23 LUFS en emisión, epígrafe
«La sonoridad del programa terminado») y el tono de la cabecera, que se da a −18 dBFS, el nivel de
alineación de la EBU R 68 (temas 4 y 13). Las especificaciones de entrega de CSRTV no constan en un
documento publicado leído.

### Reducir la resolución y cambiar la frecuencia

Se produce a 24 bits (epígrafe «De qué está hecho un fichero de audio»), pero hay destinos que piden
16 bits, como el disco compacto, u otra frecuencia de muestreo (44,1 kHz en lugar de 48, o al
revés). Son dos conversiones de la entrega, y la guía de referencia de Pro Tools las explica así.

**El *dither*.** **«Dither is used to minimize quantization artifacts when reducing the bit depth
of an audio signal, for example, from 24-bit to 16-bit.»** Esos artefactos se notan sobre todo
cerca del fondo del rango dinámico, **«such as during a quiet passage or a fade-out»**. El *dither*
los disimula **«by introducing very low-level random noise to a signal»**, y es un compromiso:
**«a trade-off between signal-to-noise performance and less-apparent distortion»**, algo más de
ruido a cambio de una distorsión menos audible. El conformado del ruido (*noise shaping*) lo mejora
desplazando ese ruido lejos de la zona media del espectro, **«(around 4 kHz), where the human ear is
most sensitive»**.

Cuándo se aplica, según la guía:

- En toda reducción de resolución: **«when mixing down to a 16-bit destination, use a dither plugin
  on the main output»**, aunque la sesión sea de 16 bits, porque por dentro se procesa con más.
- No al grabar una submezcla en una pista de la misma sesión, ni al mezclar hacia un destino de 24
  bits o hacia un destino analógico con una interfaz de 24 bits, ni al escuchar y grabar normalmente: en esos casos el *dither* se quita o se puentea.
- Va como último proceso de la cadena, en la pista máster, porque sus inserciones van después
  del fader y así el *dither* recibe los cambios de nivel del máster.
- Si no se pone, la exportación de la mezcla (*Bounce Mix*) no lo aplica por su cuenta: **«the
  resulting file will be converted by truncation»**, es decir, se cortan los bits sobrantes sin más.
  En cambio, la exportación de fragmentos y la importación a una sesión de menos bits sí aplican
  *dither* por su cuenta.

**La conversión de frecuencia de muestreo** (**SRC**, *sample rate conversion*). Pro Tools la ofrece
con cinco calidades, de **«Low (fastest, but lowest quality) to Tweak Head (highest quality, but
slowest)»**: a más calidad, más tiempo de proceso. Y si hay que hacer las dos cosas, el orden es
fijo: **«first convert the sample rate while maintaining the higher bit depth, and then reduce the
sample rate-converted file to the lower bit depth, using a dither»**. Primero se cambia la
frecuencia a 24 bits y, al final, se reduce a 16 con *dither*.

Un caso (sobre esas reglas): de un máster de emisión a 48 kHz y 24 bits se pide una copia para
disco compacto, a 44,1 kHz y 16 bits. Se convierte primero a 44,1 kHz manteniendo los 24 bits, y
después se reduce a 16 bits con *dither* en el último punto de la cadena. Hacerlo al revés, o
truncar sin *dither*, degrada los pasajes suaves y los fundidos.

### El fichero de entrega de audio: el BWF

Cuando lo que se entrega es sólo sonido —una cuña, un programa de radio, las pistas de una
postproducción— el formato de intercambio de la radiodifusión es el BWF. La EBU Tech 3285: **«The
Broadcast Wave Format (BWF) is a file format for audio data. It can be used for the seamless
exchange of audio material between different broadcast environments and between equipment based on
different computer platforms.»** Y qué es: **«The Broadcast Wave Format is based on the Microsoft
WAVE audio file format, to which the EBU has added a “Broadcast Audio Extension” chunk.»** Un BWF
es, por tanto, un WAV con un bloque de datos añadido, la extensión «bext». El audio va de ordinario
en PCM, sin comprimir; la especificación admite también audio MPEG (del grupo de expertos en imágenes en movimiento, *Moving Picture Experts Group*), con un bloque propio. Un programa que lee WAV puede abrirlo; lo que no sepa leer de la extensión, lo
ignora (oficio).

Sus versiones:

| Versión | Qué trae |
|---|---|
| 0 | La original, publicada **«in 1997 as EBU Tech 3285»** |
| 1 | **«differs from Version 0 only in that 64 of the 254 reserved bytes in Version 0 are used to contain a SMPTE UMID»** |
| 2 | **«a substantial revision of Version 1 which incorporates loudness metadata (in accordance with EBU R 128 [...])»** |

Y son compatibles hacia atrás: **«Version 2 is backwards compatible with Versions 1 and 0»**.

### Lo que lleva la extensión «bext»

| Campo | Qué guarda |
|---|---|
| Description | **«Description of the sound sequence»**, hasta 256 caracteres |
| Originator | **«Name of the originator»**, hasta 32 |
| OriginatorReference | Referencia del originador, hasta 32 |
| OriginationDate | Fecha, **«yyyy:mm:dd»** |
| OriginationTime | Hora, **«hh:mm:ss»** |
| TimeReference | **«First sample count since midnight»** (epígrafe «La marca de tiempo del BWF») |
| Version | La versión de la extensión |
| UMID | El identificador único del material, en 64 bytes |
| LoudnessValue | **«Integrated Loudness Value of the file in LUFS (multiplied by 100)»** |
| LoudnessRange | El rango de sonoridad |
| MaxTruePeakLevel | El pico verdadero máximo |
| MaxMomentaryLoudness | La sonoridad momentánea máxima |
| MaxShortTermLoudness | La sonoridad a corto plazo máxima |
| CodingHistory | El historial de codificación |

Los cinco valores de sonoridad van multiplicados por 100 (así lo dice la especificación de cada
campo): un programa de −23,0 LUFS se escribe −2300 (cálculo).
Los cinco campos de sonoridad son los de la versión 2, y son justo las medidas de la R 128 y de la
R 128 s1: integrada, LRA, pico verdadero, momentánea y a corto plazo. Una cuña entregada en BWF
versión 2 puede llevar escritas sus tres cifras de cumplimiento; aun así, la R 128 pide que los
metadatos coincidan con la sonoridad real, y el material externo se vuelve a medir (tema 13).

El historial de codificación, campo CodingHistory: **«Each string shall contain a description of a
coding process applied to the audio data. Each new coding application shall add a new string»**.
Cada paso por un códec o una conversión deja su línea, y quien recibe el fichero sabe por dónde ha
pasado.

### Archivo y distribución

Lo que se entrega a emisión va normalizado a −23 LUFS; para internet, la sonoridad de distribución
es más alta (tema 7). El documento de la AES dice que las producciones que van a seguir disponibles durante
años pueden prepararse para el futuro si se producen y archivan **«at a loudness of -24 LUFS or
lower and then remastered for distribution»**: se guarda el máster a −24 LUFS o menos y se hace una
versión para cada plataforma, en vez de archivar la versión más fuerte.

Lo que se archiva, además de la mezcla (oficio): la pista internacional, las capas por separado si
se hicieron, y la sesión con sus ficheros originales, que es lo único que permite rehacer la mezcla.

### Un caso práctico: la entrega de una cuña de radio

Una cuña de 30 segundos para emisión, paso a paso (oficio sobre las cifras citadas):

1. Mezcla terminada: voz limpia, música bajo la voz, sin silencios de más al principio ni al final.
2. Medida: integrada −23 LUFS (±0,2 LU), máxima a corto plazo no mayor de −18 LUFS (+0,2 LU de
   tolerancia), pico verdadero no mayor de −1 dBTP (R 128 s1). Sin LRA.
3. Exportación en PCM, en BWF, a la frecuencia y resolución que pida la casa (48 kHz y 24 bits son
   lo corriente en producción; no consta la especificación de CSRTV). Si piden 16 bits, con
   *dither* al final de la cadena (epígrafe «Reducir la resolución y cambiar la frecuencia»).
4. Datos del BWF: descripción, originador, fecha y hora; en versión 2, la sonoridad integrada (−2300),
   el pico verdadero y la sonoridad a corto plazo máxima.
5. Tamaño, para comprobar que el fichero es lo que dice ser: 30 s en estéreo a 48 kHz y 24 bits son
   288.000 × 30 = 8.640.000 bytes, unos 8,6 MB, más la cabecera (cálculo).

## Recomendaciones técnicas que el tema cita

| Documento | Qué se toma |
|---|---|
| EBU R 128 s1, V3 (agosto de 2020) | Por qué hay norma para las piezas cortas; definición de contenido corto y de programa; −23 LUFS (±0,2 LU); objetivo más bajo declarado; máxima a corto plazo de −18 LUFS (+5 LU, +0,2 LU de tolerancia); medida del programa entero; −1 dBTP (±0,3 dB); LRA no aplicable; historia de versiones |
| EBU Tech 3343-2023 | Procesador de sonoridad en *bypass* o sólo limitador de pico verdadero ante material conforme (§ 2.4); mezclar de oído con la escucha fija; tolerancia de ±0,2 LU en postproducción; medidores fuera de línea (§ 3.1); corrección por ganancia estática (§ 3.2) |
| EBU Tech 3285, versión 2.0 (mayo de 2011) | Qué es el BWF; WAVE más la extensión «bext»; versiones 0, 1 (UMID) y 2 (metadatos de sonoridad) y su compatibilidad; campos de la extensión; TimeReference; CodingHistory |
| AES TD1008.1.21-9 (24 de septiembre de 2021) | Piezas intersticiales en internet a −18 LUFS (+0,2 LU) y su definición; música 2 o 3 LU sobre la voz; producir y archivar a −24 LUFS o menos |

Ninguna norma legal (ley o reglamento) regula la grabación, la edición o la postproducción de
sonido: el resto del tema es documentación de fabricante, oficio y cálculo.

## Lo que este tema no da, y dónde está

- Una definición normativa de cuña, ráfaga, careta, sintonía o indicativo: no se ha leído ninguna
  (el diccionario académico no fue accesible); el tema los da como vocabulario de oficio.
- Los formatos de intercambio de sesiones entre estaciones de trabajo y sistemas de montaje, y la
  entrega por capas separadas con nombre normalizado: no se han leído en fuente.
- El desfase máximo tolerable entre sonido e imagen en emisión: no se ha leído la recomendación que
  lo fija.
- El doblaje como oficio (organización de una sala, ajuste de las frases, pautas del director de
  doblaje): sin fuente más allá del ADR; se da como oficio.
- Los modos de edición y de compensación de retardo de cada estación de trabajo concreta, y los
  nombres de sus herramientas: sólo se ha leído, de Pro Tools, la automatización (tema 4), los tipos
  de pista, el *dither* y la conversión de frecuencia de muestreo, y la reducción de ruido de
  iZotope RX 11. Los tipos de *dither* y sus ajustes, fuera de lo dicho, no se han leído.
- La norma SMPTE del código de tiempo y el reparto de sus 80 bits: no se ha leído.
- Lo propio de CSRTV: especificaciones de entrega de programas y de publicidad (formato, frecuencia,
  resolución, pistas, sonoridad exigida), su sistema de continuidad y de emisión de radio, sus
  estaciones de trabajo, su gestión de derechos musicales y de archivo sonoro. No constan en un
  documento publicado localizado.
- La sonoridad (medidor, escalas, R 128, pico verdadero, control de calidad), en el tema 13; la
  sonoridad del *streaming* y del pódcast, en el tema 7; la mezcla para emisión en directo y el
  nivel de escucha de referencia, en el tema 8; los procesos de ecualización, dinámica, filtros y
  reverberación, en el tema 5; la mesa y la automatización, en el tema 4; la captación, el doble
  sistema y la claqueta, la pista internacional de un documental y los planos de sonido, en el
  tema 6; el multicanal y la mezcla descendente, en el tema 14; la sincronía por red y el PTP
  (protocolo de tiempo de precisión, *precision time protocol*), en el tema 15; los bits y el rango
  dinámico, en el tema 1.

## Trazabilidad

Fuentes leídas el 25/09/2026 en su texto original (releídas en la verificación ese mismo día); las
recomendaciones de la UER y el documento de la AES, en su versión vigente ese día.

| Fuente | Qué sostiene |
|---|---|
| EBU R 128 s1, *Loudness Parameters for Short-form Content (adverts; promos, etc.)*, V3, Ginebra, agosto de 2020 | Motivo y fin del suplemento; definiciones de *short-form content* y de programa; puntos b), c), d), f) y g) con sus tolerancias; LRA no aplicable; versiones de 2014, 2016 y 2020 |
| EBU Tech 3343-2023, *Guidelines for Production of Programmes in accordance with EBU R 128*, noviembre de 2023 | § 2.4 procesador de sonoridad y señalización; § 2.3 y recuadro de la p. 10, mezclar de oído; § 3.1 tolerancia de ±0,2 LU en postproducción y medidores fuera de línea; § 3.2 corrección por ganancia estática |
| EBU Tech 3285, *Specification of the Broadcast Wave Format (BWF)*, versión 2.0, mayo de 2011 | Definición y base WAVE; extensión «bext»; versiones 0, 1 y 2 y compatibilidad; campos Description, Originator, OriginatorReference, OriginationDate, OriginationTime, TimeReference, Version, UMID, los cinco de sonoridad y CodingHistory |
| AES, *AESTD1008.1.21-9, Recommendations for Loudness of Internet Audio Streaming and On-Demand Distribution*, 24 de septiembre de 2021 | *Interstitial* −18 LUFS / +0,2 y su definición; normalizar la música 2 o 3 LU por encima de la palabra; producir y archivar a −24 LUFS o menos |
| iZotope, *RX 11 Manual*, módulo «Spectral De-noise» e índice de módulos | Principio de la reducción por perfil y sus usos; trozo de ruido de pocos segundos; perfil manual y modo adaptativo; umbral; partes tonales y aleatorias; aviso de degradación; artefactos (*musical noise* y ráfagas de ruido); nombres de los demás módulos |
| Avid Technology, *Pro Tools Reference Guide*, versión 2025.12 (noviembre de 2025): cap. 13 «Tracks» (p. 298-299); cap. 22, «Sample Rate Conversion Quality» (p. 628-629); cap. 52, «Dither» (p. 1464-1465); cap. 56, «Using Dither» y «Sample Rate Conversion and Bit Depth Reduction» (p. 1593-1594) | Tipos de pista y para qué sirve cada uno; formatos mono, estéreo y multicanal; qué es el *dither*, su compromiso y el conformado del ruido; cuándo se usa y dónde se inserta; truncado en la exportación de la mezcla; las cinco calidades de conversión; orden de conversión de frecuencia y de resolución |
| J. O. Smith III, *Mathematics of the Discrete Fourier Transform (DFT)*, CCRMA, Universidad de Stanford, apartado «Sampling Theorem» (web) | Teorema del muestreo: reconstrucción sin error si no hay contenido a la mitad de la frecuencia de muestreo o por encima; *aliasing* |
| Manual de estilo de RTVE (web), capítulo 3 (RNE), apartado de los cortes de voz | Duración y forma de cortar un corte de voz (referencia de oficio, no norma de CSRTV) |

Oficio sin norma detrás, y así se declara: la lista de procesos de la postproducción y de la cadena
de sonido; los tres parámetros de un audio digital y sus valores corrientes; las familias de códecs
y su terreno; los equipos de grabación; el trabajo del ambientador musical; las piezas musicales y
de continuidad y su vocabulario; la música bajo la voz y su edición a compás; la protección de la
continuidad y las comprobaciones de cada pieza; la estación de trabajo, la edición no destructiva,
la memoria intermedia pequeña para grabar y grande para mezclar, la compensación de retardo; el
uso de cada tipo de pista en una sesión de postproducción; las
operaciones de edición y sus cuidados; la EDL y lo que deja fuera; las capas de la banda sonora y
la razón comercial de separarlas; una fuente, una pista; posición, velocidad y muestra; el código de
tiempo, LTC y VITC, el *drop frame* y los 80 bits; el ADR, sus usos y su nombre; el doblaje a otro
idioma y los cuidados de una sesión; la tabla de defectos y el orden de limpieza de un diálogo; el
orden de la mezcla y su revisión; el máster y sus especificaciones; lo que se archiva. Es cálculo, y
se puede rehacer: el tamaño de los ficheros; la latencia de una memoria intermedia a 44,1 y 48 kHz;
la cuña que no pasa; la deriva de un reloj; la resta de códigos de tiempo; las muestras por
fotograma y la duración de un cuadro; la referencia de tiempo de un BWF; las correcciones de
sonoridad de un programa; el valor de sonoridad multiplicado por 100.
