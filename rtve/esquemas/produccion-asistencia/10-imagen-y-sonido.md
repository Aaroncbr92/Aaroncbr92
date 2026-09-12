# Esquema · Tema 10 del específico de Producción (Asistencia) · Imagen y sonido

**Siglas**: el Comité Consultivo Internacional de Radiocomunicaciones (**CCIR**), de cuya norma 601
se habla; la elevada gama dinámica (**HDR**, *high dynamic range*); el híbrido log-gamma (**HLG**);
la cuantización perceptiva (**PQ**); y el conector de audio de tres contactos (**XLR**).

Telegrama. **Cada línea lleva delante de dónde sale**: `[601]` = Recomendación UIT-R BT.601-7
(03/2011) · `[2100]` = Recomendación UIT-R BT.2100-1 (06/2017) · `[BOE]` = norma española ·
`[AES]` = documentación de la Audio Engineering Society · `[fís]` = física demostrable ·
`[uso]` = uso profesional y plantilla oficial, **sin norma leída**.

**Siglas**: la interfaz digital de audio multicanal (**MADI**).

**Cabecera.** Enunciado **sin norma**: «IMAGEN Y SONIDO: Captación y tratamiento» · **17
preguntas**, la **segunda materia más preguntada** del bloque específico · **7 con norma detrás**,
10 con la plantilla.

<!-- indice -->

## Índice

- [Óptica de la captación](#óptica-de-la-captación)
- [Luminancia y crominancia](#luminancia-y-crominancia)
- [Cuadro 3 de la BT.601-7 · relación 4:2:2](#cuadro-3-de-la-bt601-7--relación-422)
- [Elevada gama dinámica · BT.2100-1](#elevada-gama-dinámica--bt2100-1)
- [Medida de la señal de vídeo](#medida-de-la-señal-de-vídeo)
- [El sonido: la onda](#el-sonido-la-onda)
- [El micrófono](#el-micrófono)
- [Digitalización](#digitalización)
- [Retorno al reportero](#retorno-al-reportero)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Óptica de la captación

- `[fís]` · **Distancia focal**: distancia del centro óptico al plano de imagen enfocada al
  infinito, en **mm** · manda el **ángulo de visión**.
- `[fís]` · **Profundidad de campo**: zona nítida por delante y por detrás del punto enfocado ·
  **a más focal, MENOS profundidad** · a más número f (más cerrado), más · a más distancia al
  sujeto, más.
- `[fís]` · **Cualidades de la luz**: **reflexión** rebota · **absorción** retiene · **refracción**
  desvía al cambiar de medio · **TRANSMISIÓN** atraviesa un cuerpo no opaco y sale, difusa o
  directamente.

## Luminancia y crominancia

- `[601]` · **Punto 1.2**: la codificación digital se basa en **una señal de luminancia y dos de
  diferencia de color**.
- `[601]` · **LUMINANCIA (Y) = la señal en blanco y negro**. **Crominancia** = la información de
  color, en **diferencias** respecto de Y.
- `[601]` · **E'Y = 0,299 E'R + 0,587 E'G + 0,114 E'B** · diferencias: **E'R − E'Y** y
  **E'B − E'Y** · el **verde pesa más de la mitad**.
- `[2100]` · En elevada gama dinámica los coeficientes **cambian**: **Y' = 0,2627 R' + 0,6780 G' +
  0,0593 B'** · dependen de **los primarios del sistema**.
- `[601]` · **Submuestreo**: **4:4:4** sin submuestreo · **4:2:2** por cada **cuatro** muestras de
  luminancia, **dos de la diferencia de color rojo y dos de la azul**, reducción **horizontal** ·
  **4:2:0** también **vertical**, alternando líneas.
- **Aviso**: la **«norma CCIR 601»** del examen es hoy la **Recomendación UIT-R BT.601**, versión
  **-7 (03/2011)**. La CCIR es la **antecesora del UIT-R**.

## Cuadro 3 de la BT.601-7 · relación 4:2:2

- `[601]` · Muestras por **línea completa**, luminancia / cada diferencia de color: **858 / 429**
  (525 líneas) · **864 / 432** (625 líneas).
- `[601]` · Muestras por **línea activa digital**: **720 / 360**. **Ahí está el 4:2:2 contado.**
- `[601]` · **Estructura de muestreo: ORTOGONAL**, repetitiva en cada línea, trama e imagen · C'R
  y C'B **coinciden con las muestras impares** de Y.
- `[601]` · **Frecuencia de muestreo: 13,5 MHz** (luminancia) / **6,75 MHz** (cada diferencia de
  color). **La mitad exacta.** Los **13,5 MHz sirven para 4:3 y para 16:9**.
- `[601]` · **Codificación MIC**, cuantificación uniforme, **8 o 10 bits** · **negro en 16**,
  **blanco de cresta en 235**.
- `[601]` · **Punto 1.3**: filtros para **evitar el solape** de espectros (*antialiasing*).

## Elevada gama dinámica · BT.2100-1

- `[2100]` · Regula los parámetros de imagen de la televisión de **elevada gama dinámica** para
  producción e intercambio internacional.
- `[2100]` · **HDR = más contraste**: negros más profundos y **altas luces mucho más brillantes**.
- `[2100]` · **Dos métodos**: **PQ**, cuantización perceptiva · **HLG**, híbrido log-gamma.
- `[2100]` · **Cuadro 1**: contenedor **16:9** · píxeles **7 680 × 4 320**, **3 840 × 2 160**,
  **1 920 × 1 080** · **muestreo reticular ORTOGONAL** · píxeles **cuadrados 1:1** · orden de
  izquierda a derecha y de arriba abajo · tramas **120, 100, 60, 50, 30, 25, 24** y sus variantes
  /1,001 · **progresiva**.
- **El muestreo ortogonal NO es novedad del HDR**: ya venía de la BT.601.

## Medida de la señal de vídeo

- `[uso]` · **Monitor de forma de onda** → **LUMINANCIA**: niveles de negro y blanco, contraste,
  fuera de rango.
- `[uso]` · **VECTORSCOPIO** → **CROMINANCIA**: **tono** (ángulo) y **saturación** (distancia al
  centro) · equilibra cámaras · verifica barras.
- **Trampa**: *colorburst* y *salva de color* **son lo mismo** —la ráfaga de sincronismo— y **no
  son un instrumento**.

## El sonido: la onda

- `[fís]` · **Frecuencia** (Hz) → **tono**: a más frecuencia, **más agudo**. **Longitud de onda**
  → **inversa** de la frecuencia. **Amplitud** → **volumen**, no tono.
- `[fís]` · **Tono más GRAVE = longitud de onda LARGA**.
- `[uso]` · **TRÉMOLO**: varía la **intensidad**, la **frecuencia se mantiene**. **VIBRATO**:
  varía la **frecuencia**. No confundirlos.
- `[uso]` · Rebote del sonido: el **fenómeno físico es la REFLEXIÓN**; el examen da por buena
  **ECO** · **eco** = repetición **separada**; **reverberación** = reflexiones **tan seguidas** que
  forman una cola.
- `[BOE]` · **DB-HR del CTE (RD 1371/2007), anejo de terminología**: «**Tiempo de reverberación,
  T**: tiempo, en s, necesario para que el nivel de presión sonora **disminuya 60 dB** después del
  cese de la fuente» · **depende de la frecuencia** · los límites se miden como **media de 500,
  1000 y 2000 Hz** · de ahí el nombre **RT60**.
- **Dos avisos**: el DB-HR regula **edificios, no platós** —de aquí sale **la definición**, no una
  exigencia— · es el **texto de 2007**; revisadas sus dos modificaciones (**RD 1675/2008** y
  **Orden VIV/984/2009**), **ninguna toca esta definición**.

## El micrófono

- `[uso]` · **Por transductor**: **DINÁMICO** —bobina móvil, **robusto y versátil**, sin
  alimentación— · **CONDENSADOR** —más sensible, **necesita alimentación**, delicado— · **CINTA**
  —cálido, **muy frágil**—.
- `[uso]` · **Por patrón polar**: **OMNIDIRECCIONAL, 360º**, sin zona muerta · **BIDIRECCIONAL**
  (figura de ocho), **frente y espalda en la misma proporción**, rechaza laterales ·
  **CARDIOIDE**, frente, rechaza la espalda · **HIPERCARDIOIDE**, más directivo, **lóbulo trasero
  pequeño** · **CAÑÓN**, tubo de interferencia.
- **Trampa**: el hipercardioide **sí** tiene lóbulo trasero, pero **no del mismo tamaño**; el de
  la misma proporción es el **bidireccional**.
- `[BOE]` · **Impedancia** = oposición al paso de la corriente alterna · se mide en **OHMIOS (Ω)**,
  unidad de **resistencia eléctrica**, **V/A**, según el **RD 2032/2009** de unidades legales de
  medida, que además avala la grafía «ohmio».
- `[uso]` · Los micrófonos **profesionales son de BAJA impedancia** → **tiradas largas** de cable
  sin pérdida, **balanceado con conector XLR** de tres contactos.

## Digitalización

- `[fís]` · **Teorema de muestreo** (Nyquist-Shannon): la frecuencia de muestreo ha de ser **como
  mínimo EL DOBLE de la frecuencia MÁXIMA** de la señal · si no, **aliasing**, y por eso el filtro
  paso bajo delante.
- `[601]` · Aplicado: **13,5 MHz** para la luminancia y **6,75 MHz** para cada diferencia de
  color. **El tema no da la frecuencia de muestreo de audio**: no está en ninguna fuente leída.
- `[601]` · **Cuantificación**: **8 o 10 bits** por muestra · pocos bits → **ruido de
  cuantificación**.
- `[AES]` · **AES3** → audio digital de **dos canales**; comercialmente **AES/EBU**, y en versión
  no balanceada **S/PDIF**. **AES10 = MADI** → **audio digital MULTICANAL**, por **coaxial** o
  **fibra óptica**.
- **La AES10 NO se ha leído** (muro de pago): se afirma **qué es**, nada de su contenido.

## Retorno al reportero

- `[uso]` · **N-1** = el programa **menos la propia aportación** del reportero, para que no se
  oiga a sí mismo con retardo · se le manda **audio y vídeo del programa**.
- **No confundir con**: **señal internacional** —programa sin locución, para doblar—, **copia
  estándar** de un negativo, y **señal limpia** sin rótulos.

## Lo que se ha preguntado

- `[fís]` **más focal → menos profundidad de campo** · **transmisión** de la luz · **longitud de
  onda larga → grave** · **muestreo al doble de la máxima**.
- `[601]` **luminancia = blanco y negro** · **4:2:2 = dos de rojo y dos de azul por cada cuatro
  de luminancia**.
- `[2100]` **muestreo reticular ortogonal**.
- `[BOE]` **60 dB** de caída para el tiempo de reverberación · la impedancia en **ohmios**.
- `[AES]` **MADI es un estándar de la AES**, multicanal.
- `[uso]` **eco** · **trémolo** · **bidireccional** · **omnidireccional 360º** · **dinámico** ·
  **vectorscopio** y **crominancia** · **N-1**.
