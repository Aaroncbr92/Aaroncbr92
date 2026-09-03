# Esquema · Tema 18 del específico de Ingeniería Técnica · Telecomunicación · Seguridad de la información

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalaciones y de sistemas ·
`[norma]` = norma nombrada, sin cita literal. **Siglas**: la Organización Internacional de
Normalización (**ISO**) y la Comisión Electrotécnica Internacional (**IEC**), que publican la familia
**ISO/IEC 27000** y su norma certificable **ISO/IEC 27001**; la biblioteca de infraestructura de
tecnologías de la información (**ITIL**), en sus versiones 3 y 4; el sistema de gestión de la
seguridad de la información (**SGSI**); la zona desmilitarizada o red perimetral (**DMZ**); la red
privada virtual (**VPN**); y el Esquema Nacional de Seguridad (**ENS**).

**Cabecera.** Enunciado: punto 22 del anexo · **cero preguntas** · **pero este mismo punto es el 23 del
anexo de Técnica Informática, donde SÍ dio tres** · **aquí se escribe desde la mirada del ingeniero de
instalaciones**: **lo que hay que proteger no es una oficina, es una emisión.**

<!-- indice -->

## Índice

- [Las propiedades que se protegen](#las-propiedades-que-se-protegen)
- [La norma certificable](#la-norma-certificable)
- [La biblioteca de gestión de servicios](#la-biblioteca-de-gestión-de-servicios)
- [Lo propio de una instalación audiovisual](#lo-propio-de-una-instalación-audiovisual)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las propiedades que se protegen

| Propiedad | Qué significa |
|---|---|
| **Confidencialidad** | **Que sólo acceda quien está autorizado** |
| **Integridad** | **Que no se altere sin autorización** |
| **Disponibilidad** | **Que esté accesible cuando se necesita** |

- **LAS DOS QUE AÑADE EL ESQUEMA NACIONAL DE SEGURIDAD** · `[norma]` · **Trazabilidad** —saber quién
  hizo qué y cuándo— y **autenticidad** —que una entidad sea quien dice ser—. **Una corporación pública
  está sujeta a él.**
- **LA OBSERVACIÓN QUE ORDENA EL PUNTO PARA ESTA OCUPACIÓN** · `[of]` · **En una instalación de emisión
  la propiedad crítica es la DISPONIBILIDAD.** **Un incidente que revele información es grave; uno que
  deje el canal en negro se ve en toda España.** **Es el orden de prioridades que un informático de
  gestión suele tener al revés.**

## La norma certificable

| Norma · `[norma]` | Qué es |
|---|---|
| **ISO/IEC 27000** | **El vocabulario y la visión de conjunto** |
| **ISO/IEC 27001** | **La norma CERTIFICABLE: los requisitos de un sistema de gestión** ✔ |
| **ISO/IEC 27002** | **El código de buenas prácticas: el catálogo de controles, que no se certifica** |

- **LA DISTINCIÓN QUE SE PREGUNTA SIEMPRE** · `[of]` · **Una organización se certifica en la
  certificable, no en la de buenas prácticas.** **Una dice QUÉ hay que tener; la otra, CÓMO hacerlo.**
- **QUÉ ES UN SISTEMA DE GESTIÓN** · `[of]` · **Políticas, procedimientos y controles que se planifican,
  se aplican, se miden y se mejoran**, siguiendo el ciclo de **planificar, hacer, verificar y actuar.**
- **LA IDEA QUE LO HACE ÚTIL** · `[of]` · **La seguridad se gestiona por RIESGOS, no por lista de la
  compra.** **Comprar cortafuegos sin análisis previo es gastar sin saber en qué.**

| Tratamiento del riesgo | Qué se hace |
|---|---|
| **Mitigar** | **Poner controles que lo reduzcan** |
| **Transferir** | **Pasarlo a otro: un seguro, un proveedor** |
| **Evitar** | **Dejar de hacer lo que lo produce** |
| **Aceptar** | **Asumirlo, por escrito y con quien tenga autoridad** |

- **LA CUARTA ES LA QUE MÁS SE OLVIDA Y LA ÚNICA QUE EXIGE FIRMA** · `[of]` · **Aceptar un riesgo es
  decisión de dirección, no del técnico que lo detectó.**

## La biblioteca de gestión de servicios

- **QUÉ ES, CON PRECISIÓN** · `[of]` · **Buenas prácticas para gestionar servicios de tecnologías de la
  información.** **No es certificable para la organización: se certifican las PERSONAS.**

| Fase de la versión 3 | Qué contiene |
|---|---|
| **Estrategia del servicio** | **Gestión financiera, de la demanda y de la cartera** |
| **Diseño del servicio** | **Catálogo, nivel de servicio, capacidad, disponibilidad, continuidad, seguridad, proveedores** |
| **Transición del servicio** | **Gestión del CAMBIO, de la configuración, de versiones y del conocimiento** |
| **Operación del servicio** | **Incidentes, problemas, peticiones, accesos y eventos** |
| **Mejora continua** | **El ciclo de medición y mejora** |

| Proceso | Qué atiende | Fase |
|---|---|---|
| **Gestión de incidentes** | **Restaurar el servicio cuanto antes.** No busca la causa | **Operación** |
| **Gestión de problemas** | **Encontrar y eliminar la causa** | **Operación** |
| **Gestión del cambio** | **Autorizar y coordinar las modificaciones** | **Transición** |

- **EL MATIZ QUE ORDENA LAS DOS PRIMERAS** · `[of]` · **Un incidente se cierra cuando el servicio
  vuelve, aunque sea con un apaño; el problema se cierra cuando la causa desaparece.** **Son procesos
  distintos a propósito**, porque **el que atiende la urgencia no puede a la vez investigar despacio.**
- **QUÉ CAMBIÓ EN LA VERSIÓN 4** · `[of]` · **Desaparece la estructura de cinco fases** y entra **un
  sistema de valor del servicio con siete principios rectores y treinta y cuatro prácticas.** **La
  gestión del cambio pasa a llamarse habilitación del cambio**, con el acento en no estorbar.

## Lo propio de una instalación audiovisual

| Red | Qué lleva | Exposición |
|---|---|---|
| **De señal** | **Vídeo y audio en tiempo real** | **Cerrada: no toca internet nunca** |
| **De producción y control** | **Ficheros, configuración, automatización** | **Cerrada, con salidas controladas** |
| **Ofimática** | **Correo, navegación, gestión** | **Expuesta** |

- **LA REGLA DE DISEÑO** · `[of]` · **El tráfico va de la expuesta hacia las cerradas sólo por puntos
  controlados, y nunca al revés sin control.** **Es la zona perimetral aplicada a una televisión.**

| Riesgo propio | Por qué lo es |
|---|---|
| **Equipo audiovisual sin actualizar** | **Un mezclador o un servidor de vídeo tiene sistema operativo y NO se parchea como un ordenador**: parar la emisión para actualizar no es trivial |
| **Contraseñas por defecto** | **Muchos equipos salen de fábrica con credenciales conocidas y se instalan sin cambiarlas** |
| **Acceso remoto del fabricante** | **El soporte suele pedir acceso permanente**: puerta que hay que controlar y auditar |
| **La automatización de emisión** | **El sistema con más capacidad de daño y el que menos se protege**: quien lo controle controla lo que sale en antena |

- **LA TENSIÓN QUE DEFINE EL PUNTO PARA UN INGENIERO** · `[of]` · **La política de seguridad corporativa
  está escrita para ordenadores de oficina**, y **aplicarla literalmente a un equipo de emisión puede
  tumbar el canal.** **Lo que se pide no es saltársela: es ESCRIBIR LA EXCEPCIÓN**, con su análisis de
  riesgo, sus controles compensatorios y **la firma de quien acepta lo que queda.**
- **DONDE LAS DOS MATERIAS SE JUNTAN** · `[of]` · **El plan de continuidad de una televisión tiene que
  contemplar el caso en que los sistemas informáticos caigan y haya que emitir igual.** **Una cadena de
  emisión manual, con material en soporte y sin automatización, es la última línea de defensa**, y **es
  la que nadie ensaya.**

## Lo que se ha preguntado

- **NINGUNA PREGUNTA.**
- **LO RAZONABLEMENTE PREGUNTABLE** · `[of]` · **Las tres normas de la familia y cuál se certifica**,
  **la tabla de fases de la biblioteca de gestión** y **la distinción entre incidente, problema y
  cambio.**
