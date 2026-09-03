# Esquema · Tema 12 del específico de Realización Televisión · Formatos y procesos de registro

**Siglas**: tres contenedores de fichero y un formato de audio (**AVI**, **MOV**, **MKV** y
**WAV**), **que el tema nombra por su extensión y no desarrolla**; y la difusión de vídeo digital
terrestre de segunda generación (**DVB-T2**), **cuyas cifras de ancho de banda el temario no ha
podido contrastar**.

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio y tecnología de la señal ·
`[plan]` = plantilla oficial.

**Siglas**: los contenedores **MP4**, **AVI**, **MOV** y **MKV**, y el formato de
audio **WAV**; el conector *Bayonet Neill-Concelman* (**BNC**), el conector de audio profesional
(**XLR**, que la industria llama también **Canon** por su fabricante original), el conector de vídeo
para monitores (**VGA**) y el conector de audio de clavija (***jack***); la transformada discreta
del coseno (**DCT**, *discrete cosine transform*); la ultra alta definición (**UHD** o **UHDV**,
como la escribe un enunciado) y la alta definición (**HD**, y **HDTV** referida a la televisión); el
código de tiempo (**TC**), en su forma longitudinal (**LTC**, *longitudinal time code*) y en su
forma vertical (**VITC**); el formato de intercambio de material (**MXF**); la línea nacional
norteamericana (**NTSC**) y la línea alternada en fase (**PAL**); el conjunto redundante de discos
independientes (**RAID**); el programa de plan de cámaras **CuePilot**, que es una marca. Y unas
cuantas siglas más que sólo salen como opción falsa o como término suelto: el formato de audio de
intercambio (**AIFF**), la Unión Internacional de Telecomunicaciones (**UIT**), las dos modalidades
de código de tiempo inventadas por otro cuadernillo de este mismo proceso (**FD** y **FF**) y la
tarjeta que este examen inventa (**SWS**), que tampoco existe; las tarjetas **SxS** y **P2** y el
disco **XDCAM**.

**Cabecera.** Enunciado: «3.2. Formatos y Procesos de registro, captación y reproducción de imagen.
Tipos de archivo» · **18 preguntas: cuarto banco de la ocupación, empatado con el sonido** · **el punto más técnico de la ocupación y el que más se contesta
con cifras exactas.**

<!-- indice -->

## Índice

- [La resolución y las DOS familias del 4K](#la-resolución-y-las-dos-familias-del-4k)
- [Qué es la ultra alta definición](#qué-es-la-ultra-alta-definición)
- [Las cadencias](#las-cadencias)
- [El muestreo cromático y la compresión](#el-muestreo-cromático-y-la-compresión)
- [Contenedor, códec y formatos](#contenedor-códec-y-formatos)
- [El código de tiempo](#el-código-de-tiempo)
- [Soportes, conectores y RAID](#soportes-conectores-y-raid)
- [La emisión: DVB-T2](#la-emisión-dvb-t2)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La resolución y las DOS familias del 4K

- **PREGUNTA 20** · `[of]` · **El tamaño físico de una imagen medido en píxeles se llama RESOLUCIÓN.**

| Familia | Resolución | Relación | Dónde |
|---|---|---|---|
| **4K UHDV** —**pregunta 7**— | **3.840 × 2.160** | **16:9** | **Televisión**: es cuatro veces el HD |
| **4K Cinema (DCI)** —**pregunta 51**— | **4.096 × 2.160** | **17:9** | **Cine de sala** |

- **CÓMO NO CONFUNDIRLAS, Y ES LA CLAVE DE LAS DOS PREGUNTAS**: **la altura es LA MISMA —2.160— y lo
  que cambia es la anchura.** **La de televisión es más estrecha porque conserva el 16:9 de siempre.**
- **EL DATO QUE LO FIJA**: **3.840 = 1.920 × 2.** **El 4K de televisión es exactamente el doble del HD
  en cada lado.**

## Qué es la ultra alta definición

- **PREGUNTA 87** · `[of]` · **La UHD se basa en AUMENTAR LA RESOLUCIÓN ESPACIAL, LA RESOLUCIÓN
  TEMPORAL, EL RANGO DINÁMICO, LA CUANTIFICACIÓN Y EL ESPACIO DE COLOR.**
- **LOS CINCO EJES, Y NINGUNO SOBRA**: **más píxeles** · **más cuadros por segundo** · **más contraste**
  · **más bits** · **más colores.** **La UHD NO es sólo resolución**, y **ésa es exactamente la trampa
  de las opciones falsas.**

## Las cadencias

- **PREGUNTA 8** · `[of]` · **La cadencia del sistema NTSC es 29,97 fps.**
- **DE DÓNDE SALE EL DECIMAL**: **el NTSC en blanco y negro iba a 30**; **al añadir el color hubo que
  bajar un 0,1 % para que la subportadora de croma no interfiriera con el audio.** **PAL se quedó en 25
  exactos porque adoptó el color con otra solución.**

## El muestreo cromático y la compresión

- **PREGUNTA 48** · `[of]` · **El patrón en el que NO hay submuestreo de crominancia es 4:4:4.**
- **CÓMO SE LEE UN PATRÓN**: **el primer número es la luminancia y los otros dos, las diferencias de
  color.** **Si los tres son iguales, no se ha tirado nada.**
- **PREGUNTA 54** · `[of]` · **En la DCT, la recuantificación supone que LOS COEFICIENTES SE
  RECUANTIFICAN INDIVIDUALMENTE**, de manera que **se puede desechar información de altas frecuencias**
  manteniendo la fundamental.
- **LA IDEA EN UNA FRASE**: **la transformada no comprime; separa.** **Lo que comprime es tirar los
  coeficientes de alta frecuencia, que son los que el ojo menos nota.**

## Contenedor, códec y formatos

| Pregunta | Término | Qué es |
|---|---|---|
| **108** | **MXF** | **Un tipo de ARCHIVO CONTENEDOR** |
| **1** | **WAV** | **El único de la lista que contiene SÓLO AUDIO** |
| **31** | **MOV** | **El desarrollado por APPLE**: QuickTime Movie |
| **105** | ***Proxy*** | **Copia de MENOR resolución, muy comprimida, CON código de tiempo y metadatos básicos** |

- **LA DISTINCIÓN QUE ORDENA LA TABLA**: **un contenedor es la caja; un códec es cómo se ha comprimido
  lo de dentro.** **MXF, MOV, AVI y MKV son cajas; H.264 y ProRes son códecs.**
- **LA PALABRA QUE DECIDE EN LA 105 ES «INCLUYE CÓDIGO DE TIEMPO»**: **sin él, el montaje en baja
  resolución no se puede reconformar sobre el original.**

## El código de tiempo

- **PREGUNTA 100** · `[of]` · **Una palabra de LTC ocupa 80 BITS por fotograma.**
- **PREGUNTA 75** · `[of]` · **En una realización con CuePilot, el código de tiempo longitudinal procede
  normalmente DEL DEPARTAMENTO DE AUDIO.**
- **POR QUÉ DEL AUDIO**: **el LTC es una SEÑAL SONORA**: se graba en una pista de audio y se distribuye
  como audio. **Quien tiene la matriz de audio tiene el reparto del código.**
- **PREGUNTA 4** · `[of]` · **De 00:47:17:23 a 01:23:54:00 hay 36' 36'' 03 cuadros.**
- **CÓMO SE HACE LA RESTA**: **de derecha a izquierda, con acarreo, y el acarreo NO es de diez ni de
  sesenta en el campo de cuadros: es de 25.** **Ése es el error que las opciones falsas explotan.**

## Soportes, conectores y RAID

- **PREGUNTA 53** · `[of]` · **El que NO es soporte de grabación es la TARJETA SWS.** **SXS, XDCAM y P2
  existen; SWS es inventada.**
- **PREGUNTA 93** · `[plan]` · **El conector de la imagen es BNC.** **Depende de una fotografía.**
  **Regla de familia**: **BNC = cilíndrico con bayoneta de giro, vídeo SDI** · **Canon/XLR = tres patas,
  audio** · **jack = cilíndrico liso, audio de consumo** · **VGA = trapecio de quince patillas.**
- **PREGUNTA 104** · `[of]` · **El mínimo para un RAID 1 son 2 DISCOS.**
- **LA REGLA**: **RAID 1 es espejo, y un espejo necesita dos.** **RAID 0 también necesita dos; RAID 5
  necesita tres.**

## La emisión: DVB-T2

- **PREGUNTA 35** · `[plan]` · **Permite UN MEJOR USO DEL ESPECTRO, con entre un 30 y un 50 % EXTRA DE
  ANCHO DE BANDA**, y con ello más canales en HD y transmisiones en UHD.
- **⚠ OJO**: **esta misma respuesta aparece como OPCIÓN FALSA de la pregunta 63 del tema 17**, la de
  Dolby Atmos. **El cuadernillo usa el acierto de una pregunta como trampa de otra.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 1 | Qué formato contiene sólo audio | c) WAV ✔ |
| 4 | Duración entre dos códigos de tiempo | c) 36' 36'' 03 ✔ |
| 7 | Estándar 4K UHDV 16:9 | c) 3.840 × 2.160 ✔ |
| 8 | Cadencia del sistema NTSC | c) 29,97 ✔ |
| 20 | Cómo se llama el tamaño en píxeles | d) Resolución ✔ |
| 31 | Qué archivo desarrolló Apple | c) MOV ✔ |
| 35 | Qué permitirá el DVB-T2 | a) 30-50 % extra de ancho de banda ✔ **·** sólo con la plantilla |
| 48 | En qué patrón NO hay submuestreo | d) 4:4:4 ✔ |
| 51 | Estándar 4K Cinema 17:9 | a) 4.096 × 2.160 ✔ |
| 53 | Cuál NO es soporte de grabación | c) Tarjeta SWS ✔ |
| 54 | Recuantificación de coeficientes en DCT | d) Individualmente, desechando altas frecuencias ✔ |
| 75 | De dónde procede el LTC | b) Del departamento de audio ✔ |
| 87 | En qué se basa la UHD | d) Los cinco ejes ✔ |
| 93 | Qué conector identificas en la imagen | c) BNC ✔ **·** sólo con la plantilla |
| 100 | Bits de una palabra LTC por fotograma | a) 80 ✔ |
| 104 | Mínimo de discos para RAID 1 | b) 2 ✔ |
| 105 | Qué es un *proxy* de vídeo | a) Copia de menor resolución con código de tiempo ✔ |
| 108 | Qué es MXF | a) Un archivo contenedor ✔ |

**Las dieciocho oficiales son correctas y DOS descansan sólo en la plantilla.** · **Aviso de estudio**:
**dieciséis de las dieciocho se contestan con cifras o con definiciones cerradas.** **Es el punto que
más premia la ficha de repaso.**
