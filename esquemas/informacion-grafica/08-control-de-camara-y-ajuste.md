# Esquema · Tema 8 del específico de Información Gráfica y Captación de Imagen y Sonido · Control de cámara y ajuste de imagen

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, circuitos de cámara y práctica
del control de imagen.

**Cabecera.** Enunciado: «3.10. Control de cámaras: métodos de medición para el ajuste de cámara EFP y
ENG · 4.1. Ajustes básicos» · **7 preguntas** · **ninguna descansa sólo en la plantilla** · **es el
punto que separa al operador del que sólo sabe encuadrar**.

<!-- indice -->

## Índice

- [El mapa de la curva](#el-mapa-de-la-curva)
- [La bandera francesa](#la-bandera-francesa)
- [Las sombras: dos circuitos](#las-sombras-dos-circuitos)
- [El detalle y la dependencia del nivel](#el-detalle-y-la-dependencia-del-nivel)
- [El knee](#el-knee)
- [La ganancia](#la-ganancia)
- [El balance de blancos](#el-balance-de-blancos)
- [El DIT](#el-dit)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El mapa de la curva

- **EL MAPA QUE ORDENA TRES PREGUNTAS DE ESTE PUNTO**: **BLACK STRETCH y BLACK GAMMA trabajan en la
  PARTE BAJA de la curva · el KNEE en la PARTE ALTA · el REALCE DE DETALLE sobre los BORDES de toda
  ella.**
- **Y EL REPARTO DE PAPELES**: **en MULTICÁMARA el ajuste lo hace EL CONTROL DE IMAGEN y el operador
  EJECUTA lo que se le pide por la intercomunicación.** **En REPORTAJE el operador es también el control
  de imagen.**

## La bandera francesa

- **PREGUNTA 11** · **Si el control pide ajustar la FRENCH FLAG, el operador debe ABRIR A LA MÁXIMA
  APERTURA DE FOCAL Y RECTIFICAR SI CACHEA EL ENCUADRE.**
- **QUÉ ES**: **una pantalla opaca sobre un brazo articulado en la propia cámara, que HACE SOMBRA AL
  OBJETIVO** para evitar velo y destellos. **Es una visera de quita y pon, más grande y orientable que
  el parasol.**
- **POR QUÉ SE COMPRUEBA EN EL ANGULAR**: **el ángulo de visión MÁS AMPLIO es el del extremo angular.**
  **Si la bandera no entra en el cuadro AHÍ, no entra en ninguna focal.** **Se comprueba en el PEOR
  CASO.**
- **LAS FALSAS**: «buscar un azul o rojo saturado al 80 % del encuadre» = **un procedimiento REAL de
  ajuste de saturación y matriz, pero sin bandera** · «comunicarlo al equipo de iluminación» =
  **confunde la bandera DE CÁMARA con una DE ILUMINACIÓN** · «seleccionar la señal de diente de sierra»
  = **ajuste de nivel con señal de prueba**.
- **AVISO DE VOCABULARIO**: **«CACHEAR» es el verbo de plató para «ASOMAR EN EL ENCUADRE»**, y **«ABRIR
  LA FOCAL» significa «IR AL ANGULAR»**, no abrir el diafragma. **Quien no las conozca no entiende la
  opción correcta.**

## Las sombras: dos circuitos

| Circuito | Sobre qué actúa | Qué hace | Bidireccional |
|---|---|---|---|
| **BLACK STRETCH** | **La LUMINANCIA (Y)** | **SÓLO LEVANTA las sombras** | **NO** |
| **BLACK GAMMA** | **Los tres canales RGB** | **Levanta o comprime la parte baja** | **SÍ** |

- **PREGUNTA 24** · **El BLACK STRETCH actúa sobre la LUMINANCIA y SÓLO FUNCIONA LEVANTANDO las zonas
  de sombra.**
- **LAS CUATRO OPCIONES COMBINAN DOS VARIABLES**: **SOBRE QUÉ actúa** —luminancia frente a RGB— y **EN
  QUÉ SENTIDO** —sólo levanta frente a bidireccional—. **Hay que acertar las dos.**
- **LA TRAMPA BUENA ES «LUMINANCIA Y BIDIRECCIONAL»**: **acierta la mitad más difícil.**
- **POR QUÉ SÓLO LEVANTA, Y ES LA RAZÓN FÍSICA**: **comprimir los negros POR DEBAJO del nivel de negro
  no tiene sentido, porque NO HAY NADA POR DEBAJO DEL NEGRO.**
- **Y EL PRECIO DE LEVANTARLOS**: **se pierde contraste** y **se hace visible el RUIDO que en negro no se
  veía.**

## El detalle y la dependencia del nivel

| Control | Qué hace |
|---|---|
| **Nivel de detalle** | Cuánto realce |
| **FREQUENCY** | **En qué BANDA de detalle actúa** |
| **LEVEL DEPEND** | **REDUCE O SUPRIME EL REALCE EN LAS ZONAS OSCURAS**, donde el ruido es peor |
| **Recorte** o *crispening* | Ignora las diferencias pequeñas, que suelen ser ruido |

- **PREGUNTA 16** · **Para limpiar el ruido de una zona oscura en imagen bien diafragmada: LEVEL
  DEPEND.**
- **POR QUÉ FUNCIONA**: **el ruido de una imagen bien expuesta está sobre todo EN LAS SOMBRAS**, y **el
  realce de detalle LO AMPLIFICA ahí más que en ningún sitio.** **La dependencia del nivel APAGA el
  realce en la parte baja de la escala.**
- **LAS FALSAS**: **FREQUENCY** → **cambia la banda, no lo apaga en las sombras: puede aliviar, no
  resolver** · **BLACK GAMMA** → **cambia CÓMO SE VEN las sombras, no CUÁNTO RUIDO tienen** · **BLACK
  STRETCH** → **LA TRAMPA MEJOR PUESTA Y LA MÁS INSTRUCTIVA: levantar los negros hace el ruido MÁS
  visible, no menos.**
- **LA REGLA DE OFICIO**: **el ruido de las sombras NO se arregla iluminando la imagen desde el menú. Se
  arregla iluminando LA ESCENA, o quitándole realce a esa parte de la escala.**

## El knee

- **PREGUNTA 64** · **El KNEE CONTROLA CÓMO SE COMPRIMEN LAS ALTAS LUCES para evitar la
  sobreexposición.**
- **CON LA CURVA DELANTE**: **la respuesta es aproximadamente RECTA hasta un punto —el CODO, que es lo
  que la palabra significa— y a partir de ahí SE TUMBA.** **Todo lo que hay por encima se representa con
  MUCHOS MENOS niveles**: **cabe más margen de luz a cambio de menos matiz.**
- **SUS AJUSTES**: **PUNTO del codo** (a qué nivel empieza) · **PENDIENTE** (cuánto se tumba) · **RECORTE
  DE BLANCOS** (el techo absoluto).
- **LAS FALSAS**: «aumenta la sensibilidad» → **NO cambia la sensibilidad: reparte de otra manera lo ya
  captado** · «elimina el parpadeo» → **el parpadeo tiene otras causas** · **«reduce la luminancia de
  las altas luces PARA OSCURECER LA IMAGEN»** → **LA TRAMPA BUENA: describe bien el efecto sobre los
  VALORES y atribuye MAL el propósito.** **La imagen general NO se oscurece.**

## La ganancia

- **PREGUNTA 53** · **6 dB de ganancia = 1 f STOP.**
- **DE DÓNDE SALE**: **un paso de diafragma DUPLICA la luz**, y **en decibelios de tensión duplicar es
  +6 dB**, porque **20 × log₁₀(2) ≈ 6**.

| Ganancia | **Pasos** | Precio en ruido |
|---|---|---|
| **+3 dB** | **½** | Poco |
| **+6 dB** | **1** | Apreciable |
| **+12 dB** | **2** | **Mucho** |
| **+18 dB** | **3** | **Ya es ruidosa** |

- **LAS TRES FALSAS SON LAS EQUIVALENCIAS DE OTROS VALORES**: **medio paso = 3 dB · dos pasos = 12 dB ·
  tres pasos = 18 dB.** **Conviene aprender la tabla ENTERA, no la cifra sola.**
- **AVISO DE OFICIO**: **la ganancia es el ÚLTIMO recurso.** **El orden correcto: abrir el diafragma →
  bajar la obturación si el movimiento lo permite → añadir luz → y SÓLO ENTONCES subir ganancia.**
  **Cada paso de ganancia es un paso de ruido, y el ruido de una toma no se quita después.**

## El balance de blancos

- **PREGUNTA 67** · **Es EL AJUSTE DE LA TEMPERATURA DE COLOR DE LOS SENSORES DE LA CÁMARA A LA
  EXISTENTE EN LA ESCENA.**
- **QUÉ HACE LA MÁQUINA**: **mide una superficie que se le presenta como blanca** y **ajusta la ganancia
  relativa de los canales rojo y azul** hasta que **los tres dan el mismo valor**.
- **LA TRAMPA MEJOR PUESTA ES «AJUSTAR LA TEMPERATURA DE COLOR A LA ESCENA DEL RODAJE»**: **es CASI la
  respuesta y LE FALTA DECIR QUÉ SE AJUSTA.** **No se ajusta la temperatura de la escena: se ajusta la de
  la CÁMARA a la de la escena.**
- **LAS OTRAS DOS**: «equilibrar la iluminación para evitar dominantes» = **eso lo hace el iluminador con
  filtros** · «ajustar la sensibilidad a la luz» = **eso es la exposición y la ganancia**.
- **LA RESPUESTA CORRECTA ES LA MÁS COMPLETA, NO LA MÁS CORTA**: **dice las dos mitades Y la dirección
  del ajuste.**
- **LOS TRES CAMINOS**: **automático sobre carta blanca** (el fiable) · **preajuste de 3.200 o 5.600 K**
  (cuando no hay tiempo) · **automático continuo** (cuando la luz cambia sin control).
- **AVISO**: **el automático continuo es EL ENEMIGO DEL MONTAJE.** **Dos tomas de la misma escena salen
  de distinto color y el montador no puede casarlas.** **En reportaje: balance FIJO, rehecho cuando
  cambia la luz.**

## El DIT

- **PREGUNTA 56** · **Entre sus labores está LA CONFIGURACIÓN TÉCNICA DE LA CÁMARA, EL CONTROL DE
  CALIDAD DE LA IMAGEN, LA CALIBRACIÓN DE MONITORES Y LA GESTIÓN DE ARCHIVOS Y FORMATOS.**
- **DE DÓNDE HA SALIDO EL PUESTO**: **apareció cuando la cámara dejó de ser una máquina de tres mandos y
  se convirtió en un ordenador con menús, curvas, LUT y formatos de fichero.** **Su trabajo está ENTRE la
  cámara y la posproducción.**
- **LAS TRES FALSAS ATRIBUYEN AL PUESTO TRABAJO DE OTROS**: coordinación del equipo de producción = **de
  PRODUCCIÓN** · planificación y composición de planos = **de REALIZACIÓN o dirección de fotografía** ·
  diseño gráfico y digitalización del archivo = **de GRAFISMO y DOCUMENTACIÓN**.
- **CÓMO SE CONTESTA**: **tres opciones describen puestos que existen con OTRO nombre y una describe
  trabajo técnico sobre la imagen y sus ficheros.** **El nombre del puesto ya orienta.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 11 | Qué hacer con la bandera francesa | a) Abrir al angular y rectificar si cachea ✔ |
| 16 | Qué limpia el ruido de una zona oscura | a) Level depend ✔ |
| 24 | Cómo actúa el BLACK STRETCH | b) Sobre la luminancia y sólo levantando ✔ |
| 53 | 6 dB de ganancia en pasos | a) 1 f stop ✔ |
| 56 | Labores del DIT | c) Configuración, calidad, calibración y ficheros ✔ |
| 64 | Efecto del knee | d) Controla cómo se comprimen las altas luces ✔ |
| 67 | Qué es el balance de blancos | d) Ajuste de la temperatura de los sensores a la de la escena ✔ |

**Las siete oficiales son correctas y ninguna descansa sólo en la plantilla.** · **Aviso de estudio**:
**la 24 combina DOS variables** · **la 16 tiene como trampa el ajuste que EMPEORA el problema** · **la
67 tiene una opción que dice MEDIA verdad.** · **Aviso de vocabulario**: **el enunciado de la 11 usa
dos expresiones de plató que no están en ningún diccionario técnico.**
