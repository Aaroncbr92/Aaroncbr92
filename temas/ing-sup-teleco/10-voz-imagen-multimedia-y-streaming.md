# Tema 10 del específico de Ingeniería Superior · Telecomunicación · Tratamiento de voz e imágenes, servicios multimedia y difusión en flujo

Las siglas y símbolos de este tema, presentados de entrada: el transporte fiable y seguro (**SRT**,
*secure reliable transport*); el protocolo de transporte en tiempo real (**RTP**) y su protocolo de
control (**RTCP**); el protocolo de transporte en tiempo real seguro (**SRTP**); el protocolo de
mensajería en tiempo real (**RTMP**); la difusión adaptativa por conexión web (**HLS** y **MPEG-DASH**);
la retransmisión en tiempo real con muy baja latencia (**WebRTC**); el protocolo de inicio de sesión
(**SIP**); la voz sobre protocolo de internet (**VoIP**); la corrección de errores hacia delante
(**FEC**); la petición automática de repetición (**ARQ**); la red de distribución de contenidos
(**CDN**); la calidad de servicio (**QoS**) y la calidad de experiencia (**QoE**); la fluctuación de
retardo (**jitter**); el milisegundo (**ms**); y el megabit por segundo (**Mbit/s**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 10):
> «Tratamiento de voz y de imágenes. Características de las señales. Técnicas de Transmisión.
> Integración de voz, datos e imágenes. Servicios multimedia. Estándares. Equipamiento y aplicaciones.
> Streaming de video.»

**Es el punto de la CONVERGENCIA**, y **hay que decir de entrada qué lo separa de los temas 19 y 20**:
**aquéllos estudian la producción sobre red dentro de una casa y la red misma; éste estudia lo que
viaja por INTERNET, es decir, por una red que no se controla.**

**Y la idea que ordena el punto entero**: **una red que no se controla no garantiza nada.** **Ni
ancho de banda, ni retardo, ni orden de llegada, ni entrega.** **Todo lo que este tema describe —el
almacenamiento intermedio, la adaptación de tasa, la corrección de errores, la repetición selectiva—
existe para dar un servicio aceptable sobre un transporte que no promete nada.**

<!-- indice -->
<!-- /indice -->

## 1. Las señales y lo que las distingue

**Voz, audio e imagen no se comportan igual, y el tratamiento sale de ahí:**

| Señal | Rasgo | Qué exige del transporte |
|---|---|---|
| **VOZ** | **Banda estrecha, muy predecible, muy tolerante a la pérdida** | **RETARDO bajo**: una conversación con un segundo de retardo no funciona |
| **AUDIO de calidad** | **Banda ancha, mucho margen dinámico** | **Tasa constante y pocas pérdidas** |
| **IMAGEN fija** | **Mucho dato, sin restricción de tiempo** | **Integridad**: da igual que tarde |
| **VÍDEO** | **Muchísimo dato Y restricción de tiempo** | **Las dos cosas a la vez**: es el caso difícil |

**Y la regla que hay que tener antes de elegir nada**: **en tiempo real, el RETARDO y la INTEGRIDAD son
enemigos.** **Garantizar que todo llegue exige pedir repeticiones y esperar; garantizar que llegue a
tiempo exige renunciar a lo que se perdió.** **No se pueden tener las dos**, y **lo que cambia de un
servicio a otro es cuál de las dos se sacrifica.**

**Los tres regímenes de servicio que salen de ahí, y hay que saber colocarlos:**

| Régimen | Retardo tolerable | Ejemplo |
|---|---|---|
| **CONVERSACIONAL** | **Decenas o pocos cientos de milisegundos**, con vuelta | **Una entrevista a distancia, una llamada** |
| **DIRECTO en un sentido** | **Segundos** | **Una emisión en flujo de un acontecimiento** |
| **BAJO DEMANDA** | **El que haga falta al arrancar** | **Un catálogo** |

## 2. La integración de voz, datos e imagen

**Qué significa la palabra convergencia, dicho sin adorno**: **que los tres tipos de información viajan
por la misma red y con los mismos protocolos**, y **que el equipamiento deja de ser específico.**

**Lo que eso trae, en las dos direcciones:**

| Lo que gana | Lo que cuesta |
|---|---|
| **Una sola infraestructura** en vez de tres | **Una sola infraestructura**: cuando cae, cae todo |
| **Equipamiento estándar y barato** | **Comportamiento estadístico**: la red ya no reserva, comparte |
| **Servicios nuevos por combinación** | **La calidad hay que construirla encima**, no viene dada |
| **Escala**: crecer es añadir, no rediseñar | **Seguridad**: lo que está en la red se puede atacar |

**Y la observación de oficio que hay que dejar dicha**: **la telefonía sobre red de paquetes es el
ejemplo canónico de esta convergencia y también su aviso.** **Una red conmutada por circuitos reservaba
el camino y garantizaba la calidad por diseño; una red de paquetes no reserva nada**, y **por eso la
voz sobre red necesita marcado de prioridad, control de admisión y una red bien dimensionada.**
**Convergencia no es ahorro automático: es trasladar a la red un problema que antes resolvía el
circuito.**

## 3. El transporte en tiempo real

**Los protocolos y para qué está cada uno:**

| Protocolo | Qué hace |
|---|---|
| **De transporte en tiempo real** | **Numera y marca en el tiempo cada paquete de medio**, para que el receptor lo reordene y lo reproduzca a ritmo |
| **Su protocolo de CONTROL** | **Informa de calidad**: pérdidas, fluctuación, retardo de ida y vuelta |
| **De inicio de SESIÓN** | **Establece, modifica y termina la llamada**; **no lleva el medio** |
| **De DESCRIPCIÓN de sesión** | **Dice qué medios hay, con qué códecs y en qué puertos**; **tampoco lleva medio** |

**La distinción que un examen persigue**: **señalización y medio van por caminos distintos.** **Un
protocolo de sesión negocia y otro transporta**, y **confundirlos es el error clásico.**

**Y por qué el transporte en tiempo real va sobre un protocolo NO fiable**, que es la pregunta
conceptual: **porque la retransmisión llega tarde.** **Un protocolo fiable retransmite lo perdido y
espera a entregarlo en orden**, y **en tiempo real un paquete que llega después de su instante de
reproducción no sirve para nada.** **Se prefiere un hueco a una espera**, y **el hueco se disimula.**

**Las tres defensas contra la pérdida, con lo que cuesta cada una:**

| Defensa | Qué hace | Qué cuesta |
|---|---|---|
| **CORRECCIÓN hacia delante** | **Manda redundancia por adelantado** | **Ancho de banda constante**, se pierda o no |
| **REPETICIÓN selectiva** | **Pide sólo lo que faltó** | **Retardo**: hay que esperar la vuelta |
| **OCULTACIÓN de pérdidas** | **Rellena el hueco con lo que había** | **Calidad**: no recupera, disimula |
| **Almacenamiento intermedio** | **Guarda unos segundos antes de reproducir** | **RETARDO**, que es lo que se estaba defendiendo |

**Y la regla que las ordena**: **el almacenamiento intermedio es la moneda con la que se paga todo lo
demás.** **Cuanto más grande, más pérdidas se pueden reparar y más fluctuación se absorbe, y más
retardo hay.** **Ajustar ese tamaño es la decisión central de un servicio en flujo.**

## 4. El transporte de contribución sobre internet

**Lo que ha cambiado el oficio en los últimos años**, y **el asunto de la pregunta que esta ocupación
ha puesto en su cuadernillo.**

**El problema**: **llevar una señal de calidad de contribución desde el lugar de la noticia hasta el
centro, por internet, sin satélite y sin línea dedicada.**

**Lo que hace falta para que eso funcione:**

| Requisito | Por qué |
|---|---|
| **Recuperación de pérdidas con retardo acotado** | **Internet pierde paquetes y no avisa** |
| **Absorción de la FLUCTUACIÓN** | **El retardo de internet varía**, y el receptor tiene que entregar a ritmo constante |
| **CIFRADO** | **El camino es público** |
| **Atravesar cortafuegos y traducción de direcciones** | **Los dos extremos suelen estar detrás de un router** |
| **Latencia CONFIGURABLE** | **Para elegir el punto del intercambio entre robustez y retardo** |

**El protocolo de transporte fiable y seguro que el cuadernillo pregunta cumple los cinco**, y **hay
que saber decir qué es cierto y qué no de él:**

| Afirmación | ¿Cierta? |
|---|---|
| **Sirve para transmitir acontecimientos en directo** | **SÍ**: es exactamente para lo que se diseñó |
| **Implementa recuperación automática de errores** | **SÍ**: repite lo perdido dentro de una ventana de latencia |
| **Proporciona cifrado** | **SÍ** |
| **Sólo se puede usar en redes privadas con ancho de banda reservado de extremo a extremo** | **FALSA**, y es la respuesta |

**Y hay que razonar por qué esa última es falsa, que es lo que un examen premia**: **si sólo sirviera
en una red privada con ancho de banda reservado, NO HARÍA FALTA.** **En una red así no se pierden
paquetes ni varía el retardo**, y **el protocolo entero existe precisamente para funcionar sobre
internet pública, que es lo que no reserva nada.** **La opción falsa niega la razón de ser de la
herramienta**, y **ése es el patrón de esa clase de pregunta: la opción que contradice el propósito.**

## 5. La difusión en flujo al espectador

**El otro lado del punto**: **no llevar la señal al centro, sino del centro a millones de pantallas.**

**Cómo funciona la difusión adaptativa, que es el mecanismo que hay que saber describir:**

| Paso | Qué se hace |
|---|---|
| **1 · Codificación en varias calidades** | **El mismo contenido, a distintas tasas y resoluciones** |
| **2 · Troceado en SEGMENTOS** | **Trozos cortos, cada uno reproducible por sí mismo** |
| **3 · Un MANIFIESTO** | **Una lista que dice qué calidades hay y dónde está cada segmento** |
| **4 · El CLIENTE decide** | **Mide su ancho de banda y pide el segmento de la calidad que puede** |
| **5 · Entrega por RED DE DISTRIBUCIÓN** | **Servidores repartidos que sirven desde cerca del espectador** |

**Y las tres consecuencias que hay que saber enunciar:**

1. **La inteligencia está en el CLIENTE, no en el servidor.** **El servidor sirve ficheros; el
   reproductor decide.** **Eso es lo que permite escalar a millones: el servidor no mantiene estado
   por espectador.**
2. **La adaptación tiene un precio: el RETARDO.** **Segmentar, publicar y almacenar antes de
   reproducir suma segundos**, y **por eso la difusión en flujo va detrás de la emisión terrestre.**
   **Las variantes de baja latencia trocean más fino y entregan a trozos**, **a costa de robustez.**
3. **La red de distribución es parte del servicio, no un accesorio.** **Sin servidores cerca del
   espectador, el mismo contenido se manda un millón de veces desde el origen.**

**Y la distinción entre calidad de servicio y calidad de EXPERIENCIA, que cierra el epígrafe**: **la
primera se mide en la red —pérdidas, retardo, fluctuación—; la segunda se mide en el espectador
—tiempo de arranque, número de cortes, resolución media, abandono—.** **Una red con buenos números
puede dar una experiencia mala si el reproductor decide mal**, y **lo que se vende es la segunda.**

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma del boletín y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto es el del tema 3**, con **el matiz del tema 8**: **el enunciado
habla de «estándares», y los de esta materia son especificaciones de organismos técnicos y de
internet**, **que este proyecto no ha consultado.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ninguna latencia en milisegundos, ninguna tasa de bits, ningún tamaño de
   segmento, ningún porcentaje de pérdida admisible y ningún número de puerto.** **Son dato de
   especificación y de despliegue**, y **una cifra que no se ha leído en su fuente no se escribe.**
2. **Las cuatro afirmaciones sobre el protocolo de transporte fiable y seguro del epígrafe 4 son las
   del propio cuadernillo de esta ocupación**, y **su plantilla oficial confirma cuál es la falsa**.
   **El temario declara esa procedencia y añade el razonamiento**, que es lo que un opositor necesita;
   **no describe la especificación, que no ha leído.**
3. **Los protocolos se nombran por su función y por su sigla de uso común**, y **el temario NO les
   atribuye ningún número de documento, ninguna versión y ninguna prestación concreta.**
4. **Este tema NO nombra ninguna plataforma, ningún producto y ninguna red de distribución
   comercial.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **los
   protocolos de red y el modelo de referencia, al tema 20**; **el transporte de medios sin comprimir
   dentro de una instalación, al tema 19**; **la compresión, al tema 6**; **y el sonido y sus
   códecs, al tema 21.**

**El resto del tema va como oficio y así se declara**: la separación entre este punto y los temas 19 y
20 —la red que no se controla frente a la que sí—, la regla de que en tiempo real el retardo y la
integridad son enemigos, los tres regímenes de servicio por su retardo tolerable, la lectura de la
convergencia en sus dos direcciones y la observación de que no es ahorro automático sino traslado de un
problema, la explicación de por qué el transporte en tiempo real va sobre un protocolo no fiable, la
regla de que el almacenamiento intermedio es la moneda con la que se paga todo lo demás, el
razonamiento de por qué la afirmación de la red privada niega la razón de ser del protocolo, la
descripción en cinco pasos de la difusión adaptativa, las tres consecuencias con el subrayado de que la
inteligencia está en el cliente, y la distinción entre calidad de servicio y calidad de experiencia.
**Nada de eso está en un boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema
no lo presenta como si lo estuviera.
