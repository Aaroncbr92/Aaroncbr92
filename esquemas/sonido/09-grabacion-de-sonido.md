# Esquema · Tema 9 del específico de Sonido · Grabación de sonido

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio y audio digital. **Siglas**: el
códec libre de audio sin pérdida (**FLAC**, *free lossless audio codec*); el formato de fichero de onda (**WAV**) y el de fichero de
intercambio de audio (**AIFF**); la codificación avanzada de audio (**AAC**, *advanced audio coding*),
la capa 3 del estándar del grupo de expertos en imágenes en movimiento (**MP3**) y el códec de audio
sin pérdida de Apple (**ALAC**); el megabyte (**MB**); el
kilohercio (**kHz**); el decibelio (**dB**); y los fotogramas por segundo (**fps**).

**Cabecera.** Enunciado: «1.10. Grabación de sonido» · **4 preguntas** · **tres son cálculo y una es
de códecs.**

<!-- indice -->

## Índice

- [De qué está hecho un fichero de audio](#de-qué-está-hecho-un-fichero-de-audio)
- [La cuenta del tamaño](#la-cuenta-del-tamaño)
- [El rango dinámico y los bits](#el-rango-dinámico-y-los-bits)
- [Con pérdida y sin pérdida](#con-pérdida-y-sin-pérdida)
- [Muestras, segundos y fotogramas](#muestras-segundos-y-fotogramas)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## De qué está hecho un fichero de audio

- **TRES NÚMEROS Y NADA MÁS**: **frecuencia de muestreo, profundidad de bits y número de canales.**
- **CON ESOS TRES SE CALCULA TODO LO DEMÁS**: **el tamaño, el caudal y el rango dinámico.**

## La cuenta del tamaño

- **LA FÓRMULA**: **frecuencia × bits × canales × segundos ÷ 8 = bytes.**
- **PREGUNTA 92** · `[of]` · **Un estéreo de 44,1 kHz, 16 bits y 5 minutos ocupa aproximadamente 50
  MB.**
- **LA CUENTA**: **44.100 × 16 × 2 × 300 ÷ 8 ≈ 52,9 millones de bytes**, es decir **unos 50
  mebibytes.**
- **EL ATAJO PARA EL EXAMEN**: **un minuto de estéreo a calidad de disco compacto ocupa unos 10
  MB.** **Cinco minutos, unos 50.**

## El rango dinámico y los bits

- **LA REGLA**: **cada bit son aproximadamente 6 decibelios de rango dinámico teórico.**
- **PREGUNTA 68** · `[of]` · **El rango dinámico teórico de 16 bits es 96 dB.** **16 × 6 = 96.**
- **DE AHÍ SALEN LAS DEMÁS**: **24 bits ≈ 144 dB · 20 bits ≈ 120 dB · 8 bits ≈ 48 dB.**

## Con pérdida y sin pérdida

| Familia | Qué hace | Ejemplos |
|---|---|---|
| **Sin comprimir** | **Guarda las muestras tal cual** | **WAV, AIFF** |
| **Comprimido sin pérdida** | **Comprime y devuelve el original bit a bit** | **FLAC, ALAC** |
| **Comprimido con pérdida** | **Tira lo que el oído no percibe y no lo devuelve** | **MP3, AAC** |

- **PREGUNTA 83** · `[of]` · **El códec con el que el audio no sufre pérdida de calidad es FLAC.**
- **LA PALABRA QUE LO DELATA ESTÁ EN SU PROPIO NOMBRE**: *lossless*, **sin pérdida.**
- **AVISO DE OFICIO**: **sin comprimir y sin pérdida no son lo mismo.** **El primero no comprime
  nada; el segundo comprime y no pierde.**

## Muestras, segundos y fotogramas

- **PREGUNTA 8** · `[of]` · **13.440 muestras a 48 kHz, con 25 fotogramas por segundo, duran 7
  fotogramas.**
- **LA CUENTA EN DOS PASOS**: **13.440 ÷ 48.000 = 0,28 segundos**; **0,28 × 25 = 7 fotogramas.**
- **EL DATO QUE HAY QUE LLEVAR SABIDO**: **a 48 kHz y 25 fotogramas, cada fotograma son exactamente
  1.920 muestras.** **13.440 ÷ 1.920 = 7**, y sale en un paso.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 8 | Duración en fotogramas de 13.440 muestras a 48 kHz | b) 7 ✔ |
| 68 | Rango dinámico teórico de 16 bits | c) 96 dB ✔ |
| 83 | Códec sin pérdida de calidad | d) FLAC ✔ |
| 92 | Tamaño de un estéreo de 44,1 kHz, 16 bits y 5 minutos | c) Aproximadamente 50 MB ✔ |

**Las cuatro oficiales son correctas** y **ninguna descansa sólo en la plantilla.** · **Aviso de
estudio**: **tres fórmulas —tamaño, rango dinámico y muestras por fotograma— contestan tres de las
cuatro preguntas.** **Es el punto de mayor rendimiento por fórmula del volumen.**
