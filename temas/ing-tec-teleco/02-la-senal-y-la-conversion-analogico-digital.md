# Tema 2 del específico de Ingeniería Técnica · Telecomunicación · La señal y la conversión analógico-digital

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 2 |
| **Sirve para** | **Ing. Técnica Telecomunicación** y **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el muestreo y la cuantificación, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Punto compartido con Ing. Superior** | **Este mismo enunciado es, palabra por palabra, el punto 2 del anexo de Ingeniería Superior · Telecomunicación**, así que **el tema se comparte y sirve a las dos ocupaciones** |
| **Extensión** | **1.770 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la conversión de analógico a digital (**A/D**) y la
inversa (**D/A**); la relación entre señal y ruido (**S/N**); el decibelio (**dB**); la modulación por
impulsos codificados (**PCM**); los bits por muestra, que se abrevian por su número; y el kilohercio
(**kHz**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 2):
> «El concepto de información. Características de la comunicación. Modelo de comunicaciones. Sistemas
> analógicos y digitales. Tipos de señales. Características. Conversión analógica-digital. Conversión
> digital-analógica.»

**Este tema sirve a DOS ocupaciones**: **el enunciado de arriba es también, palabra por palabra, el
punto 2 del anexo de Ingeniería Superior · Telecomunicación**, así que **el tema se comparte con
aquella ocupación**, como se comparte el de prevención de riesgos laborales. **Nada de lo que sigue
está escrito para una sola de las dos.**

**Tres preguntas.** **Y las tres son de la misma pareja de conceptos**: **cuántas muestras por segundo
y cuántos bits por muestra.**

**Ese rasgo hace el punto extraordinariamente rentable**: **con dos fórmulas se contestan las tres**,
y **las dos fórmulas caben en dos líneas.**

<!-- indice -->

## Índice

- [1. Los dos ejes de la digitalización](#1-los-dos-ejes-de-la-digitalización)
- [2. El teorema del muestreo](#2-el-teorema-del-muestreo)
- [3. La cuantificación y el ruido](#3-la-cuantificación-y-el-ruido)
- [4. La conversión de vuelta](#4-la-conversión-de-vuelta)
- [5. El modelo de comunicaciones que el enunciado pide](#5-el-modelo-de-comunicaciones-que-el-enunciado-pide)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Los dos ejes de la digitalización

**Digitalizar es discretizar en dos ejes independientes**, y **confundirlos es el error que las tres
preguntas persiguen:**

| Eje | Operación | Qué parámetro lo fija | Qué determina |
|---|---|---|---|
| **Tiempo** | **Muestreo** | **La frecuencia de muestreo** | **Hasta qué frecuencia llega la señal** |
| **Amplitud** | **Cuantificación** | **Los bits por muestra** | **Cuánto rango dinámico hay** |

**La regla que resume la tabla y que hay que llevar aprendida**: **el muestreo decide el ANCHO DE
BANDA y la cuantificación decide el RUIDO.** **Cambiar uno no arregla lo del otro.**

**La pregunta 20**: **para aumentar el rango dinámico de una conversión de analógico a digital de
audio hay que aumentar los bits de resolución.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son exactamente el error que la tabla evita:**

| Opción | Qué cambia de verdad |
|---|---|
| **La frecuencia de muestreo** | **El ancho de banda, no el rango dinámico** |
| **La amplitud de la señal** | **El nivel, no el rango que el sistema puede representar** |
| **Invertir la fase** | **Nada relevante para esto** |
| **Aumentar los bits de resolución** | **El rango dinámico** ✔ |

**La opción de la amplitud es la trampa fina**: **subir el nivel de entrada mejora la relación entre
señal y ruido de esa grabación concreta**, y **eso no es lo mismo que aumentar el rango dinámico del
sistema**, que es lo que la pregunta dice.

## 2. El teorema del muestreo

**La pregunta 38**: **la afirmación de que la reconstrucción exacta de una señal en banda base a
partir de sus muestras es posible si la señal está limitada en banda y la tasa de muestreo es superior
al doble de su ancho de banda es el teorema de Nyquist-Shannon.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son nombres de otras materias**: **Beranek es de acústica de salas,
Cauchy es de análisis matemático y el cuarto nombre no corresponde a ningún teorema de esta
materia.**

**Las tres consecuencias del teorema que un ingeniero usa a diario:**

| Consecuencia | Qué obliga |
|---|---|
| **La frecuencia más alta representable es la mitad de la de muestreo** | **A 48 kHz de muestreo, el límite son 24 kHz** |
| **Lo que pase de ese límite se dobla hacia abajo** | **A eso se le llama solapamiento, y produce frecuencias que no estaban** |
| **Por eso hay un filtro antes del conversor** | **Un filtro paso bajo que corta antes de la mitad de la frecuencia de muestreo** |

**El aviso que hace útil el teorema y que las preguntas no cubren**: **el filtro no es opcional.**
**Sin él, una señal por encima del límite no se pierde: APARECE dentro de la banda útil como una
frecuencia falsa**, y ya no hay manera de distinguirla de una real.

**Las frecuencias de muestreo corrientes, para situar cualquier cifra que pongan:**

| Frecuencia | Dónde se usa |
|---|---|
| **44,1 kHz** | **Disco compacto** |
| **48 kHz** | **Vídeo y audio profesional** |
| **96 y 192 kHz** | **Producción de alta resolución** |

## 3. La cuantificación y el ruido

**La pregunta 69**: **el mínimo número de bits de muestreo para conseguir una relación entre señal y
ruido de 60 dB o superior es 10.** Ésa es la respuesta oficial.

---

**Y se calcula, no se memoriza.** **La fórmula es una sola:**

> **Relación entre señal y ruido, en decibelios ≈ 6,02 × número de bits + 1,76**

**Con ella se comprueban las cuatro opciones:**

| Bits | Relación resultante | ¿Llega a 60 dB? |
|---|---|---|
| **6** | **≈ 37,9 dB** | **No** |
| **8** | **≈ 49,9 dB** | **No** |
| **10** | **≈ 62,0 dB** | **Sí** ✔ |
| **12** | **≈ 74,0 dB** | **Sí, pero no es el MÍNIMO** |

**La palabra que decide es «mínimo»**: **doce bits también cumplen, y por eso la pregunta no está mal
construida**: pide el menor de los que cumplen.

**El atajo que evita hacer la cuenta**: **cada bit añade aproximadamente 6 decibelios.** **Diez bits
son unos sesenta**, y **con el término independiente sobra.** **Ocho bits son unos cuarenta y ocho, y
no llegan.**

**Las cifras que conviene tener memorizadas de esa regla:**

| Bits | Rango dinámico aproximado |
|---|---|
| **8** | **48 dB** |
| **10** | **60 dB** ✔ |
| **16** | **96 dB** |
| **24** | **144 dB** |

**Y el matiz que un ingeniero debe saber aunque el examen no lo pida**: **la fórmula da el máximo
teórico con una señal sinusoidal que ocupe toda la escala.** **En la práctica se trabaja con margen y
la relación real es menor.**

## 4. La conversión de vuelta

**El enunciado pide expresamente la conversión de digital a analógico y el examen no la ha
preguntado.** **Lo mínimo que conviene llevar visto:**

**Los tres pasos, en orden:**

1. **Reconstrucción de la escalera**: el conversor mantiene cada valor hasta la muestra siguiente.
2. **Filtrado de reconstrucción**: un filtro paso bajo suaviza esa escalera y elimina las imágenes
   espectrales que el muestreo generó.
3. **Amplificación de salida** al nivel que la línea necesita.

**El error que aparece en este lado y que en el de entrada no existe**: **la distorsión de apertura.**
**Mantener cada valor durante todo el periodo de muestra atenúa las frecuencias altas**, y **los
conversores lo compensan con un filtro que hace lo contrario.**

**Y la sobremuestreo, que es lo que hace posible el audio digital barato**: **muestrear internamente a
muchas veces la frecuencia nominal permite usar filtros analógicos suaves**, en vez de los filtros
abruptos que harían falta justo por encima del límite. **La complejidad se pasa del componente
analógico al proceso digital**, que es mucho más barato.

## 5. El modelo de comunicaciones que el enunciado pide

**El enunciado empieza por «el concepto de información» y el examen no ha entrado.** **El modelo que
un examen puede pedir es el clásico de cinco bloques:**

| Bloque | Qué hace |
|---|---|
| **Fuente** | **Genera el mensaje** |
| **Transmisor** | **Lo adapta al canal**: codifica y modula |
| **Canal** | **Lo transporta, y añade ruido** |
| **Receptor** | **Deshace lo que el transmisor hizo** |
| **Destino** | **Recibe el mensaje** |

**Y los tres conceptos de información que conviene tener vistos:**

| Concepto | Qué mide |
|---|---|
| **Cantidad de información de un símbolo** | **Cuánto sorprende**: menos probable, más información |
| **Entropía** | **La información media por símbolo de una fuente** |
| **Capacidad del canal** | **El caudal máximo que un canal admite sin errores, dado su ancho de banda y su ruido** |

**La consecuencia práctica que enlaza este epígrafe con todo el temario**: **la capacidad de un canal
crece con el ancho de banda y con la relación entre señal y ruido**, y **por eso una modulación con
más bits por símbolo exige mejor relación señal-ruido.** **Es la misma regla que explica por qué la
microfonía inalámbrica del tema 12 elige una modulación robusta y la televisión digital terrestre del
tema 5 elige una densa.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 20 | Cómo aumentar el rango dinámico de una conversión | d) Aumentar los bits de resolución ✔ |
| 38 | De qué teorema es el enunciado citado | b) Nyquist-Shannon ✔ |
| 69 | Bits mínimos para 60 dB de relación señal-ruido | a) 10 ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **con la tabla de los dos ejes y la regla de los seis decibelios por bit se
contestan las tres preguntas.** **Es el punto de mejor rendimiento por minuto de la ocupación.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **El teorema del muestreo y la fórmula de la relación señal-ruido son resultados clásicos del
   tratamiento de señales**, presentados como conocimiento común. **Ninguna fuente se ha
   consultado.**
2. **El cálculo de la pregunta 69 no se toma de ninguna fuente: se hace**, y **sus cuatro resultados
   quedan escritos para que se pueda comprobar.** **El de la opción marcada coincide con la respuesta
   oficial.**
3. **Las frecuencias de muestreo corrientes y las equivalencias de bits a rango dinámico son de uso
   universal**, dadas como referencia. **Ninguna respuesta oficial depende de ellas más allá del
   cálculo anterior.**
4. **El modelo de comunicaciones de cinco bloques y los tres conceptos de información son teoría
   clásica**, y **el examen no ha entrado por ahí.** **Se desarrollan por estar en el enunciado.**

**El resto del tema va como oficio y así se declara**: la advertencia de que la amplitud de entrada no
es el rango dinámico del sistema, el aviso sobre el filtro previo al conversor, el atajo de los seis
decibelios por bit, la distorsión de apertura, la explicación del sobremuestreo y el enlace entre
capacidad de canal y elección de modulación. **Nada de eso está en un boletín oficial ni en una norma
técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
