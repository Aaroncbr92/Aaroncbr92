# Esquema · Tema 3 del específico de Técnica de Equipos y Sistemas Electrónicos · Electrónica de potencia

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio y electrónica de potencia ·
`[plan]` = plantilla oficial. **Siglas**: el transistor bipolar de puerta aislada (**IGBT**, *insulated
gate bipolar transistor*); el transistor de efecto de campo (**FET**, *field effect transistor*) y su
versión de óxido metálico (**MOSFET**); el rectificador controlado de silicio o tiristor (**SCR**,
*silicon controlled rectifier*); y el conversor de analógico a digital (**A/D**).

**Cabecera.** Enunciado: punto 3 del anexo · **4 preguntas** · **dos son del IGBT y dos dependen de una
figura.**

<!-- indice -->

## Índice

- [Qué es la electrónica de potencia](#qué-es-la-electrónica-de-potencia)
- [Los cinco componentes del punto](#los-cinco-componentes-del-punto)
- [Dónde NO va un IGBT](#dónde-no-va-un-igbt)
- [Las dos preguntas con figura](#las-dos-preguntas-con-figura)
- [Dónde se encuentra esto en una instalación](#dónde-se-encuentra-esto-en-una-instalación)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es la electrónica de potencia

- **LA DEFINICIÓN**: **la que conmuta y convierte energía, no la que procesa información.**
- **LA DIFERENCIA DE FONDO CON EL RESTO DE LA OCUPACIÓN**: **aquí los componentes trabajan en corte y
  saturación, no en zona lineal.** **Se busca que conduzcan del todo o nada, porque cualquier punto
  intermedio se convierte en calor.**

## Los cinco componentes del punto

| Componente | Qué lo caracteriza | Dónde se usa |
|---|---|---|
| **Diodo de potencia** | **Conduce en un sentido** | **Rectificación** |
| **Tiristor (SCR)** | **Se dispara y sigue conduciendo hasta que la corriente cae** | **Control de potencia en alterna** |
| **Triac** | **Como el tiristor, en los dos sentidos** | **Atenuadores de iluminación** |
| **MOSFET** | **Se manda por tensión, muy rápido, mejor a tensiones bajas** | **Fuentes conmutadas** |
| **IGBT** | **Puerta de MOSFET y salida de bipolar: tensiones y corrientes altas con conmutación rápida** | **Variadores, alimentación de gran potencia** ✔ |

- **PREGUNTA 29** · `[of]` · **El transistor para tensiones y corrientes altas con conmutación rápida
  es el IGBT.**
- **CÓMO SE RECUERDA**: **el IGBT junta lo mejor de los dos mundos**: se manda como un MOSFET y
  aguanta como un bipolar.

## Dónde NO va un IGBT

- **PREGUNTA 20** · `[of]` · **La aplicación en la que NO es adecuado un IGBT son los conversores A/D
  de alta resolución.**
- **POR QUÉ**: **un IGBT es un interruptor de potencia**, y **un conversor de alta resolución es un
  circuito de señal pequeña y mucha precisión.** **Son los dos extremos opuestos de la electrónica.**
- **LA REGLA QUE RESUELVE ESTA CLASE DE PREGUNTAS**: **potencia y precisión no van juntas.** **Cualquier
  opción que ponga un componente de potencia en un circuito de señal es la falsa.**

## Las dos preguntas con figura

- **PREGUNTA 53** · `[plan]` · **El FET del circuito está en autopolarización por fuente.**
- **PREGUNTA 55** · `[plan]` · **La eficiencia del circuito regulador de tensión es del 50 %.**
- **ESTE ESQUEMA NO HA VISTO NINGUNA DE LAS DOS FIGURAS Y NO LAS DESCRIBE.**
- **LA REGLA DE LA FAMILIA DE LA 53**: **la autopolarización por fuente se reconoce por una resistencia
  entre la fuente y masa, sin ninguna fuente de tensión adicional en la puerta.**
- **LA REGLA DE LA FAMILIA DE LA 55**: **la eficiencia es potencia entregada partido por potencia
  consumida.** **Un regulador lineal que baja la tensión a la mitad con la misma corriente tiene por
  fuerza un rendimiento del 50 %**: la otra mitad se va en calor.

## Dónde se encuentra esto en una instalación

- **EN LAS FUENTES DE ALIMENTACIÓN DE TODO EL EQUIPAMIENTO**, en los **sistemas de alimentación
  ininterrumpida** y en los **atenuadores de iluminación del tema 11.**
- **POR QUÉ IMPORTA AL MANTENIMIENTO**: **es donde se concentra el calor**, y **el calor es la causa
  principal del envejecimiento de los equipos.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 20 | Aplicación en la que NO es adecuado un IGBT | c) Conversores A/D de alta resolución ✔ |
| 29 | Transistor para tensiones y corrientes altas y conmutación rápida | a) IGBT ✔ |
| 53 | Cómo está polarizado el FET del circuito | a) Autopolarización por fuente ✔ **·** sólo con la plantilla |
| 55 | Eficiencia del circuito regulador de tensión | b) 50 % ✔ **·** sólo con la plantilla |

**Las cuatro oficiales son correctas** · **dos descansan sólo en la plantilla.** · **Aviso de
estudio**: **el cuadro de los cinco componentes contesta las dos preguntas razonables**, y **la regla
de que potencia y precisión no van juntas sirve para muchas preguntas negativas del examen.**
