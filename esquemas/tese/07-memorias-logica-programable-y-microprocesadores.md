# Esquema · Tema 7 del específico de Técnica de Equipos y Sistemas Electrónicos · Memorias, lógica programable y microprocesadores

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio e informática de sistemas.
**Siglas**: la memoria de acceso aleatorio (**RAM**, *random access memory*) y la de sólo lectura
(**ROM**, *read only memory*); la matriz de puertas programable en campo (**FPGA**, *field programmable
gate array*); la unidad central de proceso (**CPU**); y la unidad aritmético-lógica (**ALU**).

**Cabecera.** Enunciados: puntos 8 y 9 del anexo, reunidos en un tema · **1 pregunta entre los dos** ·
**junto con el punto 13, el menos rentable de la ocupación por hora de estudio.**

<!-- indice -->

## Índice

- [La jerarquía de memoria](#la-jerarquía-de-memoria)
- [La caché](#la-caché)
- [Los dispositivos lógicos programables](#los-dispositivos-lógicos-programables)
- [El microprocesador](#el-microprocesador)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La jerarquía de memoria

| Nivel | Velocidad | Tamaño | Se pierde al apagar |
|---|---|---|---|
| **Registros del procesador** | **La mayor** | **Bytes** | **Sí** |
| **Caché** | **Muy alta** | **Kilobytes o megabytes** | **Sí** ✔ |
| **Memoria principal (RAM)** | **Alta** | **Gigabytes** | **Sí** |
| **Disco de estado sólido** | **Media** | **Cientos de gigabytes** | **No** |
| **Disco mecánico o cinta** | **Baja** | **Terabytes** | **No** |

- **LA REGLA QUE ORDENA LA TABLA**: **cuanto más rápida, más cara y más pequeña.** **La jerarquía
  existe porque no se puede tener todo a la vez.**

## La caché

- **PREGUNTA 36** · `[of]` · **Una memoria caché es una memoria de alta velocidad y pequeño tamaño para
  los datos de uso frecuente.**
- **POR QUÉ FUNCIONA**: **los programas repiten.** **Vuelven a pedir lo que acaban de pedir y lo que
  está al lado**, y guardar eso cerca del procesador ahorra la mayor parte de los accesos.
- **LAS TRES PALABRAS DE LA RESPUESTA OFICIAL**: **rápida, pequeña y de uso frecuente.** **Las tres
  juntas sólo describen la caché.**

## Los dispositivos lógicos programables

- **QUÉ SON**: **circuitos cuyo comportamiento lógico se define después de fabricarlos.**
- **LA FPGA ES LA MÁS CAPAZ DE LA FAMILIA**: **una malla de bloques lógicos y conexiones que se
  configura para ser el circuito que haga falta.**
- **POR QUÉ REAPARECE EN MANTENIMIENTO**: **muchos equipos de televisión llevan FPGA**, y **actualizar
  un equipo puede significar cargarle una configuración nueva**, no cambiar una pieza.

## El microprocesador

- **SUS TRES BLOQUES**: **unidad de control, unidad aritmético-lógica y registros.**
- **EL CICLO DE INSTRUCCIÓN**: **buscar, decodificar, ejecutar y guardar.**
- **LOS TRES BUSES**: **de datos** —qué se transporta—, **de direcciones** —a dónde— **y de control**
  —qué se hace.
- **EL DATO QUE RELACIONA BUS Y MEMORIA**: **con *n* líneas de direcciones se puede direccionar 2
  elevado a *n* posiciones.** **Es la misma potencia de dos del tema 12 con las máscaras de red.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 36 | Qué es una memoria caché | c) Memoria de alta velocidad y pequeña para los datos de uso frecuente ✔ |

**La única oficial es correcta** y **no descansa sólo en la plantilla.** · **Aviso de estudio, dicho
sin adornos**: **dos puntos del anexo y una pregunta.** **Conviene quedarse con la jerarquía de
memoria y con qué es una FPGA, y volcar el tiempo en los puntos 10, 12 y 2, que se llevan cuarenta y
cuatro preguntas entre los tres.**
