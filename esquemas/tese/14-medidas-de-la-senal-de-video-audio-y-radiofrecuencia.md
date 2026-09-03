# Esquema · Tema 14 del específico de Técnica de Equipos y Sistemas Electrónicos · Medidas de la señal de vídeo, audio y radiofrecuencia

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de medida · `[plan]` = plantilla
oficial. **Siglas**: el monitor de forma de onda (**WFM**); las componentes analógicas (**YPbPr**) y
digitales (**YCbCr**, de donde **Cr** y **Cb**); los tres primarios (**RGB**); la interfaz digital
serie de alta definición (**HD-SDI**) y el final y comienzo de vídeo activo (**EAV** y **SAV**), los
tres del tema 8; la Unión Europea de Radiodifusión (**UER**); la modulación de frecuencia (**FM**); el
sistema de datos por radio (**RDS**); la radiofrecuencia (**RF**) y el transmisor (**Tx**); el
megahercio (**MHz**) y el kilohercio (**kHz**). **Y una advertencia**: **VALID**, que aparece en una
opción del examen, se reproduce como el enunciado la escribe y **este esquema no le atribuye forma
larga.**

**Cabecera.** Enunciado: punto 16 del anexo · **9 preguntas** · **SIETE dependen de una figura: la
proporción más alta de los diecisiete temas de esta ocupación.** **Este esquema no ha visto ninguna de
las siete y no describe ninguna**: da la regla de la familia y atribuye la respuesta a la plantilla.

<!-- indice -->

## Índice

- [Las líneas de prueba](#las-líneas-de-prueba)
- [El monitor de forma de onda](#el-monitor-de-forma-de-onda)
- [Sincronía entre componentes y entre audio y vídeo](#sincronía-entre-componentes-y-entre-audio-y-vídeo)
- [La señal patológica](#la-señal-patológica)
- [Audio y radiofrecuencia](#audio-y-radiofrecuencia)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las líneas de prueba

| Señal de prueba | Qué mide |
|---|---|
| **Escalera de luminancia** | **Alinealidad de la ganancia de luminancia** ✔ |
| **Escalera modulada** | **Ganancia y fase diferenciales** |
| **Multiburst** | **Respuesta en frecuencia** |
| **Barra y ventana** | **Bajas frecuencias y transitorios** |
| **Diente de sierra** | **Linealidad de la rampa** |
| **Barras de color** | **Colorimetría y niveles** |
| **Bowtie** | **Retardo entre las tres componentes** |

- **PREGUNTA 27** · `[of]` · **La escalera de luminancia mide la alinealidad de la ganancia de
  luminancia.**
- **EL MATIZ QUE DECIDE**: **la escalera de luminancia no lleva crominancia encima**, y **sin
  crominancia no se puede medir nada diferencial.**
- **PREGUNTA 77** · `[plan]` · **La señal de la figura es un Multiburst.** **La regla de la familia**:
  **el multiburst son paquetes de frecuencia creciente y amplitud igual; el diente de sierra es una
  línea única; las barras son escalones de colores.**

## El monitor de forma de onda

| | **Overlay** | **Parade** |
|---|---|---|
| **YPbPr** | **Las tres componentes superpuestas, con las de color centradas en cero** | **Tres trazas seguidas, dos de ellas bipolares** |
| **RGB** | **Tres escaleras encajadas, todas por encima del cero** | **Tres escaleras seguidas, todas unipolares** ✔ |

- **PREGUNTA 23 del segundo llamamiento** · `[plan]` · **La configuración de la figura es «RGB» y
  «Parade».**
- **LAS DOS PREGUNTAS QUE RESUELVEN LA TABLA**: **¿tres trazas separadas o todo encima? ¿bajan por
  debajo del cero o no?** **Separadas es parade; bipolares es YPbPr.**
- **PARA QUÉ SIRVE CADA MODO**: **el RGB en desfile es el de comprobar que ninguna componente se sale
  de gama; el YPbPr superpuesto es el de trabajo diario.**
- **PREGUNTA 9 del segundo llamamiento** · `[plan]` · **Las marcas son el patrón EAV y los datos
  auxiliares de audio embebido.**
- **LO QUE SÍ SE RAZONA**: **el orden de la trama del tema 8 es EAV, espacio auxiliar, SAV**, y **el
  audio embebido viaja en el espacio auxiliar, después del EAV y no del SAV.**

## Sincronía entre componentes y entre audio y vídeo

- **PREGUNTA 4 del segundo llamamiento** · `[plan]` · **La señal de barras con tonos sirve para conocer
  el retardo entre el audio y el vídeo.**
- **LA CLAVE, SIN VER LA FIGURA**: **las opciones a, b y d nombran medidas de una sola señal.** **La
  única que necesita las dos a la vez es la correcta**, y la señal del enunciado lleva las dos.
- **EL AVISO QUE ESTE PUNTO DEJA**: **la señal Bowtie mide el retardo entre las tres componentes de
  vídeo; una señal de barras con tonos mide el retardo entre vídeo y audio.** **Son dos medidas
  distintas y el examen las puso como opciones b y c.**

## La señal patológica

- **PREGUNTA 10 del segundo llamamiento** · `[plan]` · **El ruido impulsivo en la zona magenta indica un
  problema de ecualización.**
- **ES LA MÁS RAZONABLE DE LAS SIETE CON FIGURA**, porque **el enunciado describe el síntoma con
  palabras.**
- **QUÉ ES UNA SEÑAL PATOLÓGICA**: **una secuencia de bits deliberadamente hostil**, que tras la
  codificación produce la mayor racha sin transiciones y el mayor desequilibrio de continua. **Sirve
  para llevar el enlace al límite antes de un directo.**
- **POR QUÉ FALLA AHÍ Y NO EN OTRO SITIO**: **es la zona donde el ecualizador del receptor lo tiene más
  difícil.** **Un ecualizador al límite se equivoca en bits sueltos, y bits sueltos aleatorios se ven
  como ruido impulsivo.** **Que sea aleatorio y no periódico descarta el reloj.**
- **QUÉ HACER**: **acortar el cable, cambiar el conector, mejorar el coaxial o meter un reconstructor.**

## Audio y radiofrecuencia

- **PREGUNTA 54** · `[plan]` · **El diagrama polar de la figura es cardioide.** **La regla**: **una
  circunferencia es omnidireccional; un ocho, bidireccional; un solo lóbulo con el cero justo detrás,
  cardioide; un lóbulo estrecho más otro pequeño detrás, super o hipercardioide.**
- **PREGUNTA 39** · `[of]` · **El ancho de banda de un transmisor de FM con ±25 kHz de desviación y 15
  kHz de audio es de 80 kHz.**
- **LA REGLA DE CARSON**: **el doble de la suma de la desviación y la frecuencia máxima de la
  moduladora.** **2 × (25 + 15) = 80.** **Los 215 MHz son un distractor: el ancho de banda no depende
  de dónde esté la portadora.**
- **PREGUNTA 28 del segundo llamamiento** · `[plan]` · **Lo que se ve es una medida de RF de 75 a 105
  MHz con cuatro marcadores.**
- **LA REGLA DE LA FAMILIA, QUE DECIDE CASI ENTERA LA PREGUNTA**: **una banda entera abarca decenas de
  megahercios y se ve como rayas verticales estrechas; una sola emisora abarca cientos de kilohercios y
  se ve como una campana con estructura interna.** **La opción a describe lo primero y las otras tres
  lo segundo.**
- **LAS SUBPORTADORAS DE UNA EMISIÓN ESTÉREO**: **suma hasta 15 kHz · piloto a 19 · diferencia entre
  23 y 53 · datos por radio a 57.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 27 | Qué mide la escalera de luminancia | c) La alinealidad de la ganancia de luminancia ✔ |
| 39 | Ancho de banda de un transmisor de FM | d) 80 kHz ✔ |
| 54 | Qué diagrama polar es | b) Cardioide ✔ **·** figura |
| 77 | Qué señal de prueba es | d) Multiburst ✔ **·** figura |
| 4 (2.º llam.) | Para qué sirve la señal de barras y tonos | c) Retardo entre audio y vídeo ✔ **·** figura |
| 9 (2.º llam.) | Qué representan las marcas del monitor | d) EAV y datos auxiliares de audio ✔ **·** figura |
| 10 (2.º llam.) | Qué indica el ruido en la zona magenta | d) Problema de ecualización ✔ **·** figura |
| 23 (2.º llam.) | Configuración del monitor de forma de onda | c) «RGB» y «Parade» ✔ **·** figura |
| 28 (2.º llam.) | Qué se ve en la imagen | a) Medida de RF de 75 a 105 MHz ✔ **·** figura |

**Las nueve oficiales son correctas** · **siete descansan en la plantilla.** · **Aviso de estudio, y es
el más importante de la ocupación**: **este punto no se aprueba memorizando, se aprueba habiendo
mirado pantallas.** **Los cuatro cuadros de este esquema —qué mide cada señal de prueba, los cuatro
modos del monitor, las formas de los diagramas polares y las subportadoras de la FM— reducen varias de
las siete a dos opciones antes de mirar.**
