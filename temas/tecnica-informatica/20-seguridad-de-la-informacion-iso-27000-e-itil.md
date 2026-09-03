# Tema 20 del específico de Técnica Informática · Marcos de gestión de la seguridad y del servicio

Las siglas de este tema, presentadas de entrada: la Organización Internacional de Normalización
(**ISO**) y su familia de normas de seguridad de la información (**ISO 27000**); la biblioteca de
infraestructura de tecnologías de la información (**ITIL**, *information technology infrastructure
library*), en sus versiones 3 y 4; el sistema de gestión de la seguridad de la información (**SGSI**);
el algoritmo de Rivest, Shamir y Adleman (**RSA**); el algoritmo internacional de cifrado de datos
(**IDEA**, *international data encryption algorithm*); el estándar de cifrado avanzado (**AES**,
*advanced encryption standard*); y **Diffie-Hellman** y **ElGamal**, que son apellidos y no siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 23):
> «Seguridad en tecnologías de la información. Normativas ISO 27000. Biblioteca de Infraestructura de
> Tecnologías de Información (ITIL versiones 3 y 4).»

**Tres preguntas.** **Y hay un desajuste entre el enunciado y lo preguntado que conviene señalar**:
**el enunciado nombra dos marcos de gestión y una de las tres preguntas es de criptografía**, que no
figura en él con ese nombre.

**Su reparto**: **dos preguntas son de la biblioteca de gestión de servicios** y **una es de
algoritmos de cifrado.**

<!-- indice -->

## Índice

- [1. La familia ISO 27000](#1-la-familia-iso-27000)
- [2. La biblioteca de gestión de servicios](#2-la-biblioteca-de-gestión-de-servicios)
- [3. El calendario de cambios](#3-el-calendario-de-cambios)
- [4. La criptografía](#4-la-criptografía)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. La familia ISO 27000

**Qué es, en una línea**: **el conjunto de normas internacionales sobre gestión de la seguridad de la
información.**

**Las tres que hay que saber distinguir:**

| Norma | Qué es |
|---|---|
| **ISO/IEC 27000** | **El vocabulario y la visión de conjunto de la familia** |
| **ISO/IEC 27001** | **La norma certificable**: los requisitos de un sistema de gestión de la seguridad de la información |
| **ISO/IEC 27002** | **El código de buenas prácticas**: el catálogo de controles, que no se certifica |

**La distinción que se pregunta siempre**: **una organización se certifica en la 27001, no en la
27002.** **La primera dice qué hay que tener; la segunda, cómo hacerlo.**

**Y las tres propiedades que la familia protege**, que son la base de todo lo demás y reaparecen en el
tema 23:

| Propiedad | Qué significa |
|---|---|
| **Confidencialidad** | **Que sólo acceda quien está autorizado** |
| **Integridad** | **Que no se altere sin autorización** |
| **Disponibilidad** | **Que esté accesible cuando se necesita** |

**El ciclo de mejora continua que la norma impone**: **planificar, hacer, verificar y actuar.** **Un
sistema de gestión no es un estado: es un ciclo que se repite.**

## 2. La biblioteca de gestión de servicios

**Qué es ITIL, dicho con precisión**: **un conjunto de buenas prácticas para gestionar servicios de
tecnologías de la información.** **No es una norma certificable para la organización**: **se certifican
las personas.**

**La estructura de la versión 3, que es la que la pregunta 3 usa**: **cinco fases del ciclo de vida
del servicio**, y **dentro de cada una, sus procesos:**

| Fase | Qué contiene, en lo que el examen pregunta |
|---|---|
| **Estrategia del servicio** | **Gestión financiera, de la demanda, de la cartera** |
| **Diseño del servicio** | **Gestión del catálogo, del nivel de servicio, de la capacidad, de la disponibilidad, de la continuidad, de la seguridad, de proveedores** |
| **Transición del servicio** | **Gestión del CAMBIO**, de la configuración, de versiones, del conocimiento |
| **Operación del servicio** | **Gestión de INCIDENTES, de PROBLEMAS, de peticiones, de ACCESOS, y de eventos** |
| **Mejora continua del servicio** | **El ciclo de medición y mejora** |

**La pregunta 3 es negativa**: **de los procesos de ITIL v3 enumerados, el que NO forma parte de la
Operación del Servicio es la gestión del cambio.** Ésa es la respuesta oficial.

---

**Y la tabla la contesta sola**: **incidentes, problemas y accesos están en Operación; el cambio está
en Transición.**

**La distinción que hay detrás y que conviene entender, porque explica por qué está en otra fase:**

| Proceso | Qué atiende | En qué fase |
|---|---|---|
| **Gestión de incidentes** | **Restaurar el servicio cuanto antes.** No busca la causa | **Operación** |
| **Gestión de problemas** | **Encontrar y eliminar la causa de los incidentes** | **Operación** |
| **Gestión del cambio** | **Autorizar y coordinar las modificaciones del entorno** | **Transición** ✔ |

**El matiz que ordena las dos primeras**: **un incidente se cierra cuando el servicio vuelve, aunque
sea con un apaño**; **el problema se cierra cuando la causa desaparece.** **Son procesos distintos a
propósito**, porque **el que atiende la urgencia no puede a la vez investigar despacio.**

**Y por qué el cambio está en Transición y no en Operación**: **porque un cambio no es una avería.**
**Es una modificación planificada del entorno**, y su fase es la que lleva un servicio del diseño a la
producción.

## 3. El calendario de cambios

**La pregunta 85**: **en la metodología ITIL, el uso principal de un calendario de cambios es
planificar cambios y ayudar a evitar conflictos.** Ésa es la respuesta oficial.

---

**La palabra que decide es «PRINCIPAL»**, que el propio enunciado destaca. **Las tres opciones falsas
describen usos reales o parciales del calendario**, y por eso la pregunta es fina:

| Opción | Por qué no es el uso principal |
|---|---|
| **b) Gestionar cambios de emergencia** | **Un cambio de emergencia es, por definición, el que NO estaba en el calendario** |
| **c) Respaldar la gestión de incidentes y la planificación de la mejora** | **Es un uso derivado**: saber qué se cambió ayuda a diagnosticar, pero no es para lo que se hace |
| **d) Gestionar cambios estándar** | **Los cambios estándar son los preautorizados y repetitivos.** **Son precisamente los que menos necesitan calendario** |

**Y el conflicto que el calendario evita, dicho con un ejemplo**: **dos equipos que actualizan el
mismo día el servidor de aplicaciones y la base de datos que hay debajo.** **Cada cambio, por
separado, está bien planificado; juntos, dejan el servicio caído y nadie sabe cuál de los dos lo
tumbó.**

**Los tres tipos de cambio de la biblioteca, porque las opciones los nombran:**

| Tipo | Cómo se autoriza |
|---|---|
| **Estándar** | **Preautorizado**: procedimiento conocido y riesgo bajo |
| **Normal** | **Pasa por el comité de cambios** |
| **De emergencia** | **Autorización acelerada**, y se documenta después |

**Y qué cambió con la versión 4, que el enunciado también nombra**: **desaparece la estructura de
cinco fases y se sustituye por un sistema de valor del servicio con siete principios rectores y
treinta y cuatro prácticas.** **La gestión del cambio pasa a llamarse habilitación del cambio**, con
el acento puesto en no estorbar. **La pregunta 3, al citar expresamente la versión 3, está bien
acotada.**

## 4. La criptografía

**La pregunta 96**: **de los enumerados, el algoritmo criptográfico simétrico es IDEA.** Ésa es la
respuesta oficial.

---

**La división que la contesta:**

| Familia | Cómo funciona | Ejemplos |
|---|---|---|
| **Simétrica** | **La misma clave cifra y descifra** | **IDEA** ✔, **AES**, **3DES**, **ChaCha20** |
| **Asimétrica** | **Un par de claves: la pública cifra, la privada descifra** | **RSA**, **ElGamal**, curva elíptica |
| **Intercambio de claves** | **Acordar una clave por un canal público sin transmitirla** | **Diffie-Hellman** |

**Y las tres opciones falsas son las tres asimétricas de manual**: **RSA, Diffie-Hellman y ElGamal.**
**La pregunta se contesta reconociendo que tres de las cuatro pertenecen al mismo grupo**, que es la
misma regla del tema 1.

**El matiz sobre Diffie-Hellman, porque es el que se escapa**: **no es exactamente un algoritmo de
cifrado.** **Es un método de intercambio de claves**: **permite que dos partes acuerden una clave
secreta hablando por un canal público.** **Lo que después se cifra con esa clave se hace con un
algoritmo simétrico.**

**Y por qué en la práctica se usan las dos familias juntas**: **la asimétrica es lenta y resuelve el
problema de distribuir la clave**; **la simétrica es rápida y resuelve el de cifrar mucho volumen.**
**Una conexión segura empieza con criptografía asimétrica para acordar una clave y sigue con simétrica
para el resto de la sesión.** **Es exactamente lo que hace el protocolo del tema 4.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 3 | Proceso de ITIL v3 que NO es de la Operación del Servicio | b) Gestión del cambio ✔ |
| 85 | Uso principal de un calendario de cambios | a) Planificar cambios y evitar conflictos ✔ |
| 96 | Cuál es un algoritmo criptográfico simétrico | b) IDEA ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la tabla de fases y procesos de la versión 3 contesta una pregunta entera y
es la lista más preguntable del punto.** **Y la división entre criptografía simétrica y asimétrica es
de las que caen en cualquier examen de informática**, aunque el enunciado de este punto no la nombre.

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **Las normas de la familia ISO/IEC 27000 no se han consultado**: su texto está tras un muro de
   pago. **La distinción entre la 27001 certificable y la 27002 de buenas prácticas, y las tres
   propiedades de la seguridad de la información, son de uso universal**, y **ninguna pregunta de este
   punto depende de ellas.**
2. **La biblioteca ITIL tampoco se ha consultado.** **La estructura de cinco fases de su versión 3 y
   el reparto de procesos entre ellas son de uso universal**, y **coinciden con la respuesta oficial
   de la pregunta 3.**
3. **Lo que el tema dice de la versión 4 —el sistema de valor del servicio, los siete principios
   rectores y las treinta y cuatro prácticas, y el cambio de nombre de la gestión del cambio— es de
   uso corriente en el sector.** **Ninguna pregunta depende de ello**, y la 3 acota expresamente la
   versión 3.
4. **La clasificación de algoritmos criptográficos en simétricos, asimétricos y de intercambio de
   claves es teoría clásica**, presentada como conocimiento común, **y coincide con la respuesta
   oficial de la pregunta 96.**
5. **Los nombres RSA, IDEA, AES, 3DES, ChaCha20, Diffie-Hellman y ElGamal se citan por su familia.**
   **No se ha consultado la especificación de ninguno**, y **el temario no les atribuye ninguna
   característica más allá de su clasificación.**

**El resto del tema va como oficio y así se declara**: la distinción entre gestión de incidentes y de
problemas, el argumento de por qué el cambio está en Transición, el ejemplo del conflicto de
calendario, la precisión sobre Diffie-Hellman y la explicación de por qué las dos familias
criptográficas se usan juntas. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
