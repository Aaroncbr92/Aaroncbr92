# Esquema · Tema 11 del específico de Ingeniería Superior · Telecomunicación · Producción I: cámaras, conmutación, grabación y edición

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de producción de televisión ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: la
interfaz de propósito general (**GPI**), que es la señal de disparo; la unidad de control de cámara
(**CCU**); y la interfaz digital serie (**SDI**).

**Cabecera.** Enunciado: punto 11 del anexo · **cuatro preguntas** · **sin norma del boletín**.

**La idea que lo ordena** · `[of]` · **Un plató no lo hace la cámara: lo hace la IGUALACIÓN.** **Dos
cámaras del mismo modelo con la misma luz no dan la misma imagen si no se igualan**, y **un corte entre
dos cámaras desiguales se ve inmediatamente.**

<!-- indice -->

## Índice

- [La cadena de cámara](#la-cadena-de-cámara)
- [La óptica](#la-óptica)
- [El sensor](#el-sensor)
- [La suspensión](#la-suspensión)
- [La conmutación](#la-conmutación)
- [Grabación y edición](#grabación-y-edición)
- [El cordón umbilical](#el-cordón-umbilical)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La cadena de cámara

| Pieza | Qué hace |
|---|---|
| **óptica** | **forma la imagen y decide encuadre, profundidad y luminosidad** |
| **bloque óptico y sensor** | **convierte la luz en señal** |
| **cabeza de cámara** | **procesa, codifica y manda**; visor, intercomunicación y señalización |
| **cable de cámara** | **señal, retorno, comunicaciones, mando y alimentación en un cordón** |
| **unidad de control** | **el otro medio aparato**: alimenta, recupera, procesa y entrega |
| **panel de control remoto** | **donde se ajustan diafragma, negros y matriz** |
| **panel maestro** | **configuración y ajuste fino de todas las cámaras a la vez** |

- **dos personas y dos puestos** · `[of]` · **El operador de cámara encuadra y enfoca; el de control de
  imagen expone e iguala.** **La exposición y el color tienen que ser los mismos en todas las cámaras
  del plató, y eso no se puede hacer desde el visor.**

## La óptica

| Parámetro | Qué decide |
|---|---|
| **distancia focal** | **el ángulo de visión: corta abre, larga cierra** |
| **apertura máxima** | **con qué luz se puede trabajar** |
| **profundidad de campo** | **cuánto queda enfocado por delante y por detrás** |
| **extensor** | **multiplica la focal a costa de luminosidad** |

- **LAS TRES REGLAS DE LA PROFUNDIDAD, QUE SIEMPRE SE PREGUNTAN JUNTAS** · `[of]` · **Disminuye al
  abrir el diafragma, al alargar la focal y al acercarse al motivo.** **Y a igual encuadre, un sensor
  mayor da MENOS profundidad**, que es lo contrario de lo que dice la intuición.
- **un zum no es un travelín** · `[of]` · **El zum cambia el ángulo de visión y comprime la
  perspectiva; el travelín cambia el punto de vista.** **Confundirlos es un error de lenguaje que un
  ingeniero no debe cometer al hablar con realización.**

## El sensor

| Parámetro | Qué es |
|---|---|
| **tamaño** | **la superficie sensible** |
| **tamaño del píxel** | **superficie dividida por número de píxeles** |
| **sensibilidad** | **cuánta señal da con poca luz** |
| **rango dinámico** | **cuántos pasos hay entre el ruido y la saturación** |
| **tipo de obturación** | **global o por barrido**, con su artefacto |

- **LA RELACIÓN QUE SE PREGUNTA** · `[exam]` · **A igual número de píxeles, un sensor MÁS GRANDE ofrece
  generalmente MAYOR rango dinámico**, porque **cada píxel es más grande y CAPTA MÁS LUZ**: recoge más
  señal antes de saturarse y su ruido relativo es menor.
- **por qué fallan las otras tres** · `[exam]` · **Decir que el tamaño no influye separa
  artificialmente el sensor de su física**; **decir que un sensor pequeño da más rango invierte la
  relación** —un píxel pequeño capta menos luz, no más—; **y la resolución temporal es otro parámetro
  que no tiene que ver.**
- **la obturación por barrido** · `[of]` · **Un sensor que lee línea a línea deforma lo que se mueve
  deprisa y parte los flashes.** **En estudio no suele importar; en acción o grabando pantallas, sí.**

## La suspensión

| Elemento | Qué aporta |
|---|---|
| **trípode con rótula fluida** | **movimiento amortiguado y repetible** |
| **pedestal de estudio** | **altura ajustable con compensación de peso** |
| **plataforma rodante y travelín** | **desplazamiento sobre ruedas o raíles** |
| **grúa y brazo** | **movimiento en altura y en arco** |
| **cabeza robotizada** | **movimiento motorizado con control remoto** |
| **estabilizador corporal y cardán** | **cámara en movimiento sin vibración** |
| **cámara sobre cable** | **vuelo sobre un recinto** |

- **LA PREGUNTA Y SU RAZONAMIENTO** · `[exam]` · **Controlar el movimiento de la cabeza y además el
  foco y el zum sin operador es ROBOTIZACIÓN.** **«Movimiento axial» y «rotación neumática» no son
  categorías de este oficio, y la monitorización observa pero no mueve.**
- **lo que un sistema de robotización necesita** · `[of]` · **control de cabeza y de óptica** ·
  **memorias de posición** —volver al mismo encuadre es lo que lo hace útil en un informativo diario—
  · **protección contra colisión**, con límites programados.

## La conmutación

| Equipo | Qué hace |
|---|---|
| **mezclador de producción** | **PRODUCE: barras de programa y previo, transiciones, incrustadores** |
| **matriz de conmutación** | **ENCAMINA: conecta una entrada con una salida y no toca la señal** |
| **matriz de teclado, vídeo y ratón** | **un puesto maneja varias máquinas** |

- **EL AUDIO QUE SIGUE AL VÍDEO** · `[exam]` · **Es un modo de operación asociado a los CONMUTADORES de
  vídeo y audio**: **al conmutar una fuente de vídeo se conmuta con ella su audio asociado.** **No es
  de las cámaras, ni del sistema multipantalla, ni de los servidores de grabación.** **Quien pincha
  imagen no tiene que acordarse de pinchar el sonido.**
- **LA SEÑAL DE DISPARO** · `[exam]` · **La interfaz de propósito general es una señal de DISPARO**: un
  contacto que se cierra o un nivel que cambia. **No es sincronismo, ni radiofrecuencia, ni audio.**
  **Sirve para que un equipo le diga a otro «ahora».**
- **las dos reglas del disparo** · `[of]` · **1)** es la interconexión más barata y la más frágil: **un
  contacto suelto no da error, sencillamente no dispara**, y **el fallo aparece en directo**. **2)** en
  una instalación sobre red se sustituye por un mensaje: **se gana registro y se pierde inmediatez**, y
  **por eso los disparos críticos se siguen cableando.**

## Grabación y edición

| Soporte | Rasgo |
|---|---|
| **cinta** | **acceso secuencial**; **sobrevive en archivo por su coste y su vida** |
| **tarjeta de estado sólido** | **rápida y frágil ante el borrado accidental** |
| **servidor de producción** | **la grabación es un fichero en una cabina**: es lo que domina hoy |

- **la clave del oficio actual** · `[of]` · **Con cinta, el material ESTÁ en un sitio y hay que
  llevarlo; con fichero, está DISPONIBLE y lo que se gestiona son permisos, catálogo y copias.** **El
  trabajo se traslada del transporte a la gestión**, y **por eso existen los temas 14, 18 y 19.**

| Concepto de edición | Qué es |
|---|---|
| **ingesta** | **meter el material en el sistema, con sus metadatos** |
| **copia de trabajo ligera** | **una versión de baja tasa para montar sin mover el original** |
| **lista de decisiones** | **el montaje descrito por referencias al original, sin medios** |
| **conformado** | **rehacer el montaje sobre el material de alta calidad** |

- **las dos reglas del flujo con copias ligeras** · `[of]` · **1) el original no se toca**: se monta
  sobre la copia y se conforma al final. **2) el código de tiempo es lo que ata las dos**: **si copia y
  original no lo comparten, el conformado no cuadra**, y **ése es el fallo más frecuente de una
  ingesta mal configurada.**

## El cordón umbilical

| Sistema | Su límite |
|---|---|
| **coaxial de triple malla** | **distancia y ancho de banda**: tecnología madura |
| **fibra híbrida** | **manipulación**: el conector es delicado y hay que limpiarlo |
| **cámara inalámbrica** | **espectro, latencia e interferencia**: hay que coordinar frecuencias |

- **es una decisión de instalación, no de cámara** · `[of]` · **Cambiar de coaxial a fibra en un plató
  es una obra**, y **por eso conviven los dos durante años.**
- **lo inalámbrico se PLANIFICA** · `[of]` · **Varias cámaras sin cable, micrófonos inalámbricos e
  intercomunicación necesitan un plan de frecuencias**, y **improvisarlo es como se pierde una señal en
  el peor momento.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 40 | Qué es el modo en que el audio sigue al vídeo | **Un modo operativo asociado a los conmutadores de vídeo y audio** ✔ |
| 60 | Cómo influye el tamaño del sensor en el rango dinámico | **El más grande ofrece generalmente mayor rango, porque capta más luz en cada píxel** ✔ |
| 81 | Sistema para mover la cabeza y la óptica sin operador | **Robotización** ✔ |
| 95 | Qué tipo de señal es la interfaz de propósito general | **Una señal de disparo** ✔ |
