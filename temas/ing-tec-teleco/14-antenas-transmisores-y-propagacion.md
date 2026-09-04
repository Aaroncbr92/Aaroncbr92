# Tema 14 del específico de Ingeniería Técnica · Telecomunicación · Antenas, transmisores y propagación

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 18 |
| **Sirve para** | **Ing. Técnica Telecomunicación** y **Ing. Superior Telecomunicación** |
| **Punto compartido con Ing. Superior** | **Este mismo enunciado es el punto 25 del anexo de Ingeniería Superior · Telecomunicación**, palabra por palabra —con un solo signo de puntuación distinto—, así que **el tema se comparte y sirve a las dos ocupaciones** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la radiocomunicación clásica, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Pregunta ajena declarada** | **La pregunta 75, por el reóstato, no pertenece a ningún punto del anexo.** Se clasifica aquí por proximidad con los instrumentos y los componentes, **y se declara** |
| **Extensión** | **2.279 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la modulación de amplitud (**AM**) y la de frecuencia
(**FM**); la onda corta (**OC**); la relación de onda estacionaria (**ROE**); el decibelio respecto a
un radiador isótropo (**dBi**) y respecto a un dipolo (**dBd**); la potencia radiada aparente
(**PRA**) y la isótropa equivalente (**PIRE**); la radiofrecuencia (**RF**); el gigahercio (**GHz**) y
el megahercio (**MHz**); las bandas de satélite, que se nombran por su letra (**banda C**, **banda
Ku** y **banda Ka**); y las clases de amplificador, que también se nombran por letra (**clase
A**, **clase B**, **clase AB**, **clase C** y **clase D**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 18):
> «Antenas y transmisores de radiodifusión: Líneas de transmisión. Guías de onda. Sistemas de
> comunicación por satélite. Comunicaciones en Onda Corta. Antenas, ganancia de una antena y tipos de
> antenas para las distintas bandas y servicios. Sistemas radiantes en las distintas bandas.
> Transmisores de modulación de amplitud y de modulación de frecuencia. Distorsiones y parámetros de
> la señal de audio. Medida de las distorsiones y parámetros. Instrumentos de medida.»

**Este tema sirve a DOS ocupaciones**: **el enunciado de arriba es también, palabra por palabra —con
un solo signo de puntuación distinto—, el punto 25 del anexo de Ingeniería Superior ·
Telecomunicación**, así que **el tema se comparte con aquella ocupación**, como se comparte el de
prevención de riesgos laborales. **Nada de lo que sigue está escrito para una sola de las dos.**

**Tres preguntas.** **Y el enunciado nombra diez asuntos**, así que **es, con el 10, el punto con peor
relación entre lo enunciado y lo preguntado de la ocupación.**

**Su reparto**: **una es de bandas de satélite**, **una de clases de amplificador** y **una de un
componente elemental.** **De antenas, de guías de onda, de onda corta y de medida de distorsiones no
ha caído ninguna.**

**Un aviso sobre la tercera**: **la pregunta por el reóstato no encaja en ningún punto del anexo.**
**Se clasifica aquí, con los instrumentos y los componentes, porque es donde menos violenta encaja**,
y **el temario lo declara.**

<!-- indice -->

## Índice

- [1. Las bandas de satélite](#1-las-bandas-de-satélite)
- [2. Los amplificadores y sus clases](#2-los-amplificadores-y-sus-clases)
- [3. El componente que la pregunta 75 pide](#3-el-componente-que-la-pregunta-75-pide)
- [4. Las antenas y su ganancia](#4-las-antenas-y-su-ganancia)
- [5. Las líneas de transmisión y las guías de onda](#5-las-líneas-de-transmisión-y-las-guías-de-onda)
- [6. Los transmisores de radiodifusión](#6-los-transmisores-de-radiodifusión)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Las bandas de satélite

**La pregunta 68**: **los satélites que trabajan en banda Ku se caracterizan por un enlace ascendente
de 14 GHz y un descendente de 12 GHz.** Ésa es la respuesta oficial.

---

**Y ésta es la tabla que hay que llevar, porque de ella salen las cuatro opciones:**

| Banda | Ascendente | Descendente | Rasgo |
|---|---|---|---|
| **C** | **6 GHz** | **4 GHz** | **Poco afectada por la lluvia; antenas grandes** |
| **Ku** | **14 GHz** ✔ | **12 GHz** | **Antenas pequeñas; la lluvia atenúa** |
| **Ka** | **30 GHz** | **20 GHz** | **Antenas muy pequeñas; la lluvia atenúa mucho** |

**Las dos reglas que la hacen memorizable:**

1. **El ascendente es SIEMPRE mayor que el descendente.** **Y la razón es de ingeniería, no de
   capricho**: **la estación terrena tiene potencia y espacio de sobra; el satélite no.** **Se le pone
   la frecuencia más alta —y por tanto la más difícil— al extremo que puede permitírselo.**
2. **Al subir de banda, las antenas se hacen pequeñas y la lluvia empieza a molestar.** **Es el mismo
   compromiso repetido tres veces.**

**Y la opción falsa de 2,5 y 2,2 gigahercios es la que delata**: **son frecuencias de otros servicios,
no de comunicación por satélite fija.**

**El fenómeno que este epígrafe deja como aviso y que es el que decide el diseño de un enlace**: **la
atenuación por lluvia.** **En banda C es despreciable; en Ku obliga a dejar margen; en Ka puede cortar
el enlace.** **Por eso una contribución de televisión seria por satélite sigue haciéndose en Ku con
margen sobrado, o en C donde la fiabilidad manda sobre el tamaño de la antena.**

## 2. Los amplificadores y sus clases

**La pregunta 73**: **un amplificador de clase C se caracteriza por un alto rendimiento y una gran
generación de armónicos.** Ésa es la respuesta oficial.

---

**Y la clasificación entera es la que ordena el epígrafe**, con el criterio que la define: **cuánta
parte del ciclo de la señal conduce el elemento activo.**

| Clase | Cuánto conduce | Rendimiento | Distorsión | Dónde se usa |
|---|---|---|---|---|
| **A** | **El ciclo entero** | **Bajo: hasta 25-50 %** | **Mínima** | **Audio de precisión, pequeña señal** |
| **B** | **Medio ciclo** | **Medio: hasta 78 %** | **Cruce por cero** | **Etapas de salida en contrafase** |
| **AB** | **Algo más de medio** | **Entre las dos** | **Corrige el cruce** | **La mayoría del audio de potencia** |
| **C** | **Menos de medio ciclo** | **Alto: por encima del 80 %** ✔ | **Mucha: genera armónicos** ✔ | **Radiofrecuencia con portadora sintonizada** |
| **D** | **Conmuta: no es lineal** | **Muy alto: más del 90 %** | **La del filtrado de salida** | **Audio de potencia moderno y radiofrecuencia** |

**Y la pregunta que cualquiera se hace al ver la clase C**: **si distorsiona tanto, ¿para qué sirve?**
**La respuesta es la razón de su existencia**: **en radiofrecuencia, la salida va a un circuito
resonante sintonizado a la frecuencia de trabajo.** **Ese circuito filtra los armónicos y devuelve una
sinusoide limpia.** **La distorsión se genera y se elimina**, y el rendimiento se queda.

**Por eso no sirve para audio**: **una señal de audio ocupa una banda ancha y no se puede filtrar
así.** **Ésa es toda la diferencia entre las dos aplicaciones**, y es lo que hace falsa la opción de
la «absoluta linealidad para amplificadores de estudio».

**Las otras dos opciones falsas y por qué caen**: **el bajo rendimiento es de la clase A**, y **la
elevada temperatura en ausencia de señal también**: **una clase A consume lo mismo con señal y sin
ella**, mientras que **una clase C en reposo no conduce y no calienta.**

## 3. El componente que la pregunta 75 pide

**La pregunta 75**: **un reóstato es un resistor variable.** Ésa es la respuesta oficial.

---

**Hay que decir lo que es**: **una pregunta de electrónica elemental que no pertenece a ningún punto
de este anexo.** **Se clasifica aquí por proximidad con los instrumentos y los componentes de
radiofrecuencia**, y **el temario lo declara** en vez de inventarle un encaje.

**La respuesta es correcta y no admite discusión**, y **conviene añadir la distinción que la hace
útil:**

| Componente | Qué es | Cuántos terminales usa |
|---|---|---|
| **Reóstato** | **Resistor variable usado para regular CORRIENTE** ✔ | **Dos** |
| **Potenciómetro** | **El mismo componente usado como divisor de TENSIÓN** | **Tres** |

**Son físicamente el mismo elemento con dos conexiones distintas**, y **la palabra dice cómo está
conectado, no cómo está fabricado.** **Un reóstato de potencia se construye con hilo bobinado para
disipar calor**, y ésa es la diferencia práctica con el potenciómetro de un mando de volumen.

**Las tres opciones falsas son tres componentes reales**: **un condensador variable, un aparato de
medida y un control de temperatura.** **La palabra que decide es «resistor».**

## 4. Las antenas y su ganancia

**El enunciado las pide expresamente y el examen no ha entrado.** **Lo mínimo que conviene llevar
visto:**

**Qué es la ganancia de una antena, dicho con precisión**: **una antena no amplifica.** **Concentra:
manda hacia una dirección la potencia que un radiador ideal repartiría por igual en todas.** **La
ganancia mide cuánto concentra.**

| Referencia | Qué significa |
|---|---|
| **Decibelio respecto a radiador isótropo** | **Comparada con una fuente que radia igual en todas direcciones** |
| **Decibelio respecto a dipolo** | **Comparada con un dipolo de media onda** |

**La conversión que el examen puede pedir**: **la ganancia expresada respecto al dipolo es 2,15
decibelios menor que la expresada respecto al radiador isótropo**, porque **el propio dipolo tiene esa
ganancia.**

**Los tipos de antena por banda y servicio, que es lo que el enunciado nombra:**

| Servicio | Antena típica |
|---|---|
| **Radiodifusión en amplitud modulada** | **Mástil radiante: la propia torre es la antena** |
| **Radiodifusión en frecuencia modulada** | **Dipolos o paneles, apilados para dirigir hacia el horizonte** |
| **Televisión terrestre** | **Paneles o dipolos en cortina, sobre torre** |
| **Enlaces terrestres** | **Parabólicas pequeñas, muy directivas** |
| **Satélite** | **Parabólicas, con alimentador en foco o desplazado** |

**Los tres parámetros que definen cualquier antena y que un examen puede pedir por su nombre**:
**ganancia, diagrama de radiación e impedancia de entrada.** **Y el cuarto que decide si se puede
usar: el ancho de banda.**

## 5. Las líneas de transmisión y las guías de onda

**El enunciado empieza por ellas y el examen no ha entrado.** **Los dos medios y cuándo se usa cada
uno:**

| Medio | Hasta qué frecuencia | Rasgo |
|---|---|---|
| **Línea coaxial** | **Hasta unos pocos gigahercios** | **Flexible, fácil de tender, pierde con la frecuencia** |
| **Guía de onda** | **Por encima**, en microondas | **Rígida, con muy poca pérdida, voluminosa** |

**Por qué a partir de cierta frecuencia hay que cambiar de medio**: **las pérdidas del coaxial crecen
con la frecuencia**, sobre todo por el dieléctrico, **hasta que llevar la señal cuesta más de lo que
vale.** **La guía no tiene dieléctrico ni conductor central: es un tubo por el que la onda se
propaga.**

**El parámetro que gobierna toda línea de transmisión y que hay que saber enunciar**: **la relación de
onda estacionaria.** **Mide cuánta potencia vuelve por desadaptación de impedancia.**

| Valor | Qué significa |
|---|---|
| **1 a 1** | **Adaptación perfecta: no vuelve nada** |
| **1,5 a 1** | **Aceptable en la mayoría de las instalaciones** |
| **2 a 1 o más** | **Hay un problema: conector, cable o antena** |

**Y por qué importa tanto en un transmisor de potencia**: **la potencia que vuelve se disipa en la
etapa de salida.** **Un transmisor moderno se protege reduciendo potencia o cortando**, y **una
relación alta es la avería más frecuente de un centro emisor**, casi siempre por agua en un conector
o por un latiguillo dañado.

## 6. Los transmisores de radiodifusión

**El enunciado pide los dos y el examen no ha entrado.** **La comparación mínima:**

| | **Modulación de amplitud** | **Modulación de frecuencia** |
|---|---|---|
| **Qué varía con el audio** | **La amplitud de la portadora** | **La frecuencia de la portadora** |
| **Banda que ocupa** | **Estrecha** | **Ancha** |
| **Calidad de audio** | **Limitada** | **Alta, con estéreo** |
| **Ruido** | **Le afecta directamente** | **Lo rechaza: el ruido es de amplitud** |
| **Alcance** | **Mucho, sobre todo de noche por reflexión ionosférica** | **Línea de vista, poco más del horizonte** |

**La razón de que una rechace el ruido y la otra no**: **el ruido eléctrico se suma en AMPLITUD.** **Un
receptor de frecuencia modulada limita la amplitud antes de demodular y con ella se lleva el ruido**;
**uno de amplitud no puede hacerlo sin llevarse la señal.**

**Y la comunicación en onda corta que el enunciado nombra**: **es la que aprovecha la reflexión en la
ionosfera para alcanzar miles de kilómetros con potencia moderada.** **Su alcance cambia con la hora,
la estación y el ciclo solar**, y **por eso las emisiones internacionales cambiaban de frecuencia
según el momento del día.** **Es el servicio que internet ha vaciado**, y sigue en el temario porque
sigue existiendo.

## 7. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 68 | Frecuencias de los satélites de banda Ku | d) Ascendente 14 GHz, descendente 12 GHz ✔ |
| 73 | Qué caracteriza a un amplificador de clase C | c) Alto rendimiento y gran generación de armónicos ✔ |
| 75 | Qué es un reóstato | c) Un resistor variable ✔ **·** ajena al punto |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **Una es ajena
al anexo y se declara.**

**El aviso de estudio**: **la tabla de bandas de satélite y la de clases de amplificador contestan las
dos preguntas propias del punto.** **El resto del enunciado —diez asuntos— se lee una vez y no rinde
más.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Las bandas de satélite, las clases de amplificador, la ganancia de una antena y la relación de
   onda estacionaria son teoría clásica de radiocomunicación**, presentadas como conocimiento común.
   **Ninguna fuente se ha consultado**, y **coinciden con las respuestas oficiales.**
2. **Las frecuencias del epígrafe 1 son los valores nominales de uso corriente de cada banda.** **La
   respuesta oficial de la pregunta 68 reproduce los de la banda que pregunta.**
3. **Los rendimientos del epígrafe 2 son órdenes de magnitud teóricos**, dados como referencia. **La
   respuesta oficial sólo pide si el rendimiento es alto o bajo y si hay armónicos o no.**
4. **La pregunta 75 no pertenece a este punto ni a ningún otro del anexo.** **Se clasifica aquí por
   proximidad con los instrumentos y los componentes, y el temario lo declara.** **Su respuesta es
   correcta y no admite discusión.**

**El resto del tema va como oficio y así se declara**: la razón de que el enlace ascendente vaya en la
frecuencia más alta, el compromiso entre tamaño de antena y lluvia, la explicación de por qué la clase
C sirve en radiofrecuencia y no en audio, la distinción entre reóstato y potenciómetro, la conversión
entre las dos referencias de ganancia, la razón de cambiar de coaxial a guía de onda, la avería típica
por relación de onda estacionaria y la explicación de por qué una modulación rechaza el ruido y la
otra no. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el
tema no lo presenta como si lo estuviera.
