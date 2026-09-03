# Tema 6 del específico de Ingeniería Técnica · Telecomunicación · Alta y ultraalta definición

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 7 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son las recomendaciones de resolución, color y rango dinámico, **no consultadas**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Aviso de estudio** | **La ultraalta definición no es sólo más píxeles.** Quien la resuma así falla las dos preguntas de color y de rango dinámico, que son la mitad del banco |
| **Extensión** | **1.855 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la alta definición (**HD**) y la ultraalta definición
en sus dos escalones (**UHD** y **UHD2**); el alto rango dinámico (**HDR**) y el estándar (**SDR**);
las recomendaciones de la Unión Internacional de Telecomunicaciones, que se nombran por su número
(**Rec. 601**, **Rec. 709** y **Rec. 2020**); el espacio de color de las Iniciativas de Cine Digital
(**DCI-P3**); la curva logarítmica híbrida (**HLG**) y la cuantificación perceptual (**PQ**); la curva
de compresión de altas luces, que el sector llama por su nombre inglés (**KNEE**); la curva logarítmica
de un fabricante (**S-Log3**); la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**) y la Unión
Europea de Radiodifusión (**EBU**); y las candelas por metro cuadrado (**cd/m²**), que miden el
brillo.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 7):
> «Televisión de Alta Definición (HD), Ultra Alta Definición (UHD/4K, UHD2/8K). Características,
> normativa SMPTE, ITU y EBU.»

**Cuatro preguntas.** **Y las cuatro son de los tres ejes que definen la calidad de imagen moderna**:
**cuántos píxeles, cuántos colores y cuánto contraste.**

**El aviso que ordena el punto**: **la ultraalta definición no es sólo más píxeles.** **Quien la
resuma en «cuatro veces más resolución» falla las dos preguntas de color y de rango dinámico**, que
son la mitad del banco.

<!-- indice -->

## Índice

- [1. Los tres ejes de la calidad](#1-los-tres-ejes-de-la-calidad)
- [2. La resolución](#2-la-resolución)
- [3. El espacio de color](#3-el-espacio-de-color)
- [4. El rango dinámico y sus curvas](#4-el-rango-dinámico-y-sus-curvas)
- [5. Los otros dos ejes que el enunciado no nombra](#5-los-otros-dos-ejes-que-el-enunciado-no-nombra)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Los tres ejes de la calidad

| Eje | Qué mide | Recomendación que lo fija |
|---|---|---|
| **Resolución** | **Cuántos píxeles** | **Rec. 709 para alta definición, Rec. 2020 para ultraalta** |
| **Gama de color** | **Cuántos colores distintos se pueden representar** | **Las mismas** |
| **Rango dinámico** | **Cuánta distancia hay entre lo más oscuro y lo más claro** | **Las curvas del epígrafe 4** |

**La regla que conviene llevar**: **los tres ejes son independientes.** **Hay material de alta
definición con gama amplia y hay ultraalta definición con gama estrecha.** **Una recomendación fija
los tres a la vez, pero un flujo concreto puede combinarlos como quiera**, y por eso los metadatos que
lo declaran son imprescindibles.

## 2. La resolución

**La pregunta 3**: **la resolución de una señal de vídeo de ultraalta definición es 3840 × 2160.** Ésa
es la respuesta oficial.

**La pregunta 34**: **la diferencia entre los formatos 4K y ultraalta definición es que el primero
tiene 4096 × 2160 y el segundo 3840 × 2160.** Ésa es la respuesta oficial.

---

**Las dos son la misma tabla, y la segunda es la que separa a quien lo sabe de quien lo repite:**

| Nombre | Píxeles | Relación de aspecto | De dónde viene |
|---|---|---|---|
| **Alta definición completa** | **1920 × 1080** | **16:9 exacto** | **Televisión** |
| **Ultraalta definición** | **3840 × 2160** ✔ | **16:9 exacto** | **Televisión: el doble de la anterior en cada lado** |
| **4K de cine** | **4096 × 2160** ✔ | **17:9, algo más ancho** | **Cine digital** |
| **Ultraalta definición de segundo escalón** | **7680 × 4320** | **16:9 exacto** | **Televisión** |

**La regla que fija la pareja**: **la de televisión es exactamente el doble de la anterior en cada
lado; la de cine no.** **Y la de cine es más ancha, no más alta**: **las dos tienen 2160 líneas.**

**Las opciones falsas de la pregunta 3 son un ejercicio de leer despacio**: **una cambia dos cifras
—3940 y 2260—, otra da la resolución de alta definición y otra da la de cine con una cifra cambiada.**
**Se contesta comprobando que las dos cifras correctas son el doble de 1920 y de 1080.**

## 3. El espacio de color

**La pregunta 15**: **en el diagrama de cromaticidad, el espacio de color con mayor extensión es
Rec. 2020.** Ésa es la respuesta oficial.

---

**Y la escalera completa, que es lo que hay que llevar aprendido:**

| Espacio | Para qué se definió | Extensión |
|---|---|---|
| **Rec. 601** | **Televisión de definición estándar** | **La menor** |
| **Rec. 709** | **Televisión de alta definición** | **Prácticamente la misma que la anterior** |
| **DCI-P3** | **Proyección de cine digital** | **Intermedia: más rojo y más verde** |
| **Rec. 2020** | **Ultraalta definición** | **La mayor** ✔ |

**Qué es el diagrama de cromaticidad, para que la pregunta signifique algo**: **una figura que
representa TODOS los colores que el ojo distingue**, sin su brillo. **Dentro de ella, cada espacio de
color es un TRIÁNGULO** cuyos vértices son sus tres primarios, **y sólo se puede representar lo que
cae dentro del triángulo.**

**De ahí sale la respuesta sin memorizar nada**: **el espacio con el triángulo más grande es el que
representa más colores.** **Y ninguno de los cuatro cubre la figura entera**: **hay colores que el ojo
ve y que ningún sistema de tres primarios puede reproducir.**

**El dato que hace comparable la escalera**: **el espacio de ultraalta definición cubre alrededor del
75 % de lo que el ojo distingue**, frente a poco más de un tercio del de alta definición. **Es el
salto más grande de los tres ejes**, y el que menos se nota en un televisor de gama media, porque
**pocos paneles llegan a mostrarlo entero.**

## 4. El rango dinámico y sus curvas

**La pregunta 12 es negativa**: **de las curvas o funciones de transferencia enumeradas, la que NO
permite trabajar con alto rango dinámico es la curva de compresión de altas luces.** Ésa es la
respuesta oficial.

---

**Y es la mejor pregunta del punto**, porque **las cuatro opciones son curvas reales y sólo una es de
otra época:**

| Curva | Qué es | ¿Es de alto rango dinámico? |
|---|---|---|
| **De compresión de altas luces** | **Un recurso de las cámaras de rango estándar: dobla la pendiente en la zona alta para no quemar el cielo** | **No: es un parche dentro del rango estándar** ✔ |
| **Logarítmica híbrida** | **Curva de alto rango dinámico compatible hacia atrás con receptores de rango estándar** | **Sí** |
| **Logarítmica de fabricante** | **Curva de captación que conserva todo el rango del sensor para etalonar después** | **Sí, como curva de trabajo** |
| **Cuantificación perceptual** | **Curva de alto rango dinámico absoluta, referida a niveles de brillo concretos** | **Sí** |

**La diferencia entre las dos curvas de alto rango dinámico de difusión, que es lo preguntable de lo
que no ha caído:**

| | **Logarítmica híbrida** | **Cuantificación perceptual** |
|---|---|---|
| **Referencia** | **RELATIVA: la señal dice proporciones** | **ABSOLUTA: la señal dice candelas por metro cuadrado** |
| **Compatibilidad** | **Un receptor de rango estándar la ve aceptablemente** | **Necesita receptor preparado** |
| **Dónde se usa** | **Emisión en directo** | **Producción en fichero, plataformas** |
| **Quién la impulsó** | **Radiodifusores** | **La industria del cine y del panel** |

**Y la razón de que la de altas luces NO sea de alto rango dinámico, que es la clave de la pregunta**:
**esa curva no amplía el rango que el sistema transporta.** **Lo que hace es COMPRIMIR la parte alta
dentro del mismo rango de siempre**, sacrificando fidelidad en las luces para no perderlas del todo.
**Es una solución de rango estándar a un problema de rango estándar.**

## 5. Los otros dos ejes que el enunciado no nombra

**La ultraalta definición se define en el sector por CINCO parámetros y el enunciado nombra tres.**
**Los otros dos conviene tenerlos vistos:**

| Eje | Qué aporta |
|---|---|
| **Cadencia alta de imagen** | **Movimiento limpio en panorámicas y en deporte**: 100 o 120 imágenes por segundo |
| **Profundidad de bits** | **10 bits por componente como mínimo, frente a los 8 de la alta definición** |

**Por qué la profundidad de bits es imprescindible con alto rango dinámico**: **estirar el rango con
sólo ocho bits produce bandas visibles en los degradados.** **Diez bits son el mínimo, y doce lo
deseable.**

**Y la observación de oficio que ordena el punto entero**: **de los cinco ejes, el que más se nota en
un salón no es la resolución.** **A distancia de visión normal, la diferencia entre alta y ultraalta
definición es sutil; la diferencia entre rango estándar y alto rango dinámico se ve desde la
puerta.** **El eje que da nombre al formato es el que menos aporta**, y eso conviene saberlo aunque el
examen no lo pregunte.

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 3 | Resolución de una señal de ultraalta definición | b) 3840 × 2160 ✔ |
| 12 | Qué curva NO permite trabajar con alto rango dinámico | a) La de compresión de altas luces ✔ |
| 15 | Qué espacio de color tiene mayor extensión | c) Rec. 2020 ✔ |
| 34 | Diferencia entre 4K y ultraalta definición | b) 4096 × 2160 y 3840 × 2160 ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **las dos preguntas de resolución se contestan con una sola idea —el doble de
alta definición en cada lado, y el cine es más ancho—**, y **las dos de color y rango dinámico, con la
imagen del triángulo dentro del diagrama y con saber que una de las cuatro curvas es de otra época.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Las recomendaciones de la Unión Internacional de Telecomunicaciones y las normas de la Sociedad
   de Ingenieros de Cine y Televisión y de la Unión Europea de Radiodifusión no se han consultado.**
   **Las resoluciones, el orden de extensión de los espacios de color y el cometido de cada curva son
   de uso universal en el sector**, y **coinciden con las respuestas oficiales.**
2. **El porcentaje de cobertura del diagrama de cromaticidad —alrededor del 75 % frente a poco más de
   un tercio— es un orden de magnitud de uso corriente**, dado como referencia. **Ninguna respuesta
   oficial depende de él**: la pregunta 15 sólo pide cuál es mayor.
3. **La curva logarítmica que aparece como opción falsa es de un fabricante**, y **el temario sólo
   afirma de ella que es una curva de captación de alto rango dinámico**, que es lo que la pregunta
   exige para descartarla.
4. **Los dos ejes del epígrafe 5 y la observación sobre cuál se nota más en un salón son oficio**, y
   **ninguna respuesta oficial depende de ellos.**

**El resto del tema va como oficio y así se declara**: la independencia de los tres ejes, la regla del
doble en cada lado, la imagen del triángulo dentro del diagrama de cromaticidad, la razón de que la
curva de altas luces no amplíe el rango, la comparación entre las dos curvas de difusión y la
necesidad de diez bits para evitar bandas. **Nada de eso está en un boletín oficial ni en una norma
técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
