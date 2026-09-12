# Esquema · Tema 7 del específico de Ingeniería Técnica · Telecomunicación · Vídeo y audio sobre red

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalación · `[exam]` =
opciones del propio cuadernillo · `[norma]` = norma técnica nombrada, sin cita literal. **Siglas**: el
protocolo de internet (**IP**) y el de datagramas de usuario (**UDP**); la Sociedad de Ingenieros de
Cine y Televisión (**SMPTE**), con las familias **SMPTE ST 2110** y **SMPTE ST 2022**; la Sociedad de
Ingeniería de Audio (**AES**), con **AES3** y **AES67**; el protocolo de tiempo de precisión
(**PTP**); la interfaz digital serie (**SDI**); la modulación por impulsos codificados (**PCM**); la
norma del año 2000 del grupo conjunto de expertos en fotografía (**JPEG 2000**); la red de área local
virtual (**VLAN**); y el descubrimiento, registro y control en red (**NMOS**).

**Cabecera.** Enunciado: puntos 8 y 9 del anexo, reunidos porque **el segundo es la aplicación del
primero** · **5 preguntas** · **es el punto que define hacia dónde va la ocupación**: lo que se
construye hoy es de red.

<!-- indice -->

## Índice

- [Qué cambia al pasar a la red](#qué-cambia-al-pasar-a-la-red)
- [La familia SMPTE ST 2110](#la-familia-smpte-st-2110)
- [La familia SMPTE ST 2022](#la-familia-smpte-st-2022)
- [Las dos redes](#las-dos-redes)
- [La sincronización por red](#la-sincronización-por-red)
- [La producción sobre red](#la-producción-sobre-red)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué cambia al pasar a la red

| Lo que el coaxial daba solo | Cómo se recupera |
|---|---|
| **Sincronismo** | **Reloj de precisión repartido por la propia red** |
| **Latencia previsible** | **Calidad de servicio y red bien dimensionada** |
| **Entrega ordenada y completa** | **Redundancia de camino y numeración de secuencia** |
| **Un cable, una señal** | **Ya no: por un cable van muchas, y hay que decir cuáles** |

| Ventaja | Por qué |
|---|---|
| **Un solo cable para todo** | **Vídeo, audio, control y datos por la misma infraestructura** |
| **Encaminamiento sin límite de tamaño** | **Un conmutador crece; una matriz tiene tamaño fijo** |
| **Equipo genérico** | **Electrónica de red corriente en vez de matriz de un fabricante** |
| **Flexibilidad** | **Reconfigurar es cambiar una suscripción, no recablear** |

- **EL PRECIO** · `[of]` · **La instalación pasa a depender de una red que hay que diseñar, dimensionar
  y administrar.** **Un fallo de configuración ya no deja un ordenador sin correo: deja un plató sin
  imagen.**

## La familia SMPTE ST 2110

| | **Interfaz digital serie** | **La familia de red** |
|---|---|---|
| **Vídeo, audio y datos** | **Incrustados en la misma trama** | **En flujos SEPARADOS** ✔ |
| **Cambiar un canal de audio** | **Hay que tocar la señal entera** | **Se cambia sólo ese flujo** |
| **Llevar audio a otro sitio** | **Va el vídeo con él** | **Va solo** |
| **Qué los mantiene juntos** | **La propia trama** | **El reloj común** |

- **PREGUNTA 62** · `[exam]` · **Su característica clave es la separación de vídeo, audio y metadatos
  en flujos independientes.**
- **LA CONSECUENCIA** · `[of]` · **Una mesa de sonido puede suscribirse a los flujos de audio sin
  recibir un bit de vídeo.**
- **LAS FALSAS** · `[exam]` · **«Encapsulación en un único flujo»**: lo contrario. **«Uso de
  compresión»**: su vídeo va sin comprimir. **«Depende de la interfaz de coaxial»**: es lo que
  sustituye.

| Parte | Qué normaliza |
|---|---|
| **ST 2110-10** · `[norma]` | **Arquitectura y sincronización** ✔ |
| **ST 2110-20** · `[norma]` | **Vídeo SIN COMPRIMIR** ✔ |
| **ST 2110-21** · `[norma]` | **Perfil de tráfico: cómo se reparten los paquetes en el tiempo** |
| **ST 2110-30** · `[norma]` | **Audio, basado en la norma de interoperabilidad** ✔ |
| **ST 2110-31** · `[norma]` | **Audio en formato AES3 transparente** |
| **ST 2110-40** · `[norma]` | **Datos auxiliares** |

- **PREGUNTA 5** · `[exam]` · **La descripción correcta: la 10 es arquitectura y sincronización, la 20
  vídeo sin compresión, la 30 audio basado en la norma de interoperabilidad.**
- **PREGUNTA 78** · `[exam]` · **SMPTE 2110-20 especifica el transporte de vídeo sin comprimir.**
- **LAS DOS PALABRAS QUE DECIDEN LA 5** · `[of]` · **«Sin compresión» en la parte de vídeo** y **el
  nombre de la norma en la de audio.** **La 30 se basa en la de interoperabilidad; la que usa AES3 es
  la 31.**
- **EL AVISO DE OBRA** · `[of]` · **La parte 21 no sale en el examen y es la que más problemas da.**
  **Un emisor que no respete su perfil satura las colas del conmutador y produce pérdidas** aunque el
  enlace tenga capacidad de sobra.

## La familia SMPTE ST 2022

| Parte | Qué normaliza |
|---|---|
| **ST 2022-1 y -2** · `[norma]` | **Flujo comprimido sobre red, con corrección de errores** |
| **ST 2022-5 y -6** · `[norma]` | **La señal de coaxial ENTERA sobre red** |
| **ST 2022-7** · `[norma]` | **Protección sin costura: dos caminos simultáneos** ✔ |

- **PREGUNTA 14** · `[exam]` · **SMPTE 2022-7 trata de conmutación con protección total para vídeo sin
  comprimir.**
- **CÓMO FUNCIONA** · `[of]` · **El emisor manda DOS copias idénticas por dos caminos físicamente
  distintos** · **cada paquete lleva su número de secuencia** · **el receptor toma el primero que llega
  de cada número y descarta el duplicado** · **si un camino falla, el otro ya está.**
- **DE AHÍ EL NOMBRE** · `[of]` · **No es que el cambio sea rápido: es que NO HAY cambio.**
- **LA DIFERENCIA ENTRE LAS DOS FAMILIAS** · `[of]` · **Las partes 5 y 6 meten la señal entera de
  coaxial en la red tal cual; la otra familia la descompone en flujos.** **Una es un puente entre los
  dos mundos y la otra es el mundo nuevo.**

## Las dos redes

- **PREGUNTA 67** · `[exam]` · **Las redes roja y azul son dos redes por las que se transmite la señal,
  de forma balanceada, para dar redundancia.**
- **LA PRECISIÓN DECLARADA** · `[of]` · **Las dos redes NO se reparten la carga: llevan LAS DOS el
  flujo completo, a la vez.** **«Balanceada» significa que las dos están igualmente activas** —frente a
  principal y reserva—, **no que cada una lleve la mitad.**

| Falsa | Por qué cae |
|---|---|
| **Una activa y otra de reserva** | **Eso es conmutación con hueco: lo que la protección evita** |
| **Vídeo por una y audio por la otra** | **Sería reparto, no redundancia: al caer una se pierde la mitad** |
| **Vídeo y audio por una, datos por la otra** | **Lo mismo** |

- **POR QUÉ ROJA Y AZUL** · `[of]` · **Convenio de instalación, no de norma**: **dos colores para que
  nadie confunda de qué red es un cable** y **para que las dos rutas sean físicamente distintas de
  principio a fin**: distintos conmutadores, bandejas y, a poder ser, salas.
- **EL FALLO DE DISEÑO MÁS FRECUENTE** · `[of]` · **Dos redes que comparten un conmutador, una bandeja
  o un cuadro eléctrico NO son dos redes.** **La redundancia se rompe en el punto que comparten.**

## La sincronización por red

- **QUÉ RESUELVE** · `[of]` · **En coaxial la referencia llegaba por un cable propio; en red hay que
  repartir el tiempo por la misma red que lleva la señal**, con precisión de microsegundos.
- **CÓMO FUNCIONA EL PROTOCOLO DE TIEMPO DE PRECISIÓN** · `[of]` · **Se elige un reloj maestro
  automáticamente**, por un algoritmo que compara calidades · **el maestro manda mensajes con la hora
  exacta de salida** · **cada esclavo mide el retardo de ida y vuelta** · **con él corrige su reloj.**
- **LA PIEZA QUE LO HACE POSIBLE EN RED GRANDE** · `[of]` · **Los conmutadores compatibles CORRIGEN el
  tiempo que el mensaje pasa dentro de ellos y lo escriben en el propio mensaje.**
- **EL AVISO DE INSTALACIÓN** · `[of]` · **Un conmutador que no soporte el protocolo puede pasar el
  tráfico perfectamente y arruinar la sincronía.** **No se ve en las pruebas de caudal**: aparece como
  deriva lenta que nadie relaciona con la red.

## La producción sobre red

| Capa | Qué resuelve |
|---|---|
| **Transporte** | **Las familias de normas anteriores** |
| **Sincronización** | **El reloj de precisión** |
| **Descubrimiento y registro** | **Que un equipo nuevo diga quién es y qué ofrece** |
| **Conexión** | **Que un receptor se suscriba al flujo que quiere** |
| **Control de equipos** | **La configuración remota** |

- **QUIÉN NORMALIZA QUÉ** · `[of]` · **Las dos primeras, la Sociedad de Ingenieros de Cine y
  Televisión; las dos siguientes no lo estaban**, y de ahí **el conjunto de especificaciones abiertas
  de descubrimiento y control** que la industria adoptó.
- **EL CAMBIO DE MENTALIDAD** · `[of]` · **En coaxial, encaminar era CONECTAR una salida con una
  entrada; en red, encaminar es que un receptor SE SUSCRIBA a un flujo.** **La matriz deja de ser un
  aparato y pasa a ser una función del control.**
- **LOS TRES PROBLEMAS NUEVOS** · `[of]` · **El envío a varios destinos hay que gestionarlo**: una red
  que no gestione la suscripción a grupos inunda todos los puertos y se cae sola · **el dimensionado
  deja de ser evidente**: alta definición sin comprimir son unos 1,5 gigabits por segundo y ultraalta
  cuatro veces más, así que **un enlace de diez gigabits admite muy pocas** · **la red es ya parte de la
  cadena de señal** y hay que medirla como se medía la señal, con supervisión permanente.

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 5 | Descripción correcta de las partes de la familia | **Arquitectura, vídeo sin compresión, audio interoperable** ✔ |
| 14 | De qué trata SMPTE 2022-7 | **Conmutación con protección total** ✔ |
| 62 | Característica clave de SMPTE 2110 | **Separación en flujos independientes** ✔ |
| 67 | Qué son las redes roja y azul | **Dos redes con la señal, para redundancia** ✔ **·** con precisión |
| 78 | Qué especifica SMPTE 2110-20 | **Vídeo sin comprimir** ✔ |
