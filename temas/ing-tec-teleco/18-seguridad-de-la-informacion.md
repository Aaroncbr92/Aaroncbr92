# Tema 18 del específico de Ingeniería Técnica · Telecomunicación · Seguridad de la información

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 22 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son la familia ISO/IEC 27000 y la biblioteca de gestión de servicios, **tras muro de pago**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Punto compartido** | **Este mismo punto es el 23 del anexo de Técnica Informática, donde SÍ dio tres preguntas.** Aquí se escribe desde la mirada del ingeniero de instalaciones: **lo que hay que proteger no es una oficina, es una emisión** |
| **Extensión** | **1.700 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la Organización Internacional de Normalización
(**ISO**) y la Comisión Electrotécnica Internacional (**IEC**), que publican juntas la familia
**ISO/IEC 27000** y su norma certificable **ISO/IEC 27001**; la biblioteca de infraestructura de
tecnologías de la información (**ITIL**), en sus versiones 3 y 4; el sistema de gestión de la
seguridad de la información (**SGSI**); la zona desmilitarizada o red perimetral (**DMZ**); la red
privada virtual (**VPN**); y el Esquema Nacional de Seguridad (**ENS**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 22):
> «Seguridad en tecnologías de la información. Normativa ISO/IEC 27001. Biblioteca de Infraestructura
> de Tecnologías de Información (ITIL versiones 3 y 4).»

**Cero preguntas.** **Este punto del anexo no ha dado ni una en el cuadernillo**, y **el tema se
escribe igual, contra el programa.**

**Y hay una razón para no despacharlo**: **este mismo punto es el 23 del anexo de Técnica Informática,
donde SÍ ha dado tres preguntas.** **La materia está desarrollada y verificada allí**, y **aquí se
escribe desde la mirada del ingeniero de instalaciones**, que es distinta: **lo que aquí hay que
proteger no es una oficina, es una emisión.**

<!-- indice -->

## Índice

- [1. Las propiedades que se protegen](#1-las-propiedades-que-se-protegen)
- [2. La norma certificable](#2-la-norma-certificable)
- [3. La biblioteca de gestión de servicios](#3-la-biblioteca-de-gestión-de-servicios)
- [4. Lo propio de una instalación audiovisual](#4-lo-propio-de-una-instalación-audiovisual)
- [5. Lo que el examen ha preguntado](#5-lo-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Las propiedades que se protegen

| Propiedad | Qué significa |
|---|---|
| **Confidencialidad** | **Que sólo acceda quien está autorizado** |
| **Integridad** | **Que no se altere sin autorización** |
| **Disponibilidad** | **Que esté accesible cuando se necesita** |

**Y las dos que el Esquema Nacional de Seguridad añade**, porque **una corporación pública está sujeta
a él**: **trazabilidad** —saber quién hizo qué y cuándo— y **autenticidad** —que una entidad sea quien
dice ser—.

**La observación que ordena el punto para esta ocupación**: **en una instalación de emisión, la
propiedad crítica es la DISPONIBILIDAD.** **Un incidente que revele información es grave; uno que deje
el canal en negro se ve en toda España.** **Ése es el orden de prioridades que un ingeniero de
instalaciones tiene que tener claro y que un informático de gestión suele tener al revés.**

## 2. La norma certificable

**Las tres normas de la familia que hay que saber distinguir:**

| Norma | Qué es |
|---|---|
| **ISO/IEC 27000** | **El vocabulario y la visión de conjunto** |
| **ISO/IEC 27001** | **La norma CERTIFICABLE**: los requisitos de un sistema de gestión ✔ |
| **ISO/IEC 27002** | **El código de buenas prácticas**: el catálogo de controles, que no se certifica |

**La distinción que se pregunta siempre**: **una organización se certifica en la primera de las dos
últimas, no en la segunda.** **Una dice QUÉ hay que tener; la otra, CÓMO hacerlo.**

**Qué es un sistema de gestión de la seguridad de la información, en una línea**: **un conjunto de
políticas, procedimientos y controles que se planifica, se aplica, se mide y se mejora**, siguiendo el
ciclo de **planificar, hacer, verificar y actuar.**

**Y la idea que lo hace útil y que un examen puede pedir**: **la seguridad se gestiona por RIESGOS, no
por lista de la compra.** **Se identifican los activos, se valoran las amenazas, se decide qué riesgo
se acepta y qué riesgo se trata**, y **los controles se eligen en función de eso.** **Comprar
cortafuegos sin haber hecho ese análisis es gastar sin saber en qué.**

**Las cuatro maneras de tratar un riesgo, que es la lista más preguntable de la norma:**

| Tratamiento | Qué se hace |
|---|---|
| **Mitigar** | **Poner controles que lo reduzcan** |
| **Transferir** | **Pasarlo a otro: un seguro, un proveedor** |
| **Evitar** | **Dejar de hacer lo que lo produce** |
| **Aceptar** | **Asumirlo, por escrito y con quien tenga autoridad para hacerlo** |

**La cuarta es la que más se olvida y la única que exige firma**: **aceptar un riesgo es una decisión
de dirección, no del técnico que lo detectó.**

## 3. La biblioteca de gestión de servicios

**Qué es, dicho con precisión**: **un conjunto de buenas prácticas para gestionar servicios de
tecnologías de la información.** **No es una norma certificable para la organización**: **se certifican
las personas.**

**Su versión 3 organiza el trabajo en cinco fases del ciclo de vida del servicio:**

| Fase | Qué contiene |
|---|---|
| **Estrategia del servicio** | **Gestión financiera, de la demanda y de la cartera** |
| **Diseño del servicio** | **Catálogo, nivel de servicio, capacidad, disponibilidad, continuidad, seguridad, proveedores** |
| **Transición del servicio** | **Gestión del CAMBIO, de la configuración, de versiones y del conocimiento** |
| **Operación del servicio** | **Incidentes, problemas, peticiones, accesos y eventos** |
| **Mejora continua** | **El ciclo de medición y mejora** |

**Las tres distinciones que un examen pide siempre de esta materia:**

| Proceso | Qué atiende | En qué fase |
|---|---|---|
| **Gestión de incidentes** | **Restaurar el servicio cuanto antes.** No busca la causa | **Operación** |
| **Gestión de problemas** | **Encontrar y eliminar la causa de los incidentes** | **Operación** |
| **Gestión del cambio** | **Autorizar y coordinar las modificaciones del entorno** | **Transición** |

**El matiz que ordena las dos primeras**: **un incidente se cierra cuando el servicio vuelve, aunque
sea con un apaño; el problema se cierra cuando la causa desaparece.** **Son procesos distintos a
propósito**, porque **el que atiende la urgencia no puede a la vez investigar despacio.**

**Y qué cambió en la versión 4, que el enunciado también nombra**: **desaparece la estructura de cinco
fases y entra un sistema de valor del servicio con siete principios rectores y treinta y cuatro
prácticas.** **La gestión del cambio pasa a llamarse habilitación del cambio**, con el acento puesto en
no estorbar.

## 4. Lo propio de una instalación audiovisual

**Aquí está lo que este tema aporta y que el de Técnica Informática no tiene que decir**: **cómo se
aplica todo lo anterior a una casa que emite.**

**Las tres redes que conviven, y por qué se separan:**

| Red | Qué lleva | Exposición |
|---|---|---|
| **De señal** | **Vídeo y audio en tiempo real** | **Cerrada: no toca internet nunca** |
| **De producción y control** | **Ficheros, configuración de equipos, automatización** | **Cerrada, con salidas controladas** |
| **Ofimática** | **Correo, navegación, gestión** | **Expuesta** |

**La regla de diseño**: **el tráfico va de la expuesta hacia las cerradas sólo a través de puntos
controlados**, y **nunca al revés sin control.** **Es la zona perimetral aplicada a una televisión.**

**Los cuatro riesgos propios de esta clase de instalación, que un examen de esta ocupación podría
pedir y que ninguno de gestión pediría:**

| Riesgo | Por qué es propio |
|---|---|
| **Un equipo audiovisual sin actualizar** | **Un mezclador o un servidor de vídeo tiene sistema operativo y NO se parchea como un ordenador**: parar la emisión para actualizar no es una opción trivial |
| **Contraseñas por defecto en equipos de instalación** | **Muchos equipos audiovisuales salen de fábrica con credenciales conocidas y se instalan sin cambiarlas** |
| **Acceso remoto del fabricante** | **El soporte del suministrador suele pedir acceso permanente**: es una puerta que hay que controlar y auditar |
| **La automatización de emisión** | **Es el sistema con más capacidad de daño y el que menos se protege**: quien lo controle controla lo que sale en antena |

**Y la tensión que define este punto para un ingeniero de instalaciones**: **la política de seguridad
corporativa está escrita para ordenadores de oficina**, y **aplicarla literalmente a un equipo de
emisión puede tumbar el canal.** **Lo que se pide no es saltársela: es escribir la excepción, con su
análisis de riesgo, sus controles compensatorios y la firma de quien acepta lo que queda.**

**La continuidad de negocio, que es donde las dos materias se juntan**: **el plan de continuidad de una
televisión tiene que contemplar el caso en que los sistemas informáticos caigan y haya que emitir
igual.** **Una cadena de emisión manual, con material en soporte y sin automatización, es la última
línea de defensa**, y **es la que nadie ensaya.**

## 5. Lo que el examen ha preguntado

**Ninguna pregunta.**

**El aviso de estudio**: **la materia está desarrollada en el tema 20 del específico de Técnica
Informática, donde sí ha caído.** **Lo razonablemente preguntable aquí son las tres normas de la
familia y cuál se certifica, la tabla de fases de la biblioteca de gestión y la distinción entre
incidente, problema y cambio.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **no tiene ninguna respuesta oficial que
sostener**, porque el punto no ha dado preguntas.

**Cuatro declaraciones expresas:**

1. **Las normas de la familia ISO/IEC 27000 no se han consultado**: su texto está tras un muro de
   pago. **La distinción entre la certificable y la de buenas prácticas y el ciclo de mejora son de
   uso universal**, y **se presentan como conocimiento común de la materia.**
2. **La biblioteca de gestión de servicios tampoco se ha consultado.** **Su estructura de cinco fases
   y el reparto de procesos son de uso universal**, y **están verificados contra respuesta oficial en
   el tema 20 del específico de Técnica Informática**, escrito en este mismo proyecto.
3. **El Esquema Nacional de Seguridad se menciona sin citarlo literalmente.** **Está desarrollado, con
   cita literal del Real Decreto 311/2022, en el tema 23 del específico de Técnica Informática.**
4. **Los cuatro riesgos del epígrafe 4 son oficio de instalaciones audiovisuales**, escritos como
   guía de estudio. **No describen la instalación ni la política de seguridad de ninguna casa
   concreta**, que no se han consultado.

**El resto del tema va como oficio y así se declara**: la observación de que en emisión la propiedad
crítica es la disponibilidad, la idea de gestionar por riesgos y no por lista, la advertencia de que
aceptar un riesgo exige firma, la separación de las tres redes, los cuatro riesgos propios y la
reflexión sobre la cadena de emisión manual como última línea de defensa. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
