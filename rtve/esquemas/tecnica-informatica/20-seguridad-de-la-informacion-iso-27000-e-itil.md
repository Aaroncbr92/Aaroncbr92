# Esquema · Tema 20 del específico de Técnica Informática · Marcos de gestión de la seguridad y del servicio

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de gestión de servicios ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: la Organización Internacional de Normalización
(**ISO**) y su familia de seguridad de la información (**ISO 27000**); la biblioteca de
infraestructura de tecnologías de la información (**ITIL**), en sus versiones 3 y 4; el sistema de
gestión de la seguridad de la información (**SGSI**); el algoritmo de Rivest, Shamir y Adleman
(**RSA**); el algoritmo internacional de cifrado de datos (**IDEA**); el estándar de cifrado avanzado
(**AES**); y **Diffie-Hellman** y **ElGamal**, que son apellidos y no siglas.

**Cabecera.** Enunciado: punto 23 del anexo · **3 preguntas** · **ninguna lleva figura** · **el
desajuste que conviene señalar**: **el enunciado nombra dos marcos de gestión y una de las tres
preguntas es de criptografía**, que no figura en él con ese nombre.

<!-- indice -->

## Índice

- [La familia ISO 27000](#la-familia-iso-27000)
- [La biblioteca de gestión de servicios](#la-biblioteca-de-gestión-de-servicios)
- [El calendario de cambios](#el-calendario-de-cambios)
- [Criptografía](#criptografía)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La familia ISO 27000

| Norma | Qué es |
|---|---|
| **ISO/IEC 27000** | **El vocabulario y la visión de conjunto** |
| **ISO/IEC 27001** | **La norma certificable**: los requisitos del sistema de gestión |
| **ISO/IEC 27002** | **El código de buenas prácticas**: el catálogo de controles, que no se certifica |

- **LA DISTINCIÓN QUE SE PREGUNTA SIEMPRE**: **una organización se certifica en la 27001, no en la
  27002.** **La primera dice qué hay que tener; la segunda, cómo hacerlo.**

| Propiedad | Qué significa |
|---|---|
| **Confidencialidad** | **Que sólo acceda quien está autorizado** |
| **Integridad** | **Que no se altere sin autorización** |
| **Disponibilidad** | **Que esté accesible cuando se necesita** |

- **EL CICLO QUE LA NORMA IMPONE**: **planificar, hacer, verificar y actuar.** **Un sistema de gestión
  no es un estado: es un ciclo que se repite.**
- **LAS TRES PROPIEDADES REAPARECEN EN EL TEMA 23**, donde el Esquema Nacional de Seguridad añade dos.

## La biblioteca de gestión de servicios

- **QUÉ ES, CON PRECISIÓN**: **un conjunto de buenas prácticas para gestionar servicios de
  tecnologías de la información.** **No es certificable para la organización: se certifican las
  personas.**

| Fase de la versión 3 | Qué contiene, en lo que el examen pregunta |
|---|---|
| **Estrategia del servicio** | **Gestión financiera, de la demanda, de la cartera** |
| **Diseño del servicio** | **Catálogo, nivel de servicio, capacidad, disponibilidad, continuidad, seguridad, proveedores** |
| **Transición del servicio** | **Gestión del CAMBIO**, configuración, versiones, conocimiento |
| **Operación del servicio** | **INCIDENTES, PROBLEMAS, peticiones, ACCESOS, eventos** |
| **Mejora continua del servicio** | **El ciclo de medición y mejora** |

- **PREGUNTA 3** · `[exam]` · **El proceso que NO es de la Operación del Servicio es la gestión del
  cambio.**
- **LA TABLA LA CONTESTA SOLA**: **incidentes, problemas y accesos están en Operación; el cambio está
  en Transición.**

| Proceso | Qué atiende | Fase |
|---|---|---|
| **Gestión de incidentes** | **Restaurar el servicio cuanto antes.** No busca la causa | **Operación** |
| **Gestión de problemas** | **Encontrar y eliminar la causa** | **Operación** |
| **Gestión del cambio** | **Autorizar y coordinar las modificaciones del entorno** | **Transición** ✔ |

- **EL MATIZ QUE ORDENA LAS DOS PRIMERAS**: **un incidente se cierra cuando el servicio vuelve, aunque
  sea con un apaño; el problema, cuando la causa desaparece.** **Son distintos a propósito**: **el que
  atiende la urgencia no puede a la vez investigar despacio.**
- **POR QUÉ EL CAMBIO ESTÁ EN TRANSICIÓN**: **porque un cambio no es una avería.** **Es una
  modificación planificada**, y su fase es la que lleva un servicio del diseño a la producción.

## El calendario de cambios

- **PREGUNTA 85** · `[exam]` · **Su uso principal es planificar cambios y ayudar a evitar
  conflictos.**
- **LA PALABRA QUE DECIDE ES «PRINCIPAL»**, que el propio enunciado destaca: **las tres falsas
  describen usos reales o parciales.**

| Opción falsa | Por qué no es el uso principal |
|---|---|
| **Gestionar cambios de emergencia** | **Un cambio de emergencia es, por definición, el que NO estaba en el calendario** |
| **Respaldar incidentes y mejora** | **Uso derivado**: saber qué se cambió ayuda a diagnosticar, pero no es para lo que se hace |
| **Gestionar cambios estándar** | **Son los preautorizados y repetitivos**: los que menos calendario necesitan |

- **EL CONFLICTO QUE EVITA, CON UN EJEMPLO**: **dos equipos que actualizan el mismo día el servidor de
  aplicaciones y la base de datos que hay debajo.** **Cada cambio por separado está bien planificado;
  juntos dejan el servicio caído y nadie sabe cuál lo tumbó.**

| Tipo de cambio | Cómo se autoriza |
|---|---|
| **Estándar** | **Preautorizado**: procedimiento conocido, riesgo bajo |
| **Normal** | **Pasa por el comité de cambios** |
| **De emergencia** | **Autorización acelerada**, y se documenta después |

- **QUÉ CAMBIÓ EN LA VERSIÓN 4**: **desaparecen las cinco fases y entra un sistema de valor del
  servicio con siete principios rectores y treinta y cuatro prácticas.** **La gestión del cambio pasa
  a llamarse habilitación del cambio.** **La pregunta 3 cita expresamente la versión 3 y está bien
  acotada.**

## Criptografía

- **PREGUNTA 96** · `[exam]` · **El algoritmo simétrico es IDEA.**

| Familia | Cómo funciona | Ejemplos |
|---|---|---|
| **Simétrica** | **La misma clave cifra y descifra** | **IDEA** ✔, **AES**, **3DES**, **ChaCha20** |
| **Asimétrica** | **Par de claves: la pública cifra, la privada descifra** | **RSA**, **ElGamal**, curva elíptica |
| **Intercambio de claves** | **Acordar una clave por canal público sin transmitirla** | **Diffie-Hellman** |

- **LAS TRES FALSAS SON LAS TRES ASIMÉTRICAS DE MANUAL**: **tres de las cuatro son del mismo grupo**,
  que es la regla del tema 1.
- **EL MATIZ SOBRE DIFFIE-HELLMAN**: **no es exactamente cifrado: es intercambio de claves.** **Lo que
  después se cifra con esa clave se hace con un algoritmo simétrico.**
- **POR QUÉ EN LA PRÁCTICA VAN JUNTAS**: **la asimétrica es lenta y resuelve distribuir la clave; la
  simétrica es rápida y resuelve cifrar mucho volumen.** **Una conexión segura empieza con asimétrica
  y sigue con simétrica**, que es lo que hace el protocolo del tema 4.

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 3 | Proceso que NO es de la Operación del Servicio | b) Gestión del cambio ✔ |
| 85 | Uso principal del calendario de cambios | a) Planificar cambios y evitar conflictos ✔ |
| 96 | Algoritmo criptográfico simétrico | b) IDEA ✔ |

**Las tres oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**la tabla de fases y procesos contesta una pregunta entera y es la lista más preguntable.** **Y la
división simétrica/asimétrica cae en cualquier examen de informática**, aunque el enunciado no la
nombre.
