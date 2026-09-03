# Esquema · Tema 4 del específico de Edición, Montaje y Procesos Audiovisuales · Tratamiento digital de la señal de televisión

Telegrama. **Cada línea lleva delante de dónde sale**: `[2020]` = Recomendación UIT-R BT.2020-2 ·
`[709]` = Recomendación UIT-R BT.709-6 · `[of]` = oficio · `[plan]` = plantilla oficial, **sin fuente
por encima que la contraste**.

**Cabecera.** Enunciado: «2. Tratamiento digital de la señal de televisión · 2.1. Normas de
codificación, compresión y soporte · 2.3. Codificadores y sistemas de compresión» · **15 preguntas:
EL BANCO MÁS GRANDE DE ESTA OCUPACIÓN** · **dos descansan sólo en la plantilla (6 y 67)**.

<!-- indice -->

## Índice

- [Resoluciones y aspecto](#resoluciones-y-aspecto)
- [La profundidad de bits en UHD](#la-profundidad-de-bits-en-uhd)
- [El muestreo cromático](#el-muestreo-cromático)
- [Progresivo y entrelazado](#progresivo-y-entrelazado)
- [UIT y SMPTE](#uit-y-smpte)
- [Compuesto, componentes y digital](#compuesto-componentes-y-digital)
- [El jitter](#el-jitter)
- [Intracuadro e intercuadro](#intracuadro-e-intercuadro)
- [Los códecs y sus autores](#los-códecs-y-sus-autores)
- [DF y NDF](#df-y-ndf)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Resoluciones y aspecto

| Formato | Píxeles | Aspecto |
|---|---|---|
| **Definición estándar** | 720 × 576 | 4:3 o 16:9 |
| **HD** | 1.280 × 720 | 16:9 |
| **Full HD** | 1.920 × 1.080 | 16:9 |
| **UHD** (4K de TV) | **3.840 × 2.160** | **16:9** |
| **4K DCI** (cine) | 4.096 × 2.160 | 1,90:1 |
| **8K** | **7.680 × 4.320** | **16:9** |

- **PREGUNTA 46** · `[2020]` · **8K en 16:9 = 7.680 horizontales × 4.320 verticales.** El **Cuadro 1**
  lo recoge junto a 3.840 × 2.160, con formato **«16:9»**.
- **LAS FALSAS**: 4.320 × 7.680 = **los números INVERTIDOS** (imagen vertical) · 3.840 × 2.160 = **es
  UHD** · 4.096 × 2.160 = **es el 4K DE CINE, y no es 16:9**.
- **PREGUNTA 65** · **La relación de aspecto en UHD es 16:9**, la misma que HD: **UHD multiplica
  píxeles, no cambia la forma**. Falsas: 21:9 (panorámico), 4:3 (TV antigua), 1,85:1 (proyección).
- **LA CONFUSIÓN QUE HAY QUE DESHACER**: **«4K» NO ES UNA SOLA COSA.** **UHD = 3.840 × 2.160 y es
  16:9; DCI = 4.096 × 2.160 y NO es 16:9.** El examen usa las dos.

## La profundidad de bits en UHD

- **PREGUNTA 6** · `[plan]` · **La profundidad de la fase 1 de UHD en 3.840 × 2.160 es 10 BITS.**
- **LO QUE LA NORMA DICE**: `[2020]` · el **Cuadro 5** fija como formato de codificación **«10 ó 12
  bits por componente»**. **Los dos valen.**
- **LO QUE LA NORMA NO DICE**: **«fase 1» NO es un concepto de la Recomendación**: es una fase de
  despliegue de los organismos de radiodifusión, **que eligió 10 bits** de los dos permitidos. **Esa
  documentación no se ha consultado.**
- **LAS FALSAS**: **12 bits** = la otra que la norma admite, y la de la fase 2 y del cine · **14 bits**
  = **no aparece en ninguna** · **8 bits** = definición estándar y alta definición de consumo.
- **POR QUÉ IMPORTA**: **a 8 bits un cielo o un fundido se rompen en franjas**, y con la mayor
  luminancia del UHD se vería más. **Diez bits es el mínimo con el que un degradado aguanta.**

## El muestreo cromático

| Notación | Qué guarda | Dónde |
|---|---|---|
| **4:4:4** | **Una muestra de color por píxel** | Grafismo, croma, cine |
| **4:2:2** | **La mitad en horizontal** | **El estándar de producción** |
| **4:2:0** | **La mitad en horizontal Y en vertical** | Emisión y distribución |
| **4:1:1** | Una cuarta parte en horizontal | Formatos antiguos |

- **PREGUNTA 18** · **4:4:4:4 = señal RGB SIN submuestreo MÁS información del CANAL ALFA.**
- **QUÉ ES EL ALFA**: **un cuarto canal que dice, píxel a píxel, cuánto de opaco es.** **No lleva
  color: lleva transparencia.**
- **LAS TRES FALSAS SON LA MISMA FRASE CON EL FINAL CAMBIADO**: «sin submuestreo» a secas = **eso es
  4:4:4, tres cifras** · «más metadatos» = **los metadatos van en la cabecera, no en un canal** · «con
  submuestreo» = **contradice la notación**.
- **LA REGLA**: **la cuarta cifra es SIEMPRE el canal alfa**, y sólo puede ser 4 (alfa completo) o 0.

## Progresivo y entrelazado

- **PROGRESIVO** = cada imagen entera, línea a línea · **ENTRELAZADO** = dos pasadas, impares y pares.
  **Cada pasada es un campo; dos campos, un cuadro.**
- **PREGUNTA 69** · **En PAL el entrelazado es necesario PARA EVITAR EL PARPADEO.**
- **EL RAZONAMIENTO, EN TRES PASOS**: con 25 imágenes completas **el movimiento va fluido pero la
  pantalla parpadea** · con 50 completas no parpadearía **pero haría falta el doble de banda** · **el
  entrelazado da 50 refrescos con la información de 25 imágenes.**
- **LAS FALSAS**: «llenar la pantalla» → **se llena igual en progresivo** · «dos cañones que se
  entrecruzan» → **un tubo en color tiene TRES cañones, no dos, y el entrelazado no depende de eso** ·
  «ya no se usa en PAL» → **PAL es entrelazado por definición**.
- **PREGUNTA 43** · **En HD-SDI 1080 50i contamos con 50 IMÁGENES por segundo.**
- **CÓMO SE LEE LA NOTACIÓN**: **«1080» = líneas activas · «50» = CAMPOS por segundo · «i» =
  entrelazado.** **50 campos = 25 cuadros**, y **cada campo llega a la pantalla**.
- **POR QUÉ LA OPCIÓN «50 *FRAMES*» ES LA FALSA MEJOR CONSTRUIDA**: **50i NO son 50 cuadros.** Si lo
  fueran, la notación sería **1080p50**. **Ésa es la distinción que la pregunta mide.** Las otras dos
  —líneas y píxeles por segundo— **son absurdas por magnitud**.

## UIT y SMPTE

| Familia | Quién | Qué define |
|---|---|---|
| **Recomendaciones UIT-R BT** | La Unión Internacional de Telecomunicaciones | **Los PARÁMETROS de la imagen** |
| **Normas SMPTE** | La sociedad de ingenieros de cine y televisión | **La INTERFAZ y el formato de la señal** |

- **PREGUNTA 91** · **La recomendación de la señal digital en HD es la UIT-R BT.709.**
- **LA CADENA MNEMOTÉCNICA**: **601 estándar · 709 alta · 2020 ultra alta · 2100 alto rango
  dinámico.** Con esas cuatro se contestan la 91, la 7 y medio tema 2.
- **PREGUNTA 67** · `[plan]` · **La norma de la señal HD 1080/50i es SMPTE-274M.**
- **LAS FALSAS**: **ITU-R BT.601-5** = definición estándar · **SMPTE-296M** = **la hermana, pero de
  1280 × 720** · **R91-2004** = una recomendación de la Unión Europea de Radiodifusión, no un formato
  de imagen.
- **LA DISTINCIÓN**: **274M es la de 1080; 296M es la de 720.** **El examen pone las dos juntas.**
- **DECLARACIÓN**: **el texto de las normas SMPTE no se ha consultado** —son de pago—. **La
  atribución descansa en la plantilla y en la literatura corriente.**

## Compuesto, componentes y digital

| Señal | Cómo va |
|---|---|
| **COMPUESTO** | **Luminancia y crominancia MEZCLADAS**, con el color **modulado en AMPLITUD sobre una subportadora** |
| **Componentes** | **Tres señales separadas** en banda base |
| **Digital** | Muestreada, cuantificada, serializada |

- **PREGUNTA 71** · **El que usa modulación de amplitud es el VÍDEO COMPUESTO.**
- **POR QUÉ**: en PAL y NTSC **el color se modula sobre una subportadora que se suma a la
  luminancia**, con **la fase llevando el tono y la amplitud la saturación**.
- **LAS FALSAS**: digital → **hay muestras, no modulación de crominancia** · componentes → **no modula:
  van separadas** · **«señal de vídeo 4K» NO ES UN TIPO DE SEÑAL: ES UNA RESOLUCIÓN.** **Se descarta
  sin saber nada de modulación.**

## El jitter

- **PREGUNTA 44** · ***Jitter* = UNA CADENA DE BITS CON TIEMPOS INESTABLES.**
- **QUÉ ES**: **la variación del instante en que llega cada bit.** **No cambia el valor: cambia
  cuándo.**
- **POR QUÉ IMPORTA**: el receptor **recupera el reloj de la propia señal**; si los flancos no llegan a
  tiempo, **decide mal dónde está cada bit**. **El vídeo digital falla de golpe, y el jitter es una de
  las causas.**
- **LAS FALSAS**: «frecuencia modulada» = **una técnica de transmisión** · «aumento de amplitud» =
  **ganancia** · «ruido aleatorio» = **LA TRAMPA BUENA**: el jitter es ruido, **pero DE FASE, no de
  amplitud**.
- **LA PALABRA QUE RESUELVE ES «TIEMPOS»**: **sólo una opción habla de tiempo.**

## Intracuadro e intercuadro

| Tipo | Qué aprovecha | Consecuencia |
|---|---|---|
| **Espacial / INTRACUADRO** | Redundancia **dentro de cada imagen** | **Cada cuadro se decodifica solo**: corte exacto |
| **Temporal / INTERCUADRO** | Redundancia **entre imágenes sucesivas** | **Hace falta el grupo entero** |

- **PREGUNTA 47** · **El códec que usa compresión temporal es H.265.**
- **LAS TRES FALSAS SON LOS TRES CÓDECS INTRACUADRO DE MONTAJE**: **ProRes**, **DNxHR** y **JPEG
  2000**.
- **Y ÉSA ES LA RAZÓN DE QUE SEAN LOS DE MONTAJE**: **se cortan en cualquier cuadro sin recalcular
  nada.** Pesan más y van más rápido en la sala.
- **LA REGLA DE OFICIO**: **para editar, intracuadro; para distribuir, intercuadro.** Por eso **el
  material de cámara en H.264 o H.265 se transcodifica antes de montar**.

## Los códecs y sus autores

| Códec | Quién | Qué es |
|---|---|---|
| **H.264 / AVC** y **H.265 / HEVC** | **UIT-T y MPEG** | Intercuadro, de distribución |
| **ProRes** | **Apple** | Intracuadro, de montaje |
| **DNxHD / DNxHR** | **AVID** | Intracuadro, de montaje |
| **JPEG 2000** | **El grupo JPEG** | Intracuadro, **el del cine digital** |
| **MPEG-2** | MPEG | Televisión digital de primera generación y DVD |

- **PREGUNTA 27** · **H.265 admite UHD 8K a tasas bajas y ahorra hasta un 50 % respecto a H.264.**
  **Las tres falsas dicen lo CONTRARIO** —que no admite HDR, que tiene peor calidad, que sigue peor el
  movimiento—: **basta saber que es el SUCESOR y no el predecesor.**
- **PREGUNTA 68** · **El códec del cine digital es JPEG 2000.**
- **LAS FALSAS SON UNA LECCIÓN DE VOCABULARIO**: **DPX** = **imagen fija, una por cuadro; NO es códec
  de vídeo** · **MPEG-2** = códec, pero **de televisión y DVD** · **MXF** = **NO ES CÓDEC: ES
  CONTENEDOR**.
- **LA DISTINCIÓN QUE MÁS CASTIGA ESTE CUADERNILLO**: **el códec dice cómo se COMPRIME; el contenedor
  dice cómo se EMPAQUETA.** **MXF, MOV y MP4 son contenedores; H.264, ProRes y JPEG 2000 son códecs.**
- **PREGUNTA 96** · **DNxHD lo desarrolló AVID.** Falsas: **Apple** hizo ProRes, **Blackmagic Design**
  su RAW, **Adobe** formatos de intercambio.

## DF y NDF

| Modalidad | Qué hace | Cuándo |
|---|---|---|
| **NDF** (*non-drop frame*) | **Cuenta TODOS los cuadros** | **Cadencia ENTERA**: 24, 25, 30, 50 |
| **DF** (*drop frame*) | **Se salta NÚMEROS de cuadro** para cuadrar con el reloj | **Cadencia NO entera**: 29,97 o 59,94 |

- **PREGUNTA 84** · **En un sistema de 25 fps se usa NDF.**
- **POR QUÉ**: **25 es entero: veinticinco cuadros son exactamente un segundo y no hay nada que
  corregir.** El *drop frame* nació en el sistema americano, **cuya cadencia real es 29,97 y no 30**:
  contando de treinta en treinta **el código se adelanta unos 3,5 segundos por hora**.
- **EL MALENTENDIDO QUE HAY QUE DESHACER**: **el *drop frame* NO TIRA CUADROS. SALTA NÚMEROS EN LA
  CUENTA.** El material queda intacto; **cambia la etiqueta**.
- **LAS FALSAS**: **DF** = la contraria y **no procede a 25** · **«FD» y «FF»** = **las mismas letras
  invertidas; no son modalidades de nada**.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 6 | Profundidad de bits en la fase 1 de UHD | b) 10 bits ✔ **·** sólo con la plantilla |
| 18 | Qué significa un muestreo 4:4:4:4 | a) RGB sin submuestreo más canal alfa ✔ |
| 27 | Qué es un archivo con códec H.265 | d) UHD 8K y hasta un 50 % de ahorro ✔ |
| 43 | Qué contamos en HD-SDI 1080 50i | d) 50 imágenes por segundo ✔ |
| 44 | Qué significa *jitter* | d) Cadena de bits con tiempos inestables ✔ |
| 46 | Resolución espacial de 8K en 16:9 | d) 7.680 × 4.320 ✔ |
| 47 | Qué códec usa compresión temporal | a) H.265 ✔ |
| 65 | Relación de aspecto en UHD | a) 16:9 ✔ |
| 67 | Norma de HD 1080/50i | b) SMPTE-274M ✔ **·** sólo con la plantilla |
| 68 | Códec del cine digital | d) JPEG 2000 ✔ |
| 69 | Por qué el entrelazado en PAL | d) Para evitar el parpadeo ✔ |
| 71 | Señal que usa modulación de amplitud | c) Vídeo compuesto ✔ |
| 84 | Código de tiempo a 25 fps | a) NDF ✔ |
| 91 | Recomendación de la señal digital en HD | a) UIT-R BT.709 ✔ |
| 96 | Quién desarrolló DNxHD | b) Avid ✔ |

**Las quince oficiales son correctas** y **dos descansan sólo en la plantilla**. · **Aviso de
reparto**: **quince de noventa y seis: es el mayor banco de la ocupación.** · **Aviso de estudio**:
**la 43 mide una sola distinción** —50i son cincuenta CAMPOS y veinticinco cuadros—, y **la 68 mete un
CONTENEDOR entre los códecs**: quien no distinga MXF de JPEG 2000 tiene dos opciones plausibles en
lugar de una.
