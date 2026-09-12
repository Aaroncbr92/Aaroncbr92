# Esquema · Tema 21 del específico de Ingeniería Superior · Telecomunicación · Sonido

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de sonido · `[plan]` = enunciado
del propio anexo · `[exam]` = opciones del propio cuadernillo · `[LGCA]` = Ley 13/2022, General de
Comunicación Audiovisual, citada literalmente en el tema. **Siglas**: el hercio (**Hz**) y el kilohercio
(**kHz**); la interfaz de audio digital profesional de dos canales (**AES3**), también nombrada
**AES/EBU**; la interfaz digital multicanal (**MADI**); el conversor de frecuencia de muestreo
(**SRC**); y la Ley General de Comunicación Audiovisual (**LGCA**).

**Cabecera.** Enunciado: punto 23 del anexo · **siete preguntas** · **CON norma**: **su último
enunciado pide la regulación básica de la radiodifusión sonora en España**, y **eso es el título IV de
la Ley 13/2022**, que **el tema cita literalmente.** **Es el único punto del específico de esta
ocupación que se apoya en el boletín.**

**La idea que lo ordena** · `[of]` · **Casi todo lo que se pregunta consiste en saber cuál de los
atributos del sonido se está tocando.** **Quien confunde intensidad con frecuencia falla la pregunta
más fácil; quien confunde nivel con volumen percibido, la más difícil.**

<!-- indice -->

## Índice

- [Los atributos](#los-atributos)
- [De analógico a digital](#de-analógico-a-digital)
- [La trama profesional y sus bits](#la-trama-profesional-y-sus-bits)
- [Medida y control](#medida-y-control)
- [Captación y escucha](#captación-y-escucha)
- [Contenedor, códec y compresión](#contenedor-códec-y-compresión)
- [La regulación de la radiodifusión sonora](#la-regulación-de-la-radiodifusión-sonora)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los atributos

| Atributo | Qué determina |
|---|---|
| **frecuencia** | **el TONO o altura** |
| **amplitud** | **la sonoridad** |
| **composición armónica** | **el timbre** |
| **duración** | **cuánto dura, no cómo suena** |
| **velocidad de propagación** | **nada de la percepción**: es propiedad del MEDIO |

- **el aviso** · `[of]` · **La velocidad de propagación no es un atributo del sonido sino del medio por
  el que viaja.** **Aparece en las opciones porque suena a magnitud de sonido y no lo es.**

## De analógico a digital

| Decisión | Qué limita |
|---|---|
| **frecuencia de muestreo** | **la frecuencia más alta que se puede representar** |
| **bits por muestra** | **la finura con que se distinguen niveles, y con ella el margen dinámico** |

- **la regla que las une** · `[of]` · **Para representar una frecuencia hay que muestrear a más del
  doble.** **Por debajo, las frecuencias altas no desaparecen: reaparecen disfrazadas de bajas que
  nunca estuvieron ahí**, y **eso ya no se deshace.** **Filtrar antes es la única defensa.**
- **EL CASO DE LAS DOS FRECUENCIAS** · `[exam]` · **Una mesa digital que recibe una señal muestreada a
  otra frecuencia usa un CONVERSOR de frecuencia de muestreo.** **Meterla por analógico son dos
  conversiones innecesarias; un atenuador cambia el nivel y no la frecuencia; y decir que no se puede
  es falso.**
- **el aviso** · `[of]` · **Convertir no es gratis**: **recalcula muestras que no se tomaron e introduce
  su propio error, además de retardo.** **Cuando se puede, se sincroniza toda la instalación y no se
  convierte nada.**

## La trama profesional y sus bits

| Bit | Para qué sirve |
|---|---|
| **V, de validez** | **decir si la muestra es apta para un procesado posterior, como pasarla a analógica** |
| **U, de usuario** | **transportar información del usuario, ajena a la muestra** |
| **C, de estado de canal** | **describir el propio flujo: formato, uso, frecuencia** |
| **P, de paridad** | **permitir detectar errores en la trama** |

- **LA TRAMPA DE ESA PREGUNTA** · `[exam]` · **Las tres opciones falsas son verdad… DE OTRO BIT**: **la
  detección de errores es de la paridad, la información de usuario es del suyo, y lo de la frecuencia
  de muestreo va en el estado de canal.** **Separa a quien se sabe la tabla de quien reconoce las
  palabras.**
- **el enganche con el tema 19** · `[of]` · **Lo que la parte 31 de la familia de transporte por red
  lleva de forma transparente son precisamente estos cuatro bits.** **No basta con llevar el audio: hay
  que llevar la trama.**
- **el paso a muchos canales** · `[exam]` · **La interfaz multicanal lleva por un solo enlace un haz de
  canales digitales**, y **la plantilla confirma la cifra de sesenta y cuatro para el caso que su
  pregunta plantea.** **El temario no da ninguna otra capacidad de esa interfaz.**

## Medida y control

| Instrumento | Qué mide |
|---|---|
| **medidor de valor medio** | **nivel promediado, con respuesta lenta**: no ve los picos |
| **medidor de picos** | **el valor instantáneo máximo**: es el que PROTEGE |
| **medidor de sonoridad** | **el nivel percibido**: iguala el volumen entre programas |
| **medidor de correlación** | **la relación de FASE entre los dos canales de un estéreo** |
| **sonómetro** | **la presión sonora en el aire de una sala**: no mide señales eléctricas |

- **LA PREGUNTA DE LA FASE** · `[exam]` · **Se detecta con el MEDIDOR DE CORRELACIÓN.** **Las otras
  tres opciones miden NIVEL, cada una a su manera, y ninguna mira la relación entre canales.**
- **por qué importa** · `[of]` · **Dos canales en contrafase se CANCELAN al sumarlos a monofonía.**
  **Como parte del público escucha en un solo altavoz, una contrafase no detectada es un programa que
  se emite prácticamente mudo para esa parte del público.**
- **la distinción de nivel** · `[of]` · **El pico se vigila para no romper; la sonoridad, para no
  molestar.** **Dos programas con el mismo pico pueden sonar muy distinto.**

## Captación y escucha

| Patrón polar | De dónde capta | Cuándo se elige |
|---|---|---|
| **omnidireccional** | **de todas las direcciones por igual** | **ambiente, cuando no hay ruido que rechazar** |
| **cardioide** | **sobre todo de delante; rechaza lo de atrás** | **una fuente al frente, con ruido alrededor** |
| **bidireccional** | **de delante y de atrás; rechaza los lados** | **dos fuentes enfrentadas** |
| **cañón** | **un ángulo frontal muy estrecho** | **cuando no se puede acercar el micrófono** |

- **LA TRAMPA DE ESA PREGUNTA** · `[exam]` · **«Inalámbrico» no es un patrón polar sino una forma de
  llevar la señal.** **Un micrófono inalámbrico tiene además su patrón.** **Mezclar la clasificación
  por patrón con la clasificación por enlace es el error que la opción busca.**
- **el altavoz de graves** · `[exam]` · **Su colocación NO es especialmente crítica.** **El oído
  localiza por diferencias de tiempo e intensidad entre los dos oídos, y ambas se vuelven inservibles
  cuando la longitud de onda es mucho mayor que la cabeza**, que es el caso de las frecuencias que ese
  altavoz reproduce.
- **el matiz para no decir una tontería** · `[of]` · **Eso vale para la LOCALIZACIÓN, no para la
  respuesta de la sala.** **En una esquina excita los modos del recinto y suena más; en el centro puede
  caer en un mínimo.** **La posición no cambia de dónde parece venir, pero sí cuánto suena.**

## Contenedor, códec y compresión

| Concepto | Qué es |
|---|---|
| **codificación** | **cómo se representan las muestras** |
| **códec** | **el algoritmo que comprime y descomprime** |
| **contenedor** | **el envoltorio de fichero, con sus datos descriptivos** |

- **la regla que evita el error** · `[of]` · **El contenedor no dice cómo suena.** **Preguntar «qué
  calidad tiene este formato» sin mirar el códec no tiene respuesta.**
- **cómo funciona la compresión con pérdida** · `[of]` · **Aprovecha que un sonido fuerte tapa a otro
  más flojo cercano en frecuencia o inmediatamente posterior.** **Un códec no se juzga por lo que
  conserva sino por lo bien que acierta al decidir qué tirar.**
- **el aviso** · `[of]` · **Comprimir con pérdida dos veces no descarta dos veces lo mismo.** **Cada
  paso decide sobre lo que le llega.** **Se trabaja sin comprimir o sin pérdida y se comprime una sola
  vez, al final.**
- **el transporte simétrico** · `[of]` · **La conexión simétrica no elimina el ruido por blindaje, sino
  por RESTA**: el ruido se induce por igual en los dos conductores y desaparece al hacer la diferencia.
  **Por eso una tirada larga se hace simétrica y no más gruesa.**

## La regulación de la radiodifusión sonora

- **dónde está** · `[LGCA]` · **En el título IV de la Ley 13/2022**, rotulado **«La prestación del
  servicio de comunicación audiovisual radiofónico y sonoro a petición»**, **en su redacción vigente el
  21 de diciembre de 2022, que es la inicial.**
- **la distinción sobre la que se construye** · `[LGCA]` · **Hay DOS servicios: el radiofónico, que es
  la radio, y el sonoro a petición, que es el catálogo.** **El régimen se parece pero no coincide, y
  las preguntas viven en la diferencia.**

| Artículo | Qué resuelve |
|---|---|
| **76** | **comunicación previa sin espectro; LICENCIA en concurso con espectro** |
| **77** | **Consejo de Ministros por encima de una Comunidad Autónoma; la Comunidad, dentro** |
| **78** | **los cuatro límites de concentración** |
| **79** | **emisión en cadena** |
| **80** | **negocios sobre licencias: autorización, dos años, prohibición de subarriendo** |
| **81** | **radio comunitaria sin ánimo de lucro** |
| **82** | **cesión de la señal, con el matiz del prestador público** |
| **83** | **menores, y la franja de la una a las cinco** |
| **84** | **accesibilidad de los servicios sonoros a petición** |
| **85** | **comunicaciones comerciales, patrocinio y emplazamiento** |

- **LA REGLA EN UNA LÍNEA** · `[LGCA]` · **Si se usa espectro radioeléctrico, hace falta licencia
  obtenida en concurso; si no se usa, basta con comunicar antes de empezar.** **Lo que separa los dos
  regímenes no es el contenido ni el tamaño: es el uso de las ondas hertzianas terrestres.**
- **los cuatro límites de concentración** · `[LGCA]` · **más del cincuenta por ciento de las licencias
  que coincidan sustancialmente en su ámbito** · **más de CINCO licencias en un mismo ámbito de
  cobertura** · **más de un tercio de las de ámbito estatal** · **más del cuarenta por ciento en una
  Comunidad Autónoma, en ámbitos con una sola licencia.**
- **las dos reglas de cómputo** · `[LGCA]` · **quedan fuera las emisoras gestionadas de forma directa
  por entidades públicas**, y **los límites se aplican de forma independiente a lo digital y a lo
  analógico**, lo que **impide sumar unas y otras.**
- **lo que hay que retener del artículo 80** · `[LGCA]` · **transmisión y arrendamiento exigen que hayan
  pasado al menos DOS AÑOS desde la adjudicación inicial**; **el arrendatario pasa a ser prestador del
  servicio**; y **en todo caso está prohibido el subarriendo.**
- **la franja horaria** · `[LGCA]` · **De la una a las cinco** para **esoterismo y paraciencias con
  participación de los oyentes** —con responsabilidad subsidiaria del prestador— y para **juegos de
  azar y apuestas**, salvo los sorteos de las loterías reservadas y los juegos de concursos conexos a
  la actividad ordinaria del prestador.

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 4 | Cuántos audios monofónicos digitales caben en la interfaz multicanal | **64** ✔ |
| 6 | Dónde se coloca el altavoz de graves en una escucha multicanal | **Su colocación no es especialmente crítica** ✔ |
| 50 | Para qué se usa el bit de validez | **Para decir si la muestra es apta para un procesado adicional** ✔ |
| 57 | Con qué se detecta si un estéreo está en fase o contrafase | **Medidor de correlación** ✔ |
| 64 | Qué hacer con una señal digital de otra frecuencia de muestreo | **Un conversor de frecuencia de muestreo** ✔ |
| 79 | Qué micrófono en entorno ruidoso con el entrevistado al frente | **Cardioide** ✔ |
| 80 | Qué atributo determina el tono o la altura | **La frecuencia** ✔ |
