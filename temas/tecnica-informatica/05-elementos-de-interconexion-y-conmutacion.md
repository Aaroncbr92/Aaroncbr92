# Tema 5 del específico de Técnica Informática · Elementos de interconexión y conmutación

Las siglas de este tema, presentadas de entrada: el par trenzado sin apantallar (**UTP**, *unshielded
twisted pair*) y el apantallado (**STP**, *shielded twisted pair*); los gigabits por segundo
(**Gbps**) y los megabits por segundo (**Mbps**); el kilómetro (**km**); el control de acceso al medio
(**MAC**); el protocolo de internet (**IP**); y las designaciones de las variantes de Ethernet
sobre cobre (**10BASE-T**, **100BASE-TX** y **1000BASE-T**), que son nombres de norma y no siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 6):
> «Elementos de interconexión y conmutación. Conmutadores, enrutadores, puertas de enlace.»

**Dos preguntas.** **Y las dos son de medio físico, no de equipo**: **el enunciado nombra
conmutadores, enrutadores y puertas de enlace, y el examen ha preguntado por el cable.**

**Eso conviene decirlo porque cambia dónde apretar**: **lo preguntado ha sido qué medio elegir y
cuántos hilos usa**, **y lo enunciado —los tres equipos— sigue sin caer y puede caer.**

<!-- indice -->

## Índice

- [1. Qué medio para qué distancia](#1-qué-medio-para-qué-distancia)
- [2. Cuántos pares usa el cobre](#2-cuántos-pares-usa-el-cobre)
- [3. Los tres equipos que el enunciado nombra y el examen no ha preguntado](#3-los-tres-equipos-que-el-enunciado-nombra-y-el-examen-no-ha-preguntado)
- [4. Los datos que el examen ha preguntado](#4-los-datos-que-el-examen-ha-preguntado)
- [5. Trazabilidad](#5-trazabilidad)

<!-- /indice -->

## 1. Qué medio para qué distancia

**La pregunta 6 plantea un caso**: **interconectar dos edificios separados 5 km, sin ningún
dispositivo electrónico intermedio y con 1 Gbps de ancho de banda.** **La respuesta oficial es fibra
óptica monomodo.**

---

**El dato que decide es la distancia, y se resuelve con este cuadro:**

| Medio | Alcance típico | Para qué |
|---|---|---|
| **Par trenzado, apantallado o no** | **100 metros** | **Dentro de un edificio** |
| **Fibra multimodo** | **Cientos de metros**, hasta unos 550 a un gigabit | **Entre plantas o entre edificios próximos** |
| **Fibra monomodo** | **Decenas de kilómetros** | **Enlaces largos** ✔ |

**Con eso, las dos opciones de cobre se caen a la primera**: **100 metros contra 5.000 no admite
discusión.** **Y entre las dos fibras decide otra vez la distancia**: **la multimodo no llega a cinco
kilómetros a un gigabit.**

**La condición «sin ningún dispositivo electrónico intermedio» está en el enunciado a propósito**:
**es la que impide resolverlo poniendo repetidores.** **Sin ella, el cobre podría encadenarse cada
cien metros.**

**Y la diferencia física entre las dos fibras, que es lo que hay detrás del cuadro:**

| | **Multimodo** | **Monomodo** |
|---|---|---|
| **Núcleo** | **Ancho**: 50 o 62,5 micras | **Estrecho**: unas 9 micras |
| **Cómo viaja la luz** | **Por muchos caminos a la vez**, que llegan con desfase | **Por un solo camino** |
| **Qué la limita** | **La dispersión modal**: los caminos se separan con la distancia | **La atenuación, mucho más tarde** |
| **Coste del equipo** | **Menor** | **Mayor** |

**La regla que resume el epígrafe**: **la multimodo es más barata y llega menos; la monomodo es más
cara y llega mucho más.** **La distancia manda.**

## 2. Cuántos pares usa el cobre

**La pregunta 42**: **en 1000BASE-T con cableado de categoría 6 a 1000 Mbps en dúplex completo se
utilizan cuatro pares para transmisión y recepción simultánea.** Ésa es la respuesta oficial.

---

**Y ahí está la ruptura con las generaciones anteriores**, que es lo que la pregunta mide:

| Variante | Velocidad | Cómo usa los cuatro pares |
|---|---|---|
| **10BASE-T** | **10 Mbps** | **Dos pares**: uno transmite y otro recibe |
| **100BASE-TX** | **100 Mbps** | **Dos pares**: uno transmite y otro recibe |
| **1000BASE-T** | **1000 Mbps** | **Los cuatro, a la vez, en los dos sentidos** ✔ |

**Cómo es posible transmitir y recibir por el mismo par a la vez**: **cada extremo resta de lo que le
llega lo que él mismo está enviando**, y **lo que queda es lo que envió el otro.** **Es la misma idea
que un teléfono manos libres cancelando el eco**, y en el sector se llama cancelación de eco híbrida.

**El aviso práctico que se deriva**: **un cable con dos pares partidos funcionaba a cien megabits y no
funciona a mil.** **Es la avería típica de una instalación vieja reaprovechada**: la red «va» hasta
que alguien cambia una tarjeta por una de gigabit.

## 3. Los tres equipos que el enunciado nombra y el examen no ha preguntado

| Equipo | En qué capa trabaja | Qué decide | Con qué dirección |
|---|---|---|---|
| **Concentrador** | **1, física** | **Nada: repite por todos los puertos** | **Ninguna** |
| **Conmutador** | **2, enlace** | **Por qué puerto sale la trama** | **La dirección física** |
| **Enrutador** | **3, red** | **A qué red se manda el paquete** | **La dirección IP** |
| **Puerta de enlace** | **La que haga falta** | **Traduce entre dos mundos distintos** | **La que corresponda** |

**Qué es exactamente una puerta de enlace, porque el término se usa con dos sentidos:**

1. **En la configuración de un equipo, la puerta de enlace predeterminada es la dirección del
   enrutador** por el que sale lo que no es de su red. **Ése es el uso corriente.**
2. **En su sentido estricto, una puerta de enlace es el elemento que traduce entre dos protocolos o
   dos formatos distintos** —una pasarela de correo, una de voz sobre red a telefonía—, **y ahí puede
   trabajar hasta en la capa de aplicación.**

**Y el concentrador merece una línea aunque ya no se instale**: **repetía cada bit por todos los
puertos**, de modo que **todos los equipos compartían un solo dominio de colisión.** **El conmutador
lo sustituyó dándole a cada puerto el suyo**, que es lo que el tema 3 explica al hilo de la
pregunta 43.

## 4. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 6 | Medio para 5 km a 1 Gbps sin equipo intermedio | b) Fibra óptica monomodo ✔ |
| 42 | Pares de cobre en 1000BASE-T a 1000 Mbps en dúplex completo | d) Cuatro para transmisión y recepción simultánea ✔ |

**Las dos respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **las dos preguntas caídas son de medio físico y el enunciado pide equipos.**
**Lo que hay que llevar aprendido son las dos tablas: alcance por medio y capa por equipo.** **Con
ellas se contesta lo que cayó y lo que puede caer.**

## 5. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Tres declaraciones expresas:**

1. **La familia de normas IEEE 802.3, que define 10BASE-T, 100BASE-TX y 1000BASE-T, no se ha
   consultado.** **El número de pares que usa cada variante y su velocidad son de uso universal**, y
   **coinciden con la respuesta oficial de la pregunta 42.**
2. **Los alcances del cuadro del epígrafe 1 son órdenes de magnitud del uso corriente** —cien metros
   para el par trenzado, cientos de metros para la fibra multimodo, decenas de kilómetros para la
   monomodo—. **Ninguna norma se ha consultado para ellos**, y **la respuesta oficial de la pregunta 6
   se decide por una diferencia de dos órdenes de magnitud**, no por una cifra ajustada.
3. **Los diámetros de núcleo del cuadro de fibras —50 o 62,5 micras y unas 9 micras— son los valores
   corrientes del catálogo del sector**, dados como referencia. **Ninguna pregunta depende de ellos.**

**El resto del tema va como oficio y así se declara**: la explicación de por qué la condición «sin
dispositivo intermedio» está en el enunciado, la cancelación de eco que permite usar los cuatro pares
en los dos sentidos, la avería típica del cable con pares partidos, el cuadro de equipos por capa y
los dos sentidos del término «puerta de enlace». **Nada de eso está en un boletín oficial ni en una
norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
