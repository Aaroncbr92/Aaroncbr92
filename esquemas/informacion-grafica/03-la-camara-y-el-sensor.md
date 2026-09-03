# Esquema · Tema 3 del específico de Información Gráfica y Captación de Imagen y Sonido · La cámara de vídeo y el sensor

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, física del sensor y de la
óptica · `[plan]` = plantilla oficial, **sin documentación de fabricante que la contraste**.

**Cabecera.** Enunciado: «3.1. Cámara de video: ENG, EFP y cinematografía digital · 3.4. Sensores y
señal · 3.5. Sistemas de grabación · 3.13. Ajustes en producción ligera · 4.1. Ajustes básicos» · **8
preguntas** · **CUATRO son física y CUATRO son menú de una máquina concreta**.

<!-- indice -->

## Índice

- [Las tres familias](#las-tres-familias)
- [Del fotón al número](#del-fotón-al-número)
- [CCD y CMOS](#ccd-y-cmos)
- [La máscara de Bayer](#la-máscara-de-bayer)
- [Sensor grande y profundidad de campo](#sensor-grande-y-profundidad-de-campo)
- [La curva logarítmica y el visor](#la-curva-logarítmica-y-el-visor)
- [Los formatos y el proxy](#los-formatos-y-el-proxy)
- [La pregrabación](#la-pregrabación)
- [El envío desde la cámara](#el-envío-desde-la-cámara)
- [Dos cámaras a la vez](#dos-cámaras-a-la-vez)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las tres familias

| Familia | Dónde | Cómo trabaja |
|---|---|---|
| **ENG** | **Reportaje e informativos** | **Autónoma**: batería, tarjeta, un operador. **Al hombro** |
| **EFP** | Retransmisiones | **En cadena**: cuelga de un control por triax o fibra |
| **Cinematografía digital** | Ficción | Autónoma, con flujo de etalonaje |

- **LA DISTINCIÓN QUE ORDENA EL TEMA**: **la ENG lo lleva todo dentro y decide sola; la EFP delega el
  control de imagen.** **Este punto es mayoritariamente de ENG, porque el puesto lo es.**

## Del fotón al número

1. **El fotosito convierte fotones en CARGA.**
2. **La carga se convierte en TENSIÓN y se amplifica.**
3. **El conversor analógico-digital traduce la tensión en un NÚMERO BINARIO.**
4. **El procesador aplica ganancia, balance, curva y compresión.**

- **PREGUNTA 30** · **El que convierte las tensiones en valores digitales de código binario es el ADC o
  CONVERSOR ANALÓGICO/DIGITAL.**
- **LAS TRES FALSAS SON PIEZAS REALES QUE HACEN OTRO PASO**: **el sensor CMOS** y **el sensor CCD** →
  **el paso 1** · **el amplificador integrado en cada fotosito** → **el paso 2**. **Es la trampa mejor
  puesta**, porque **esa pieza SÍ existe y SÍ está en cada fotosito de un CMOS**: **lo que la descarta
  es que AMPLIFICA, no digitaliza.**
- **LA PALABRA QUE DECIDE ES «BINARIO».**

## CCD y CMOS

| | **CCD** | **CMOS** |
|---|---|---|
| Dónde se lee la carga | **Se transporta pozo a pozo a UN conversor común** | **Cada fotosito tiene SU amplificador** |
| Obturación | **GLOBAL**: toda la imagen a la vez | **Por BARRIDO de líneas** |
| Defecto característico | ***SMEAR***: **columna vertical clara** bajo luz fuerte | ***ROLLING SHUTTER***: **verticales INCLINADAS** en movimiento rápido |
| Consumo | Mayor | **Menor** |
| Hoy | Cámaras de estudio antiguas | **Prácticamente todo** |

## La máscara de Bayer

- **PREGUNTA 59** · **Es una SUPERPOSICIÓN DE MICROFILTROS para sensores de imagen que permiten que los
  píxeles REGISTREN LAS LONGITUDES DE ONDA de la luz.**
- **POR QUÉ HACE FALTA**: **un fotosito NO distingue color: cuenta fotones y da un número.** **Para
  captar color con UN solo sensor hay que poner delante de cada fotosito un filtro de una banda.**
- **CÓMO ESTÁ CONSTRUIDA**: **LA MITAD de los elementos son VERDES**, y una cuarta parte rojos y otra
  azules. **El doble de verdes porque el ojo obtiene del verde la mayor parte del brillo** —los
  coeficientes de luminancia del tema 2—.
- **LA CONSECUENCIA**: **cada píxel conoce SÓLO UNO de los tres colores y los otros dos se
  INTERPOLAN** de sus vecinos. **Ese proceso es el *demosaicing*.**
- **LAS TRES FALSAS**: «registren SÓLO la intensidad» → **eso es un sensor SIN máscara: blanco y
  negro** · «consigue alta sensibilidad y alta resolución en un solo sensor» → **la máscara REDUCE las
  dos** · «limita el tamaño mínimo de los detalles para que no haya muaré» → **LA TRAMPA MEJOR PUESTA:
  eso es el FILTRO ÓPTICO PASO BAJO**, otra pieza real que va **justo al lado, en el mismo bloque**.
- **LA DISTINCIÓN**: **la máscara de Bayer da COLOR; el filtro paso bajo evita el MUARÉ.**

## Sensor grande y profundidad de campo

- **PREGUNTA 54** · **Los sensores grandes dan menos profundidad de campo porque CAPTURAN UN ÁREA MAYOR
  DE LA ESCENA Y POR TANTO REQUIEREN DISTANCIAS FOCALES MAYORES para el mismo encuadre.**
- **EL RAZONAMIENTO, EN TRES PASOS**: **la profundidad depende de FOCAL, DIAFRAGMA y DISTANCIA DE
  ENFOQUE** —**el tamaño del sensor NO está en la lista**— · **pero un sensor grande abarca más escena,
  así que para el mismo encuadre desde el mismo sitio hay que alargar la focal** · **y a más focal,
  menos profundidad.**
- **POR TANTO**: **el sensor grande NO reduce la profundidad por sí mismo. La reduce la FOCAL MÁS LARGA
  que obliga a usar.**
- **LAS TRES FALSAS**: «son menos luminosos y se usan diafragmas más abiertos» → **al contrario: a
  igual número de píxeles, fotositos mayores y MÁS sensibilidad** · «multiplican la distancia focal» →
  **es lo contrario del factor de recorte: son los PEQUEÑOS los que "multiplican"** · «píxeles más
  grandes» → **afecta al círculo de confusión, pero NO es la causa que la pregunta busca**.
- **LA CONSECUENCIA DE OFICIO**: **por eso los informativos han trabajado décadas con sensores de 2/3
  de pulgada**: **su mayor profundidad de campo PERDONA el error de foco cuando no hay tiempo de
  medir.**

## La curva logarítmica y el visor

- **PREGUNTA 40** · **SÍ afecta: la imagen del visor parecerá LAVADA, plana, blanquecina y sin
  contraste. Para previsualizar el aspecto final SE DEBE APLICAR UNA LUT.**

| | Lo que se GRABA | Lo que se VE en el visor |
|---|---|---|
| **Sin LUT** | Logarítmico | **Logarítmico: lavado** |
| **Con LUT de monitorización** | **Logarítmico, sin cambios** | **Con contraste: juzgable** |

- **POR QUÉ ES UN PROBLEMA DE OPERACIÓN**: **el operador juzga exposición, foco y encuadre POR EL
  VISOR.** **Con una imagen lavada, el contraste no dice nada.**
- **LAS TRES FALSAS**: «no afectará» → **sí** · «no afectará, pero en 4K sobreexponemos» → **la
  resolución NO tiene nada que ver con la exposición** · **«sí afecta, pero conectando por SDI a un
  monitor se verá correctamente»** → **LA TRAMPA BUENA**: **la salida digital lleva la MISMA señal
  logarítmica.** **Una interfaz digital NO CORRIGE NADA: es un transporte, no un procesador.**

## Los formatos y el proxy

- **PREGUNTA 62** · `[plan]` · **De los formatos que el examen enumera, el de MENOR calidad es PROXY
  AV.**
- **POR QUÉ ESO ES UNA VIRTUD**: **el *proxy* no está para verse, está para trabajar.** **Se transmite
  por una línea estrecha, se visiona desde la redacción y permite montar en baja resolución** mientras
  el original espera. **Es el flujo *offline*-*online*.**
- **LAS FALSAS SON FORMATOS REALES DE MÁS CALIDAD**, y **la trampa está en «DVCA»**, **grafía
  incompleta de DVCAM**: **quien no lo reconozca lo descarta por inventado y acierta por el motivo
  equivocado.**

## La pregrabación

- **PREGUNTA 57** · `[plan]` · **El modo para tener pregrabación antes de pulsar el botón es PICTURE
  CACHE.**
- **QUÉ HACE**: **la cámara graba continuamente en una MEMORIA INTERMEDIA CIRCULAR aunque no esté
  grabando en el soporte.** **Al pulsar, escribe también los segundos ANTERIORES.**
- **EL CASO DE USO ES EL DEL ENUNCIADO**: **una puerta por la que va a salir alguien en un momento que
  nadie controla.** **Sin pregrabación: grabar horas o arriesgarse a pulsar tarde.**
- **LAS TRES FALSAS SON MODOS REALES**: **clip continuo** = todo en un fichero · **grabación
  simultánea** = en dos soportes a la vez · ***timelapse*** = **un cuadro cada cierto tiempo: lo
  contrario**.
- **LA PALABRA QUE RESUELVE ES «ANTES».**

## El envío desde la cámara

- **PREGUNTA 90** · `[plan]` · **Para enviar por internet a través de un móvil hay que activar el ACCESS
  POINT MODE.**
- **CÓMO FUNCIONA**: **la cámara no tiene línea propia a internet** · **el móvil sí, y puede
  compartirla** · **el modo de punto de acceso hace que la cámara se comporte como CLIENTE de una red
  AJENA en lugar de crear la suya.**
- **LAS TRES FALSAS SON AJUSTES REALES DEL MISMO MENÚ**: **Network** = **el menú contenedor** ·
  **Wireless LAN** = **el interruptor general de la radio** · **NFC** = **emparejar acercando, no
  transmitir ficheros**.
- **LA DISTINCIÓN**: **encender la radio NO es lo mismo que decidir A QUÉ RED se conecta.**

## Dos cámaras a la vez

- **PREGUNTA 101** · `[plan]` · **LA MÁS LARGA DEL CUADERNILLO.** **Código de tiempo en FREE RUN ·
  cable de la SALIDA DE VÍDEO de la cámara 1 a la ENTRADA DE GENLOCK de la 2 · cable de TC OUT a TC IN
  hasta que aparezca EXT. LINK y las dos tengan el mismo código · configuración SCENE grabada en
  tarjeta y cargada en la cámara 2 para igualar el PAINT.**

| Qué se hace | Para qué |
|---|---|
| **Código de tiempo en marcha libre** | **Que siga corriendo aunque no se grabe**: es lo que permite compartir la cuenta |
| **Sincronización externa desde la cámara 1** | **Que las dos vayan al MISMO COMPÁS DE CUADRO** |
| **Misma configuración de escena** | **Que las dos imágenes se PAREZCAN.** Sin esto, el corte se ve |

- **LAS TRES FALSAS**: **a)** conecta vídeo a **ENTRADA DE VÍDEO**, que **no sincroniza nada**, y activa
  la grabación simultánea, **que no tiene nada que ver** · **b)** pone el código en **«Clock»**, que
  **no se puede enlazar entre dos cámaras** · **d)** conecta la **SALIDA de sincronización de la cámara
  1**, que **una cámara ENG normalmente no tiene**, y **omite comprobar el código**.
- **CÓMO SE CONTESTA**: **buscando los DOS ERRORES DE BULTO** —una entrada de vídeo donde debía ir una
  de sincronización, y un modo de código que no se enlaza—, **no leyendo las cuatro de arriba abajo.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 30 | Qué convierte tensiones en código binario | b) El conversor analógico-digital ✔ |
| 40 | Si la curva logarítmica afecta al visor | d) Sí: lavada, y hace falta una LUT ✔ |
| 54 | Por qué un sensor grande da menos profundidad | c) Requiere focales mayores ✔ |
| 57 | Modo de pregrabación | c) Picture Cache ✔ **·** sólo con la plantilla |
| 59 | Qué es una máscara de Bayer | a) Microfiltros para registrar las longitudes de onda ✔ |
| 62 | Formato de menor calidad | a) Proxy AV ✔ **·** sólo con la plantilla |
| 90 | Qué activar para enviar por internet con un móvil | b) Access Point Mode ✔ **·** sólo con la plantilla |
| 101 | Ajustes para dos cámaras ENG simultáneas | c) Free Run, genlock y archivo de escena ✔ **·** sólo con la plantilla |

**Las ocho oficiales son correctas y CUATRO descansan sólo en la plantilla**: las cuatro que dependen
de un rótulo de menú o de un nombre de formato de fabricante. · **Aviso de estudio**: **la 101 se
contesta por descarte de dos errores de bulto** · **la 40 castiga un error de concepto muy extendido:
creer que una interfaz digital corrige la señal que transporta.**
