# Esquema · Tema 7 del específico de Sonido · Mezcla y tratamiento del sonido

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de mezcla y procesado.
**Siglas**: el amplificador controlado por tensión (**VCA**, *voltage controlled amplifier*); el factor
de calidad de un filtro (**Q**); y el decibelio (**dB**).

**Cabecera.** Enunciado: punto 5 del anexo, «Mezcla y tratamiento del sonido» · **7 preguntas** · **cuatro son de
dinámica y tres de ecualización.**

<!-- indice -->

## Índice

- [El headroom](#el-headroom)
- [Qué hace un compresor](#qué-hace-un-compresor)
- [El limitador](#el-limitador)
- [Las tecnologías de compresor](#las-tecnologías-de-compresor)
- [Los ecualizadores](#los-ecualizadores)
- [El factor Q y el filtro notch](#el-factor-q-y-el-filtro-notch)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El headroom

- **PREGUNTA 21** · `[of]` · **La diferencia entre el nivel nominal y el punto de saturación se llama
  headroom.**
- **QUÉ ES, EN UNA LÍNEA**: **el margen que queda por encima de donde se trabaja antes de que la señal
  recorte.**
- **POR QUÉ HACE FALTA**: **la música y la voz tienen picos muy por encima de su nivel medio**, y sin
  margen esos picos se cortan.

## Qué hace un compresor

- **LOS CUATRO MANDOS**: **umbral** —a partir de qué nivel actúa—, **relación** —cuánto reduce—,
  **ataque y relajación** —con qué rapidez entra y sale—, **y ganancia de recuperación.**
- **PREGUNTA 22** · `[of]` · **El ajuste make-up de un compresor recupera ganancia.**
- **POR QUÉ EXISTE ESE MANDO**: **comprimir baja el nivel general**; el make-up devuelve lo perdido
  para que la señal comprimida no suene más floja que la original.

## El limitador

- **PREGUNTA 40** · `[of]` · **El compresor que sólo atenúa las señales por encima del umbral y deja
  inalteradas las de nivel inferior es el compresor limitador.**
- **LA DIFERENCIA CON UN COMPRESOR CORRIENTE**: **es de grado, no de clase.** **Un limitador es un
  compresor con relación muy alta**: por encima del umbral, la salida prácticamente no sube.

## Las tecnologías de compresor

| Tecnología | Rasgo |
|---|---|
| **De válvula** | **La más lenta y la de carácter más marcado** |
| **Óptica** | **Suave, con ataque y relajación dependientes del programa** |
| **De diodos o de transistores** | **Rápida** |
| **VCA** | **La más rápida y la más precisa** |

- **PREGUNTA 56** · `[of]` · **El compresor con velocidad de respuesta superior es el VCA.**
- **CÓMO SE RECUERDA**: **cuanto más electrónico y menos físico el elemento que controla la ganancia,
  más deprisa responde.**

## Los ecualizadores

- **PREGUNTA 23** · `[of]` · **De los enumerados, el que NO es un tipo de ecualizador es
  «multibanda».**
- **LOS QUE SÍ LO SON**: **gráfico, paramétrico, semiparamétrico y de filtros fijos.**
- **DÓNDE ESTÁ LA TRAMPA**: **«multibanda» sí existe como término, pero de compresor, no de
  ecualizador.** **Un compresor multibanda parte el espectro y comprime cada trozo por separado.**

## El factor Q y el filtro notch

- **PREGUNTA 91** · `[of]` · **Un factor Q de 1,41 corresponde aproximadamente a 1 octava de anchura.**
- **LA RELACIÓN ES INVERSA**: **a más Q, más estrecha la campana.** **Q de 1,41 es aproximadamente una
  octava; Q de 2,87, media octava; Q por debajo de 1, más de una octava.**
- **PREGUNTA 45** · `[of]` · **Un filtro notch se utiliza idealmente para evitar un acople con una
  megafonía.**
- **POR QUÉ ES ÉL Y NO OTRO**: **el acople ocurre en una frecuencia muy concreta**, y **el notch es el
  filtro más estrecho y profundo que hay**: quita esa frecuencia y no toca lo demás.
- **ENLACE CON EL TEMA 10**: **el acople es el efecto Larsen**, y el notch es una de las cuatro
  maneras de combatirlo.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 21 | Diferencia entre nivel nominal y saturación | d) Headroom ✔ |
| 22 | Qué hace el ajuste make-up de un compresor | c) Recupera ganancia ✔ |
| 23 | Cuál NO es un tipo de ecualizador | c) Multibanda ✔ |
| 40 | Compresor que sólo atenúa por encima del umbral | c) Compresor limitador ✔ |
| 45 | Para qué se usa un filtro notch | a) Para evitar un acople con una megafonía ✔ |
| 56 | Qué compresor responde más rápido | d) VCA ✔ |
| 91 | Octavas de un factor Q de 1,41 | c) 1 octava ✔ |

**Las siete oficiales son correctas** y **ninguna descansa sólo en la plantilla.** · **Aviso de
estudio**: **los cuatro mandos del compresor y la relación inversa del factor Q contestan cuatro de
las siete.** **Es uno de los puntos más razonables del volumen.**
