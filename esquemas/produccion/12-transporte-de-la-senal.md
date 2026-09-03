# Esquema · Tema 12 del específico de Producción · Transporte de la señal

**Siglas**: la Unión Internacional de Telecomunicaciones (**UIT**).

Telegrama. **Cada línea lleva delante de dónde sale**: `[UIT-R]` = Recomendación UIT-R SNG.770-2, en
su edición en español · `[LiveU]` = ficha del producto LU800 del fabricante, leída el 03/09/2026 ·
`[oficio]` = práctica de contribución, declarada como tal.

**Siglas**: la línea de abonado digital asimétrica (**ADSL**); la Unión
Internacional de Telecomunicaciones (**UIT**) con su Sector de Radiocomunicaciones (**UIT-R**);
Unión Internacional de Telecomunicaciones (**UIT**).

**Cabecera.** Enunciado: «TRANSPORTE DE LA SEÑAL» · **4 preguntas**, **una por cada vía del epígrafe
de vías**, sin repetir materia · **la 38 es la ÚNICA pregunta de todo el examen contrastable en la
ficha de un fabricante**.

<!-- indice -->

## Índice

- [Contribución y distribución](#contribución-y-distribución)
- [Las vías de transporte](#las-vías-de-transporte)
- [Qué NO transmite](#qué-no-transmite)
- [El enlace por satélite](#el-enlace-por-satélite)
- [Las mochilas de agregación](#las-mochilas-de-agregación)
- [La producción remota](#la-producción-remota)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Contribución y distribución

| | **CONTRIBUCIÓN** | **DISTRIBUCIÓN** o emisión |
|---|---|---|
| Qué es | **Hacia el CENTRO DE PRODUCCIÓN**, para seguir trabajando la señal | **Hacia el ESPECTADOR** |
| Calidad | **Alta**: se va a manipular después | La que permita el sistema de emisión |
| Compresión | **Poca o ninguna** | La del sistema de emisión |
| Retardo | **El menor posible** | Menos crítico |
| Quién la ve | El equipo técnico | El público |

- **Este punto trata LA CONTRIBUCIÓN.** La distribución es del tema 13.

## Las vías de transporte

| Vía | Ventaja | Límite |
|---|---|---|
| **Fibra óptica** | **Capacidad, calidad, retardo mínimo** | **Hay que tenerla puesta**: no vale para lo imprevisto |
| **Microondas** | Rápido de montar | **Necesita VISIÓN DIRECTA** y coordinar frecuencias |
| **Satélite (DSNG)** | **Llega desde cualquier sitio** | Coste, licencia y **RETARDO** |
| **Agregación de redes móviles** | **Ligerísimo y barato** | Cobertura y **latencia variable** |
| **Redes de datos** (FTTH, dedicadas) | Barato donde hay red | Depende de la red de un tercero |

- **La tendencia que atraviesa las cinco**: **la señal viaja cada vez más sobre redes de datos y menos
  sobre circuitos dedicados.** **Abarata y complica a la vez**: la red ya existe, pero **una red
  compartida no garantiza por sí sola ni el ancho de banda ni el retardo**.

## Qué NO transmite

- **PREGUNTA 2, formulada en NEGATIVO** · **La que NO transmite es AVID COMMAND** —el cuadernillo
  escribe «Avid comand»—: **es un sistema de AUTOMATIZACIÓN DE EMISIÓN de informativos**: dispara la
  escaleta y controla los equipos del control.
- **Los otros tres SÍ transportan**: **FTTH** (fibra hasta el domicilio) · **mochila 4G** (agregación
  celular) · **DSNG** (periodismo electrónico digital por satélite).
- **Lo que distingue al primero: NO MUEVE señal de un sitio a otro, LA GOBIERNA.**
- **DECLARADO**: la documentación de **Avid sobre el iNEWS Command está cerrada** —**ocho rutas
  probadas con agente de navegador**, todas «prohibido» o «no encontrado»—. Lo que sostiene la
  respuesta es que **los otros tres sí son sistemas de transmisión**, y para una pregunta en negativo
  eso basta.

## El enlace por satélite

- `[oficio]` · **ASCENDENTE = *UPLINK*** → sube de la estación terrena al satélite, con parabólica de
  gran ganancia. **DESCENDENTE = *DOWNLINK*** → el satélite reemite hacia su zona de cobertura, **en
  una banda de frecuencias distinta**.
- **PREGUNTA 34** · **El enlace de subida es el *UPLINK*.** Falsas: ***downlink*** → **la mitad
  contraria** · **modulación en fase** → **una técnica de modulación, no un tramo** · **símplex** →
  **un modo de comunicación en un solo sentido**.
- **POR QUÉ BANDAS DISTINTAS**: si reemitiera en la misma frecuencia en que recibe, **se realimentaría
  a sí mismo**. El transpondedor **recibe en una banda, traslada y reemite en otra**.
- **Lo que la producción gestiona, y es lo que lo hace caro**: **reservar SEGMENTO ESPACIAL** —tiempo
  de transpondedor, contratado por horas— · coordinar la frecuencia · **licencia del país desde el que
  se sube** · **comprobar que el punto de recepción está dentro de la HUELLA**.
- `[UIT-R]` · El periodismo por satélite es **temporal y ocasional**, y **su activación a menudo no
  puede determinarse con gran antelación**; se hace con **estaciones terrenas de enlace ascendente
  portátiles o fácilmente transportables**. **Ésa es su razón de ser y también la de su precio.**

## Las mochilas de agregación

- `[oficio]` · **Suma varias conexiones de telefonía móvil para conseguir un canal estable.** **Pesa
  dos kilos, cuesta una fracción de un enlace y llega donde hay cobertura.**
- **Cómo funciona**: reparte el flujo entre **varias tarjetas de operadores distintos**, más red local
  e inalámbrica, y **el receptor del centro reordena los trozos y reconstruye la señal**. **Si una
  conexión cae, las demás la absorben.**
- **PREGUNTA 38** · `[LiveU]` · **Cuatro señales de alta resolución sincronizadas → LU800.** La ficha
  del fabricante, literal: «**Up to four high-res, fully frame-synced feeds from a single portable
  unit**», y se convierte en multicámara **con la licencia correspondiente**. Agrega **hasta 14
  conexiones** con **8 módems internos de doble tarjeta**, **hasta 60 Mbps**.
- **Las tres falsas**: **LU600** → modelo anterior de la familia, **de una sola señal** · **LU900** →
  **no corresponde a un modelo de esa gama** · «con ninguno, es imposible» → **la ficha lo desmiente**.
- **LA PIEZA QUE HACE POSIBLE LA RESPUESTA ES LA SINCRONIZACIÓN**: mandar cuatro señales es cuestión
  de ancho de banda; **mandarlas sincronizadas fotograma a fotograma es lo difícil**, porque cada una
  viaja por caminos distintos. **Sin esa sincronía un mezclador no puede conmutar entre ellas.**

## La producción remota

| | **Tradicional** | **REMOTA (MCRP)** |
|---|---|---|
| Dónde está el control | **En la unidad móvil, en el recinto** | **En el centro de producción** |
| Qué viaja | **El programa ya realizado** | **TODAS las señales de cámara**, y los retornos |
| Personal desplazado | Todo el equipo | **Sólo cámaras, sonido y técnicos de campo** |
| Coste de desplazamiento | Alto | **Mucho menor** |
| Exigencia de red | Un enlace | **Muchos, con MUY BAJA LATENCIA** |

- **PREGUNTA 41** · **Centraliza cámaras y facilita coordinar a los operadores desde un control
  remoto, PERO exige enlaces de fibra de baja latencia**, con dificultades donde la infraestructura no
  es adecuada o no existe.
- **Su acierto está en la SEGUNDA MITAD: el problema del MCRP es la RED.** Mover una señal realizada
  necesita un enlace; mover veinte **más retornos, intercomunicador y datos de control** necesita
  capacidad y, sobre todo, **latencia baja y ESTABLE**. Sin eso **el realizador corta con retardo y los
  cámaras reciben las órdenes tarde**.
- **Las tres falsas fallan cada una en un punto técnico**: a) grabación autónoma en cámara «reduce la
  necesidad de conectividad» → **es lo contrario: la señal viaja EN DIRECTO** · b) control «por ADSL» y
  congestión por el público → **el ADSL no da ni capacidad ni latencia**, y la red móvil del público
  **no afecta a un enlace dedicado** · d) «las cámaras remotas no pueden ajustarse en tiempo real» →
  **falso: el control de imagen las ajusta a distancia desde sus CCU, que es lo que HACE POSIBLE la
  producción remota**.
- **REGLA DE LECTURA, la misma de los temas 4 y 7**: **la correcta es la que reconoce a la vez LA
  VENTAJA Y EL LÍMITE REAL**; las falsas **afirman imposibilidades o culpan a la causa equivocada**.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 2 | Cuál NO es un sistema de transmisión de imágenes | a) Avid Command ✔ |
| 34 | Cómo se denomina el enlace de subida a satélite | b) *Uplink* ✔ |
| 38 | Modelo de LiveU para cuatro señales sincronizadas | c) LU 800 ✔ |
| 41 | Efecto del MCRP y sus dificultades técnicas | c) Centraliza cámaras, pero exige fibra de baja latencia ✔ |

**Las cuatro oficiales son correctas.** · **Errata de grafía**: «Avid comand» por **Avid Command**. No
afecta. · **Aviso**: **ninguna repite materia. Hay que estudiar el punto entero.**
