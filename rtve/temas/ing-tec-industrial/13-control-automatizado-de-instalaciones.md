# Tema 13 del específico de Ingeniería Técnica · Industrial · Control automatizado de instalaciones industriales

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Industrial · punto 13 |
| **Sirve para** | **Ing. Técnica Industrial** |
| **Fuente** | **Sin norma: el enunciado no nombra ninguna.** Su materia es la gestión técnica de edificios, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Único punto del anexo sin norma en su enunciado** | **Una línea de doce palabras y unas siglas entre paréntesis.** Lo único normativo que lo toca son las exigencias de control de OTROS puntos, reunidas en su epígrafe sexto |
| **Extensión** | **2.834 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el sistema de gestión técnica de edificios, que el
propio enunciado del anexo abrevia por su nombre inglés (**BMS**, *building management system*); el
autómata programable (**PLC**, *programmable logic controller*); el control de supervisión y
adquisición de datos (**SCADA**); la interfaz entre la persona y la máquina (**HMI**, *human-machine
interface*); la entrada y salida (**E/S**); el protocolo de internet (**IP**); el Reglamento de
Instalaciones Térmicas en los Edificios (**RITE**), del tema 1; el Código Técnico de la Edificación
(**CTE**), del tema 3, con sus exigencias básicas de ahorro de energía (**HE 3**) y de seguridad de
utilización (**SUA 4**); y el multiplexado digital de iluminación (**DMX512**), que la producción
audiovisual usa en paralelo.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Industrial, punto 13):
> «Control automatizado de instalaciones industriales (BMS).»

**Es el único punto del anexo SIN NORMA.** **Los otros quince nombran uno o varios reales decretos con
su identificador y su fecha de consolidación; éste es una línea de doce palabras y unas siglas entre
paréntesis.**

**Eso obliga a decir de dónde sale este tema**: **va entero como oficio de ingeniería de control y de
instalaciones**, y **lo declara.** **Lo único normativo que lo toca son las exigencias de regulación y
control que otras normas del propio anexo imponen** —el RITE, el Código Técnico y el reglamento de
alumbrado exterior—, y **el epígrafe 6 las reúne.**

<!-- indice -->

## Índice

- [1. Qué es un sistema de gestión técnica y qué no](#1-qué-es-un-sistema-de-gestión-técnica-y-qué-no)
- [2. La pirámide de automatización](#2-la-pirámide-de-automatización)
- [3. Las señales y los puntos](#3-las-señales-y-los-puntos)
- [4. Los buses de campo y los protocolos](#4-los-buses-de-campo-y-los-protocolos)
- [5. Las estrategias de control que se programan](#5-las-estrategias-de-control-que-se-programan)
- [6. Lo que la normativa del anexo exige de control](#6-lo-que-la-normativa-del-anexo-exige-de-control)
- [7. Lo propio de una instalación audiovisual](#7-lo-propio-de-una-instalación-audiovisual)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Qué es un sistema de gestión técnica y qué no

**La definición que este temario propone, y la declara como suya**: **un sistema de gestión técnica de
edificios es el conjunto de sensores, actuadores, controladores, red y programas que supervisa y
regula de forma centralizada las instalaciones de un edificio o de un complejo.**

**Y lo que hay que separar antes de nada, porque el vocabulario del sector los confunde:**

| Sistema | Qué gobierna | Quién lo proyecta |
|---|---|---|
| **Gestión técnica de edificios** | **Climatización, alumbrado, agua, energía, elevación, y la supervisión de las demás** | **Ingeniería de instalaciones** |
| **Control industrial de proceso** | **Una máquina o una línea de producción** | **Ingeniería de automatización** |
| **Seguridad y protección contra incendios** | **Detección, extinción, control de humos** | **Va aparte y por normativa propia**, la del tema 6 |
| **Seguridad física** | **Control de accesos, intrusión, videovigilancia** | **Va aparte, con protección de datos del tema 19 del anexo de otra ocupación** |

**La regla de diseño que sale de esa tabla y que un examen podría pedir**: **el sistema de gestión
supervisa a los otros tres, pero NO los sustituye ni los manda.** **Una central de incendios no
obedece al sistema de gestión: le informa.** **Confundir supervisión con mando es el error de
arquitectura más caro del punto.**

**Y las cuatro razones por las que se instala, que son lo preguntable de la introducción:**

| Razón | Qué aporta |
|---|---|
| **Ahorro energético** | **Ajustar el consumo a la ocupación y a la demanda reales** |
| **Confort** | **Mantener condiciones estables sin intervención manual** |
| **Mantenimiento** | **Detectar la avería antes de que la note el usuario**, y **saber qué equipo ha trabajado cuánto** |
| **Explotación** | **Operar con menos gente y desde un solo puesto** |

**La tercera es la que más se infravalora al comprar y la que más se agradece después**: **un sistema
que registra horas de funcionamiento permite pasar de mantenimiento por calendario a mantenimiento por
condición.**

## 2. La pirámide de automatización

**Es el modelo clásico y ordena el punto entero.** **Cuatro niveles, y cada uno con su equipo, su
tiempo de respuesta y su tipo de dato:**

| Nivel | Qué hay | Tiempo de respuesta | Qué maneja |
|---|---|---|---|
| **De campo** | **Sensores y actuadores** | **Milisegundos** | **La magnitud física** |
| **De control** | **Autómatas programables y controladores** | **Decenas de milisegundos** | **La lógica y los lazos** |
| **De supervisión** | **Puestos de operación, sinópticos** | **Segundos** | **El estado y la orden del operador** |
| **De gestión** | **Informes, históricos, gestión energética** | **Horas o días** | **La tendencia y el coste** |

**La regla que ordena la pirámide y que hay que saber enunciar**: **cuanto más abajo, más rápido y más
concreto; cuanto más arriba, más lento y más agregado.** **Un lazo de temperatura se cierra en el
nivel de control, no en el de gestión**, y **un sistema que suba cada lectura al nivel de gestión para
decidir se cae solo.**

**Y el principio de autonomía, que es el que decide si una instalación aguanta un fallo**: **cada nivel
debe seguir funcionando si el de arriba desaparece.** **Un autómata sin supervisión sigue regulando;
una válvula con posicionador local sigue en su última consigna.** **Ésa es la diferencia entre un
sistema robusto y uno que deja el edificio a oscuras cuando cae un servidor.**

## 3. Las señales y los puntos

**El «punto» es la unidad de cuenta de un sistema de gestión técnica**, y **es con lo que se
presupuesta.** **Las cuatro clases:**

| Tipo de punto | Qué es | Ejemplos |
|---|---|---|
| **Entrada digital** | **Un contacto: abierto o cerrado** | **Estado de marcha, alarma, posición de un interruptor** |
| **Salida digital** | **Una orden de todo o nada** | **Arranque de bomba, mando de contactor** |
| **Entrada analógica** | **Una magnitud continua medida** | **Temperatura, presión, caudal, consumo** |
| **Salida analógica** | **Una consigna continua** | **Apertura de válvula, velocidad de variador** |

**Y las señales normalizadas que un ingeniero encuentra en obra:**

| Señal | Rango | Rasgo |
|---|---|---|
| **Corriente** | **4-20 miliamperios** | **El cero está en 4**: si llega 0, el lazo está roto y se sabe |
| **Tensión** | **0-10 voltios** | **Más barata y más sensible a la caída en el cable** |
| **Resistiva** | **Sondas de resistencia** | **Para temperatura; la longitud del cable falsea la lectura** |
| **Contacto libre de tensión** | **Abierto o cerrado** | **La más robusta de todas** |

**La ventaja del rango 4-20 es el dato de oficio más útil de este epígrafe**: **al no empezar en cero,
un cable cortado da una lectura imposible y el sistema lo detecta.** **En 0-10 voltios, un cable
cortado se lee como «cero grados» y nadie se entera.**

**Y la regla de dimensionado que evita el error de proyecto más frecuente**: **el número de puntos se
cierra al final y siempre crece.** **Se deja reserva de puntos en cada controlador y de espacio en
cada cuadro**, exactamente por la misma razón por la que se deja reserva de cable en el tema 16.

## 4. Los buses de campo y los protocolos

**Lo que un ingeniero tiene que saber decidir es si el sistema será ABIERTO o PROPIETARIO**, y **la
decisión se toma en el pliego, no después.**

| Enfoque | Qué da | Qué cuesta |
|---|---|---|
| **Protocolo abierto** | **Varios fabricantes pueden ampliar y mantener** | **Integración más trabajosa** |
| **Protocolo propietario** | **Integración perfecta y rápida** | **Dependencia de un solo suministrador para toda la vida de la instalación** |

**El aviso de contratación pública que esto arrastra, y que enlaza con el tema 15**: **un pliego que
describe prestaciones y exige protocolo abierto admite competencia; uno que describe un producto la
excluye.** **La elección de protocolo es, en la práctica, una decisión de competencia disfrazada de
decisión técnica.**

**Los grandes grupos de protocolos, sin entrar en producto:**

| Grupo | Dónde se usa |
|---|---|
| **Buses de campo de automatización de edificios** | **Climatización, alumbrado, persianas** |
| **Buses de campo industriales** | **Proceso, máquina, variadores** |
| **Protocolos sobre red de datos** | **Supervisión, integración entre sistemas, acceso remoto** |
| **Protocolos de instalación eléctrica** | **Contadores, analizadores de red, cuadros** |

**Y la tendencia que ordena los cuatro, y que es la misma de todo el temario técnico**: **lo que antes
era un bus dedicado hoy viaja sobre red de datos.** **Es exactamente el mismo movimiento que el vídeo
recorrió, y trae los mismos problemas: separación de redes, direccionamiento y seguridad.**

**El aviso de seguridad, que es la contrapartida de esa tendencia**: **un sistema de gestión técnica
en la misma red que la ofimática es una puerta al edificio.** **Los cuadros, las calderas y los
grupos de frío quedan a un clic de quien abra un correo con adjunto malicioso.** **La separación de
redes no es una comodidad de red: es una medida de seguridad física.**

## 5. Las estrategias de control que se programan

**Ésta es la parte que un examen puede pedir enumerada, y es lo que de verdad ahorra energía:**

| Estrategia | Qué hace |
|---|---|
| **Programación horaria** | **Arrancar y parar por calendario, con festivos y excepciones** |
| **Arranque óptimo** | **Calcular a qué hora hay que arrancar para llegar a consigna justo a la de ocupación**, aprendiendo de los días anteriores |
| **Parada óptima** | **Parar antes del final de la jornada aprovechando la inercia del edificio** |
| **Enfriamiento gratuito** | **Usar aire exterior cuando sus condiciones son mejores que las de recirculación** |
| **Compensación por temperatura exterior** | **Mover la consigna de impulsión según la exterior, en vez de mantenerla fija** |
| **Control por ocupación** | **Regular caudal, alumbrado y consigna por presencia real** |
| **Limitación de potencia** | **Escalonar arranques para no superar la potencia contratada** |
| **Rotación de equipos** | **Igualar horas de funcionamiento entre bombas o enfriadoras redundantes** |

**Las dos primeras se confunden y no son lo mismo**: **la programación horaria arranca a una hora
fija; el arranque óptimo calcula esa hora cada día.** **La diferencia entre las dos, en un edificio
grande, es una hora de climatización diaria.**

**Y las tres últimas son las que un ingeniero de instalaciones pone y nadie le pide**: **la limitación
de potencia evita una penalización en factura, y la rotación de equipos evita que la bomba de reserva
sea la que nunca ha girado y se gripe el día que hace falta.**

**El lazo de control clásico, con sus tres acciones, que hay que saber nombrar:**

| Acción | Qué corrige |
|---|---|
| **Proporcional** | **El error presente**: cuanto mayor la desviación, mayor la corrección |
| **Integral** | **El error acumulado**: elimina la desviación permanente |
| **Derivativa** | **La velocidad del error**: anticipa y frena la oscilación |

**El aviso de ajuste que se aprende en obra**: **en climatización la acción derivativa se usa poco y
suele desconectarse**, porque **las inercias térmicas son lentas y el ruido de la sonda la hace
oscilar.** **La mayoría de los lazos de un edificio son proporcional más integral.**

## 6. Lo que la normativa del anexo exige de control

**Este punto no tiene norma propia, y sin embargo el control aparece en cuatro puntos del mismo
anexo.** **Reunirlos es lo más útil que un temario puede hacer aquí:**

| Norma | Qué exige de control | Dónde está en este temario |
|---|---|---|
| **RITE, artículo 12.3** | **Sistemas de regulación y control necesarios para mantener las condiciones de diseño, ajustando los consumos a las variaciones de la demanda e interrumpir el servicio** | **Tema 1** |
| **RITE, artículo 12.4** | **Sistemas de CONTABILIZACIÓN para que el usuario conozca su consumo y para repartir gastos** | **Tema 1** |
| **RITE, artículo 2.1** | **Los sistemas de automatización y control son PARTE de la instalación térmica**, a efectos de ámbito | **Tema 1** |
| **Código Técnico, exigencia HE 3** | **Sistema de control que ajuste el funcionamiento a la ocupación real** y **sistema de regulación que optimice el aprovechamiento de la luz natural** | **Tema 3** |
| **Código Técnico, exigencia SUA 4** | **Alumbrado de emergencia en caso de fallo del normal** | **Tema 3** |
| **Reglamento de alumbrado exterior, artículo 4.3.º** | **Sistema de accionamiento y de regulación del nivel luminoso donde se requiera** | **Tema 12** |

**La conclusión que ese cuadro permite, y que es la respuesta de fondo de este punto**: **el control no
es un extra del proyecto.** **Es una exigencia reglamentaria de tres normas distintas**, y **un
proyecto de climatización o de alumbrado sin sistema de control no cumple.**

**Y un matiz que conviene subrayar del artículo 2.1 del RITE**: **los sistemas de automatización y
control están dentro de la definición de instalación térmica.** **Eso significa que se les aplica todo
el reglamento —documentación, ejecución, mantenimiento e inspección—**, y **no son un suministro
informático aparte.**

## 7. Lo propio de una instalación audiovisual

**Aquí está lo que este tema aporta y que ningún manual de gestión técnica dice**: **cómo convive un
sistema de gestión de edificios con una casa que emite.**

**Los cuatro conflictos reales, y cómo se resuelven:**

| Conflicto | Por qué ocurre | Cómo se resuelve |
|---|---|---|
| **La parada óptima contra el directo** | **El sistema apaga la climatización antes del final de jornada; el plató sigue grabando a las once de la noche** | **Los espacios de producción se sacan del calendario general y se gobiernan por ocupación real o por reserva** |
| **La limitación de potencia contra el arranque de un plató** | **Escalonar arranques puede retrasar la iluminación de un decorado** | **La producción se declara carga no escalonable** |
| **El alumbrado por presencia contra la grabación** | **Un detector apaga la luz de un pasillo por el que no pasa nadie durante una toma** | **Las zonas contiguas a plató se excluyen del apagado automático mientras la luz roja esté encendida** |
| **El ruido de la climatización contra el sonido directo** | **El sistema sube el caudal para mantener consigna y el micrófono lo oye** | **Modo «silencio de plató»: consigna relajada y caudal limitado durante la toma** |

**Los cuatro se resuelven con la misma idea, y conviene enunciarla así**: **el sistema de gestión tiene
que conocer el estado de PRODUCCIÓN del edificio.** **Una señal de «en grabación» procedente del
control de realización vale más que veinte sensores de presencia.**

**Y el aviso de diseño que cierra el punto**: **esa señal es una integración entre dos mundos que no se
hablan** —el de instalaciones y el de producción—, **y hay que pedirla en el pliego desde el
principio.** **Añadirla después cuesta diez veces más**, porque **implica tocar los dos sistemas y a
dos suministradores.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **es el ÚNICO punto de este anexo sin norma
detrás**: **su enunciado es una línea de doce palabras y no nombra ningún real decreto.**

**Cuatro declaraciones expresas:**

1. **No se ha consultado la documentación de ningún fabricante de sistemas de gestión técnica, de
   autómatas ni de protocolos.** **Los nombres comerciales de protocolos y de productos NO aparecen
   en este tema, a propósito**: **lo que se describe son grupos y funciones**, y **la razón está
   escrita en el epígrafe 4.**
2. **Las normas que el epígrafe 6 reúne son las de otros puntos de este mismo anexo**, y **están
   citadas literalmente o identificadas en los temas 1, 3 y 12 de este específico**: **el artículo
   12.4 del RITE se cita literalmente en el tema 1**, y **el 12.3, el 2.1, las exigencias básicas del
   Código Técnico y el artículo 4 del reglamento de alumbrado exterior van identificados allí.**
   **Aquí se reúnen, no se vuelven a citar.**
3. **La pirámide de automatización, las clases de punto, las señales normalizadas, las estrategias de
   control y las tres acciones del lazo son teoría clásica de la ingeniería de control y oficio de
   instalaciones**, presentadas como conocimiento común de la materia.
4. **Los cuatro conflictos del epígrafe 7 son oficio de instalaciones audiovisuales**, escritos como
   guía de proyecto. **No describen la instalación de ninguna casa concreta**, cuya documentación no
   se ha consultado.

**El resto del tema va como oficio y así se declara**: la definición de sistema de gestión técnica que
el temario propone, la tabla que lo separa del control de proceso y de la seguridad, la regla de que
supervisa pero no manda, la observación sobre el mantenimiento por condición, la regla de que cuanto
más abajo más rápido y el principio de autonomía por niveles, la ventaja del rango 4-20 frente al
0-10, la advertencia de dejar reserva de puntos, la lectura de la elección de protocolo como decisión
de competencia, el aviso de seguridad sobre la red compartida, la distinción entre programación
horaria y arranque óptimo, el aviso sobre la acción derivativa en climatización y los cuatro
conflictos del epígrafe 7 con su resolución común. **Nada de eso está en un boletín oficial ni en una
norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
