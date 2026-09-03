# Esquema · Tema 5 del específico de Montaje de Equipos Audiovisuales · Conectores, cables y elementos de conexión

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, sin norma detrás ·
`[plan]` = plantilla oficial de respuestas, **sin documentación de fabricante que la contraste**.

**Cabecera.** Enunciado: «2.4. Conectores y elementos de conexión · 3.2. Conectores y elementos de
conexión (sonido)» · **17 preguntas: EL PUNTO MÁS PREGUNTADO DE ESTA OCUPACIÓN** · **dos descansan
sólo en la plantilla (4 y 10)**.

<!-- indice -->

## Índice

- [Las cuatro capas de un cable](#las-cuatro-capas-de-un-cable)
- [El coaxial](#el-coaxial)
- [El BNC](#el-bnc)
- [El XLR](#el-xlr)
- [El speakon](#el-speakon)
- [El RJ45](#el-rj45)
- [La fibra óptica](#la-fibra-óptica)
- [Los híbridos](#los-híbridos)
- [Los materiales](#los-materiales)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las cuatro capas de un cable

| Capa | Para qué |
|---|---|
| **Conductor** (el alma, de cobre) | **Lleva la señal** |
| **Dieléctrico** o aislante | **SEPARA LOS CONDUCTORES ENTRE SÍ** y fija la impedancia |
| **Malla** o pantalla | **REDUCE LAS INTERFERENCIAS ELECTROMAGNÉTICAS** y devuelve la corriente |
| **Cubierta** | Protege mecánicamente |

- **PREGUNTA 66** · **La función del dieléctrico es SEPARAR LOS CONDUCTORES ENTRE SÍ.**
- **PREGUNTA 6** · **La parte que reduce las interferencias es LA MALLA.**
- **NO CONFUNDIRLAS**: **el dieléctrico separa; la malla apantalla.** Las dos son «aislar» en lenguaje
  corriente, y **el examen pregunta por las dos**.

## El coaxial

| Propiedad | Dato |
|---|---|
| **Impedancia** | **75 Ω** en vídeo y televisión; 50 Ω en radiofrecuencia |
| **Qué transporta** | Vídeo analógico o digital, radiofrecuencia, datos. **NO lleva alimentación** |
| **Ventaja** | Fácil de instalar, duradero, **resistente a interferencias por su malla** |
| **Límite** | **LA ATENUACIÓN CRECE CON LA FRECUENCIA Y CON LA DISTANCIA** |

- **PREGUNTA 78** · **Lo que NO es característica del coaxial: «altas frecuencias a largas distancias
  sin pérdidas».** **Precisamente lo contrario:** a más frecuencia, menos metros.
- **PREGUNTA 61** · **La impedancia de una conexión BNC de vídeo SDI es 75 ohmios.**
- **EL ERROR DE MONTAJE MÁS CARO**: **usar un coaxial de 50 Ω en una línea de vídeo.** Encaja, y da
  reflexiones.

## El BNC

- **PREGUNTA 5** · **Un BNC es un conector DE DOS POLOS PARA CABLE COAXIAL**: **vivo y malla**.
- **CÓMO ES**: **de bayoneta** —se mete y se gira un cuarto de vuelta—, de ahí *Bayonet
  Neill-Concelman*.
- `[plan]` · **PREGUNTA 4** · **El BNC de alta densidad para paneles y matrices es el 5282-HD, aéreo y
  macho, para cable VK 7.**
- `[plan]` · **PREGUNTA 10** · **La antena receptora Sennheiser AD 3700 se conecta con un cable con
  conector BNC.**

## El XLR

- **LOS TRES CONTACTOS, DE MEMORIA**: **1 = MASA O MALLA · 2 = VIVO O POSITIVO · 3 = RETORNO O
  NEGATIVO.**
- **PREGUNTA 13** · **Construcción correcta de un XLR macho: 1-malla, 2-positivo, 3-negativo.**
- **PREGUNTA 94** · **Un XLR está balanceado cuando lleva TRES CONDUCTORES: señal, señal invertida y
  masa.**
- **POR QUÉ EL BALANCEADO CANCELA EL RUIDO**: **la señal viaja dos veces, una invertida**; **el ruido
  entra igual en las dos**; **al restarlas en el receptor, la señal se suma y el ruido se va.**
- **REGLA MNEMOTÉCNICA**: **1 masa, 2 más, 3 menos.**

## El speakon

- **PREGUNTA 27** · **El speakon es un conector PARA ALTAVOCES Y AMPLIFICADORES.**
- **POR QUÉ EXISTE**: **la línea de altavoz lleva potencia**, no señal de línea. El speakon **cierra
  con giro**, **no deja contactos accesibles** y **aguanta corriente**.
- **LO QUE NUNCA HAY QUE HACER**: **conectar un altavoz pasivo por XLR.** Encaja en la mesa y **no
  aguanta la potencia**.

## El RJ45

- **PREGUNTA 40** · **Un RJ45 consta de 8 HILOS** —cuatro pares—.
- **PREGUNTA 50** · **El conector de red de alta velocidad en sistemas audiovisuales es el RJ45.**
- **LO QUE HAY QUE SABER EN MONTAJE**: **la categoría del cable manda sobre la velocidad**, y **la
  tirada tiene límite**.

## La fibra óptica

| Tipo | Núcleo | Para qué |
|---|---|---|
| **Monomodo** | **8 a 10 µm** | **LARGA DISTANCIA**: un solo camino, sin dispersión modal |
| **Multimodo** | 50 o 62,5 µm | **CORTA DISTANCIA**: varios caminos, más fácil de conectorizar |

- **PREGUNTA 28** · **El núcleo de la monomodo mide de 8 a 10 micrómetros.**
- **PREGUNTA 74** · **La fibra para corta distancia es la MULTIMODO.**
- **REGLA**: **núcleo fino → lejos. Núcleo grueso → cerca.** Parece al revés y no lo es.

| Conector | Qué es |
|---|---|
| **SC** | De empuje y tracción, cuadrado |
| **LC** | **Como el SC pero de la mitad de tamaño** |
| **FC** | **Roscado**, para instalaciones con vibración |
| **ST** | De bayoneta, redondo |
| **RC** | **NO EXISTE** |

- **PREGUNTA 91** · **El que NO es conector de fibra óptica es el RC.**

## Los híbridos

- **PREGUNTA 68** · **Los cables de tecnología híbrida llevan ENERGÍA, FIBRA Y SEÑAL** en una sola
  manguera.
- **DÓNDE SE VEN**: **el cable de cámara SMPTE**, que sube alimentación por cobre y baja señal por
  fibra. **Un solo cable en lugar de tres.**

## Los materiales

| Material | ¿Termoplástico? | Dónde |
|---|---|---|
| **Polietileno** | **Sí** | Dieléctrico de coaxiales |
| **Polipropileno** | **Sí** | Aislamientos |
| **Teflón** | **Sí** | Alta temperatura y baja pérdida |
| **EPDM** | **NO: ES UN ELASTÓMERO, UN CAUCHO** | Cubiertas flexibles y juntas |

- **PREGUNTA 64** · **El que NO es termoplástico es el EPDM.**
- **LA DIFERENCIA, EN UNA LÍNEA**: **el termoplástico se ablanda con el calor y se puede volver a
  moldear; el elastómero está vulcanizado y no.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 4 | BNC de alta densidad para paneles y matrices | d) 5282-HD aéreo macho para VK 7 ✔ **·** sólo con la plantilla |
| 5 | Qué es un conector BNC | c) De dos polos para cable coaxial ✔ |
| 6 | Parte que reduce interferencias | b) La malla ✔ |
| 10 | Conexión de la antena Sennheiser AD 3700 | a) Cable con conector BNC ✔ **·** sólo con la plantilla |
| 13 | Construcción correcta de un cable XLR | d) 1-malla, 2-positivo, 3-negativo ✔ |
| 27 | Qué es un conector speakon | d) Para altavoces y amplificadores ✔ |
| 28 | Núcleo de la fibra monomodo | b) 8 a 10 µm ✔ |
| 40 | De cuántos hilos consta un RJ45 | d) 8 ✔ |
| 50 | Conector de red de alta velocidad | b) RJ45 ✔ |
| 61 | Impedancia de un BNC de vídeo SDI | c) 75 ohmios ✔ |
| 64 | Cuál NO es un termoplástico | b) EPDM ✔ |
| 66 | Función del dieléctrico | d) Separar los conductores entre sí ✔ |
| 68 | Qué son los cables híbridos | a) Energía, fibra y señal ✔ |
| 74 | Fibra para corta distancia | a) Multimodo ✔ |
| 78 | Cuál NO es característica del coaxial | b) Altas frecuencias a larga distancia sin pérdidas ✔ |
| 91 | Cuál NO es un conector de fibra | a) Conector RC ✔ |
| 94 | Cuándo un XLR está balanceado | c) Tres conductores ✔ |

**Las diecisiete oficiales son correctas**, y **dos descansan sólo en la plantilla**. · **Aviso de
reparto**: **diecisiete preguntas de noventa y seis salen de aquí: casi una de cada cinco.** **Es el
punto que más renta por hora de estudio de todo el específico de Montaje de Equipos.** · **Aviso de
formato**: **tres de las diecisiete son preguntas negativas** —«cuál NO es»—: **64, 78 y 91**.
Leer el enunciado dos veces.
