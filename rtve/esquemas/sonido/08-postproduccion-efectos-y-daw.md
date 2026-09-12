# Esquema · Tema 8 del específico de Sonido · Postproducción, efectos sonoros y estación de trabajo

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de postproducción · `[plan]` =
plantilla oficial. **Siglas**: la estación de trabajo de audio digital (**DAW**, *digital audio
workstation*); los golpes por minuto (**BPM**, *beats per minute*); los milisegundos (**ms**); el
kilohercio (**kHz**) y el hercio (**Hz**).

**Cabecera.** Enunciados: puntos 6 y 16 del anexo, «Postproducción y efectos sonoros» y «Operación DAW» · **2 preguntas**
· **las dos son cálculo, y las dos tienen una salvedad que el temario declara.**

<!-- indice -->

## Índice

- [El delay a tempo](#el-delay-a-tempo)
- [La latencia de la estación de trabajo](#la-latencia-de-la-estación-de-trabajo)
- [La cadena de postproducción](#la-cadena-de-postproducción)
- [Los efectos y sus familias](#los-efectos-y-sus-familias)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El delay a tempo

- **PREGUNTA 15** · `[of]` · **A 102 golpes por minuto, un retardo de corchea dura aproximadamente 294
  milisegundos.**
- **LA CUENTA**: **la negra dura 60.000 dividido entre los golpes por minuto** —60.000 ÷ 102 ≈ 588 ms—
  **y la corchea es su mitad**: 294 ms.
- **LA TABLA QUE VALE PARA CUALQUIER TEMPO**: **redonda = 4 negras · blanca = 2 negras · negra =
  60.000/BPM · corchea = mitad de la negra · semicorchea = cuarta parte.**
- **POR QUÉ SE HACE ASÍ**: **un retardo a tempo suena musical y uno fuera de tempo enturbia.** **Es el
  ajuste más frecuente de una sesión de mezcla.**

## La latencia de la estación de trabajo

- **PREGUNTA 36** · `[plan]` · **La fórmula de la latencia de un búfer es muestras × 1.000 ÷ frecuencia
  de muestreo.**
- **SALVEDAD DECLARADA**: **la fórmula sólo da milisegundos si la frecuencia va en hercios**, y **el
  enunciado la escribe en kilohercios.** **Con 128 muestras a 48.000 Hz salen 2,67 ms; con 48 kHz
  metidos tal cual en la fórmula saldría un número mil veces mayor.** **El temario lo declara y
  sostiene la respuesta oficial, que es la única de las cuatro con la estructura correcta.**
- **DE QUÉ DEPENDE LA LATENCIA**: **del tamaño del búfer y de la frecuencia de muestreo, y de nada
  más.** **Búfer grande, sistema estable y latencia alta; búfer pequeño, latencia baja y riesgo de
  cortes.**
- **LA REGLA DE TRABAJO**: **búfer pequeño para grabar** —porque el músico se oye— **y búfer grande
  para mezclar** —porque hay muchos procesos y nadie está tocando.

## La cadena de postproducción

- **EL ORDEN HABITUAL**: **montaje de diálogos, limpieza y sustitución, efectos de sala, ambientes,
  música, mezcla y control de sonoridad.**
- **DÓNDE ENLAZA CON EL TEMA 14**: **el último paso de esa cadena es normalizar el nivel de sonoridad**,
  que es lo que la recomendación R 128 regula.

## Los efectos y sus familias

| Familia | Qué hace | Ejemplos |
|---|---|---|
| **De tiempo** | **Retrasa o repite** | **Retardo, reverberación** |
| **De modulación** | **Mueve un parámetro con un oscilador** | **Chorus, flanger, phaser** |
| **De dinámica** | **Cambia la relación entre fuerte y suave** | **Compresor, puerta, limitador** |
| **De espectro** | **Cambia el reparto por frecuencias** | **Ecualizador, filtros** |

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 15 | Duración de un delay de corchea a 102 BPM | b) 294 ms ✔ |
| 36 | Fórmula de la latencia de un búfer de 128 muestras | b) Muestras × 1.000 ÷ frecuencia ✔ **·** con salvedad |

**Las dos oficiales son correctas** · **una con la salvedad de unidades declarada.** · **Aviso de
estudio**: **el punto tiene dos preguntas y las dos son cuenta**: **quien lleve las dos fórmulas
memorizadas las gana las dos.**
