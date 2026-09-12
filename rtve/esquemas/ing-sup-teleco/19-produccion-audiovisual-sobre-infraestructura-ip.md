# Esquema · Tema 19 del específico de Ingeniería Superior · Telecomunicación · Producción audiovisual sobre infraestructura de red

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de producción sobre red ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo · `[norma]` = norma
técnica nombrada en la pregunta y confirmada por la plantilla. **Siglas**: el protocolo de internet
(**IP**); la sociedad que publica las normas de la serie **ST**; la interfaz digital serie (**SDI**) y
su versión de alta definición (**HD-SDI**); el protocolo de transporte en tiempo real (**RTP**) y el
datagrama de usuario (**UDP**); el de descripción de sesión (**SDP**); el de tiempo de precisión
(**PTP**) y el algoritmo del mejor reloj maestro (**BMCA**); las especificaciones de red abierta para
medios (**NMOS**) y sus interfaces (**IS**); el audio digital profesional (**AES3**); la compresión
ligera **JPEG-XS**; y el nanosegundo (**ns**).

**Cabecera.** Enunciado: punto 21 del anexo · **ONCE preguntas: es el punto más preguntado de todo el
cuadernillo** · **sin norma del boletín**: las normas que nombra son técnicas y este proyecto no tiene
su texto; **de ellas sólo se recoge lo que la plantilla confirma.**

**La idea que lo ordena** · `[of]` · **La interfaz serie llevaba una señal completa por un cable
dedicado, en un solo sentido.** **La red no lleva señales: lleva flujos.** **Todo lo demás —separar
esencias, numerar paquetes, repartir un reloj, descubrir quién hay— existe porque al quitar el cable
dedicado hubo que reconstruir con protocolos lo que el cable daba gratis.**

<!-- indice -->

## Índice

- [Lo que se pierde y lo que se gana](#lo-que-se-pierde-y-lo-que-se-gana)
- [Encapsular lo que ya había](#encapsular-lo-que-ya-había)
- [Separar las esencias](#separar-las-esencias)
- [El transporte](#el-transporte)
- [El ancho de banda](#el-ancho-de-banda)
- [La sincronización](#la-sincronización)
- [El control y el descubrimiento](#el-control-y-el-descubrimiento)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Lo que se pierde y lo que se gana

| Lo que daba el cable | Cómo lo daba |
|---|---|
| **sincronismo** | **el propio flujo continuo marcaba el tiempo** |
| **rutado** | **un conector es un destino: se ve dónde va** |
| **aislamiento** | **una señal por cable** |
| **retardo constante** | **el mismo camino siempre, sin colas** |

| Lo que da la red | Por qué importa |
|---|---|
| **un solo medio para todo** | **vídeo, audio, datos y control por la misma infraestructura** |
| **capacidad que crece** | **cambiar de definición es cambiar de configuración, no de cableado** |
| **rutado sin matriz** | **el conmutador de red hace de matriz** |
| **difusión selectiva** | **un origen alcanza muchos destinos sin duplicar el envío** |

## Encapsular lo que ya había

- **la familia de transición** · `[of]` · **No cambia la señal: la mete en paquetes tal como está.**
- **LA PARTE QUE TRANSPORTA LA INTERFAZ ENTERA** · `[exam]` · **Su paquete puede contener vídeo, audio
  O los datos auxiliares de los intervalos vertical y horizontal.** **Si lo que se encapsula es el
  flujo completo, dentro va todo lo que ese flujo llevaba: la norma no separa nada y por eso no puede
  excluir nada.** **Quien responde «sólo vídeo» está pensando en la otra familia.**
- **LA PARTE DE REDUNDANCIA** · `[exam]` · **Envía dos copias por dos caminos y el receptor reconstruye
  tomando de cualquiera el paquete que falte a la otra.** **Es la que tiene redundancia de conectividad
  en los equipos finales.**
- **las tres cosas de esa redundancia** · `[of]` · **1) es SIN CORTE**: no se conmuta, se reconstruye
  paquete a paquete. **2) los dos caminos deben ser de verdad distintos**: **dos flujos por el mismo
  conmutador no protegen de la caída de ese conmutador.** **3) no es exclusiva de su familia**: se
  aplica también a los flujos de la otra, **y por eso la respuesta correcta la nombra como norma de
  redundancia y no de vídeo.**

## Separar las esencias

- **las tres razones de la separación** · `[of]` · **se lleva sólo lo que hace falta** · **se cambia una
  esencia sin tocar las demás** · **cada esencia se dimensiona por separado.**

| Parte | Qué transporta |
|---|---|
| **la 10** | **el sistema y la descripción de las sesiones** |
| **la 20** | **el vídeo SIN comprimir** |
| **la 21** | **el perfil de emisión del tráfico en el tiempo** |
| **la 22** | **el vídeo comprimido** |
| **la 30** | **el audio** |
| **la 31** | **el audio digital profesional de dos canales, de forma transparente** |
| **la 40** | **los datos auxiliares** |

- **regla mnemotécnica** · `[of]` · **Las decenas van en el orden en que se descompone una señal**:
  **veinte imagen, treinta sonido, cuarenta lo auxiliar.**
- **la diferencia entre llevar el audio y llevar el FORMATO del audio** · `[exam]` · **La parte 30 lleva
  las muestras; preservar los bits de validez, usuario, canal y paridad exige transportar la TRAMA
  entera, y eso es la parte 31.**
- **el vídeo comprimido** · `[exam]` · **Por la parte 20 NO se puede mandar.** **La parte 20 es la del
  vídeo sin comprimir y el comprimido tiene su propia parte.** **La trampa de las otras opciones es
  discutir qué compresión admite la 20, cuando la respuesta es que ninguna porque no es su cometido.**

## El transporte

| Propiedad | Consecuencia |
|---|---|
| **va sobre datagramas, no sobre conexión** | **no espera confirmaciones: no añade retardo por esperar** |
| **es unidireccional** | **del origen al destino, sin vuelta** |
| **numera y marca en el tiempo cada paquete** | **el receptor sabe el orden y el instante** |
| **admite difusión selectiva** | **un origen sirve a muchos destinos con un envío** |

- **LO QUE NO HACE** · `[exam]` · **No controla los paquetes perdidos.** **Numerarlos no es
  controlarlos**: el receptor DETECTA que falta uno, pero **no pide que se lo reenvíen y no espera.**
- **la consecuencia de diseño** · `[of]` · **Una red de medios se diseña para que NO se pierdan
  paquetes, en lugar de para recuperarlos**: **la recuperación llegaría tarde.** **Y por eso la
  redundancia de la otra familia tiene sentido: es la única forma de sobrevivir a una pérdida sin
  retransmitir.**
- **la pieza que falta** · `[of]` · **El receptor tiene que saber a qué grupo de difusión escuchar y qué
  formato va dentro**: **eso lo dice el protocolo de descripción de sesión**, la ficha de cada flujo.
  **Sin ella, un flujo de medios en la red es tráfico ininteligible.**

## El ancho de banda

- **LA COMPARACIÓN QUE SE PREGUNTA** · `[exam]` · **La interfaz digital serie necesita MÁS ancho de
  banda que el transporte por red para la misma señal.**
- **el razonamiento en tres pasos** · `[of]` · **1)** la interfaz serie transporta la trama completa,
  **con sus intervalos de borrado, herencia del barrido de los tubos**; **2)** la parte de vídeo por red
  transporta **sólo la imagen activa**, y lo de los intervalos va aparte; **3)** **menos datos por
  segundo con el mismo contenido útil.**
- **el aviso de oficio** · `[of]` · **Eso no significa que la red salga gratis**: **exige una red sin
  sobresuscripción y con el reparto de paquetes en el tiempo bien perfilado.** **Ahorra ancho de banda
  y gasta ingeniería.**

## La sincronización

- **el problema** · `[of]` · **Al desaparecer el flujo continuo desapareció el sincronismo que llevaba
  dentro**, y **las esencias van ahora por flujos separados**: **sin tiempo común, el audio y el vídeo
  de la misma escena no se pueden volver a juntar.**
- **cómo funciona, en cuatro pasos** · `[of]` · **un reloj es el maestro y difunde la hora** · **cada
  equipo mide el retardo de ida y vuelta hasta él** · **corrige su hora con esa medida, y la distancia
  deja de importar** · **los conmutadores declaran cuánto tiempo estuvo el mensaje dentro**, para que
  **la cola no se confunda con distancia.**
- **EL ORDEN DE LOS CRITERIOS DE ELECCIÓN DEL MAESTRO** · `[exam]` · **La prioridad primera va antes que
  la CLASE DE RELOJ, y la clase de reloj antes que la precisión, la desviación y la prioridad
  segunda.** **Las dos preguntas de la plantilla sostienen ese orden, y el temario no afirma el orden
  relativo de los tres últimos, porque ninguna pregunta lo desempata.**
- **el ejemplo de los cuatro generadores** · `[exam]` · **Se compara primero la prioridad primera y gana
  el valor MÁS BAJO** —quedan dos—; **luego la clase de reloj, y también gana el más bajo.** **Ni la
  precisión ni la prioridad segunda llegan a mirarse**, y **ahí está la enseñanza: el generador MÁS
  PRECISO de los cuatro no gana.**
- **el aviso contraintuitivo** · `[of]` · **El valor más bajo gana en todos estos campos.** **Prioridad
  uno es mejor que prioridad dos.**

## El control y el descubrimiento

| Interfaz | Cometido |
|---|---|
| **la 04** | **registro y descubrimiento: qué equipos hay y qué ofrecen** |
| **la 05** | **conexión: quién envía a quién** |
| **la 06** | **control de la red** |
| **la 07** | **eventos y avisos, incluida la señalización de antena** |
| **la 08** | **encaminamiento de los canales de audio dentro de un equipo** |

- **el transporte de la interfaz de eventos** · `[exam]` · **La conexión bidireccional permanente sobre
  la web.** **Un aviso hay que empujarlo al destinatario en cuanto ocurre, y para eso hace falta un
  canal abierto en los dos sentidos**, no el envío unidireccional de los flujos ni la simple ficha de
  descripción de una sesión.
- **la que está descontinuada** · `[exam]` · **La de control de red.** **Es una pregunta de estado del
  conjunto de especificaciones y no de doctrina técnica**: **la interfaz existió, no se adoptó y se
  retiró.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 1 | Qué puede contener el paquete de la parte que encapsula la interfaz entera | **Vídeo, audio o los datos auxiliares de los intervalos** ✔ |
| 34 | Qué afirmación reparte bien las esencias entre partes | **La parte 30 lleva audio** ✔ |
| 44 | Qué parte transporta el audio digital profesional preservando sus bits de servicio | **La 31** ✔ **·** llevar la trama, no sólo las muestras |
| 45 | Qué NO corresponde al protocolo de transporte en tiempo real | **Tener control de paquetes perdidos** ✔ |
| 46 | Si se puede mandar vídeo comprimido por la parte de vídeo sin comprimir | **No** ✔ |
| 47 | Qué estándar tiene redundancia de conectividad en equipos finales | **La parte de redundancia de la otra familia** ✔ |
| 62 | Qué criterio pesa más en la elección del reloj maestro | **La clase de reloj** ✔ |
| 73 | Qué generador elegiría el algoritmo entre cuatro | **El segundo** ✔ **·** desempata la prioridad primera y luego la clase |
| 83 | Qué necesita más ancho de banda, la interfaz serie o el transporte por red | **La interfaz serie** ✔ **·** lleva los intervalos de borrado |
| 91 | Qué transporte admite la interfaz de eventos | **La conexión bidireccional permanente sobre la web** ✔ |
| 93 | Qué especificación está descontinuada | **La de control de red** ✔ |
