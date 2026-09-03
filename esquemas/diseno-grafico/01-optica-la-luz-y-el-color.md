# Esquema · Tema 1 del específico de Diseño Gráfico · Óptica: la luz, el color y la imagen

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de diseño y de imagen ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: el modelo de rojo, verde y azul (**RGB**) y el
de cian, magenta, amarillo y negro (**CMYK**); el tono, la saturación y el brillo (**HSB**); el
nanómetro (**nm**); el grado kelvin (**K**); y el número f (**f**).

**Cabecera.** Enunciado: punto 1 del anexo · **8 preguntas** · **ninguna lleva figura** · **es el
punto que sostiene todo lo demás**: el color vuelve en los temas 5, 10 y 11.

<!-- indice -->

## Índice

- [Las dos mezclas](#las-dos-mezclas)
- [Temperatura de color](#temperatura-de-color)
- [Los colores en un espacio](#los-colores-en-un-espacio)
- [Profundidad de bits](#profundidad-de-bits)
- [Objetivo y profundidad de campo](#objetivo-y-profundidad-de-campo)
- [Iluminación](#iluminación)
- [El ojo y los monitores](#el-ojo-y-los-monitores)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las dos mezclas

- **LA LUZ SE SUMA Y LA TINTA SE RESTA.**

| | **Aditiva** | **Sustractiva** |
|---|---|---|
| **Con qué** | **Luces** | **Pigmentos o tintas** |
| **Primarios** | **Rojo, verde, azul** | **Cian, magenta, amarillo** ✔ |
| **Secundarios** | **Cian, magenta, amarillo** | **Rojo, verde, azul** |
| **Sumarlo todo** | **Blanco** ✔ | **Negro**, en teoría |
| **No poner nada** | **Negro** | **Blanco**: el del papel |

- **PREGUNTA 14** · `[exam]` · **Los primarios sustractivos son cian, magenta y amarillo.**
- **PREGUNTA 73** · `[exam]` · **Los tres primarios de luz sumados dan blanco.**
- **LA SIMETRÍA QUE UNE LAS DOS FILAS**: **los primarios de una son los secundarios de la otra.** **No
  hay que memorizarlo aparte**: **cada primario sustractivo es el blanco menos un primario aditivo**
  —cian es blanco menos rojo, magenta es blanco menos verde, amarillo es blanco menos azul.
- **POR QUÉ LA TINTA TIENE CUATRO LETRAS Y LA LUZ TRES**: **sumar las tres tintas no da negro limpio,
  da un pardo sucio**, y por eso la imprenta añade la negra.
- **PREGUNTA 37** · `[exam]` · **Dos primarios de luz dan el secundario complementario del tercer
  primario.**

| Dos primarios | Secundario | Complementario de |
|---|---|---|
| **Rojo + verde** | **Amarillo** | **Azul** |
| **Rojo + azul** | **Magenta** | **Verde** |
| **Verde + azul** | **Cian** | **Rojo** |

- **LA DEMOSTRACIÓN, EN UNA LÍNEA**: **si rojo más verde da amarillo, y los tres dan blanco, entonces
  amarillo más azul da blanco**: son complementarios.
- **LAS FALSAS SE CAEN CON LO MISMO**: **al sumar luz nunca se oscurece**, así que el secundario ni es
  más oscuro ni es neutro.

## Temperatura de color

- **PREGUNTA 24** · `[exam]` · **Un color frío tiene temperatura de color ALTA.**
- **POR QUÉ ES ASÍ Y NO AL REVÉS**: **no mide el calor de la luz**: **mide a qué temperatura habría
  que calentar un cuerpo negro ideal para que emitiera esa luz.** **Un hierro al rojo está a menos
  temperatura que uno al blanco azulado.**

| Fuente | Aproximada | Cómo la vemos |
|---|---|---|
| **Vela** | **1.800 K** | **Muy cálida** |
| **Incandescente** | **2.800 a 3.200 K** | **Cálida** |
| **Luz de día** | **5.500 a 6.500 K** | **Neutra** |
| **Cielo cubierto o sombra** | **7.000 K y más** | **Fría** ✔ |

- **LA REGLA DE MEMORIA**: **cálido es número bajo, frío es número alto.** **Justo lo contrario de lo
  que sugiere la palabra**, y ésa es toda la dificultad.

## Los colores en un espacio

- **PREGUNTA 96** · `[exam]` · **Los espacios con colores cálidos parecen más grandes, cercanos y
  pesados.**

| | **Cálidos** | **Fríos** |
|---|---|---|
| **Distancia aparente** | **Se adelantan** ✔ | **Se alejan** |
| **Tamaño aparente** | **Agrandan** | **Empequeñecen** |
| **Peso aparente** | **Pesan** | **Aligeran** |

- **ES PERCEPCIÓN, NO FÍSICA**, y el temario lo dice: **no hay norma detrás, hay consenso de oficio.**
- **LA APLICACIÓN DIARIA**: **un rótulo rojo parece mayor que el mismo en azul**, y hay que
  compensarlo con el tamaño.

## Profundidad de bits

- **PREGUNTA 70** · `[exam]` · **16 bits dan 65.536 colores.**
- **ES UN CÁLCULO, NO UN DATO**: **dos elevado a dieciséis.**

| Bits | Valores | Dónde |
|---|---|---|
| **1** | **2** | **Blanco y negro puro** |
| **8** | **256** | **Un canal, o imagen indexada** |
| **16** | **65.536** ✔ | **Alta precisión por canal** |
| **24** | **16,7 millones** | **Ocho por canal: el color «verdadero»** |

- **EL ERROR QUE LA FALSA BUSCA**: **16,7 millones es lo de 24 bits, o sea OCHO POR CANAL**, que es la
  cifra que la gente asocia a «color de verdad». **La pregunta dice 16 bits a secas.**
- **«16 BITS» NO ES «16 BITS POR CANAL»**: lo segundo son cuarenta y ocho en total.

## Objetivo y profundidad de campo

- **PREGUNTA 76** · `[exam]` · **La menor profundidad de campo la da f/1,4.**

| Número f | Diafragma | Luz | Profundidad de campo |
|---|---|---|---|
| **1,4** | **Muy abierto** | **Mucha** | **Mínima** ✔ |
| **8** | **Medio** | **Media** | **Media** |
| **16** | **Cerrado** | **Poca** | **Grande** |
| **22** | **Muy cerrado** | **Muy poca** | **Máxima** |

- **POR QUÉ VA AL REVÉS**: **el número f es una fracción** —focal entre diámetro—, y **un denominador
  grande da una fracción pequeña.**
- **LOS TRES MANDOS QUE LA CONTROLAN**: **el diafragma** —más abierto, menos—, **la focal** —más
  larga, menos— y **la distancia** —más cerca, menos—.

## Iluminación

- **PREGUNTA 91** · `[exam]` · **El triángulo básico son principal, relleno y contraluz.**

| Luz | Dónde | Qué hace |
|---|---|---|
| **Principal** | **A un lado, más alta que el sujeto** | **Da la forma y decide las sombras** |
| **Relleno** | **Al otro lado, más suave** | **Abre las sombras sin borrarlas** |
| **Contraluz** | **Detrás y arriba** | **Separa al sujeto del fondo** |

- **LA RELACIÓN ENTRE PRINCIPAL Y RELLENO DECIDE EL CONTRASTE**: **cerca en potencia, imagen plana;
  separadas, dramática.**
- **POR QUÉ ESTÁ EN UN TEMARIO DE DISEÑO**: **es el mismo esquema que se monta en tres dimensiones en
  el tema 10.** **Las luces virtuales se colocan igual que las reales.**

## El ojo y los monitores

- **BASTONES**: **luminosidad, poca luz.** **CONOS**: **color, necesitan luz**, y hay tres tipos.
  **De ahí salen los tres primarios de la pantalla**: no es una elección técnica, es cómo vemos.
- **ESPECTRO VISIBLE**: **de unos 380 a unos 780 nanómetros.**

| | **Monitor de informática** | **Monitor de vídeo** |
|---|---|---|
| **Calibrado para** | **Trabajo gráfico y ofimático** | **El color de la norma de emisión** |
| **Rango** | **Suele usar el completo** | **Suele usar el legal de vídeo** |
| **Muestra además** | **Nada** | **Zona segura, forma de onda, falso color** |

- **EL AVISO**: **un grafismo aprobado en monitor de informática puede verse distinto en emisión.**
  **Lo que se emite se juzga en monitor de vídeo calibrado.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 14 | Primarios en mezcla sustractiva | d) Cian, magenta y amarillo ✔ |
| 24 | Qué es un color frío | d) Temperatura de color alta ✔ |
| 37 | Qué dan dos primarios de luz | c) El secundario complementario del tercero ✔ |
| 70 | Colores de una imagen de 16 bits | d) 65.536 ✔ |
| 73 | Suma de los tres primarios de luz | d) Blanco ✔ |
| 76 | Apertura de menor profundidad de campo | b) 1,4 ✔ |
| 91 | En qué consiste el triángulo de iluminación | a) Principal, relleno y contraluz ✔ |
| 96 | Qué caracteriza a los espacios cálidos | d) Más grandes, cercanos y pesados ✔ |

**Las ocho oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**la tabla de las dos mezclas contesta tres preguntas y ayuda en los temas 10 y 11.** **Lo segundo que
hay que fijar es que la temperatura de color va al revés de lo que sugiere la palabra.**
