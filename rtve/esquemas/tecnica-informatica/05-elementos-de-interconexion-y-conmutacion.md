# Esquema · Tema 5 del específico de Técnica Informática · Elementos de interconexión y conmutación

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalación de redes ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: el par trenzado sin apantallar (**UTP**) y el
apantallado (**STP**); los gigabits por segundo (**Gbps**) y los megabits por segundo (**Mbps**); el
kilómetro (**km**); el control de acceso al medio (**MAC**); el protocolo de internet (**IP**); y las
designaciones de Ethernet sobre cobre (**10BASE-T**, **100BASE-TX**, **1000BASE-T**), que son nombres
de norma y no siglas.

**Cabecera.** Enunciado: punto 6 del anexo · **2 preguntas** · **ninguna lleva figura** · **el aviso
que cambia dónde apretar**: **el enunciado nombra conmutadores, enrutadores y puertas de enlace, y el
examen ha preguntado por el cable.** **Los tres equipos siguen sin caer y pueden caer.**

<!-- indice -->

## Índice

- [Qué medio para qué distancia](#qué-medio-para-qué-distancia)
- [Cuántos pares usa el cobre](#cuántos-pares-usa-el-cobre)
- [Los tres equipos que el enunciado pide](#los-tres-equipos-que-el-enunciado-pide)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué medio para qué distancia

- **PREGUNTA 6** · `[exam]` · **Dos edificios a 5 km, sin dispositivo electrónico intermedio, a
  1 Gbps: fibra óptica monomodo.**

| Medio | Alcance típico | Para qué |
|---|---|---|
| **Par trenzado, apantallado o no** | **100 metros** | **Dentro de un edificio** |
| **Fibra multimodo** | **Cientos de metros**, hasta unos 550 a un gigabit | **Entre plantas o edificios próximos** |
| **Fibra monomodo** | **Decenas de kilómetros** | **Enlaces largos** ✔ |

- **LAS DOS OPCIONES DE COBRE SE CAEN A LA PRIMERA**: **100 metros contra 5.000 no admite discusión.**
- **ENTRE LAS DOS FIBRAS DECIDE OTRA VEZ LA DISTANCIA**: **la multimodo no llega a cinco kilómetros a
  un gigabit.**
- **LA CONDICIÓN «SIN DISPOSITIVO INTERMEDIO» ESTÁ A PROPÓSITO**: **es la que impide resolverlo
  poniendo repetidores.** **Sin ella, el cobre se encadenaría cada cien metros.**

| | **Multimodo** | **Monomodo** |
|---|---|---|
| **Núcleo** | **Ancho**: 50 o 62,5 micras | **Estrecho**: unas 9 micras |
| **Cómo viaja la luz** | **Por muchos caminos**, que llegan con desfase | **Por uno solo** |
| **Qué la limita** | **La dispersión modal** | **La atenuación, mucho más tarde** |
| **Coste del equipo** | **Menor** | **Mayor** |

- **LA REGLA QUE RESUME EL EPÍGRAFE**: **la multimodo es más barata y llega menos; la monomodo es más
  cara y llega mucho más.** **La distancia manda.**

## Cuántos pares usa el cobre

- **PREGUNTA 42** · `[exam]` · **1000BASE-T con categoría 6 a 1000 Mbps en dúplex completo usa los
  cuatro pares para transmisión y recepción simultánea.**

| Variante | Velocidad | Cómo usa los pares |
|---|---|---|
| **10BASE-T** | **10 Mbps** | **Dos**: uno transmite, otro recibe |
| **100BASE-TX** | **100 Mbps** | **Dos**: uno transmite, otro recibe |
| **1000BASE-T** | **1000 Mbps** | **Los cuatro, a la vez, en los dos sentidos** ✔ |

- **CÓMO SE PUEDE TRANSMITIR Y RECIBIR POR EL MISMO PAR** · `[of]` · **cada extremo resta de lo que le
  llega lo que él mismo envía, y lo que queda es lo del otro.** **La misma idea que un manos libres
  cancelando el eco.**
- **EL AVISO PRÁCTICO**: **un cable con dos pares partidos funcionaba a cien megabits y no funciona a
  mil.** **Es la avería típica de la instalación vieja reaprovechada**: la red «va» hasta que alguien
  cambia una tarjeta por una de gigabit.

## Los tres equipos que el enunciado pide

| Equipo | Capa | Qué decide | Con qué dirección |
|---|---|---|---|
| **Concentrador** | **1, física** | **Nada: repite por todos los puertos** | **Ninguna** |
| **Conmutador** | **2, enlace** | **Por qué puerto sale la trama** | **La física** |
| **Enrutador** | **3, red** | **A qué red se manda el paquete** | **La IP** |
| **Puerta de enlace** | **La que haga falta** | **Traduce entre dos mundos distintos** | **La que corresponda** |

- **PUERTA DE ENLACE TIENE DOS SENTIDOS**: **en la configuración de un equipo es la dirección del
  enrutador por el que sale lo que no es de su red** —el uso corriente—; **en sentido estricto es el
  elemento que traduce entre dos protocolos o formatos** —una pasarela de correo, una de voz a
  telefonía—, **y ahí llega hasta la capa de aplicación.**
- **EL CONCENTRADOR, AUNQUE YA NO SE INSTALE**: **repetía cada bit por todos los puertos, con un solo
  dominio de colisión para todos.** **El conmutador lo sustituyó dando a cada puerto el suyo.**
- **NINGUNO DE LOS TRES HA CAÍDO.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 6 | Medio para 5 km a 1 Gbps sin equipo intermedio | b) Fibra óptica monomodo ✔ |
| 42 | Pares en 1000BASE-T a 1000 Mbps en dúplex completo | d) Cuatro, transmisión y recepción simultánea ✔ |

**Las dos oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**lo que cayó es medio físico y lo que el enunciado pide son equipos.** **Las dos tablas que hay que
llevar son alcance por medio y capa por equipo**: con ellas se contesta lo que cayó y lo que puede
caer.
