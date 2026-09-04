# Esquema · Tema 13 del específico de Ingeniería Superior · Telecomunicación · Las salas: estudio, continuidad y controles técnicos

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalaciones de televisión ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: el
visualizador bajo el monitor (**UMD**); la imagen dentro de imagen (**PiP**); la matriz de teclado,
vídeo y ratón (**KVM**); la candela por metro cuadrado (**cd/m²**); y el lumen y el lux, que van con su
nombre entero.

**Cabecera.** Enunciado: puntos 13, 14 y 15 del anexo, unidos en un solo tema porque **son la misma
frase con el nombre de la sala cambiado** · **cinco preguntas** · **sin norma del boletín**.

**La idea que lo ordena** · `[of]` · **Una casa que emite es un puñado de salas colgando de DOS
decisiones**: **una sola referencia de sincronismo y una sola matriz de encaminamiento.** **Dos
referencias producen deslizamiento; dos matrices sin pasarela producen islas.**

<!-- indice -->

## Índice

- [Lo que todas comparten](#lo-que-todas-comparten)
- [El estudio](#el-estudio)
- [La continuidad](#la-continuidad)
- [Las salas técnicas y el monitorado](#las-salas-técnicas-y-el-monitorado)
- [La interconexión y los puestos](#la-interconexión-y-los-puestos)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Lo que todas comparten

| Elemento | Qué es |
|---|---|
| **referencia de sincronismo** | **una sola por instalación** |
| **matriz de encaminamiento** | **el sistema nervioso: qué señal llega a qué sala** |
| **intercomunicación** | **órdenes y coordinación: es lo que hace posible el directo** |
| **señalización de cámara en el aire** | **quién está emitiendo** |
| **código de tiempo** | **la referencia temporal común** |
| **monitorado** | **multipantallas y monitores de referencia** |
| **alimentación protegida** | **sistema ininterrumpido y grupo** |
| **climatización** | **sin frío no hay sala técnica** |

- **EL OLVIDO CLÁSICO** · `[of]` · **La climatización es parte del sistema, no del edificio.** **Una
  sala técnica sin frío se apaga en minutos**, y **por eso la refrigeración de las salas críticas va en
  el suministro protegido, no en el general.**

## El estudio

- **la aclaración de vocabulario** · `[of]` · **Plató y estudio no son lo mismo**: **el plató es el
  espacio de grabación con su decorado y su parrilla; el estudio es el plató MÁS sus controles.**

| Espacio | Qué se hace |
|---|---|
| **plató** | **se graba** |
| **control de realización** | **se SUPERVISA Y SE DECIDE qué imágenes forman parte de la grabación o la emisión** |
| **control de cámaras** | **se expone y se iguala la imagen de todas las cámaras** |
| **control de sonido** | **se mezcla el audio** |
| **control de iluminación** | **se lanzan y ajustan los estados de luz** |
| **sala de equipos** | **donde viven los racks** |

- **LA PREGUNTA DE LA SALA** · `[exam]` · **Donde se decide qué imágenes forman parte de la grabación o
  la emisión es el CONTROL DE REALIZACIÓN.** **El control de imagen ajusta y no decide; una cabina de
  grabación o de edición trabaja sobre material ya registrado.**
- **LA PREGUNTA DEL MONITOR** · `[exam]` · **Los monitores de mayor calidad están en el CONTROL DE
  CÁMARAS.** **Es el único puesto donde se juzga la IMAGEN en sí misma** —exposición, color, ruido,
  detalle—, y **eso exige un monitor calibrado.** **En realización se juzga QUÉ se ve, no CÓMO está**:
  sus monitores tienen que ser muchos y fiables, no de referencia.

## La continuidad

- **en qué se distingue del estudio** · `[of]` · **El estudio produce contenido; la continuidad monta
  la emisión.** **Su producto no es un programa: es la cadena de veinticuatro horas.**

| Equipo | Qué hace |
|---|---|
| **mezclador de continuidad** | **encadena las fuentes de emisión** |
| **servidores de emisión** | **reproducen lo grabado según la lista** |
| **sistema de automatización** | **ejecuta la escaleta: qué se emite, cuándo y cuánto** |
| **insertadores de subtítulos y audiodescripción** | **accesibilidad, que es exigencia legal** |
| **vigilancia de emisión** | **comprueba que hay señal y que es la correcta** |

- **las cinco cosas de la automatización** · `[of]` · **1)** trabaja sobre una **lista con tiempos**;
  **2)** **manda sobre los demás equipos** y por eso está en el centro; **3)** **convive con el
  directo**, y **volver a engancharse con la escaleta después es la maniobra delicada**; **4)** tiene
  **modos de degradación** —automático, semiautomático y manual—; **5)** **su fallo es un fallo de
  emisión**, y por eso las continuidades van **redundadas**.
- **la frase que resume la sala** · `[of]` · **Una continuidad se juzga por lo que NO pasa.** **Su
  único indicador de calidad es la ausencia de negro en antena.**

## Las salas técnicas y el monitorado

| Sala | Qué contiene |
|---|---|
| **control central** | **ajusta la calidad técnica de todo lo que entra y sale** |
| **sala de matriz y equipos** | **matriz principal, sincronizadores, conversores, distribución** |
| **sala de servidores** | **tema 18** |
| **sala de intercambios** | **recepción y envío de señales de fuera** |
| **sala de red** | **tema 20** |
| **sala de energía** | **sistemas ininterrumpidos y cuadros** |

| Concepto de multipantalla | Qué es |
|---|---|
| **multipantalla** | **un procesador que compone muchas fuentes en una pantalla grande** |
| **ventana** | **cada fuente dentro de esa composición** |
| **visualizador bajo el monitor** | **el TEXTO debajo de cada ventana que dice qué señal es** |
| **señalización en el aire** | **el indicador de que esa fuente está en programa** |
| **imagen dentro de imagen** | **una imagen pequeña superpuesta a otra**: es otra cosa |

- **LA PREGUNTA DEL RÓTULO** · `[exam]` · **El texto que nombra la señal debajo de la imagen es el
  VISUALIZADOR BAJO EL MONITOR.** **No la imagen dentro de imagen, que es una ventana superpuesta; ni
  la señalización en el aire, que es el indicador de emisión; ni el PROTOCOLO que gestiona esas
  señalizaciones.** **Confundir el rótulo con el protocolo que lo alimenta es lo que la pregunta
  busca.**

| Magnitud | Unidad | Qué mide |
|---|---|---|
| **luminancia** | **candela por metro cuadrado** | **la luz que EMITE una superficie** |
| **flujo luminoso** | **lumen** | **lo que emite una fuente en total** |
| **iluminancia** | **lux** | **la luz que LLEGA a una superficie** |
| **paso de diafragma** | — | **una relación, no una unidad de luz** |

- **LA REGLA QUE LAS SEPARA** · `[exam]` · **El lux es lo que RECIBE una superficie; la candela por
  metro cuadrado, lo que EMITE.** **Un monitor emite: su brillo se mide en candelas por metro
  cuadrado.** **Un plató se ilumina: su nivel se mide en lux.**
- **la regla de calibración** · `[of]` · **Un monitor de referencia sin calibrar no es de
  referencia.** **La calibración tiene fecha y se repite**, y **un monitor que nadie calibra es un
  monitor de producción caro.**

## La interconexión y los puestos

- **LA PREGUNTA CON ESQUEMA** · `[exam]` · **Si varios técnicos tienen que poder trabajar con
  CUALQUIERA de varias estaciones, hace falta una MATRIZ de teclado, vídeo y ratón.** **Un EXTENSOR
  lleva un puesto a distancia, uno a uno, y no permite elegir máquina; un distribuidor de interfaz de
  monitor reparte imagen pero no lleva teclado ni ratón; y un concentrador de bus multiplica puertos en
  una sola máquina.** **La palabra clave del enunciado es «cualquiera de»: eso es conmutación de muchos
  a muchos.**
- **las tres ventajas que hay que saber defender** · `[of]` · **1)** las máquinas viven en la sala
  técnica, refrigeradas y sin ruido en el puesto; **2)** cualquier puesto sirve para cualquier tarea, y
  **una avería de puesto no para el trabajo**; **3)** el acceso se controla y se registra, que es
  materia del tema 25.

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 19 | En qué se mide la luz que emite un monitor | **Candelas por metro cuadrado** ✔ **·** el lux es lo que recibe una superficie |
| 29 | Cómo se llama el texto que nombra la señal debajo de la imagen | **El visualizador bajo el monitor** ✔ |
| 37 | Qué sistema necesitan varios técnicos para trabajar con cualquiera de las estaciones | **Una matriz de teclado, vídeo y ratón** ✔ |
| 69 | Sección donde se decide qué imágenes forman parte de la grabación o la emisión | **Control de realización** ✔ |
| 71 | En qué control están los monitores de mayor calidad | **Control de cámaras** ✔ |
