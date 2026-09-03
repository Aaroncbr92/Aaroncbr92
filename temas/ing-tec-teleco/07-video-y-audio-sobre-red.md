# Tema 7 del específico de Ingeniería Técnica · Telecomunicación · Vídeo y audio sobre red

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · puntos 8 y 9 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son las familias de vídeo y audio sobre red, **tras muro de pago**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Dos puntos en uno** | **El punto 9 es la aplicación del 8**: uno da las normas y el otro dice cómo se monta una producción con ellas |
| **Extensión** | **2.624 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el protocolo de internet (**IP**) y el de datagramas
de usuario (**UDP**); la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**), que publica las
familias **SMPTE ST 2110** y **SMPTE ST 2022**; la Sociedad de Ingeniería de Audio (**AES**), que
publica **AES3** y la norma de interoperabilidad **AES67**; el protocolo de tiempo de precisión
(**PTP**); la interfaz digital serie (**SDI**) del tema 3; la modulación por impulsos codificados
(**PCM**); el grupo conjunto de expertos en fotografía y su norma del año 2000 (**JPEG 2000**); la red
de área local virtual (**VLAN**); y el descubrimiento, registro y control en red (**NMOS**, del inglés
*networked media open specifications*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, puntos 8 y 9):
> «8. Señal video IP: Señal video IP y audio IP. SMPTE 2110. SMPTE 2022. Sincronización PTP»
>
> «9. Producción audiovisual sobre infraestructura IP.»

**Cinco preguntas.** **Y es el punto que define hacia dónde va la ocupación**: **las instalaciones que
se construyen hoy son de red, y las que quedan de cable coaxial se están sustituyendo.**

**Este tema reúne los dos puntos del anexo porque el segundo es la aplicación del primero**: **uno da
las normas y el otro dice cómo se monta una producción con ellas.** **Separarlos daría dos temas que
se repetirían.**

<!-- indice -->

## Índice

- [1. Qué cambia al pasar el vídeo a la red](#1-qué-cambia-al-pasar-el-vídeo-a-la-red)
- [2. La familia SMPTE ST 2110](#2-la-familia-smpte-st-2110)
- [3. La familia SMPTE ST 2022 y la redundancia](#3-la-familia-smpte-st-2022-y-la-redundancia)
- [4. Las dos redes de una instalación](#4-las-dos-redes-de-una-instalación)
- [5. La sincronización por red](#5-la-sincronización-por-red)
- [6. La producción sobre esa infraestructura](#6-la-producción-sobre-esa-infraestructura)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Qué cambia al pasar el vídeo a la red

| Garantía que el coaxial daba sola | Cómo se recupera en la red |
|---|---|
| **Sincronismo** | **Con un reloj de precisión repartido por la propia red** |
| **Latencia previsible** | **Con calidad de servicio y una red bien dimensionada** |
| **Entrega ordenada y completa** | **Con redundancia de camino y numeración de secuencia** |
| **Un cable, una señal** | **Ya no: por un cable van muchas, y hay que decir cuáles** |

**Lo que se gana, que es la razón del cambio:**

| Ventaja | Por qué |
|---|---|
| **Un solo cable para todo** | **Vídeo, audio, control y datos por la misma infraestructura** |
| **Encaminamiento sin límite de tamaño** | **Un conmutador crece añadiendo equipos; una matriz tiene tamaño fijo** |
| **Equipo genérico** | **Electrónica de red corriente en vez de matrices de un solo fabricante** |
| **Flexibilidad** | **Reconfigurar es cambiar una suscripción, no recablear** |

**Y el precio, que conviene decir con la misma claridad**: **la instalación pasa a depender de una red
que hay que diseñar, dimensionar y administrar.** **Un fallo de configuración de red ya no deja un
ordenador sin correo: deja un plató sin imagen.**

## 2. La familia SMPTE ST 2110

**La pregunta 62**: **una característica clave de esa familia es la separación de vídeo, audio y
metadatos en flujos independientes.** Ésa es la respuesta oficial.

---

**Y ése es su rasgo definitorio, el que la distingue de todo lo anterior:**

| | **Interfaz digital serie** | **La familia de red** |
|---|---|---|
| **Cómo van vídeo, audio y datos** | **Incrustados en la misma trama** | **En flujos SEPARADOS** ✔ |
| **Para cambiar un canal de audio** | **Hay que tocar la señal entera** | **Se cambia sólo ese flujo** |
| **Para llevar audio a otro sitio** | **Va el vídeo con él** | **Va solo** |
| **Qué los mantiene juntos** | **La propia trama** | **El reloj común** |

**La consecuencia práctica de esa separación**: **una mesa de sonido puede suscribirse a los flujos de
audio sin recibir un solo bit de vídeo.** **En coaxial habría que llevarle la señal entera y
desincrustar.**

**Y las tres opciones falsas de la pregunta se caen con esa misma tabla**: **la encapsulación en un
único flujo es exactamente lo contrario**; **el uso de compresión no es propio de esta familia**, cuya
parte de vídeo va sin comprimir; **y la dependencia de la interfaz de coaxial es lo que viene a
sustituir.**

**La pregunta 5**: **de las descripciones enumeradas, la correcta es que la parte 10 es arquitectura y
sincronización, la parte 20 es vídeo sin compresión y la parte 30 es audio basado en AES67.** Ésa es
la respuesta oficial.

**La pregunta 78**: **la norma SMPTE 2110-20 especifica el transporte de señal de vídeo sin
comprimir.** Ésa es la respuesta oficial.

---

**Las dos se contestan con la misma tabla de partes:**

| Parte | Qué normaliza |
|---|---|
| **ST 2110-10** | **La arquitectura y la sincronización de todo el conjunto** ✔ |
| **ST 2110-20** | **El vídeo SIN COMPRIMIR** ✔ |
| **ST 2110-21** | **El perfil de tráfico: cómo se reparten los paquetes en el tiempo** |
| **ST 2110-30** | **El audio, basado en la norma de interoperabilidad de la Sociedad de Ingeniería de Audio** ✔ |
| **ST 2110-31** | **El audio en formato de la norma AES3 transparente** |
| **ST 2110-40** | **Los datos auxiliares** |

**Y las dos palabras que deciden la pregunta 5, porque las tres opciones falsas cambian una de
ellas**: **«sin compresión» en la parte de vídeo**, y **el nombre de la norma en la de audio.**

| Opción falsa | Qué cambia |
|---|---|
| **Vídeo comprimido en la parte 20** | **Va sin comprimir** |
| **Audio basado en AES3 en la parte 30** | **La 30 se basa en la norma de interoperabilidad; la que usa AES3 es la 31** |
| **Vídeo con compresión en la parte 10** | **La 10 no es de vídeo: es arquitectura y sincronización** |

**El aviso que este epígrafe deja y que un ingeniero necesita**: **la parte 21 no aparece en el examen
y es la que más problemas da en obra.** **Define cómo se espacian los paquetes**, y **un emisor que no
respete su perfil satura las colas del conmutador y produce pérdidas** aunque el enlace tenga
capacidad de sobra.

## 3. La familia SMPTE ST 2022 y la redundancia

**La pregunta 14**: **la norma SMPTE 2022-7 trata específicamente de conmutación con protección total
para flujos de vídeo sin comprimir.** Ésa es la respuesta oficial.

---

**Y conviene ver la familia entera, porque el enunciado la nombra junto a la otra:**

| Parte | Qué normaliza |
|---|---|
| **ST 2022-1 y -2** | **Transporte de flujo comprimido sobre red, con corrección de errores** |
| **ST 2022-5 y -6** | **Transporte de la señal de coaxial ENTERA sobre red** |
| **ST 2022-7** | **Protección sin costura: dos caminos simultáneos** ✔ |

**Cómo funciona esa protección, que es lo que hay que entender:**

1. **El emisor manda DOS copias idénticas del mismo flujo**, cada una por un camino físicamente
   distinto.
2. **Cada paquete lleva su número de secuencia.**
3. **El receptor toma el primero que llega de cada número y descarta el duplicado.**
4. **Si un camino falla, el receptor ya tiene el otro**: **no hay conmutación, no hay hueco.**

**De ahí el nombre «sin costura»**: **no es que el cambio sea rápido, es que NO HAY cambio.**

**Y la diferencia con las dos familias del epígrafe anterior**: **la de 2022 partes 5 y 6 mete la
señal entera de coaxial en la red, tal cual**; **la de 2110 la descompone en flujos.** **La primera es
un puente entre los dos mundos y la segunda es el mundo nuevo.**

## 4. Las dos redes de una instalación

**La pregunta 67**: **las redes roja y azul de una instalación basada en esa familia son las dos redes
por las que se transmite la señal, de forma balanceada, para proporcionar redundancia en caso de fallo
de una de ellas.** Ésa es la respuesta oficial.

---

**Y aquí el temario tiene que hacer una precisión, porque cambia cómo se entiende el sistema**: **las
dos redes no se reparten la carga: llevan LAS DOS el flujo completo, a la vez.** **Eso es lo que el
epígrafe anterior describe.**

**La palabra «balanceada» de la respuesta oficial se entiende bien si significa que las dos están
igualmente activas** —frente a un esquema de principal y reserva—, **y así es como se marca.** **Lo
que no significa es que cada una lleve la mitad.**

**Las tres opciones falsas y por qué caen, que es lo que confirma la lectura:**

| Opción | Por qué es falsa |
|---|---|
| **Una activa y otra de reserva, con cambio al fallar** | **Eso es conmutación con hueco: es justo lo que la protección sin costura evita** |
| **El vídeo por una y el audio por la otra** | **Sería un reparto, no una redundancia: al caer una se perdería la mitad** |
| **Vídeo y audio por una, datos por la otra** | **Lo mismo** |

**Por qué se llaman roja y azul**: **es convenio de instalación, no de norma.** **Se pintan de dos
colores para que nadie pueda confundir de qué red es un cable**, y **para que las dos rutas sean
físicamente distintas de principio a fin**: distintos conmutadores, distintas bandejas y, a poder ser,
distintas salas.

**El aviso de oficio que este epígrafe deja**: **dos redes que comparten un mismo conmutador, una
misma bandeja o un mismo cuadro eléctrico NO son dos redes.** **La redundancia se rompe en el punto
que comparten**, y ése es el fallo de diseño más frecuente.

## 5. La sincronización por red

**El enunciado la nombra expresamente y el examen no la ha preguntado.** **Es lo más preguntable de lo
que falta:**

**Qué resuelve**: **en coaxial, la referencia llegaba por un cable propio.** **En red hay que repartir
el tiempo por la misma red que lleva la señal**, y con una precisión de microsegundos.

**Cómo funciona el protocolo de tiempo de precisión, en cuatro pasos:**

1. **Un reloj maestro se elige automáticamente entre los candidatos**, por un algoritmo que compara su
   calidad.
2. **El maestro manda mensajes con la hora exacta de salida.**
3. **Cada esclavo mide el retardo de ida y vuelta** con un intercambio de mensajes.
4. **Con ese retardo corrige su propio reloj.**

**Y la pieza que lo hace posible en una red grande**: **los conmutadores compatibles CORRIGEN el
tiempo que el mensaje pasa dentro de ellos**, y lo escriben en el propio mensaje. **Sin esa
corrección, la variabilidad del conmutador arruinaría la precisión.**

**El aviso de instalación**: **un conmutador que no soporte ese protocolo puede pasar el tráfico
perfectamente y arruinar la sincronía.** **Es un fallo que no se ve en las pruebas de caudal**, y
aparece como deriva lenta que nadie relaciona con la red.

## 6. La producción sobre esa infraestructura

**El punto 9 del anexo pide precisamente esto, y no ha dado ninguna pregunta.** **Lo que un ingeniero
tiene que saber montar:**

| Capa | Qué resuelve |
|---|---|
| **Transporte** | **Las normas de los epígrafes 2 y 3** |
| **Sincronización** | **El reloj del epígrafe 5** |
| **Descubrimiento y registro** | **Que un equipo nuevo diga quién es y qué ofrece, y que el sistema lo sepa** |
| **Conexión** | **Que un receptor se suscriba al flujo que quiere, por orden del control** |
| **Control de equipos** | **La configuración remota del tema 15** |

**Las dos primeras están normalizadas por la Sociedad de Ingenieros de Cine y Televisión; las dos
siguientes no lo estaban**, y **de ahí nació el conjunto de especificaciones abiertas de descubrimiento
y control** que la industria adoptó para que equipos de fabricantes distintos se encuentren solos.

**Y el cambio de mentalidad que la producción sobre red exige, que es lo que conviene llevar
entendido**: **en coaxial, encaminar era CONECTAR una salida con una entrada.** **En red, encaminar es
que un receptor SE SUSCRIBA a un flujo.** **La matriz deja de ser un aparato y pasa a ser una función
del control.**

**Los tres problemas nuevos que aparecen y que no existían con coaxial:**

1. **El envío a varios destinos hay que gestionarlo.** **Una red que no gestione la suscripción a
   grupos inunda todos los puertos y se cae sola.**
2. **El dimensionado deja de ser evidente.** **Una señal de alta definición sin comprimir ocupa
   alrededor de 1,5 gigabits por segundo, y una de ultraalta cuatro veces más**: **un enlace de diez
   gigabits admite muy pocas.**
3. **La red es ahora una parte de la cadena de señal**, y **hay que medirla como se medía la señal**:
   con supervisión permanente y no sólo cuando algo falla.

## 7. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 5 | Qué describe correctamente las partes de la familia | c) Arquitectura, vídeo sin compresión y audio interoperable ✔ |
| 14 | De qué trata la norma SMPTE 2022-7 | a) Conmutación con protección total para vídeo sin comprimir ✔ |
| 62 | Característica clave de la familia SMPTE 2110 | b) Separación en flujos independientes ✔ |
| 67 | Qué son las redes roja y azul | a) Dos redes con la señal, para redundancia ✔ **·** con precisión |
| 78 | Qué especifica la norma SMPTE 2110-20 | a) Transporte de vídeo sin comprimir ✔ |

**Las cinco respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **Una lleva
precisión declarada**: la 67, cuya palabra «balanceada» significa que las dos redes están igualmente
activas, no que cada una lleve la mitad del tráfico.

**El aviso de estudio**: **la tabla de partes de la familia contesta dos preguntas y descarta los
distractores de una tercera.** **Y la idea de que la protección manda dos copias completas por dos
caminos contesta las dos restantes.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **El articulado de las familias de normas de la Sociedad de Ingenieros de Cine y Televisión no se
   ha consultado**: está tras un muro de pago. **Los títulos y el cometido de cada parte son de uso
   universal en el sector y figuran en el índice público de la propia sociedad**, volcado en este
   proyecto para el temario específico de Técnica Informática. **Coinciden con las respuestas
   oficiales.**
2. **La norma de interoperabilidad de audio de la Sociedad de Ingeniería de Audio tampoco se ha
   consultado**, y **el temario sólo afirma de ella lo que la respuesta oficial afirma**: que es la
   base de la parte de audio.
3. **La precisión sobre la pregunta 67 es del temario, no una impugnación**: **la respuesta oficial es
   la única de las cuatro que describe una redundancia real**, y **el temario aclara qué significa
   «balanceada» en ese contexto.**
4. **El protocolo de tiempo de precisión y el conjunto de especificaciones de descubrimiento y control
   se describen con lo que es de uso corriente en el sector.** **Ninguna respuesta oficial depende de
   ellos**: el examen no ha entrado por ahí.
5. **Las cifras de caudal del epígrafe 6 —alrededor de 1,5 gigabits por segundo para alta definición
   sin comprimir y cuatro veces más para ultraalta— son órdenes de magnitud**, coherentes con la
   escalera de la interfaz digital serie del tema 3.

**El resto del tema va como oficio y así se declara**: la tabla de garantías perdidas y recuperadas,
la consecuencia práctica de la separación en flujos, el aviso sobre el perfil de tráfico, la
explicación en cuatro pasos de la protección sin costura, la advertencia sobre dos redes que comparten
un punto, el aviso sobre los conmutadores que no soportan el protocolo de tiempo y los tres problemas
nuevos de la producción sobre red. **Nada de eso está en un boletín oficial ni en una norma técnica de
las consultadas**, y el tema no lo presenta como si lo estuviera.
