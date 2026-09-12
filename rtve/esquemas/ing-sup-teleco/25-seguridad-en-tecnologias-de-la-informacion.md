# Esquema · Tema 25 del específico de Ingeniería Superior · Telecomunicación · Seguridad en tecnologías de la información

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de seguridad en instalaciones
audiovisuales · `[plan]` = enunciado del propio anexo · `[norma]` = Real Decreto 311/2022, del Esquema
Nacional de Seguridad, citado literalmente en el tema. **Siglas**: la Organización Internacional de
Normalización (**ISO**) y la Comisión Electrotécnica Internacional (**IEC**), que publican la familia
**ISO/IEC 27000**; el sistema de gestión de la seguridad de la información (**SGSI**); la biblioteca de
infraestructura de tecnologías de la información (**ITIL**); y el Esquema Nacional de Seguridad
(**ENS**).

**Cabecera.** Enunciado: punto 27 del anexo · **cero preguntas** · **el enunciado NO es el mismo que el
del punto 22 de Ingeniería Técnica**: aquél dice «Normativa ISO/IEC 27001» y éste «Normativas ISO/IEC
27000-series». **Por eso el tema no se comparte.**

**La advertencia de método, dicha de entrada** · `[of]` · **Ni la familia de normas ni la biblioteca de
gestión de servicios son textos del boletín**: **son publicaciones de pago que este proyecto no
tiene.** **De ellas no se cita ni una cláusula**: lo que se dice va **como conocimiento común de la
materia, declarado.** **Lo único que se cita literalmente es el Esquema Nacional de Seguridad.**

<!-- indice -->

## Índice

- [Qué se protege](#qué-se-protege)
- [La familia de normas de gestión](#la-familia-de-normas-de-gestión)
- [La biblioteca de gestión de servicios](#la-biblioteca-de-gestión-de-servicios)
- [La norma española](#la-norma-española)
- [Lo propio de una instalación de emisión](#lo-propio-de-una-instalación-de-emisión)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué se protege

| Propiedad | Qué garantiza |
|---|---|
| **acceso** | **que quien tiene derecho pueda llegar a la información** |
| **confidencialidad** | **que no llegue quien no está autorizado** |
| **integridad** | **que no se altere sin autorización** |
| **trazabilidad** | **que se pueda saber quién hizo qué y cuándo** |
| **autenticidad** | **que quien dice ser algo lo sea** |
| **disponibilidad** | **que esté accesible cuando hace falta** |
| **conservación** | **que siga estando dentro de años, y siga pudiendo leerse** |

- **de dónde salen las siete** · `[norma]` · **Del apartado 2 del primer artículo del Esquema Nacional
  de Seguridad**, que **las enumera todas y no sólo las tres de manual.**
- **LA OBSERVACIÓN QUE ORDENA LA LISTA AQUÍ** · `[of]` · **En una casa que emite, la propiedad crítica
  es la DISPONIBILIDAD, no la confidencialidad.** **Un incidente que revele un documento es grave y se
  gestiona; uno que deje la señal en negro lo ve el país entero.** **Quien llegue con el orden de
  prioridades de una oficina se equivocará en la primera decisión.**
- **conservar no es guardar** · `[of]` · **Un fichero que sobrevive treinta años en una cinta que ya no
  tiene lector no se ha conservado: se ha perdido con orden.** **Migrar de soporte y de formato antes
  de que mueran es una obligación de SEGURIDAD, no una tarea de archivo.**

## La familia de normas de gestión

| Norma | Qué papel desempeña |
|---|---|
| **la 27000** | **el vocabulario y la visión de conjunto** |
| **la 27001** | **los requisitos del sistema de gestión: es la CERTIFICABLE** |
| **la 27002** | **el catálogo de buenas prácticas y controles: NO se certifica** |

- **la distinción que se pregunta siempre** · `[of]` · **Una organización se certifica en la de
  requisitos, no en la de buenas prácticas.** **Una dice qué hay que tener; la otra, cómo
  conseguirlo.**
- **la tesis del modelo** · `[of]` · **La seguridad no se compra, se gestiona.** **Lo que distingue a
  una organización segura no son sus cortafuegos sino su manera de decidir dónde ponerlos.**
- **la gestión por riesgos** · `[of]` · **Se inventarían activos, se valoran amenazas y
  vulnerabilidades, se estima el impacto, se decide qué se acepta y qué se trata**, y **sólo entonces
  se eligen los controles.** **Comprar antes de ese análisis deja fuera el riesgo que nadie miró.**

| Tratamiento del riesgo | En qué consiste |
|---|---|
| **mitigar** | **controles que reduzcan probabilidad o impacto** |
| **transferir** | **pasarlo a un tercero: un seguro, un proveedor** |
| **evitar** | **dejar de hacer la actividad que lo genera** |
| **aceptar** | **asumirlo tal como está** |

- **la que más se olvida** · `[of]` · **Aceptar exige FIRMA**: **es una decisión de dirección y no del
  técnico que lo detectó.** **Un riesgo aceptado por quien no tiene autoridad no está aceptado: está
  oculto.**

## La biblioteca de gestión de servicios

- **qué es, con precisión** · `[of]` · **Un cuerpo de buenas prácticas para gestionar servicios de
  tecnologías de la información.** **No es certificable para la organización: quienes se certifican son
  las personas.**
- **por qué el programa la pone junto a la seguridad** · `[of]` · **Porque casi todo lo que rompe la
  seguridad de una instalación entra por un FALLO DE GESTIÓN DE SERVICIO**: un cambio sin autorizar,
  una configuración sin registrar, un incidente que nadie escala.

| Fase de la versión 3 | De qué se ocupa |
|---|---|
| **estrategia** | **qué servicios se prestan y con qué recursos** |
| **diseño** | **nivel de servicio, capacidad, disponibilidad, continuidad, seguridad** |
| **transición** | **cómo pasa a producción sin romper lo que había** |
| **operación** | **incidentes, problemas, peticiones, accesos** |
| **mejora continua** | **medir y corregir; atraviesa a las otras cuatro** |

| Concepto | Qué persigue | Cuándo se cierra |
|---|---|---|
| **incidente** | **devolver el servicio cuanto antes** | **cuando vuelve, aunque sea con un apaño** |
| **problema** | **eliminar la causa** | **cuando la causa desaparece** |
| **cambio** | **autorizar y coordinar una modificación** | **cuando está hecha y comprobada** |

- **el matiz que ordena las dos primeras** · `[of]` · **Quien atiende una urgencia no puede a la vez
  investigar despacio.** **Separarlos no es burocracia: son dos oficios con dos relojes.**
- **qué cambia en la versión 4** · `[of]` · **Desaparece la estructura rígida de fases y entra un
  sistema de valor del servicio con principios rectores y prácticas.** **La gestión del cambio pasa a
  llamarse habilitación del cambio, y el nombre no es cosmético: dice que el papel del proceso es
  facilitar con control, no frenar.**
- **lo que el temario NO da** · `[of]` · **Ni el número de principios ni el de prácticas**: **la
  publicación no se ha consultado.**

## La norma española

- **ámbito** · `[norma]` · **Se aplica a TODO EL SECTOR PÚBLICO**, y **también a las entidades privadas
  cuando, en virtud de una relación contractual, presten servicios o provean soluciones a entidades del
  sector público.**
- **la consecuencia práctica** · `[of]` · **El esquema no se queda dentro de la casa**: **alcanza al
  proveedor, y el propio artículo manda que los pliegos incluyan los requisitos de conformidad,
  extendiendo la cautela a la cadena de suministro.** **Quien redacta un pliego de un sistema de
  emisión está escribiendo, lo sepa o no, una cláusula de seguridad.**

| Principio básico | |
|---|---|
| **a** | **seguridad como proceso integral** |
| **b** | **gestión basada en los riesgos** |
| **c** | **prevención, detección, respuesta y conservación** |
| **d** | **existencia de líneas de defensa** |
| **e** | **vigilancia continua** |
| **f** | **reevaluación periódica** |
| **g** | **diferenciación de responsabilidades** |

- **la frase que hay que retener de las líneas de defensa** · `[norma]` · **Han de estar constituidas
  por medidas de naturaleza ORGANIZATIVA, FÍSICA Y LÓGICA.** **Una instalación con sólo capas lógicas
  no tiene defensa en profundidad: tiene una capa gruesa.**
- **la diferenciación de responsabilidades** · `[norma]` · **Se diferencia el responsable de la
  información, el del servicio, el de la seguridad y el del sistema**, y **la responsabilidad de la
  seguridad está separada de la de EXPLOTACIÓN.**
- **por qué esa separación es una regla de seguridad y no de organigrama** · `[of]` · **Quien explota
  tiene el incentivo de que funcione y quien responde de la seguridad, el de que no se rompa.**
  **Cuando caen en la misma persona, la primera gana siempre**, porque **la avería se ve hoy y la
  brecha dentro de un año.**

## Lo propio de una instalación de emisión

| Red | Cuánto se expone |
|---|---|
| **de señal** | **cerrada: no toca la red pública** |
| **de control y automatización** | **cerrada, con accesos contados** |
| **de producción** | **cerrada con salidas controladas** |
| **de gestión** | **expuesta** |

- **la regla de diseño** · `[of]` · **El tráfico va de la expuesta hacia las cerradas sólo por puntos
  controlados, y nunca al revés sin control.**

| Riesgo propio | Por qué es de aquí |
|---|---|
| **el equipo que no se puede parchear** | **parar la emisión para actualizar no es una decisión técnica sino editorial** |
| **la credencial de fábrica** | **mucho equipo se pone en servicio sin cambiarla** |
| **el acceso remoto del suministrador** | **una puerta permanente que hay que acotar, registrar y poder cerrar** |
| **la automatización de emisión** | **el sistema con más capacidad de daño y el menos vigilado** |
| **el reloj de la instalación** | **atacar el reloj es tumbar la producción sin tocar un solo flujo** |

- **la tensión que define el punto** · `[of]` · **La política corporativa está escrita para ordenadores
  de oficina**, y **aplicarla al pie de la letra a un equipo de emisión puede tumbar el canal.** **Lo
  que se espera no es saltársela sino ESCRIBIR LA EXCEPCIÓN**: con su análisis de riesgo, sus controles
  compensatorios y la firma de quien acepta lo que queda.
- **la continuidad** · `[of]` · **El plan tiene que contemplar el caso en que los sistemas informáticos
  caigan y haya que emitir igual.** **Una cadena reducida y gobernada a mano es la última línea de
  defensa**, y **un plan que no se ha ensayado no es un plan: es un documento.**

## Lo que se ha preguntado

**Ninguna pregunta.** **Lo razonablemente preguntable**: **las propiedades que se protegen y cuáles
añade el esquema español a las tres clásicas** · **cuál de las normas de la familia es la certificable**
· **las cuatro maneras de tratar un riesgo y cuál exige firma** · **las cinco fases de la versión 3 y
el cambio de enfoque de la 4** · **la distinción entre incidente, problema y cambio** · **los siete
principios básicos, que van todos en un solo artículo.**
