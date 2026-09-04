# Tema 19 del específico de Ingeniería Superior · Telecomunicación · Producción audiovisual sobre infraestructura de red

Las siglas y símbolos de este tema, presentados de entrada: el protocolo de internet (**IP**); la
sociedad de ingenieros de cine y televisión (**SMPTE**) y sus normas de la serie **ST**; la interfaz
digital serie (**SDI**) y su versión de alta definición (**HD-SDI**); el protocolo de transporte en
tiempo real (**RTP**) y el datagrama de usuario (**UDP**) sobre el que viaja; el protocolo de
descripción de sesión (**SDP**); el protocolo de tiempo de precisión (**PTP**) y el algoritmo del
mejor reloj maestro (**BMCA**); las especificaciones de red abierta para medios (**NMOS**) y sus
interfaces (**IS**); el audio digital profesional de dos canales (**AES3**); el grupo de expertos en
imágenes en movimiento (**MPEG**) y la compresión ligera **JPEG-XS**; y el nanosegundo (**ns**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 21):
> «Producción audiovisual sobre infraestructura IP. Formatos de señal ST2022 y ST2110. Sincronización
> PTP ST2059‐2.»

**Este es el punto que más preguntas ha dado de todo el cuadernillo de esta ocupación**: **once de las
ochenta y seis del específico.** **No es casualidad**: **es la transformación técnica que está en curso
en todas las casas de televisión y sobre la que se está contratando.** **Merece leerse dos veces.**

**Y la idea que ordena el punto**: **la interfaz digital serie llevaba una señal completa por un cable
dedicado, de un sitio a otro y en un solo sentido.** **La red no lleva señales: lleva flujos.**
**Todo lo que sigue —separar las esencias, numerar los paquetes, repartir un reloj común, descubrir
quién hay y decidir quién habla con quién— existe porque al quitar el cable dedicado hubo que
reconstruir con protocolos lo que el cable daba gratis.**

<!-- indice -->
<!-- /indice -->

## 1. Qué se pierde y qué se gana al dejar el cable dedicado

**Lo que la interfaz digital serie daba sin pedirlo:**

| Lo que daba el cable | Cómo lo daba |
|---|---|
| **Sincronismo** | **el propio flujo continuo marcaba el tiempo** |
| **Rutado** | **un conector es un destino: se ve dónde va** |
| **Aislamiento** | **una señal por cable; nada de lo que pase en otro le afecta** |
| **Retardo constante** | **el mismo camino siempre, sin colas** |

**Lo que la red da a cambio:**

| Lo que da la red | Por qué importa |
|---|---|
| **Un solo medio para todo** | **vídeo, audio, datos y control por la misma infraestructura** |
| **Capacidad que crece** | **cambiar de definición es cambiar de configuración, no de cableado** |
| **Rutado sin matriz** | **el conmutador de red hace de matriz de conmutación** |
| **Distancia** | **lo que antes exigía conversión a fibra viaja como tráfico normal** |
| **Difusión selectiva** | **un origen alcanza muchos destinos sin duplicar el envío** |

**El coste de la mudanza es que hay que devolver por protocolo las cuatro cosas de la primera tabla**,
y **ese es exactamente el contenido del punto**: **las series de normas que reconstruyen la señal, y
el reloj que reconstruye el sincronismo.**

## 2. La primera respuesta: encapsular lo que ya había

**La familia de normas 2022 no cambia la señal: la mete en paquetes tal como está.** **Es la solución
de transición y sigue en explotación.**

**Las dos partes que este temario necesita:**

**La parte 6 transporta la interfaz digital serie entera.** **La pregunta 1 del cuadernillo de esta
ocupación pregunta qué puede contener el paquete de esa norma y la plantilla oficial da como buena la
opción más amplia**: **datos de vídeo, de audio o de los datos auxiliares alojados en los intervalos
vertical y horizontal.**

**El razonamiento es la clave de toda la familia**: **si lo que se encapsula es el flujo digital serie
completo, entonces dentro va todo lo que ese flujo llevaba.** **La norma no separa nada, y por eso no
puede excluir nada.** **Quien responde «sólo vídeo» está pensando en la otra familia.**

**La parte 7 es la redundancia.** **Envía dos copias del mismo flujo por dos caminos distintos de la
red y el receptor reconstruye tomando de cualquiera de las dos el paquete que le falte a la otra.**
**La pregunta 47 pregunta qué estándar de vídeo sobre red tiene redundancia de conectividad en los
equipos finales y la plantilla da como buena esa parte 7.**

**Las tres cosas que hay que saber decir de esa redundancia:**

1. **Es sin corte.** **No hay conmutación que se note, porque no se conmuta: se reconstruye paquete a
   paquete.**
2. **Los dos caminos deben ser de verdad distintos.** **Dos flujos por el mismo conmutador no protegen
   de la caída de ese conmutador, que es de lo que se trataba.**
3. **No es exclusiva de la familia 2022.** **Se aplica también a los flujos de la familia 2110**, y
   por eso **la respuesta correcta la nombra como norma de redundancia y no como norma de vídeo.**

## 3. La segunda respuesta: separar las esencias

**La familia 2110 hace lo contrario que la 2022**: **en vez de encapsular la señal entera, la
descompone y manda cada esencia por su flujo.** **Vídeo por un lado, audio por otro, datos auxiliares
por otro.**

**Las razones de esa separación, que son de explotación y no de doctrina:**

- **Se lleva sólo lo que hace falta.** **Un puesto que sólo necesita el audio no arrastra el vídeo.**
- **Se cambia una esencia sin tocar las demás.** **Sustituir la mezcla de audio no obliga a rehacer el
  camino del vídeo.**
- **Cada esencia se dimensiona por separado.**

**El reparto de partes, que es lo que se pregunta:**

| Parte | Qué transporta |
|---|---|
| **La parte 10** | **el sistema: cómo se construye el conjunto y cómo se describen las sesiones** |
| **La parte 20** | **el vídeo sin comprimir** |
| **La parte 21** | **el perfil de emisión del tráfico: cómo se reparten los paquetes en el tiempo** |
| **La parte 22** | **el vídeo comprimido** |
| **La parte 30** | **el audio** |
| **La parte 31** | **el audio digital profesional de dos canales transportado de forma transparente** |
| **La parte 40** | **los datos auxiliares** |

**La pregunta 34 del cuadernillo pide la afirmación correcta entre cuatro que reparten mal las partes,
y la plantilla da como buena la que dice que la parte 30 lleva audio.** **Las otras tres colocan datos
auxiliares en la parte de vídeo, vídeo en la parte de datos auxiliares, y las tres esencias en un mismo
flujo bajo la norma de redundancia.** **Es una pregunta de tabla: quien tiene la tabla no falla.**

**Regla mnemotécnica para retener el reparto**: **las decenas van en el orden en que se descompone una
señal.** **Primero el sistema, luego la imagen, luego el sonido, luego lo que va pegado a la imagen sin
ser imagen.** **Veinte imagen, treinta sonido, cuarenta lo auxiliar.**

**Las dos preguntas que afinan dentro de la familia:**

**La primera, la 44**: **cuál de las normas de la serie permite transportar señales de audio digital
profesional preservando sus bits de validez, de usuario, de canal y de paridad.** **La plantilla da
como buena la parte 31.** **El razonamiento es que la parte 30 lleva las muestras de audio, es decir,
el sonido; y que preservar los bits de servicio de la trama exige transportar la trama entera y no sólo
su contenido.** **Esa es la diferencia entre llevar el audio y llevar el formato del audio.**

**La segunda, la 46**: **si se puede enviar vídeo comprimido con la parte 20.** **La plantilla da como
buena la respuesta más corta: no.** **La parte 20 es la del vídeo sin comprimir, y el vídeo comprimido
tiene su propia parte, la 22, que es la que admite compresiones ligeras como la que el enunciado
nombra.** **La trampa de las otras tres opciones consiste en discutir qué formato de compresión admite
la parte 20, cuando la respuesta es que no admite ninguno porque no es su cometido.**

## 4. El transporte: cómo viaja un flujo de medios por la red

**Toda la familia 2110 y la parte 6 de la 2022 usan el mismo transporte**: **el protocolo de tiempo
real, que a su vez viaja sobre datagramas de usuario.**

**Las cuatro propiedades de ese transporte y por qué se eligió:**

| Propiedad | Consecuencia |
|---|---|
| **Va sobre datagramas, no sobre conexión** | **no espera confirmaciones: no introduce retardo por esperar** |
| **Es unidireccional** | **el flujo va del origen al destino y no hay vuelta** |
| **Numera y marca en el tiempo cada paquete** | **el receptor sabe el orden y el instante de cada uno** |
| **Admite difusión selectiva** | **un origen sirve a muchos destinos con un solo envío** |

**La pregunta 45 pide cuál de cuatro características no corresponde a ese protocolo, y la plantilla da
como buena la que lo describe como un protocolo con control de paquetes perdidos.** **Y ahí está la
propiedad que hay que entender:**

**Numerar los paquetes no es controlarlos.** **El protocolo pone un número de secuencia para que el
receptor detecte que falta uno, pero no pide que se lo reenvíen y no espera a que llegue.** **La
detección es del receptor y la reparación no existe.** **Por eso una red de medios se diseña para que
no se pierdan paquetes, en lugar de para recuperarlos**: **la recuperación llegaría tarde.** **Y por
eso la redundancia de la parte 7 de la familia 2022 tiene sentido: es la única forma de sobrevivir a
una pérdida sin retransmitir.**

**Y la pieza que falta para que todo esto se pueda usar**: **el receptor tiene que saber a qué grupo de
difusión escuchar y qué formato va dentro.** **Eso lo dice el protocolo de descripción de sesión, que
es la ficha de cada flujo.** **Sin esa descripción, un flujo de medios en la red es tráfico
ininteligible.**

## 5. El ancho de banda: la comparación que se pregunta

**La pregunta 83 compara la misma señal de vídeo de alta definición progresiva a cincuenta imágenes
por segundo, transportada por la interfaz digital serie de alta definición y por la parte 20 de la
familia 2110, y pregunta cuál necesita más ancho de banda.** **La plantilla da como buena que necesita
más la interfaz digital serie.**

**El razonamiento, que es el que hay que saber explicar y no la cifra:**

1. **La interfaz digital serie transporta la trama completa, con sus intervalos de borrado vertical y
   horizontal.** **Esos intervalos son herencia del barrido de los tubos y ya no pintan nada, pero
   ocupan sitio en el cable.**
2. **La parte 20 transporta sólo la imagen activa.** **Lo que había en los intervalos, si hace falta,
   se manda aparte por la parte 40.**
3. **Menos datos por segundo con el mismo contenido útil**: **el transporte por red necesita menos
   ancho de banda.**

**El aviso de oficio que acompaña a esa respuesta**: **eso no significa que la red salga gratis.**
**El flujo por red exige que la red esté dimensionada sin sobresuscripción y con el reparto de
paquetes en el tiempo bien perfilado**, lo que **es más exigente de diseñar que tirar un cable.**
**Ahorra ancho de banda y gasta ingeniería.**

## 6. La sincronización: el reloj repartido por la red

**El problema que resuelve**: **al desaparecer el flujo continuo, desapareció el sincronismo que
llevaba dentro.** **Y las esencias van ahora por flujos separados: sin un tiempo común, el audio y el
vídeo de la misma escena no se pueden volver a juntar.**

**La solución es el protocolo de tiempo de precisión, y el enunciado del punto nombra expresamente el
perfil que lo adapta a la producción de televisión**: **la norma 2059-2 de la misma sociedad.** **Un
perfil no es un protocolo nuevo: es el conjunto de parámetros con que se usa el protocolo general en un
entorno concreto.**

**Cómo funciona, en cuatro pasos:**

1. **Un reloj de la red es el maestro y difunde la hora.**
2. **Cada equipo mide el retardo del camino de ida y vuelta hasta el maestro.**
3. **Corrige su hora con esa medida**, de modo que **la distancia deja de importar.**
4. **Los conmutadores del camino declaran cuánto tiempo ha estado el mensaje dentro de ellos**, para
   que **la cola de un conmutador no se confunda con distancia.**

**Y la pieza que se pregunta dos veces**: **cómo se elige el maestro.** **Lo decide el algoritmo del
mejor reloj maestro, que compara los relojes candidatos por una lista ordenada de criterios y se queda
con el primero que desempata.**

**La pregunta 62 pide cuál de cuatro criterios pesa más en esa elección**, y **la plantilla da como
buena la clase de reloj**, por delante de la precisión, de la desviación y de la prioridad segunda.

**La pregunta 73 plantea cuatro generadores con sus cinco parámetros y pide cuál saldría elegido.**
**La plantilla da como bueno el generador 2, y el camino es este:**

| Generador | Prioridad 1 | Prioridad 2 | Precisión | Desviación | Clase |
|---|---|---|---|---|---|
| **1** | **127** | **128** | **20 ns** | **la misma** | **7** |
| **2** | **127** | **129** | **40 ns** | **la misma** | **6** |
| **3** | **128** | **128** | **10 ns** | **la misma** | **7** |
| **4** | **128** | **129** | **60 ns** | **la misma** | **6** |

1. **Se compara primero la prioridad primera y gana el valor más bajo.** **Los generadores 1 y 2 valen
   127 y los otros dos, 128**: **quedan fuera el 3 y el 4.**
2. **Entre los dos que quedan se compara la clase de reloj, y también gana el valor más bajo.** **El
   generador 2 vale 6 y el 1 vale 7**: **gana el 2.**
3. **Ni la precisión ni la prioridad segunda llegan a mirarse**, y **ahí está la enseñanza de la
   pregunta**: **el generador 3 era el más preciso de los cuatro y no gana, porque la precisión se
   mira después de dos criterios que ya han desempatado.**

**Las dos preguntas juntas confirman el orden de los criterios sin necesidad de memorizarlo de otra
fuente**: **la prioridad primera va antes que la clase de reloj —lo dice la pregunta 73— y la clase de
reloj va antes que la precisión, la desviación y la prioridad segunda —lo dice la pregunta 62—.**
**Ese es el orden que este temario afirma, y es el que las dos plantillas sostienen.**

**El aviso de explotación**: **el valor más bajo gana en todos estos campos.** **Es contrario a la
intuición de quien lee «prioridad» y piensa que más prioridad es más número.** **Aquí prioridad uno es
mejor que prioridad dos.**

## 7. El control: descubrir, conectar y avisar

**Las normas de las familias 2022 y 2110 dicen cómo viaja la señal, no cómo se enciende.** **En una
matriz de conmutación se apretaba un botón; en una red hace falta que los equipos se encuentren y que
alguien les diga con quién hablan.**

**Eso lo cubren las especificaciones de red abierta para medios**, un conjunto de interfaces
numeradas, cada una con su cometido. **Las que este temario necesita:**

| Interfaz | Cometido |
|---|---|
| **La 04** | **registro y descubrimiento: qué equipos hay y qué ofrecen** |
| **La 05** | **conexión: quién envía a quién** |
| **La 06** | **control de la red** |
| **La 07** | **eventos y avisos, incluida la señalización de antena** |
| **La 08** | **encaminamiento de los canales de audio dentro de un equipo** |

**Las dos preguntas del cuadernillo sobre este epígrafe:**

**La 91 pregunta qué protocolo de transporte admite la interfaz de eventos y avisos, y la plantilla da
como buena la conexión por sitio de trabajo bidireccional sobre la web.** **Tiene sentido con lo que
esa interfaz hace**: **un aviso hay que empujarlo al destinatario en cuanto ocurre, y para eso hace
falta un canal permanentemente abierto en los dos sentidos**, no el envío en un solo sentido de los
flujos de medios ni la simple ficha de descripción de una sesión.

**La 93 pregunta cuál de las especificaciones está en desuso y descontinuada, y la plantilla da como
buena la de control de red, la 06.** **Es una pregunta de estado del conjunto de especificaciones y no
de doctrina técnica**: **la interfaz existió, no se adoptó y se retiró.** **Se recoge porque la
plantilla la confirma.**

## 8. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma del boletín y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.** **Las normas que este
tema nombra son normas técnicas de una sociedad de ingeniería y de un foro de la industria, no
disposiciones publicadas en un boletín oficial**, y **este proyecto no tiene su texto**: **se citan por
el número con que las nombran el propio enunciado del programa y las preguntas de la plantilla, y por
lo que la plantilla confirma de cada una, nunca por su articulado.**

**Cinco declaraciones expresas:**

1. **Las once respuestas que la plantilla oficial confirma se recogen con su número de pregunta y con
   el razonamiento que lleva a cada una**: **el contenido del paquete de la parte 6 de la familia 2022,
   en la pregunta 1**; **el reparto de esencias entre las partes de la familia 2110, en la 34**; **el
   transporte transparente del audio digital profesional por la parte 31, en la 44**; **la ausencia de
   control de pérdidas del protocolo de tiempo real, en la 45**; **la imposibilidad de mandar vídeo
   comprimido por la parte 20, en la 46**; **la redundancia de conectividad de la parte 7 de la familia
   2022, en la 47**; **el peso de la clase de reloj en el algoritmo de elección, en la 62**; **la
   elección del segundo generador, en la 73**; **el mayor ancho de banda de la interfaz digital serie
   frente a la parte 20, en la 83**; **el transporte admitido por la interfaz de eventos, en la 91**;
   y **la interfaz descontinuada, en la 93.**
2. **Los cinco parámetros de los cuatro generadores de la tabla del epígrafe 6 están tomados del
   propio enunciado de la pregunta 73 y no de ninguna otra fuente.** **La desviación se recoge como «la
   misma» porque el enunciado da a los cuatro el mismo valor y por tanto no desempata.**
3. **El orden de los criterios del algoritmo de elección del maestro que este tema afirma —la prioridad
   primera antes que la clase de reloj, y la clase de reloj antes que la precisión, la desviación y la
   prioridad segunda— se deriva de las dos preguntas de la plantilla y así se declara.** **El tema no
   afirma el orden relativo entre la precisión, la desviación y la prioridad segunda, porque ninguna
   pregunta lo desempata.**
4. **Este tema no da ningún ancho de banda en bits por segundo, ninguna cifra de retardo admisible,
   ninguna tolerancia de sincronismo, ningún tamaño de paquete y ninguna versión de norma.** **Son dato
   de la propia norma técnica, que este proyecto no tiene**, y **una cifra que no se ha leído en su
   fuente no se escribe.** **Los nanosegundos del epígrafe 6 son los del enunciado de la pregunta.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **las redes,
   sus modelos de referencia, la difusión selectiva y la conmutación, al tema 20**; **el
   almacenamiento y los servidores sobre esa misma infraestructura, al tema 18**; **la señal digital
   serie, sus formatos y su medida, a los temas 5 y 8**; **la compresión, al tema 6**; **el audio y sus
   formatos, al tema 21**; y **las salas y su equipamiento, al tema 13.**

**El resto del tema va como oficio y así se declara**: la idea de que todo el punto existe para
reconstruir con protocolos lo que el cable dedicado daba gratis, las dos tablas de lo que se pierde y
lo que se gana al dejar la interfaz dedicada, el razonamiento de que encapsular el flujo completo
obliga a admitir todo lo que ese flujo llevaba, las tres cosas que hay que saber decir de la
redundancia sin corte y el aviso de que dos caminos por el mismo conmutador no protegen, las tres
razones de explotación por las que se separan las esencias, la regla mnemotécnica de las decenas, la
distinción entre llevar el audio y llevar el formato del audio, la lectura de que numerar paquetes no
es controlarlos y de que por eso la red se diseña para no perderlos, el papel de la descripción de
sesión como ficha del flujo, el razonamiento del ancho de banda por los intervalos de borrado con el
aviso de que la red ahorra ancho de banda y gasta ingeniería, los cuatro pasos del reparto de hora, la
enseñanza de que el generador más preciso no gana, el aviso de que el valor más bajo gana en todos los
campos de la elección, y la explicación de por qué una interfaz de avisos necesita un canal abierto en
los dos sentidos. **Nada de eso está en un boletín oficial ni en ninguna fuente consultada para este
proyecto**, y el tema no lo presenta como si lo estuviera.
