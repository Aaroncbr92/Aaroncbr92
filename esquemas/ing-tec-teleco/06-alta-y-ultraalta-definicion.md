# Esquema · Tema 6 del específico de Ingeniería Técnica · Telecomunicación · Alta y ultraalta definición

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de imagen · `[exam]` = opciones
del propio cuadernillo · `[norma]` = norma o recomendación nombrada, sin cita literal. **Siglas**: la
alta definición (**HD**) y la ultraalta definición en sus dos escalones (**UHD** y **UHD2**); el alto
rango dinámico (**HDR**) y el estándar (**SDR**); las recomendaciones de la Unión Internacional de
Telecomunicaciones (**Rec. 601**, **Rec. 709**, **Rec. 2020**); el espacio de las Iniciativas de Cine
Digital (**DCI-P3**); la curva logarítmica híbrida (**HLG**) y la cuantificación perceptual (**PQ**);
la curva de compresión de altas luces (**KNEE**); la logarítmica de fabricante (**S-Log3**); la
Sociedad de Ingenieros de Cine y Televisión (**SMPTE**) y la Unión Europea de Radiodifusión (**EBU**);
y las candelas por metro cuadrado (**cd/m²**).

**Cabecera.** Enunciado: punto 7 del anexo · **4 preguntas** · **las cuatro de los tres ejes de la
calidad**: cuántos píxeles, cuántos colores, cuánto contraste · **el aviso que ordena el punto**: **la
ultraalta definición no es sólo más píxeles**, y quien la resuma así falla la mitad del banco.

<!-- indice -->

## Índice

- [Los tres ejes](#los-tres-ejes)
- [La resolución](#la-resolución)
- [El espacio de color](#el-espacio-de-color)
- [El rango dinámico y sus curvas](#el-rango-dinámico-y-sus-curvas)
- [Los dos ejes que el enunciado calla](#los-dos-ejes-que-el-enunciado-calla)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los tres ejes

| Eje | Qué mide | Quién lo fija |
|---|---|---|
| **Resolución** | **Cuántos píxeles** | **Rec. 709 y Rec. 2020** · `[norma]` |
| **Gama de color** | **Cuántos colores representables** | **Las mismas** |
| **Rango dinámico** | **Distancia entre lo más oscuro y lo más claro** | **Las curvas de transferencia** |

- **LA REGLA** · `[of]` · **Los tres ejes son INDEPENDIENTES.** **Hay alta definición con gama amplia y
  ultraalta con gama estrecha.** **Por eso los metadatos que lo declaran son imprescindibles.**

## La resolución

| Nombre | Píxeles | Aspecto | De dónde |
|---|---|---|---|
| **Alta definición completa** | **1920 × 1080** | **16:9 exacto** | **Televisión** |
| **Ultraalta definición** | **3840 × 2160** ✔ | **16:9 exacto** | **El doble de la anterior en cada lado** |
| **4K de cine** | **4096 × 2160** ✔ | **17:9, más ancho** | **Cine digital** |
| **Segundo escalón** | **7680 × 4320** | **16:9 exacto** | **Televisión** |

- **PREGUNTA 3** · `[exam]` · **La resolución de ultraalta definición es 3840 × 2160.**
- **PREGUNTA 34** · `[exam]` · **La diferencia con 4K: el de cine es 4096 × 2160 y el de televisión
  3840 × 2160.**
- **LA REGLA QUE FIJA LA PAREJA** · `[of]` · **La de televisión es exactamente el doble de la anterior
  en cada lado; la de cine no.** **Y la de cine es más ANCHA, no más alta**: las dos tienen 2160
  líneas.
- **LAS FALSAS DE LA 3 SON DE LEER DESPACIO** · `[exam]` · **Una cambia dos cifras —3940 y 2260—, otra
  da la de alta definición y otra la de cine con una cifra cambiada.**

## El espacio de color

| Espacio | Para qué | Extensión |
|---|---|---|
| **Rec. 601** · `[norma]` | **Definición estándar** | **La menor** |
| **Rec. 709** · `[norma]` | **Alta definición** | **Casi la misma que la anterior** |
| **DCI-P3** · `[norma]` | **Proyección de cine digital** | **Intermedia: más rojo y más verde** |
| **Rec. 2020** · `[norma]` | **Ultraalta definición** | **La mayor** ✔ |

- **PREGUNTA 15** · `[exam]` · **El de mayor extensión en el diagrama de cromaticidad es Rec. 2020.**
- **QUÉ ES ESE DIAGRAMA** · `[of]` · **Una figura con TODOS los colores que el ojo distingue, sin su
  brillo.** **Cada espacio es un TRIÁNGULO cuyos vértices son sus tres primarios**, y **sólo se
  representa lo que cae dentro.**
- **LA RESPUESTA SIN MEMORIZAR** · `[of]` · **El triángulo más grande representa más colores.**
  **Ninguno cubre la figura entera**: hay colores que el ojo ve y que ningún sistema de tres primarios
  reproduce.
- **EL DATO QUE HACE COMPARABLE LA ESCALERA** · `[of]` · **El de ultraalta cubre alrededor del 75 % de
  lo que el ojo distingue**, frente a poco más de un tercio del de alta definición. **Es el salto mayor
  de los tres ejes y el que menos se nota**, porque pocos paneles lo muestran entero.

## El rango dinámico y sus curvas

| Curva | Qué es | ¿Alto rango dinámico? |
|---|---|---|
| **De compresión de altas luces** | **Recurso de cámara de rango estándar: dobla la pendiente arriba para no quemar el cielo** | **No: parche dentro del rango estándar** ✔ |
| **Logarítmica híbrida** | **Alto rango dinámico compatible hacia atrás** | **Sí** |
| **Logarítmica de fabricante** | **Conserva todo el rango del sensor para etalonar** | **Sí, como curva de trabajo** |
| **Cuantificación perceptual** | **Alto rango dinámico absoluto, referido a brillos concretos** | **Sí** |

- **PREGUNTA 12, NEGATIVA** · `[exam]` · **La que NO permite alto rango dinámico es la de compresión de
  altas luces.**
- **LA CLAVE** · `[of]` · **Esa curva no AMPLÍA el rango que el sistema transporta**: **COMPRIME la
  parte alta dentro del rango de siempre**, sacrificando fidelidad en las luces para no perderlas.
  **Solución de rango estándar a un problema de rango estándar.**

| | **Logarítmica híbrida** | **Cuantificación perceptual** |
|---|---|---|
| **Referencia** | **RELATIVA: proporciones** | **ABSOLUTA: candelas por metro cuadrado** |
| **Compatibilidad** | **Un receptor de rango estándar la ve aceptablemente** | **Necesita receptor preparado** |
| **Dónde** | **Emisión en directo** | **Fichero y plataformas** |
| **Quién la impulsó** | **Radiodifusores** | **Cine y fabricantes de panel** |

## Los dos ejes que el enunciado calla

| Eje | Qué aporta |
|---|---|
| **Cadencia alta de imagen** | **Movimiento limpio en panorámicas y deporte**: 100 o 120 por segundo |
| **Profundidad de bits** | **10 bits por componente como mínimo**, frente a los 8 de alta definición |

- **POR QUÉ 10 BITS SON IMPRESCINDIBLES CON ALTO RANGO DINÁMICO** · `[of]` · **Estirar el rango con
  ocho bits produce bandas visibles en los degradados.** **Diez es el mínimo y doce lo deseable.**
- **LA OBSERVACIÓN QUE ORDENA EL PUNTO** · `[of]` · **De los cinco ejes, el que más se nota en un salón
  NO es la resolución.** **A distancia normal la diferencia de resolución es sutil; la de rango
  dinámico se ve desde la puerta.** **El eje que da nombre al formato es el que menos aporta.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 3 | Resolución de ultraalta definición | **3840 × 2160** ✔ |
| 12 | Qué curva NO permite alto rango dinámico | **La de compresión de altas luces** ✔ |
| 15 | Espacio de color de mayor extensión | **Rec. 2020** ✔ |
| 34 | Diferencia entre 4K y ultraalta definición | **4096 × 2160 y 3840 × 2160** ✔ |
