# Tema 5 del específico de Ingeniería Técnica · Telecomunicación · Difusión terrestre y por satélite

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · puntos 5 y 6 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son las normas de difusión terrestre y por satélite, **de acceso restringido**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Dos puntos en uno** | **Los enunciados 5 y 6 son la misma frase con el medio cambiado**, y separarlos daría dos temas que se repetirían |
| **Extensión** | **1.859 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la televisión digital terrestre (**TDT**); la
difusión de vídeo digital terrestre en sus dos generaciones (**DVB-T** y **DVB-T2**) y por satélite
(**DVB-S** y **DVB-S2**); la multiplexación por división de frecuencias ortogonales codificada
(**COFDM**); la modulación de amplitud en cuadratura (**QAM**) y la de desplazamiento de fase
(**PSK**); la modulación de frecuencia (**FM**); el formato de intercambio de material (**MXF**), que
aparece como opción falsa; la modulación por desplazamiento mínimo gaussiano (**GMSK**), que también;
la codificación de vídeo avanzada (**AVC**); el intervalo de guarda (**IG**); los dos códigos de corrección de errores que la segunda
generación usa —la comprobación de paridad de baja densidad y el código de Bose, Chaudhuri y
Hocquenghem (**BCH**)—; y el gigahercio (**GHz**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, puntos 5 y 6):
> «5. Televisión digital terrestre (TDT). Características, estándares, sistemas de transmisión y
> distribución primaria de televisión digital.»
>
> «6. Televisión digital Satélite (DVB-S). Características, estándares, sistemas de transmisión y
> distribución primaria de televisión digital.»

**Tres preguntas, las tres del punto 5.** **Del punto 6 no ha caído ninguna en este tema**, aunque
**una pregunta sobre bandas de satélite sí ha caído, y va en el tema 14**, con las antenas y los
transmisores.

**Este tema reúne los dos puntos del anexo porque sus enunciados son la misma frase con el medio
cambiado**: **«características, estándares, sistemas de transmisión y distribución primaria de
televisión digital».** **Separarlos daría dos temas que se repetirían entre sí**, que es lo que el
método de este proyecto prohíbe.

<!-- indice -->

## Índice

- [1. Los dos medios, uno frente a otro](#1-los-dos-medios-uno-frente-a-otro)
- [2. La modulación terrestre](#2-la-modulación-terrestre)
- [3. Las dos generaciones terrestres](#3-las-dos-generaciones-terrestres)
- [4. La modulación por satélite](#4-la-modulación-por-satélite)
- [5. La distribución primaria](#5-la-distribución-primaria)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Los dos medios, uno frente a otro

| | **Terrestre** | **Satélite** |
|---|---|---|
| **Qué estorba** | **Los ecos: la señal llega por varios caminos** ✔ | **La lluvia y el ruido térmico: la señal llega muy débil** |
| **Modulación** | **Multiportadora, con intervalo de guarda** ✔ | **Monoportadora, por fase** |
| **Ancho de banda por canal** | **8 megahercios** | **Decenas de megahercios** |
| **Cobertura** | **Por emisores, con red de frecuencia única** | **Un haz cubre un país entero** |
| **Recepción** | **Antena de tejado** | **Parabólica orientada** |

**La regla que explica las dos filas primeras y que es toda la clave del punto**: **cada medio se
defiende de su enemigo.** **En tierra el enemigo es el eco, y la defensa es repartir la información
entre muchas portadoras lentas.** **En satélite el enemigo es la debilidad de la señal, y la defensa
es una modulación sencilla y robusta con mucha corrección de errores.**

## 2. La modulación terrestre

**La pregunta 42**: **el tipo de modulación que se usa en televisión digital terrestre de primera
generación es COFDM.** Ésa es la respuesta oficial.

**La pregunta 26**: **esa modulación se utiliza para mejorar la resistencia a las interferencias por
multitrayecto.** Ésa es la respuesta oficial.

---

**Las dos son la misma materia: qué se usa y por qué.** **Y las tres opciones falsas de la primera son
tres siglas de otras materias**: **una modulación analógica, un formato de fichero y una modulación de
telefonía móvil.**

**Cómo funciona, en cuatro pasos, que es lo que hace entendible la respuesta de la segunda:**

1. **En vez de una portadora rápida, se usan miles de portadoras lentas** repartidas por el canal.
2. **Cada una lleva poquísima información**, de modo que **su símbolo dura mucho tiempo.**
3. **Entre símbolo y símbolo se deja un hueco: el intervalo de guarda.**
4. **Un eco que llegue con retardo menor que ese hueco cae dentro de él y NO estorba al símbolo
   siguiente.**

**Ésa es exactamente la resistencia al multitrayecto que la respuesta oficial nombra**, y **de ahí
sale la consecuencia que hace posible la televisión digital terrestre moderna:**

**La red de frecuencia única**: **si los ecos no molestan, dos emisores pueden transmitir lo mismo en
la misma frecuencia.** **El segundo emisor es, para el receptor, un eco más.** **Con modulación
analógica eso era imposible**, y por eso cada emisor necesitaba su propia frecuencia.

**Las tres opciones falsas de la pregunta 26 y por qué caen:**

| Opción | Por qué es falsa |
|---|---|
| **Para reducir el retardo de transmisión** | **Es al revés**: el símbolo largo y el intervalo de guarda AÑADEN retardo |
| **Porque es menos compleja** | **Es mucho más compleja**: exige transformadas rápidas en los dos extremos |
| **Porque requiere menos ancho de banda** | **Ocupa el mismo canal de 8 megahercios** |

**El precio del intervalo de guarda, que conviene saber**: **es tiempo en el que no se transmite
información.** **Un intervalo largo tolera ecos más lejanos y desperdicia más caudal.** **Elegirlo es
un compromiso entre el tamaño de la red y el caudal disponible.**

## 3. Las dos generaciones terrestres

**La pregunta 44 —que se desarrolla en el tema 4— pide el formato de vídeo de la segunda
generación**, y **aquí interesa la comparación completa:**

| | **Primera generación** | **Segunda generación** |
|---|---|---|
| **Modulación de cada portadora** | **Hasta 64 estados** | **Hasta 256 estados** |
| **Corrección de errores** | **Convolucional más Reed-Solomon** | **Comprobación de paridad de baja densidad más BCH** |
| **Formato de vídeo** | **MPEG-2** | **MPEG-4 AVC** ✔ |
| **Caudal por canal** | **Unos 19,9 Mbps con los parámetros habituales** | **Hasta un 30-50 % más** |
| **Constelación rotada** | **No** | **Sí, para mejorar en canales difíciles** |

**La regla que resume el salto de generación**: **la segunda no cambia el principio, lo afina.**
**Misma multiportadora, mismo intervalo de guarda, misma idea de red de frecuencia única**, pero
**mejor corrección de errores y modulación más densa.** **De ahí sale el caudal extra que hace posible
la alta definición en el mismo canal.**

**Y la relación entre modulación densa y robustez, que es la misma regla de todo el temario**:
**cuantos más estados por símbolo, más caudal y menos margen frente al ruido.** **Una constelación de
256 estados exige una relación señal-ruido que muchas recepciones domésticas no tienen**, y por eso
la elección de parámetros es una decisión de cobertura, no de laboratorio.

## 4. La modulación por satélite

**El punto 6 del anexo no ha dado preguntas, y conviene tener lo mínimo:**

| | **DVB-S** | **DVB-S2** |
|---|---|---|
| **Modulación** | **Por desplazamiento de fase en cuadratura** | **La misma, más de 8 y 16 estados** |
| **Corrección de errores** | **Convolucional más Reed-Solomon** | **Comprobación de paridad de baja densidad más BCH** |
| **Codificación y modulación adaptativas** | **No** | **Sí** |
| **Ganancia de caudal** | **—** | **Alrededor de un 30 %** |

**Por qué el satélite usa modulación por fase y no por amplitud**: **porque el amplificador del
satélite trabaja cerca de la saturación para aprovechar la potencia**, y **en saturación la amplitud
no se conserva.** **Una modulación que sólo usa la fase sobrevive a eso; una que usa la amplitud, no.**

**Y la codificación adaptativa de la segunda generación merece una línea**: **el sistema mide la
calidad del enlace de cada receptor y le manda la modulación que puede recibir.** **Con buen tiempo,
más caudal; con lluvia, más robustez.** **Eso no se puede hacer en difusión pura**, y por eso se usa
sobre todo en contribución y en servicios de datos.

## 5. La distribución primaria

**Los dos enunciados del anexo terminan con las mismas tres palabras**, y **son las que definen el
oficio de esta ocupación:**

**Qué es la distribución primaria**: **el transporte de la señal desde el centro de producción hasta
los centros emisores.** **No la ve el espectador y es donde una avería deja una región entera sin
televisión.**

| Medio de distribución primaria | Rasgo |
|---|---|
| **Fibra óptica** | **El habitual hoy: capacidad y fiabilidad** |
| **Radioenlace** | **Donde la fibra no llega o como respaldo** |
| **Satélite** | **Cobertura amplia de una vez, y respaldo de los otros dos** |

**Los tres principios que gobiernan su diseño y que un ingeniero debe saber enunciar:**

1. **Redundancia de camino**: **dos rutas físicamente distintas, no dos fibras en la misma zanja.**
2. **Conmutación automática**: **el cambio a la ruta de respaldo no puede depender de que alguien lo
   vea.**
3. **Supervisión extremo a extremo**: **saber que la ruta de respaldo funciona ANTES de necesitarla.**

**El aviso que resume el epígrafe**: **una ruta de respaldo que no se prueba no es una ruta de
respaldo.** **Es la misma idea que la prueba de restauración de una copia de seguridad**, y falla por
la misma razón: **nadie la comprueba hasta el día que hace falta.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 26 | Por qué se usa esa modulación en la terrestre de primera generación | a) Para mejorar la resistencia al multitrayecto ✔ |
| 42 | Qué modulación se usa en televisión digital terrestre | d) COFDM ✔ |
| 44 | Formato de vídeo de la terrestre de segunda generación | b) MPEG-4 AVC ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **La 44 se
desarrolla en el tema 4**, con los estándares de compresión, y **aquí se recoge por pertenecer también
a este punto.**

**El aviso de estudio**: **los cuatro pasos de la multiportadora contestan las dos preguntas del punto
y explican la red de frecuencia única**, que es lo más preguntable de lo que no ha caído.

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Las normas de la familia de difusión de vídeo digital no se han consultado.** **El principio de
   la multiportadora, el intervalo de guarda y la red de frecuencia única son de uso universal en el
   sector**, y **coinciden con las respuestas oficiales.**
2. **Las cifras del epígrafe 3 —los estados de constelación, el caudal aproximado por canal y la
   ganancia de la segunda generación— son órdenes de magnitud de uso corriente**, dados como
   referencia. **Ninguna respuesta oficial depende de ellas.**
3. **El epígrafe 4 desarrolla el punto 6 del anexo, que no ha dado ninguna pregunta**, y **su
   contenido se presenta como conocimiento común de la materia.**
4. **Los tres principios de diseño de la distribución primaria son oficio de ingeniería de
   instalaciones**, escritos a partir del propio enunciado del anexo. **No describen la red de ninguna
   casa concreta**, que no se ha consultado.

**El resto del tema va como oficio y así se declara**: la regla de que cada medio se defiende de su
enemigo, la explicación en cuatro pasos de por qué la multiportadora resiste los ecos, la consecuencia
de la red de frecuencia única, el precio en caudal del intervalo de guarda, la razón de que el
satélite module en fase y el aviso sobre las rutas de respaldo que nadie prueba. **Nada de eso está en
un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
