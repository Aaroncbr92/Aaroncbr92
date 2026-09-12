# Esquema · Tema 2 del específico de Ingeniería Técnica · Telecomunicación · La señal y la conversión analógico-digital

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de telecomunicación ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: la conversión de analógico a digital (**A/D**)
y la inversa (**D/A**); la relación entre señal y ruido (**S/N**); el decibelio (**dB**); la
modulación por impulsos codificados (**PCM**); y el kilohercio (**kHz**).

**Cabecera.** Enunciado: punto 2 del anexo · **3 preguntas** · **las tres de la misma pareja de
conceptos**: cuántas muestras por segundo y cuántos bits por muestra · **con dos fórmulas se contestan
las tres**: es el punto de mejor rendimiento por minuto de la ocupación.

**Tema compartido.** **El enunciado de este punto es también, palabra por palabra, el punto 2 del
anexo de Ingeniería Superior · Telecomunicación**, así que **este esquema sirve a las dos
ocupaciones.**

<!-- indice -->

## Índice

- [Los dos ejes](#los-dos-ejes)
- [El teorema del muestreo](#el-teorema-del-muestreo)
- [Cuantificación y ruido](#cuantificación-y-ruido)
- [La conversión de vuelta](#la-conversión-de-vuelta)
- [El modelo de comunicaciones](#el-modelo-de-comunicaciones)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los dos ejes

- **LA REGLA MADRE** · `[of]` · **El muestreo decide el ANCHO DE BANDA y la cuantificación decide el
  RUIDO.** **Cambiar uno no arregla lo del otro.**

| Eje | Operación | Parámetro | Qué determina |
|---|---|---|---|
| **Tiempo** | **Muestreo** | **Frecuencia de muestreo** | **Hasta qué frecuencia llega la señal** |
| **Amplitud** | **Cuantificación** | **Bits por muestra** | **Cuánto rango dinámico hay** |

- **PREGUNTA 20** · `[exam]` · **Para aumentar el rango dinámico hay que aumentar los bits de
  resolución.**

| Opción falsa | Qué cambia de verdad |
|---|---|
| **La frecuencia de muestreo** | **El ancho de banda, no el rango dinámico** |
| **La amplitud de la señal** | **El nivel, no el rango representable** |
| **Invertir la fase** | **Nada relevante** |

- **LA TRAMPA FINA** · `[of]` · **Subir el nivel de entrada mejora la relación señal-ruido de ESA
  grabación**, y **eso no es aumentar el rango dinámico del sistema.**

## El teorema del muestreo

- **PREGUNTA 38** · `[exam]` · **Reconstrucción exacta si la señal está limitada en banda y la tasa de
  muestreo supera el doble de su ancho de banda: teorema de Nyquist-Shannon.**
- **LAS FALSAS SON DE OTRAS MATERIAS** · `[exam]` · **Beranek es acústica de salas y Cauchy es
  análisis matemático.**

| Consecuencia | Qué obliga |
|---|---|
| **La frecuencia más alta es la mitad de la de muestreo** | **A 48 kHz, el límite son 24 kHz** |
| **Lo que pase de ahí se dobla hacia abajo** | **Solapamiento: frecuencias que no estaban** |
| **Por eso hay filtro antes del conversor** | **Paso bajo que corta antes de la mitad** |

- **EL AVISO QUE NO ENTRA EN PREGUNTA Y SÍ EN OBRA** · `[of]` · **El filtro no es opcional.** **Sin él
  la señal de más allá del límite no se pierde: APARECE dentro de la banda útil**, y ya no se
  distingue de una real.

| Frecuencia | Dónde |
|---|---|
| **44,1 kHz** | **Disco compacto** |
| **48 kHz** | **Vídeo y audio profesional** |
| **96 y 192 kHz** | **Alta resolución** |

## Cuantificación y ruido

- **LA FÓRMULA, LA ÚNICA** · `[of]` · **Relación señal-ruido en decibelios ≈ 6,02 × bits + 1,76.**
- **EL ATAJO** · `[of]` · **Cada bit añade unos 6 decibelios.**

| Bits | Relación | ¿Llega a 60 dB? |
|---|---|---|
| **6** | **≈ 37,9 dB** | **No** |
| **8** | **≈ 49,9 dB** | **No** |
| **10** | **≈ 62,0 dB** | **Sí** ✔ |
| **12** | **≈ 74,0 dB** | **Sí, pero no es el MÍNIMO** |

- **PREGUNTA 69** · `[exam]` · **Mínimo número de bits para 60 dB o más: 10.**
- **LA PALABRA QUE DECIDE** · `[of]` · **«Mínimo»**: doce también cumplen, y por eso la pregunta está
  bien construida.

| Bits | Rango dinámico |
|---|---|
| **8** | **48 dB** |
| **10** | **60 dB** ✔ |
| **16** | **96 dB** |
| **24** | **144 dB** |

- **EL MATIZ DEL INGENIERO** · `[of]` · **La fórmula da el máximo teórico con sinusoide a plena
  escala.** **En obra se trabaja con margen y la relación real es menor.**

## La conversión de vuelta

- **LOS TRES PASOS** · `[of]` · **Reconstrucción de la escalera** —cada valor se mantiene hasta la
  muestra siguiente— · **filtrado de reconstrucción** —paso bajo que suaviza y quita las imágenes
  espectrales— · **amplificación de salida.**
- **EL ERROR PROPIO DE ESTE LADO** · `[of]` · **La distorsión de apertura**: **mantener el valor todo
  el periodo atenúa las frecuencias altas**, y el conversor lo compensa con un filtro que hace lo
  contrario.
- **EL SOBREMUESTREO** · `[of]` · **Muestrear internamente a muchas veces la frecuencia nominal permite
  filtros analógicos suaves** en vez de abruptos: **la complejidad se pasa de lo analógico a lo
  digital**, que es más barato.

## El modelo de comunicaciones

| Bloque | Qué hace |
|---|---|
| **Fuente** | **Genera el mensaje** |
| **Transmisor** | **Codifica y modula** |
| **Canal** | **Transporta, y añade ruido** |
| **Receptor** | **Deshace lo del transmisor** |
| **Destino** | **Recibe** |

| Concepto | Qué mide |
|---|---|
| **Cantidad de información** | **Cuánto sorprende**: menos probable, más información |
| **Entropía** | **Información media por símbolo** |
| **Capacidad del canal** | **Caudal máximo sin errores, dados ancho de banda y ruido** |

- **EL ENLACE CON TODO EL TEMARIO** · `[of]` · **La capacidad crece con el ancho de banda y con la
  relación señal-ruido**, y por eso **más bits por símbolo exigen mejor relación señal-ruido.** **Es lo
  que explica que la microfonía inalámbrica elija modulación robusta y la televisión digital terrestre
  una densa.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 20 | Cómo aumentar el rango dinámico | **Aumentar los bits de resolución** ✔ |
| 38 | De qué teorema es el enunciado | **Nyquist-Shannon** ✔ |
| 69 | Bits mínimos para 60 dB | **10** ✔ |
