# Esquema · Tema 3 del específico de Ingeniería Técnica · Telecomunicación · La señal audiovisual y su sincronización

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalación audiovisual ·
`[exam]` = opciones del propio cuadernillo · `[norma]` = norma técnica nombrada, sin cita literal.
**Siglas**: la interfaz digital serie (**SDI**), en sus generaciones **HD-SDI**, **3G-SDI**,
**6G-SDI** y **12G-SDI**; la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**); la Sociedad de
Ingeniería de Audio (**AES**), con **AES10** —que es **MADI**— y **AES11**; el comienzo y el fin del
vídeo activo (**SAV** y **EAV**); la interfaz serie asíncrona (**ASI**); la interfaz de transporte de
datos serie (**SDTI**); el sistema de línea alternada en fase (**PAL**); la codificación sin retorno a
cero (**NRZ**); el conector coaxial de bayoneta (**BNC**); la matriz de gráficos de vídeo (**VGA**),
la interfaz visual digital (**DVI**), la interfaz multimedia de alta definición (**HDMI**) y el
**DisplayPort** (**DP**); los gigabits por segundo (**Gbps**) y los megahercios (**MHz**); y la
ultraalta definición (**UHD**).

**Cabecera.** Enunciado: punto 3 del anexo · **14 preguntas: el tercer banco de la ocupación** ·
**reparto**: 6 de interfaz serie y sus generaciones, 3 de sincronismo y medida, 2 de cableado, 2 de
interfaces de vídeo, 1 de televisión analógica · **es el punto que más distingue a un ingeniero de
televisión de uno de telecomunicación general.**

<!-- indice -->

## Índice

- [La escalera de caudales](#la-escalera-de-caudales)
- [La trama por dentro](#la-trama-por-dentro)
- [Codificación y medida](#codificación-y-medida)
- [Lo que cabe por el mismo cable](#lo-que-cabe-por-el-mismo-cable)
- [Las señales de sincronización](#las-señales-de-sincronización)
- [El cableado de cámara](#el-cableado-de-cámara)
- [Interfaces del mundo informático](#interfaces-del-mundo-informático)
- [Lo que queda de lo analógico](#lo-que-queda-de-lo-analógico)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La escalera de caudales

| Norma | Nombre | Caudal | Qué transporta |
|---|---|---|---|
| **SMPTE 259M** · `[norma]` | **SD-SDI** | **270 Mbps** | **Definición estándar** |
| **SMPTE 292M** · `[norma]` | **HD-SDI** | **1,485 Gbps** ✔ | **Hasta 1080i y 720p** |
| **SMPTE 424M** · `[norma]` | **3G-SDI** | **2,970 Gbps** | **1080p a 50 y 60** |
| **SMPTE 2081** · `[norma]` | **6G-SDI** | **5,940 Gbps** | **2160p hasta 30** ✔ |
| **SMPTE 2082** · `[norma]` | **12G-SDI** | **11,880 Gbps** | **2160p hasta 60** ✔ |

- **LA RELACIÓN QUE AHORRA MEMORIZAR** · `[of]` · **Cada generación DOBLA la anterior**, salvo el
  primer salto. **Sabiendo 1,485 salen las tres siguientes.** **La cifra no es 1,5 redonda por el
  factor 1000/1001 de las cadencias fraccionarias.**
- **PREGUNTA 8** · `[exam]` · **Tasa de bits de SMPTE-292M: 1,485 Gbps.**
- **PREGUNTA 66** · `[exam]` · **SMPTE-292M especifica la interfaz de alta definición a 1,5 Gbps.**
- **POR QUÉ LAS DOS CIFRAS NO SE CONTRADICEN** · `[of]` · **Una pide el caudal y la otra qué
  especifica la norma**, y en el sector esa interfaz se llama «uno y medio».
- **PREGUNTA 46** · `[exam]` · **Por la interfaz de seis gigabits cabe 2160p30.**
- **LA CUENTA QUE LA RESUELVE** · `[of]` · **2160p30 pide unas cuatro veces 1080p30**, y **4 × 1,485 =
  5,94.** **2160p60 pide el doble —es la de doce—; 2160p120, cuatro veces más; 1080p150 no es cadencia
  normalizada.**
- **PREGUNTA 59** · `[exam]` · **En ultraalta definición se usa la de doce gigabits porque transmite 4K
  sin comprimir en UN SOLO CABLE.** **La alternativa era llevarla por cuatro cables de tres**, con
  cuatro veces el cableado, las matrices y los puntos de fallo.
- **LAS FALSAS DE LA 59** · `[exam]` · **«Reducir la longitud»**: es al revés. **«Compatible con
  definición estándar y alta»**: cierto, pero la de tres también. **«Modulación sin retorno a cero»**:
  la usan todas.
- **EL AVISO DE OBRA** · `[of]` · **El alcance BAJA con el caudal**: donde la definición estándar
  pasaba de doscientos metros, doce gigabits no llega a unas decenas. **Por eso lo nuevo va a fibra o a
  red.**

## La trama por dentro

| Marca | Qué significa | Dónde |
|---|---|---|
| **SAV** | **Comienzo del vídeo activo** | **Antes de la parte visible** |
| **EAV** | **Fin del vídeo activo** ✔ | **Después de la parte visible** |

- **PREGUNTA 7** · `[exam]` · **EAV es fin de vídeo activo.** **La falsa «duración de vídeo activo» es
  la buena**, porque ese parámetro existe: **la sigla nombra el FIN, no la duración.**
- **PARA QUÉ SIRVEN** · `[of]` · **La interfaz serie no lleva sincronismos separados: van DENTRO de la
  trama como códigos reservados.**
- **LO QUE VA ENTRE UNA Y OTRA** · `[of]` · **El intervalo de borrado horizontal**, que es **donde se
  mete el audio incrustado, el código de tiempo y los datos auxiliares.** **Ésa es la razón de que un
  coaxial lleve vídeo, dieciséis canales de audio y datos a la vez.**

## Codificación y medida

| Codificación | Cómo representa | Rasgo |
|---|---|---|
| **Sin retorno a cero** | **Un nivel por bit** ✔ | **Aprovecha el ancho de banda; pide aleatorización** |
| **Con retorno a cero** | **Vuelve a cero entre bits** | **Gasta el doble** |
| **Manchester** | **Transición en medio de cada bit** | **Lleva el reloj dentro; gasta el doble** |
| **Bifase** | **De la misma familia** | **Código de tiempo longitudinal** |

- **PREGUNTA 41** · `[exam]` · **La interfaz digital serie usa codificación sin retorno a cero.**
- **LA PRECISIÓN DECLARADA** · `[of]` · **En rigor es sin retorno a cero INVERTIDO y con aleatorización
  previa.** **De las cuatro opciones, la marcada es la única de esa familia.**
- **POR QUÉ HAY QUE ALEATORIZAR** · `[of]` · **Una tira larga de ceros o de unos no da transiciones**, y
  **el receptor recupera el reloj DE las transiciones.**
- **PREGUNTA 55** · `[exam]` · **En un diagrama de ojo se analiza el jitter.**

| Qué se mira | Qué dice |
|---|---|
| **Apertura VERTICAL** | **Margen de amplitud frente al ruido** |
| **Apertura HORIZONTAL, grosor de los cruces** | **El jitter** ✔ |

- **QUÉ ES EL JITTER Y POR QUÉ MATA** · `[of]` · **La variación del instante de cada transición.** **Si
  pasa del margen del receptor, éste muestrea donde no debe**: **el fallo es de todo o nada** —cortes o
  congelación, no ruido—, y por eso se mide antes de que ocurra.

## Lo que cabe por el mismo cable

| | **Interfaz digital serie** | **Interfaz serie asíncrona** |
|---|---|---|
| **Qué lleva** | **Vídeo sin comprimir** | **Flujo de transporte comprimido** |
| **Caudal** | **Fijo, el de la norma** | **Variable, hasta 270 Mbps** |
| **Capa física** | **Coaxial de 75 ohmios** | **La misma** ✔ |

- **PREGUNTA 19** · `[exam]` · **Sí se puede distribuir una señal asíncrona con un distribuidor de
  vídeo digital serie.** **Un distribuidor no interpreta la señal: la reamplifica.**
- **DÓNDE ESTÁ EL LÍMITE** · `[of]` · **Un distribuidor REGENERADOR sí puede fallar**, porque
  reconstruye la trama y espera estructura de vídeo.
- **PREGUNTA 33** · `[exam]` · **Impedancia de la conexión coaxial de bayoneta para vídeo: 75 ohmios.**

| Impedancia | Dónde |
|---|---|
| **50 ohmios** | **Radiofrecuencia, instrumentación** |
| **75 ohmios** | **Vídeo y televisión** ✔ |
| **110 ohmios** | **Audio digital por par simétrico** |
| **600 ohmios** | **Audio analógico antiguo** |

- **EL AVISO QUE HACE ÚTIL EL DATO** · `[of]` · **El conector de bayoneta existe en las dos impedancias
  y se parecen mucho.** **Uno de 50 en línea de vídeo refleja**: en definición estándar apenas se nota
  y **en doce gigabits tumba el enlace.**
- **PREGUNTA 74** · `[exam]` · **La interfaz de transporte de datos serie llega hasta cuatro veces la
  velocidad de reproducción.** **Es SERIE —va por coaxial— y el factor corriente es CUATRO.**

## Las señales de sincronización

| Señal | Qué sincroniza | Dónde |
|---|---|---|
| **Negro de barras** | **El vídeo**, sincronismos de dos niveles | **Definición estándar y mixtas** |
| **Tres niveles** | **Lo mismo, con tres niveles** | **Alta definición** |
| **AES11** · `[norma]` | **El audio digital** | **Referencia de audio** |
| **Reloj de palabra** | **Cada muestra de audio** | **Enlaces cortos de audio** |
| **Tiempo de precisión** | **Todo, sobre red** | **Instalaciones sobre red** |

- **PREGUNTA 35, NEGATIVA** · `[exam]` · **La que NO sirve para sincronización es AES10**, porque **esa
  norma es MADI: transporte de 64 canales de audio, no referencia de tiempo.**
- **LA REGLA SIN MEMORIZAR NÚMEROS** · `[of]` · **Tres opciones llevan sólo tiempo y una lleva audio.**
  **La que lleva audio es la intrusa.**
- **EL AVISO DE INSTALACIÓN** · `[of]` · **La referencia de vídeo y la de audio tienen que estar
  BLOQUEADAS entre sí.** **Si el reloj de audio deriva aparecen deslizamientos** —chasquidos
  periódicos— **de los fallos más difíciles de localizar**, porque tardan horas en salir.

## El cableado de cámara

- **PREGUNTA 31** · `[exam]` · **El cable SMPTE 311M es híbrido de fibra para cámaras: vídeo, audio,
  control y alimentación.** **Dos fibras monomodo más dos conductores de cobre**, de ahí «híbrido».

| | **Triaxial** | **Híbrido de fibra** |
|---|---|---|
| **Medio** | **Cobre, tres capas concéntricas** | **Dos fibras más dos conductores** ✔ |
| **Alcance** | **Cientos de metros, degradando** | **Kilómetros, sin degradar** |
| **Qué lleva** | **Vídeo, audio, control, alimentación** | **Lo mismo** |
| **Manejo** | **Pesado y rígido** | **Más ligero, conector delicado** |

- **EL AVISO DE UNIDAD MÓVIL** · `[of]` · **El conector es la pieza más frágil y más cara.** **Se
  limpia con material específico antes de cada conexión**: **una mota de polvo en la cara de la fibra
  deja la cámara sin imagen.**

## Interfaces del mundo informático

| Interfaz | Vídeo | Audio | Rasgo |
|---|---|---|---|
| **Matriz de gráficos de vídeo** | **Sólo analógico** | **No** | **La antigua de quince patillas** |
| **Interfaz visual digital** | **Analógico Y digital** ✔ | **No** | **Nació en la transición** |
| **Interfaz multimedia de alta definición** | **Sólo digital** | **Sí** | **El del equipo doméstico** |
| **DisplayPort** | **Sólo digital** | **Sí** | **El informático, con retención mecánica** |

- **PREGUNTA 82** · `[exam]` · **La que lleva analógico y digital es la interfaz visual digital.**
- **LA REGLA** · `[of]` · **Una es sólo analógica, dos son sólo digitales y una es las dos.** **La que
  nació en la transición lleva las dos.**

## Lo que queda de lo analógico

| Sistema | Subportadora de color |
|---|---|
| **Línea alternada en fase** | **4,43 MHz** ✔ |
| **Sistema estadounidense** | **3,58 MHz** |

- **PREGUNTA 13** · `[exam]` · **La ráfaga del sistema de línea alternada en fase va a 4,43 MHz.**
- **QUÉ ES ESA RÁFAGA** · `[of]` · **Unos ciclos de la subportadora de color enviados en cada línea,
  antes de la imagen, para que el receptor sepa con qué fase y frecuencia demodular.** **Sin ella no
  hay color.**
- **LAS FALSAS SON FRECUENCIAS REALES DE OTRA COSA** · `[exam]` · **10,7 megahercios es la frecuencia
  intermedia de un receptor de frecuencia modulada** y **21,4 es su doble.**
- **POR QUÉ SIGUE EN UN TEMARIO DE 2022** · `[of]` · **Las instalaciones conservan referencia de negro
  de barras**, que lleva esa subportadora, **y los equipos de medida la usan.** **La emisión analógica
  se apagó; la referencia no.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 7 | Siglas del fin de vídeo activo | **Fin de vídeo activo** ✔ |
| 8 | Tasa de bits de SMPTE-292M | **1,485 Gbps** ✔ |
| 13 | Frecuencia de la ráfaga de color | **4,43 MHz** ✔ |
| 19 | Si un distribuidor de vídeo sirve para señal asíncrona | **Sí** ✔ |
| 31 | Qué es el cable SMPTE 311M | **Fibra híbrida con vídeo, audio, control y alimentación** ✔ |
| 33 | Impedancia del coaxial de vídeo | **75 ohmios** ✔ |
| 35 | Cuál NO se usa para sincronización | **AES10** ✔ |
| 41 | Codificación de la interfaz digital serie | **Sin retorno a cero** ✔ **·** con precisión |
| 46 | Qué cabe por la interfaz de seis gigabits | **2160p30** ✔ |
| 55 | Qué se analiza en un diagrama de ojo | **Jitter** ✔ |
| 59 | Por qué doce gigabits en ultraalta definición | **4K sin comprimir en un solo cable** ✔ |
| 66 | Qué especifica SMPTE-292M | **Interfaz de alta definición a 1,5 Gbps** ✔ |
| 74 | Qué es la interfaz de transporte de datos serie | **Serie, hasta cuatro veces la velocidad** ✔ |
| 82 | Qué interfaz lleva analógico y digital | **La interfaz visual digital** ✔ |
