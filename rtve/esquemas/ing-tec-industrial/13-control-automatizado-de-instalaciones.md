# Esquema · Tema 13 del específico de Ingeniería Técnica · Industrial · Control automatizado de instalaciones industriales

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de ingeniería de control y de
instalaciones · `[norma]` = exigencia de una norma de OTRO punto de este mismo anexo · `[plan]` =
enunciado del anexo. **Siglas**: el sistema de gestión técnica de edificios, que el propio enunciado
abrevia por su nombre inglés (**BMS**, *building management system*); el autómata programable
(**PLC**, *programmable logic controller*); el control de supervisión y adquisición de datos
(**SCADA**); la interfaz entre persona y máquina (**HMI**, *human-machine interface*); la entrada y
salida (**E/S**); el protocolo de internet (**IP**); el Reglamento de Instalaciones Térmicas en los
Edificios (**RITE**); el Código Técnico de la Edificación (**CTE**) con sus exigencias de ahorro de
energía (**HE 3**) y de seguridad de utilización (**SUA 4**); y el multiplexado digital de iluminación
(**DMX512**).

**Cabecera.** Enunciado: punto 13 del anexo, **una línea de doce palabras y unas siglas entre
paréntesis** · **es el único punto del anexo SIN NORMA** · **de dónde sale el tema entonces**: **va
entero como oficio, y lo declara** · **lo único normativo que lo toca**: **las exigencias de regulación
y control que otras normas del propio anexo imponen** —RITE, Código Técnico y reglamento de alumbrado
exterior—, **reunidas en su epígrafe sexto.**

<!-- indice -->

## Índice

- [Qué es un sistema de gestión técnica y qué no](#qué-es-un-sistema-de-gestión-técnica-y-qué-no)
- [La pirámide de automatización](#la-pirámide-de-automatización)
- [Las señales y los puntos](#las-señales-y-los-puntos)
- [Buses de campo y protocolos](#buses-de-campo-y-protocolos)
- [Las estrategias que se programan](#las-estrategias-que-se-programan)
- [Lo que la normativa del anexo exige de control](#lo-que-la-normativa-del-anexo-exige-de-control)
- [Lo propio de una instalación audiovisual](#lo-propio-de-una-instalación-audiovisual)

<!-- /indice -->

## Qué es un sistema de gestión técnica y qué no

- **LA DEFINICIÓN QUE EL TEMARIO PROPONE Y DECLARA COMO SUYA** · `[of]` · **Conjunto de sensores,
  actuadores, controladores, red y programas que supervisa y regula de forma centralizada las
  instalaciones de un edificio o de un complejo.**

| Sistema | Qué gobierna | Quién lo proyecta |
|---|---|---|
| **Gestión técnica de edificios** | **Climatización, alumbrado, agua, energía, elevación, y la supervisión de las demás** | **Ingeniería de instalaciones** |
| **Control industrial de proceso** | **Una máquina o una línea de producción** | **Ingeniería de automatización** |
| **Seguridad y protección contra incendios** | **Detección, extinción, control de humos** | **Aparte, por normativa propia**, la del tema 6 |
| **Seguridad física** | **Control de accesos, intrusión, videovigilancia** | **Aparte, con protección de datos** |

- **LA REGLA DE DISEÑO QUE SALE DE ESA TABLA** · `[of]` · **El sistema de gestión supervisa a los otros
  tres, pero NO los sustituye ni los manda.** **Una central de incendios no obedece al sistema de
  gestión: le informa.** **Confundir supervisión con mando es el error de arquitectura más caro del
  punto.**

| Por qué se instala | Qué aporta |
|---|---|
| **Ahorro energético** | **Ajustar el consumo a la ocupación y a la demanda reales** |
| **Confort** | **Mantener condiciones estables sin intervención manual** |
| **Mantenimiento** | **Detectar la avería antes de que la note el usuario** y **saber qué equipo ha trabajado cuánto** |
| **Explotación** | **Operar con menos gente y desde un solo puesto** |

- **LA TERCERA ES LA QUE MÁS SE INFRAVALORA AL COMPRAR** · `[of]` · **Un sistema que registra horas de
  funcionamiento permite pasar de mantenimiento por calendario a mantenimiento por CONDICIÓN.**

## La pirámide de automatización

| Nivel | Qué hay | Tiempo de respuesta | Qué maneja |
|---|---|---|---|
| **De campo** | **Sensores y actuadores** | **Milisegundos** | **La magnitud física** |
| **De control** | **Autómatas programables y controladores** | **Decenas de milisegundos** | **La lógica y los lazos** |
| **De supervisión** | **Puestos de operación, sinópticos** | **Segundos** | **El estado y la orden del operador** |
| **De gestión** | **Informes, históricos, gestión energética** | **Horas o días** | **La tendencia y el coste** |

- **LA REGLA QUE ORDENA LA PIRÁMIDE** · `[of]` · **Cuanto más abajo, más rápido y más concreto; cuanto
  más arriba, más lento y más agregado.** **Un lazo de temperatura se cierra en el nivel de control, no
  en el de gestión**, y **un sistema que suba cada lectura al de gestión para decidir se cae solo.**
- **EL PRINCIPIO DE AUTONOMÍA** · `[of]` · **Cada nivel debe seguir funcionando si el de arriba
  desaparece.** **Un autómata sin supervisión sigue regulando; una válvula con posicionador local sigue
  en su última consigna.** **Es la diferencia entre un sistema robusto y uno que deja el edificio a
  oscuras cuando cae un servidor.**

## Las señales y los puntos

- **LA UNIDAD DE CUENTA** · `[of]` · **El «punto»**, y **es con lo que se presupuesta.**

| Tipo de punto | Qué es | Ejemplos |
|---|---|---|
| **Entrada digital** | **Un contacto: abierto o cerrado** | **Estado de marcha, alarma, posición de un interruptor** |
| **Salida digital** | **Una orden de todo o nada** | **Arranque de bomba, mando de contactor** |
| **Entrada analógica** | **Una magnitud continua medida** | **Temperatura, presión, caudal, consumo** |
| **Salida analógica** | **Una consigna continua** | **Apertura de válvula, velocidad de variador** |

| Señal normalizada | Rango | Rasgo |
|---|---|---|
| **Corriente** | **4-20 miliamperios** | **El cero está en 4**: si llega 0, el lazo está roto y se sabe |
| **Tensión** | **0-10 voltios** | **Más barata y más sensible a la caída en el cable** |
| **Resistiva** | **Sondas de resistencia** | **Para temperatura; la longitud del cable falsea la lectura** |
| **Contacto libre de tensión** | **Abierto o cerrado** | **La más robusta de todas** |

- **EL DATO DE OFICIO MÁS ÚTIL DEL EPÍGRAFE** · `[of]` · **Al no empezar en cero, un cable cortado da
  en 4-20 una lectura imposible y el sistema lo detecta.** **En 0-10 voltios, un cable cortado se lee
  como «cero grados» y nadie se entera.**
- **LA REGLA DE DIMENSIONADO QUE EVITA EL ERROR MÁS FRECUENTE** · `[of]` · **El número de puntos se
  cierra al final y siempre crece.** **Reserva de puntos en cada controlador y de espacio en cada
  cuadro**, por la misma razón por la que se deja reserva de cable en el tema 16.

## Buses de campo y protocolos

| Enfoque | Qué da | Qué cuesta |
|---|---|---|
| **Protocolo abierto** | **Varios fabricantes pueden ampliar y mantener** | **Integración más trabajosa** |
| **Protocolo propietario** | **Integración perfecta y rápida** | **Dependencia de un solo suministrador para toda la vida de la instalación** |

- **LA DECISIÓN SE TOMA EN EL PLIEGO, NO DESPUÉS** · `[of]` · **Un pliego que describe prestaciones y
  exige protocolo abierto admite competencia; uno que describe un producto la excluye.** **La elección
  de protocolo es una decisión de competencia disfrazada de decisión técnica.**

| Grupo de protocolos | Dónde se usa |
|---|---|
| **Buses de automatización de edificios** | **Climatización, alumbrado, persianas** |
| **Buses de campo industriales** | **Proceso, máquina, variadores** |
| **Protocolos sobre red de datos** | **Supervisión, integración entre sistemas, acceso remoto** |
| **Protocolos de instalación eléctrica** | **Contadores, analizadores de red, cuadros** |

- **LA TENDENCIA QUE ORDENA LOS CUATRO** · `[of]` · **Lo que antes era un bus dedicado hoy viaja sobre
  red de datos.** **Es el mismo movimiento que recorrió el vídeo, y trae los mismos problemas**:
  separación de redes, direccionamiento y seguridad.
- **EL AVISO DE SEGURIDAD, CONTRAPARTIDA DE ESA TENDENCIA** · `[of]` · **Un sistema de gestión técnica
  en la misma red que la ofimática es una puerta al edificio**: **cuadros, calderas y grupos de frío a
  un clic de quien abra un correo con adjunto malicioso.** **La separación de redes no es una comodidad
  de red: es una medida de seguridad física.**

## Las estrategias que se programan

| Estrategia | Qué hace |
|---|---|
| **Programación horaria** | **Arrancar y parar por calendario, con festivos y excepciones** |
| **Arranque óptimo** | **Calcular a qué hora arrancar para llegar a consigna justo a la de ocupación**, aprendiendo de los días anteriores |
| **Parada óptima** | **Parar antes del final de jornada aprovechando la inercia del edificio** |
| **Enfriamiento gratuito** | **Usar aire exterior cuando sus condiciones son mejores que las de recirculación** |
| **Compensación por temperatura exterior** | **Mover la consigna de impulsión según la exterior, en vez de mantenerla fija** |
| **Control por ocupación** | **Regular caudal, alumbrado y consigna por presencia real** |
| **Limitación de potencia** | **Escalonar arranques para no superar la potencia contratada** |
| **Rotación de equipos** | **Igualar horas de funcionamiento entre bombas o enfriadoras redundantes** |

- **LAS DOS PRIMERAS SE CONFUNDEN Y NO SON LO MISMO** · `[of]` · **La horaria arranca a hora fija; el
  arranque óptimo calcula esa hora cada día.** **En un edificio grande, la diferencia es una hora de
  climatización diaria.**
- **LAS TRES ÚLTIMAS SON LAS QUE NADIE PIDE Y UN INGENIERO PONE** · `[of]` · **La limitación de potencia
  evita una penalización en factura**, y **la rotación evita que la bomba de reserva sea la que nunca
  ha girado y se gripe el día que hace falta.**

| Acción del lazo | Qué corrige |
|---|---|
| **Proporcional** | **El error presente**: cuanto mayor la desviación, mayor la corrección |
| **Integral** | **El error acumulado**: elimina la desviación permanente |
| **Derivativa** | **La velocidad del error**: anticipa y frena la oscilación |

- **EL AVISO DE AJUSTE QUE SE APRENDE EN OBRA** · `[of]` · **En climatización la derivativa se usa poco
  y suele desconectarse**, porque **las inercias térmicas son lentas y el ruido de la sonda la hace
  oscilar.** **La mayoría de los lazos de un edificio son proporcional más integral.**

## Lo que la normativa del anexo exige de control

| Norma | Qué exige de control | Dónde |
|---|---|---|
| **RITE, artículo 12.3** | **Sistemas de regulación y control para mantener las condiciones de diseño, ajustar los consumos a las variaciones de la demanda e interrumpir el servicio** | **Tema 1** |
| **RITE, artículo 12.4** | **Sistemas de CONTABILIZACIÓN para que el usuario conozca su consumo y para repartir gastos** | **Tema 1** |
| **RITE, artículo 2.1** | **Los sistemas de automatización y control son PARTE de la instalación térmica** | **Tema 1** |
| **Código Técnico, exigencia HE 3** | **Control que ajuste el funcionamiento a la ocupación real** y **regulación que optimice el aprovechamiento de la luz natural** | **Tema 3** |
| **Código Técnico, exigencia SUA 4** | **Alumbrado de emergencia ante fallo del normal** | **Tema 3** |
| **Reglamento de alumbrado exterior, art. 4.3.º** | **Accionamiento y regulación del nivel luminoso donde se requiera** | **Tema 12** |

- **LA RESPUESTA DE FONDO DEL PUNTO** · `[norma]` · **El control no es un extra del proyecto: es
  exigencia reglamentaria de tres normas distintas**, y **un proyecto de climatización o de alumbrado
  sin sistema de control no cumple.**
- **EL MATIZ QUE CONVIENE SUBRAYAR** · `[norma]` · **Por el artículo 2.1 del RITE, los sistemas de
  automatización y control están DENTRO de la definición de instalación térmica**: **se les aplica todo
  el reglamento —documentación, ejecución, mantenimiento e inspección—**, y **no son un suministro
  informático aparte.**

## Lo propio de una instalación audiovisual

| Conflicto | Por qué ocurre | Cómo se resuelve |
|---|---|---|
| **La parada óptima contra el directo** | **El sistema apaga la climatización antes del final de jornada; el plató sigue grabando a las once de la noche** | **Los espacios de producción salen del calendario general y se gobiernan por ocupación real o por reserva** |
| **La limitación de potencia contra el arranque de un plató** | **Escalonar arranques puede retrasar la iluminación de un decorado** | **La producción se declara carga NO escalonable** |
| **El alumbrado por presencia contra la grabación** | **Un detector apaga la luz de un pasillo por el que no pasa nadie durante una toma** | **Las zonas contiguas a plató se excluyen del apagado automático mientras la luz roja esté encendida** |
| **El ruido de la climatización contra el sonido directo** | **El sistema sube el caudal para mantener consigna y el micrófono lo oye** | **Modo «silencio de plató»: consigna relajada y caudal limitado durante la toma** |

- **LOS CUATRO SE RESUELVEN CON LA MISMA IDEA** · `[of]` · **El sistema de gestión tiene que conocer el
  estado de PRODUCCIÓN del edificio.** **Una señal de «en grabación» procedente del control de
  realización vale más que veinte sensores de presencia.**
- **EL AVISO DE DISEÑO QUE CIERRA EL PUNTO** · `[of]` · **Esa señal es una integración entre dos mundos
  que no se hablan** —instalaciones y producción—, **y hay que pedirla en el pliego desde el
  principio.** **Añadirla después cuesta diez veces más**, porque **implica tocar los dos sistemas y a
  dos suministradores.**
