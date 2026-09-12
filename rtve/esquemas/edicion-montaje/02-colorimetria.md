# Esquema · Tema 2 del específico de Edición, Montaje y Procesos Audiovisuales · Colorimetría y el color en televisión

**Siglas**: la Unión Internacional de Telecomunicaciones (**UIT**).

Telegrama. **Cada línea lleva delante de dónde sale**: `[709]` = Recomendación UIT-R BT.709-6 ·
`[2020]` = Recomendación UIT-R BT.2020-2 · `[2100]` = Recomendación UIT-R BT.2100-1 · `[of]` =
oficio, sin norma detrás.

**Siglas**: la Comisión Internacional de la Iluminación (**CIE**); el alto rango
dinámico (**HDR**, *high dynamic range*), con su curva híbrida logarítmica-gamma (**HLG**, *hybrid
log-gamma*), y el rango dinámico estándar (**SDR**); la luminancia constante (**CL**, *constant
luminance*) y la no constante (**NCL**, que el examen escribe **NFL**); los tres primarios rojo,
verde y azul (**RGB**); la Unión Internacional de Telecomunicaciones (**UIT**), cuyo sector de
radiocomunicaciones (**UIT-R**) publica las recomendaciones **BT.709**, **BT.2020** y **BT.2100**;
la Unión Internacional de Telecomunicaciones (**UIT**).

**Cabecera.** Enunciado: «1.3. Conceptos básicos de colorimetría» · **10 preguntas de UN SOLO
SUBPUNTO** · **el anexo le dedica una frase y el examen diez preguntas** · **ninguna descansa sólo en
la plantilla**.

<!-- indice -->

## Índice

- [Las leyes de Grassmann](#las-leyes-de-grassmann)
- [Colores no espectrales](#colores-no-espectrales)
- [La luminancia y sus coeficientes](#la-luminancia-y-sus-coeficientes)
- [Luma constante y no constante](#luma-constante-y-no-constante)
- [La gamma logarítmica](#la-gamma-logarítmica)
- [Bits y banding](#bits-y-banding)
- [HDR y el nit](#hdr-y-el-nit)
- [Las LUT](#las-lut)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las leyes de Grassmann

- **EL PUNTO DE PARTIDA**: **el ojo tiene TRES tipos de conos**, así que **bastan TRES estímulos para
  reproducir cualquier color percibido**. Eso es **la síntesis aditiva**.
- **PREGUNTA 10** · El enunciado de la síntesis aditiva con tres franjas independientes es **LA
  PRIMERA LEY DE GRASSMANN**.

| Ley | Qué dice |
|---|---|
| **Primera** | **Tres estímulos INDEPENDIENTES** —ninguno obtenible de los otros dos— |
| **Segunda** | Un color se sustituye por su mezcla equivalente |
| **Tercera** | La suma de dos mezclas equivalentes sigue siendo equivalente |
| **Cuarta** | La intensidad de la mezcla es la suma de las intensidades |

- **LA PALABRA QUE IDENTIFICA LA PRIMERA**: **«independientes»**, o su formulación —**«que ninguno se
  obtenga por mezcla de los otros dos»**—. **Quien lea esa cláusula no necesita las otras tres.**

## Colores no espectrales

- **ESPECTRAL** = corresponde a **UNA sola longitud de onda** (los del prisma) · **NO ESPECTRAL** = **no
  corresponde a ninguna**: sólo se percibe **mezclando los dos extremos del espectro**.
- **PREGUNTA 83** · **Los no espectrales son EL PÚRPURA Y EL MAGENTA.**
- **POR QUÉ**: en el diagrama de la CIE **los espectrales forman la herradura** y los púrpuras y
  magentas están **en la recta que cierra sus dos extremos**: **la «línea de los púrpuras»**.
- **LAS FALSAS MEZCLAN**: azul y verde → **los dos espectrales** · magenta y verde → **el verde no** ·
  púrpura y azul → **el azul no**.
- **LA CONSECUENCIA**: **el magenta NO aparece en el arcoíris.** Es una mezcla que el cerebro
  construye.

## La luminancia y sus coeficientes

- **POR QUÉ NO SE TRANSMITE RGB**: el ojo distingue **mucho mejor el brillo que el color**, así que se
  manda **luminancia + dos diferencias de color** y **se ahorra banda en el color sin que se note**.
- **PREGUNTA 7** · `[709]` · **Y = 0,2126 R + 0,7152 G + 0,0722 B.** Está en el **Cuadro 1, apartado
  3.2, «Determinación de la señal de luminancia»**.

| Recomendación | Para qué | R | G | B |
|---|---|---|---|---|
| **BT.601** | Definición estándar | 0,299 | 0,587 | 0,114 |
| **BT.709** | **Alta definición** | **0,2126** | **0,7152** | **0,0722** |
| **BT.2020** | Ultra alta definición | 0,2627 | 0,6780 | 0,0593 |

- **EL DISTRACTOR MEJOR CONSTRUIDO**: la opción b) **son los coeficientes VERDADEROS de la BT.2020**.
  **Es la respuesta correcta a otra pregunta.**
- **LAS OTRAS DOS SON DEFORMACIONES**: 0,279/0,587/0,134 = **la BT.601 con dos cifras cambiadas** ·
  0,2637/0,6790/0,0593 = **la BT.2020 con dos dígitos movidos**.
- **EL VERDE APORTA LA MAYOR PARTE DEL BRILLO Y EL AZUL LA MENOR**, en las tres recomendaciones.

## Luma constante y no constante

- **PREGUNTA 5** · **La luma CONSTANTE procesa Y a partir del RGB ANTES de la corrección de gamma; la
  NO constante, DESPUÉS.**

| Sistema | Orden |
|---|---|
| **Constante (CL)** | **Y primero** (RGB lineal), **gamma después** |
| **No constante (NCL)** | **Gamma primero**, **Y' después** |

- **POR QUÉ EXISTEN LAS DOS**: **la constante es la correcta colorimétricamente** —Y contiene toda la
  luminancia—; **la no constante es la que se usa**, porque **la heredó toda la cadena de
  radiodifusión y cambiarla obligaría a cambiarlo todo**.
- **EL DEFECTO DE LA NO CONSTANTE**: **parte de la luminancia se cuela por los canales de color**, y al
  submuestrearlos (4:2:2, 4:2:0) **se pierde brillo en los colores muy saturados**.
- `[2020]` · La Recomendación ofrece **las dos**: la constante «cuando lo más importante es la
  retención exacta de la información de luminancia»; la no constante «cuando lo más importante es
  utilizar las mismas prácticas operativas».
- **CÓMO SE CONTESTA**: **dos de las cuatro opciones hablan de RASTERIZACIÓN**, que **no es una etapa
  de la codificación de color**: **se descartan sin más**. De las dos que quedan, **la buena pone la
  constante ANTES**.
- **AVISO DE GRAFÍA**: **el examen escribe «NFL» donde la literatura escribe «NCL»** (*non-constant
  luminance*).

## La gamma logarítmica

- `[709]` · **La precorrección no lineal va con exponente 0,45**, que es aproximadamente **la inversa
  de 2,2**. De ahí sale la gamma de 2,2.
- **PREGUNTA 72** · **Un plano con curva logarítmica GENERA UNA IMAGEN MÁS LAVADA QUE NECESITA
  CORRECCIÓN DE COLOR POSTERIOR.**
- **POR QUÉ SALE LAVADA**: **reparte los valores por TODO el rango dinámico del sensor** en lugar de
  concentrarlos donde quedarían bien a la vista → **bajo contraste y baja saturación**, **pero conserva
  altas luces y sombras**. **Es material de trabajo, no imagen final.**
- **LAS TRES FALSAS**: «recoge directamente lo del sensor» → **eso es el RAW** · «contraste adecuado
  para la visualización final» → **lo contrario** · «menor rango dinámico y *look* definitivo» → **las
  dos mitades falsas**.

## Bits y banding

- **8 bits = 256 niveles · 10 bits = 1.024 · 12 bits = 4.096**, por canal.
- **PREGUNTA 94** · **La ventaja de 10 bits sobre 8: MAYOR RANGO DINÁMICO Y GRADACIÓN DE COLOR MÁS
  SUAVE.**
- **LAS TRES FALSAS SE CAEN CON UNA FRASE**: **más bits NUNCA es menos peso.** «Menor tamaño» →
  contrario · «más cuadros por segundo» → **nada que ver** · «mejor compatibilidad con antiguos» →
  **los antiguos son de 8 bits**.
- **PREGUNTA 13** · **El *color banding* se produce POR UNA ESCASA PROFUNDIDAD DE COLOR.**
- **QUÉ ES**: **cuando un degradado suave no tiene niveles suficientes, se rompe en franjas
  visibles.** **Faltan escalones.**
- **LA DISTINCIÓN QUE RESUELVE LA PREGUNTA**: **resolución espacial = cuántos píxeles hay ·
  profundidad de color = cuántos valores puede tomar cada uno.** **El *banding* es de la segunda.**

## HDR y el nit

- **HDR NO ES MÁS RESOLUCIÓN: ES MÁS RECORRIDO DE BRILLO**, y con él más detalle en luces y sombras a
  la vez.
- **PREGUNTA 66** · **La unidad del brillo de una pantalla HDR es el NIT.**

| Unidad | Qué mide |
|---|---|
| ***Nit*** | **Luminancia: UNA CANDELA POR METRO CUADRADO** |
| **Candela** | **Intensidad luminosa**: no incluye superficie |
| **Candela / cm²** | Luminancia **en otra escala**: 1 cd/cm² = 10.000 nits |
| **Lumen** | **Flujo luminoso** total |

- `[2100]` · **Las cifras de referencia**: monitor de **≥ 1.000 cd/m²** de pico y **≤ 0,005 cd/m²** de
  negro. **Una pantalla SDR trabaja alrededor de 100 nits.**
- **PREGUNTA 50** · **Para etalonar en HDR un máster HDR se necesita un monitor con *HIGH* Dynamic
  Range.** **No se puede juzgar lo que no se ve.**
- **LAS TRES FALSAS**: «*Hybrid* Dynamic Range» → **NO EXISTE**; *hybrid* es de **HLG**, *hybrid
  log-gamma*, **que es una curva y no un tipo de monitor** · «el HDR sólo afecta a la grabación» →
  **afecta a toda la cadena, y al etalonaje el que más** · «monitor SDR con espacio BT.2020» →
  **confunde GAMA DE COLOR con RANGO DINÁMICO**.
- **LA DISTINCIÓN QUE LA ÚLTIMA PONE A PRUEBA**: **gama y rango dinámico son DOS EJES DISTINTOS.**

## Las LUT

- **PREGUNTA 40** · **Las LUT son TABLAS DE CONSULTA PARA TRANSFORMAR EL COLOR DE UNA IMAGEN.**
- **CÓMO FUNCIONAN**: **para cada RGB de entrada, la tabla da un RGB de salida.** **No calcula:
  consulta.** De ahí *look-up table*.
- **TÉCNICA** (traduce entre espacios: de log a Rec. 709) frente a **CREATIVA** (aplica un *look*) ·
  **1D** (curvas por canal) frente a **3D** (tono y saturación).
- **LAS TRES FALSAS LA LLEVAN A OTRO SITIO**: «ajustar la exposición» → **el diafragma o la ganancia**
  · «filtros de sonido» → nada que ver · «un tipo de lente» → vocabulario óptico.
- **AVISO DE OFICIO**: **una LUT NO corrige un plano mal expuesto.** Se aplica **después** de ajustar
  exposición y balance: sobre material mal expuesto **exagera el error**.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 5 | Luma constante frente a no constante | c) La constante procesa Y antes de la gamma ✔ |
| 7 | Luminancia en la Rec. UIT-R BT.709 | a) 0,2126 R + 0,7152 G + 0,0722 B ✔ |
| 10 | A qué ley corresponde la síntesis aditiva | a) Primera ley de Grassmann ✔ |
| 13 | Por qué se produce el *color banding* | d) Escasa profundidad de color ✔ |
| 40 | Qué son las LUT | c) Tablas de consulta para transformar el color ✔ |
| 50 | Monitor para etalonar en HDR | b) Con *High Dynamic Range* ✔ |
| 66 | Unidad del brillo de una pantalla HDR | a) *Nit* ✔ |
| 72 | Qué genera una curva logarítmica | b) Imagen más lavada, con corrección posterior ✔ |
| 83 | Colores no espectrales | c) El púrpura y el magenta ✔ |
| 94 | Ventaja de 10 bits frente a 8 | b) Mayor rango dinámico y gradación más suave ✔ |

**Las diez oficiales son correctas y ninguna descansa sólo en la plantilla**; **dos se sostienen con
norma técnica delante** (la 7 y la 66). · **Aviso de estudio**: **la 5 tiene cuatro opciones casi
idénticas** —la diferencia son dos palabras: **antes o después**, **gamma o rasterización**— y **la 7
usa como distractor los coeficientes VERDADEROS de otra recomendación.** · **Aviso de grafía**: el
examen escribe **«NFL»** por NCL y **«Hybrid Dynamic Range»** por algo que no existe.
