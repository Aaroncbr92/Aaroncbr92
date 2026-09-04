# Esquema · Tema 10 del específico de Ingeniería Superior · Telecomunicación · Voz, imagen, multimedia y difusión en flujo

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de transporte de medios ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: el
protocolo de transporte en tiempo real (**RTP**) y su protocolo de control (**RTCP**); el de inicio de
sesión (**SIP**); el de descripción de sesión (**SDP**); el de transporte fiable y seguro (**SRT**); la
red de distribución de contenidos (**CDN**); y el milisegundo (**ms**).

**Cabecera.** Enunciado: punto 10 del anexo · **una pregunta** · **sin norma del boletín**.

**La idea que lo ordena** · `[of]` · **En tiempo real, el RETARDO y la INTEGRIDAD son enemigos.**
**Garantizar que todo llegue exige esperar; garantizar que llegue a tiempo exige renunciar a lo
perdido.** **Lo que cambia de un servicio a otro es cuál de las dos se sacrifica.**

<!-- indice -->

## Índice

- [Las señales y los tres regímenes](#las-señales-y-los-tres-regímenes)
- [La convergencia](#la-convergencia)
- [El transporte en tiempo real](#el-transporte-en-tiempo-real)
- [Contribución sobre internet](#contribución-sobre-internet)
- [La difusión en flujo](#la-difusión-en-flujo)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las señales y los tres regímenes

| Señal | Qué exige del transporte |
|---|---|
| **voz** | **retardo bajo**: una conversación con un segundo de retardo no funciona |
| **audio de calidad** | **tasa constante y pocas pérdidas** |
| **imagen fija** | **integridad**: da igual que tarde |
| **vídeo** | **las dos cosas a la vez**: es el caso difícil |

| Régimen | Retardo tolerable | Ejemplo |
|---|---|---|
| **conversacional** | **decenas o pocos cientos de milisegundos, con vuelta** | **una entrevista a distancia** |
| **directo en un sentido** | **segundos** | **una emisión en flujo** |
| **bajo demanda** | **el que haga falta al arrancar** | **un catálogo** |

## La convergencia

| Lo que gana | Lo que cuesta |
|---|---|
| **una sola infraestructura** | **una sola infraestructura: cuando cae, cae todo** |
| **equipamiento estándar y barato** | **comportamiento estadístico**: la red comparte, no reserva |
| **servicios nuevos por combinación** | **la calidad hay que construirla encima** |
| **escala: crecer es añadir** | **seguridad: lo que está en la red se puede atacar** |

- **el ejemplo canónico y su aviso** · `[of]` · **La telefonía sobre red de paquetes.** **Un circuito
  reservaba el camino y garantizaba la calidad por diseño; una red de paquetes no reserva nada**, y
  **por eso la voz sobre red necesita marcado de prioridad, control de admisión y una red bien
  dimensionada.** **Convergencia no es ahorro automático: es trasladar a la red un problema que antes
  resolvía el circuito.**

## El transporte en tiempo real

| Protocolo | Qué hace |
|---|---|
| **de transporte en tiempo real** | **numera y marca en el tiempo cada paquete de medio** |
| **su protocolo de control** | **informa de pérdidas, fluctuación y retardo de ida y vuelta** |
| **de inicio de sesión** | **establece, modifica y termina la llamada**; **no lleva medio** |
| **de descripción de sesión** | **dice qué medios hay, con qué códecs y en qué puertos**; **tampoco lleva medio** |

- **la distinción que se persigue** · `[of]` · **Señalización y medio van por caminos distintos.**
- **POR QUÉ VA SOBRE UN PROTOCOLO NO FIABLE** · `[of]` · **Porque la retransmisión llega tarde.** **Un
  paquete que llega después de su instante de reproducción no sirve para nada.** **Se prefiere un hueco
  a una espera, y el hueco se disimula.**

| Defensa contra la pérdida | Qué cuesta |
|---|---|
| **corrección hacia delante** | **ancho de banda constante, se pierda o no** |
| **repetición selectiva** | **retardo: hay que esperar la vuelta** |
| **ocultación** | **calidad: no recupera, disimula** |
| **almacenamiento intermedio** | **RETARDO**, que es lo que se estaba defendiendo |

- **la regla que las ordena** · `[of]` · **El almacenamiento intermedio es la moneda con la que se paga
  todo lo demás.** **Ajustar su tamaño es la decisión central de un servicio en flujo.**

## Contribución sobre internet

| Requisito | Por qué |
|---|---|
| **recuperación con retardo acotado** | **internet pierde paquetes y no avisa** |
| **absorción de la fluctuación** | **el retardo varía y hay que entregar a ritmo constante** |
| **cifrado** | **el camino es público** |
| **atravesar cortafuegos y traducción de direcciones** | **los dos extremos están detrás de un encaminador** |
| **latencia configurable** | **para elegir el punto entre robustez y retardo** |

- **LO QUE ES FALSO DEL PROTOCOLO DE TRANSPORTE FIABLE Y SEGURO** · `[exam]` · **Que sólo se pueda usar
  en redes privadas con ancho de banda reservado de extremo a extremo.** **Sí sirve para directos, sí
  recupera errores y sí cifra.**
- **por qué esa opción es falsa, razonada** · `[of]` · **Si sólo sirviera en una red privada
  reservada, NO HARÍA FALTA**: **en una red así no se pierden paquetes ni varía el retardo.** **El
  protocolo existe precisamente para funcionar sobre internet pública.** **Es el patrón de esa clase de
  pregunta: la opción que contradice el propósito de la herramienta.**

## La difusión en flujo

| Paso | Qué se hace |
|---|---|
| **1 · varias calidades** | **el mismo contenido a distintas tasas y resoluciones** |
| **2 · segmentos** | **trozos cortos, cada uno reproducible por sí mismo** |
| **3 · manifiesto** | **la lista de qué calidades hay y dónde está cada segmento** |
| **4 · el cliente decide** | **mide su ancho de banda y pide lo que puede** |
| **5 · red de distribución** | **servidores repartidos que sirven desde cerca del espectador** |

- **la inteligencia está en el CLIENTE** · `[of]` · **El servidor sirve ficheros; el reproductor
  decide.** **Eso es lo que permite escalar a millones: el servidor no mantiene estado por
  espectador.**
- **la adaptación se paga en RETARDO** · `[of]` · **Segmentar, publicar y almacenar antes de reproducir
  suma segundos**, y **por eso la difusión en flujo va detrás de la emisión terrestre.**
- **calidad de servicio frente a calidad de EXPERIENCIA** · `[of]` · **La primera se mide en la red
  —pérdidas, retardo, fluctuación—; la segunda, en el espectador —arranque, cortes, resolución media,
  abandono—.** **Una red con buenos números puede dar una experiencia mala si el reproductor decide
  mal**, y **lo que se vende es la segunda.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 77 | Qué NO es cierto del protocolo de transporte fiable y seguro | **Que sólo sirva en redes privadas con ancho de banda reservado** ✔ **·** si así fuera, no haría falta |
