# Tema 12 del específico de Oficial Técnico Electricista · Sistemas de gestión técnica de edificios y monitorización

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Oficial Técnico Electricista · punto 12 |
| **Sirve para** | Puesto 2.27, Oficial Técnico Electricista (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | El enunciado no nombra ninguna norma. Lo normativo sale del Real Decreto 1027/2007, de 20 de julio, por el que se aprueba el Reglamento de Instalaciones Térmicas en los Edificios (BOE-A-2007-15820): artículos 2.1, 12.3 y 25.3; IT 1.2.4.3.1, IT 1.2.4.3.5, IT 1.2.4.4, IT 1.2.4.5.1, IT 1.3.4.1.2, IT 2.3.4, IT 3.3, IT 3.4.2, IT 3.4.4, IT 3.4.5, IT 3.6, IT 3.7 e IT 4.3.4; apéndices 1 (términos y definiciones) y 2 (normas de referencia). Y del Real Decreto 513/2017, de 22 de mayo, por el que se aprueba el Reglamento de instalaciones de protección contra incendios (BOE-A-2017-6606): anexo I, sección 1.ª, apartado 1.7. Fuente técnica: guía técnica de mantenimiento de instalaciones térmicas del IDAE (2007); ISO 16484-5:2026 (BACnet); especificación del protocolo Modbus V1.1b3; glosario del NIST. Lo demás, oficio, y así se dice |
| **Redacción que se estudia** | La vigente el día de la lectura (05/10/2026). El RITE no ha cambiado desde el 01/07/2021 (Real Decreto 178/2021, de 23 de marzo, BOE-A-2021-4572). El anexo I, sección 1.ª, del reglamento de protección contra incendios tiene la redacción vigente desde el 10/05/2025 (Real Decreto 164/2025, BOE-A-2025-7190) |
| **Extensión** | 11.000 palabras aproximadamente |

<!-- /portada -->

Siglas y unidades que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); sistema de gestión técnica
del edificio, que el enunciado abrevia por su nombre inglés (**BMS**, *building management
system*); control de supervisión y adquisición de datos (**SCADA**, *supervisory control and data
acquisition*); autómata programable (**PLC**, *programmable logic controller*); interfaz entre la
persona y la máquina (**HMI**, *human-machine interface*); control digital directo (**DDC**, *direct
digital control*), que es como la guía del IDAE llama al control computerizado; protocolo de internet (**IP**) y su pila de transporte (**TCP/IP**); modelo de
interconexión de sistemas abiertos (**OSI**); Reglamento de Instalaciones Térmicas en los Edificios
(**RITE**) y sus instrucciones técnicas (**IT**); Reglamento de instalaciones de protección contra
incendios (**RIPCI**) y su equipo de control e indicación, la central de incendios (**e.c.i.**);
Instituto para la Diversificación y Ahorro de la Energía (**IDAE**); Asociación Técnica Española
de Climatización y Refrigeración (**ATECYR**); Federación de Asociaciones de Mantenedores e
Instaladores de Calor y Frío (**AMICYF**); Organización Internacional de Normalización (**ISO**); normas europeas adoptadas por la Asociación Española de
Normalización (**UNE-EN**); Instituto Nacional de Estándares y Tecnología de los Estados Unidos
(**NIST**); calefacción, ventilación, aire acondicionado y refrigeración (**HVAC&R**, del inglés);
sistema de alimentación ininterrumpida (**SAI**); centro de proceso de datos (**CPD**); unidad de
tratamiento de aire (**UTA**); coeficiente de eficiencia frigorífica (**EER**, *energy efficiency
ratio*); y las unidades kilovatio (**kW**), miliamperio (**mA**) y voltio (**V**).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.27, punto 12):
>
> Sistemas de gestión técnica de edificios y monitorización: BMS/SCADA, sensores, alarmas,
> históricos, telemedida y actuación ante avisos.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué es un sistema de automatización y control de edificios según el
RITE, qué edificios deben tenerlo y qué tiene que ser capaz de hacer, qué ventaja da tenerlo en
inspecciones y en mantenimiento, cuáles son sus cuatro niveles, cómo se pone en servicio y quién
mantiene sus programas; qué diferencia un BMS de un SCADA y de un autómata, qué es un protocolo
abierto, qué son BACnet y Modbus y qué tablas de datos usa Modbus; qué es un punto, qué tipos de
punto hay, qué señales se usan en campo y por qué la de 4-20 mA detecta el cable cortado; qué es
una alarma, cómo se prioriza, qué prioridad tiene la protección contra incendios en un sistema
integrado y cada cuánto se prueban las alarmas; qué datos debe registrar el sistema por exigencia
del RITE, cuánto se conservan y qué copias de seguridad se hacen; qué es la telemedida y la
telegestión y qué se comprueba en ellas; y qué hace el técnico ante un aviso. En la aplicación
práctica: qué hacer al llegar por la mañana y ver alarmas en el puesto central, cómo se comprueba
que una sonda dice la verdad, qué pasa si se cae el servidor del puesto central, por qué no basta
con abrir un interruptor que el sistema puede volver a cerrar, o cómo se evita que la gestión
técnica apague la climatización de un plató en pleno directo.

<!-- indice -->

## Índice

- [1. Sistemas de gestión técnica de edificios y monitorización](#1-sistemas-de-gestión-técnica-de-edificios-y-monitorización)
  - [1.1 Qué es un sistema de gestión técnica](#11-qué-es-un-sistema-de-gestión-técnica)
  - [1.2 Para qué se instala](#12-para-qué-se-instala)
  - [1.3 Qué edificios deben tenerlo y qué tiene que hacer: la IT 1.2.4.3.5](#13-qué-edificios-deben-tenerlo-y-qué-tiene-que-hacer-la-it-12435)
  - [1.4 Los cuatro niveles del sistema](#14-los-cuatro-niveles-del-sistema)
  - [1.5 Puesta en servicio y quién mantiene los programas](#15-puesta-en-servicio-y-quién-mantiene-los-programas)
- [2. BMS/SCADA](#2-bmsscada)
  - [2.1 BMS, SCADA y autómata: qué es cada uno](#21-bms-scada-y-autómata-qué-es-cada-uno)
  - [2.2 Los buses de campo y los protocolos](#22-los-buses-de-campo-y-los-protocolos)
  - [2.3 Las estrategias de control que se programan](#23-las-estrategias-de-control-que-se-programan)
  - [2.4 Mantenimiento del puesto central y de los controladores](#24-mantenimiento-del-puesto-central-y-de-los-controladores)
- [3. Sensores](#3-sensores)
  - [3.1 Los puntos: la unidad de cuenta del sistema](#31-los-puntos-la-unidad-de-cuenta-del-sistema)
  - [3.2 Las señales de campo](#32-las-señales-de-campo)
  - [3.3 Que el sensor diga la verdad: contraste y calibración](#33-que-el-sensor-diga-la-verdad-contraste-y-calibración)
- [4. Alarmas](#4-alarmas)
  - [4.1 Qué es una alarma y de dónde sale](#41-qué-es-una-alarma-y-de-dónde-sale)
  - [4.2 Prioridades y notificación](#42-prioridades-y-notificación)
  - [4.3 Reconocer no es resolver](#43-reconocer-no-es-resolver)
  - [4.4 Las alarmas también se mantienen](#44-las-alarmas-también-se-mantienen)
- [5. Históricos](#5-históricos)
  - [5.1 Qué se registra](#51-qué-se-registra)
  - [5.2 Cuánto se conserva y a quién se enseña](#52-cuánto-se-conserva-y-a-quién-se-enseña)
  - [5.3 Para qué sirve un histórico](#53-para-qué-sirve-un-histórico)
  - [5.4 Que el histórico sirva: hora, copia y capacidad](#54-que-el-histórico-sirva-hora-copia-y-capacidad)
- [6. Telemedida](#6-telemedida)
  - [6.1 Telemedida, telemando y telegestión](#61-telemedida-telemando-y-telegestión)
  - [6.2 Lo que hay que comprobar en una telemedida](#62-lo-que-hay-que-comprobar-en-una-telemedida)
- [7. Actuación ante avisos](#7-actuación-ante-avisos)
  - [7.1 Lo que dice la norma](#71-lo-que-dice-la-norma)
  - [7.2 El procedimiento diario del técnico de mantenimiento](#72-el-procedimiento-diario-del-técnico-de-mantenimiento)
  - [7.3 Los pasos ante un aviso](#73-los-pasos-ante-un-aviso)
  - [7.4 Casos del puesto](#74-casos-del-puesto)
  - [7.5 La gestión técnica en una casa que emite](#75-la-gestión-técnica-en-una-casa-que-emite)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Sistemas de gestión técnica de edificios y monitorización

### 1.1 Qué es un sistema de gestión técnica

El RITE lo define en su apéndice 1 con otro nombre, el de sistema de automatización y control de
edificios: «**Sistema de automatización y control de edificios: sistema que incluya todos los
productos, programas informáticos y servicios de ingeniería que puedan apoyar el funcionamiento
eficiente energéticamente, económico y seguro de las instalaciones técnicas del edificio mediante
controles automatizados y facilitando su gestión manual de dichas instalaciones técnicas del
edificio.**»

Tres rasgos de esa definición: no es sólo un equipo, sino también los programas y la ingeniería;
su fin es triple (eficiente, económico y seguro); y no elimina la gestión manual, la facilita.
Monitorizar es la parte de ese sistema que vigila: medir, presentar, registrar y avisar.

Para el RITE el sistema de control es parte de la instalación térmica. Su artículo 2.1 considera
instalaciones térmicas las de climatización y agua caliente sanitaria, «**incluidas las
interconexiones a redes urbanas de calefacción o refrigeración y los sistemas de automatización y
control.**» Consecuencia (lectura de oficio): al control de la climatización se le aplica todo el
reglamento —ejecución, puesta en servicio, mantenimiento e inspección—, y no es un suministro
informático aparte.

Y lo que hay que separar antes de nada, porque el vocabulario del sector los confunde (oficio):

| Sistema | Qué gobierna | Quién lo proyecta |
|---|---|---|
| Gestión técnica de edificios | Climatización, alumbrado, agua, energía, elevación, y la supervisión de las demás | Ingeniería de instalaciones |
| Control industrial de proceso | Una máquina o una línea de producción | Ingeniería de automatización |
| Seguridad y protección contra incendios | Detección, extinción, control de humos | Va aparte y por normativa propia (tema 11) |
| Seguridad física | Control de accesos, intrusión, videovigilancia | Va aparte, con su propia normativa |

La regla de diseño que sale de esa tabla y que un examen podría pedir: el sistema de gestión
supervisa a los otros tres, pero NO los sustituye ni los manda. Una central de incendios no
obedece al sistema de gestión: le informa. Confundir supervisión con mando es el error de
arquitectura más caro del punto.

Para la protección contra incendios esa regla tiene apoyo en norma. El RIPCI exige que la gestión
de la alarma de incendio la controle siempre la central de incendios y, si sus señales pasan a un
sistema integrado, que tengan la prioridad máxima (anexo I, sección 1.ª, apartado 1.7): «**El
sistema de comunicación de la alarma permitirá transmitir señales diferenciadas, que serán
generadas, bien manualmente desde un puesto de control, o bien de forma automática, y su gestión
será controlada, en cualquier caso, por el e.c.i.**» «**Cuando las señales sean transmitidas a un
sistema integrado, los sistemas de protección contra incendios tendrán un nivel de prioridad
máximo.**»

### 1.2 Para qué se instala

Las cuatro razones por las que se instala, que son lo preguntable de la introducción (oficio):

| Razón | Qué aporta |
|---|---|
| Ahorro energético | Ajustar el consumo a la ocupación y a la demanda reales |
| Confort | Mantener condiciones estables sin intervención manual |
| Mantenimiento | Detectar la avería antes de que la note el usuario, y saber qué equipo ha trabajado cuánto |
| Explotación | Operar con menos gente y desde un solo puesto |

La tercera es la que más se infravalora al comprar y la que más se agradece después: un sistema
que registra horas de funcionamiento permite pasar de mantenimiento por calendario a mantenimiento
por condición.

El RITE pide control a toda instalación térmica, tenga o no un sistema centralizado. El artículo
12.3: «**Regulación y control: las instalaciones estarán dotadas de los sistemas de regulación y
control necesarios para que se puedan mantener las condiciones de diseño previstas en los locales
climatizados, ajustando, al mismo tiempo, los consumos de energía a las variaciones de la demanda
térmica, así como interrumpir el servicio.**» Y la IT 1.2.4.3.1, apartado 1, lo repite como
exigencia técnica: «**Todas las instalaciones térmicas estarán dotadas de los sistemas de control
automático necesarios para que se puedan mantener en los locales las condiciones de diseño
previstas, ajustando los consumos de energía a las variaciones de la carga térmica.**» Los
controles locales que eso exige (termostatos, controles todo-nada permitidos, control de agua
caliente sanitaria) son del tema 10; aquí interesa el paso siguiente: reunirlos y vigilarlos desde
un sistema central.

### 1.3 Qué edificios deben tenerlo y qué tiene que hacer: la IT 1.2.4.3.5

La obligación está en la IT 1.2.4.3.5, apartado 1: «**Cuando sea técnica y económicamente viable,
los edificios no residenciales con una potencia nominal útil para instalaciones de calefacción,
refrigeración, instalaciones combinadas de calefacción y ventilación, o para instalaciones
combinadas de refrigeración y ventilación de más de 290 kW deberán estar equipados con sistemas de
automatización y control de edificios.**»

Tres condiciones juntas: edificio no residencial, más de 290 kW en cualquiera de esas
instalaciones, y viabilidad técnica y económica. Con ellas el verbo es «deberán».

Lo que el sistema tiene que ser capaz de hacer, en tres letras:

- «**a) Monitorizar, registrar, analizar y permitir la adaptación del consumo de energía de forma
  continua;**»
- «**b) Efectuar una evaluación comparativa de la eficiencia energética del edificio, detectar las
  pérdidas de eficiencia de sus instalaciones técnicas e informar sobre las posibilidades de mejora
  de la eficiencia energética a la persona responsable de la instalación o de la gestión técnica
  del edificio;**»
- «**c) Permitir la comunicación con instalaciones técnicas conectadas y otros aparatos que estén
  dentro del edificio, así como garantizar la interoperabilidad con instalaciones técnicas del
  edificio de distintos tipos de tecnologías patentadas, dispositivos y fabricantes.**»

Las tres letras recorren el enunciado de este tema: la a) es monitorización e históricos; la b),
alarma de eficiencia e informe; la c), comunicaciones y protocolo abierto (epígrafe 2.2). La norma
de referencia que el RITE nombra: «**Será considerado, a efectos de esta exigencia, la
automatización y el control que tienen un impacto en la eficiencia energética del edificio, como
los recogidos en la norma UNE-EN 15232-1.**» El RITE la lista en su apéndice 2 con la edición de
2018 y el título «**Eficiencia energética de los edificios. Impacto de la automatización, el
control y la gestión de los edificios.**»

Los edificios residenciales no están obligados: el apartado 2 de la IT 1.2.4.3.5 dice que «**podrán**» tener
monitorización electrónica continua y funcionalidades de control.

El apartado 3 fija lo que se hace una vez instalado:

- Adaptarlo al edificio: «**se adaptarán al tamaño o capacidad de la instalación, habida cuenta de
  las necesidades y de las características del edificio en las condiciones de uso previstas**».
- Comprobarlo y ajustarlo en uso real: «**Una vez instalado el sistema de automatización y control,
  será necesario realizar acciones de comprobación de que el sistema funciona con arreglo a sus
  especificaciones y acciones de ajuste, en su caso, en la instalación en condiciones de uso
  real.**»
- Configurarlo para el mínimo consumo: debe operar las instalaciones con las condiciones de
  bienestar e higiene del artículo 11 «**con el mínimo consumo de energía**», teniendo en cuenta
  «**los periodos de inactividad del edificio, el uso de los espacios, los regímenes de operación en
  el punto de máximo rendimiento de los equipos y el máximo aprovechamiento de las energías
  renovables y residuales disponibles**».
- Documentarlo: «**Las indicaciones e instrucciones para la correcta operación del sistema de
  automatización y control deberán recogerse en el ‘‘Manual de Uso y Mantenimiento’’.**»

Dos ventajas reglamentarias de tenerlo:

1. Exención de inspecciones periódicas de eficiencia. IT 4.3.4: «**Los edificios no
   residenciales que cuenten con un sistema de automatización y control que cumpla los requisitos
   establecidos en el apartado 1 de la IT 1.2.4.3.5, así como los edificios residenciales que
   cuenten con un sistema de automatización y control que cumpla los requisitos establecidos en el
   apartado 2 de la IT 1.2.4.3.5, quedarán exentos del cumplimiento de los requisitos establecidos
   en la IT 4.2.1, IT 4.2.2 y IT 4.2.3.**» Es decir, de las inspecciones de calefacción, de aire
   acondicionado y de la instalación completa (tema 10). El sistema tiene que cumplir las tres
   capacidades de verdad: uno que sólo arranca y para equipos no basta (lectura de oficio).
2. Mantenimiento menos frecuente en instalaciones pequeñas vigiladas. IT 3.3, al pie de la
   tabla 3.1: «**En instalaciones de potencia útil nominal hasta 70 kW, con supervisión remota en
   continuo, la periodicidad se puede incrementar hasta 2 años, siempre que estén garantizadas las
   condiciones de seguridad y eficiencia energética.**»

### 1.4 Los cuatro niveles del sistema

El RITE ordena el sistema en cuatro niveles. La IT 2.3.4, apartado 2, manda seguir su ajuste
«**en base a los niveles del proceso siguientes: nivel de unidades de campo, nivel de proceso, nivel
de comunicaciones, nivel de gestión y telegestión.**» Y el apéndice 1 define cada uno:

| Nivel | Definición del RITE (apéndice 1) | Ejemplos de oficio |
|---|---|---|
| Unidades de campo | «**corresponde a los equipos de campo como: elementos primarios de medida, sondas, unidades de ambiente, termostatos, indicadores de estados y alarmas, así como elementos finales de control y mando, válvulas, actuadores, variadores de tensión/frecuencia, elementos finales de control, etc.**» | Sonda de temperatura de impulsión, presostato, contacto auxiliar de un interruptor, servomotor de compuerta |
| Proceso | «**corresponde a los controladores, tanto analógicos como digitales, que manejan los elementos del nivel de periferia.**» | Controlador DDC de una UTA, autómata de la sala de calderas |
| Comunicaciones | «**corresponde a todos los controladores e interfaces de comunicación del sistema de gestión, así como a los buses de comunicación, drivers, redes, etc.**» | Bus de campo, pasarela entre protocolos, conmutador de red |
| Gestión y telegestión | «**corresponde a los puestos centrales, programas residentes y periféricos asociados a los puestos centrales, tales como impresoras, pantallas de vídeo, módems, routers, etc.**» | Puesto de operación con sinópticos, servidor de históricos, acceso remoto |

La ingeniería de control usa un modelo equivalente, la pirámide de automatización, con nombres
distintos (oficio). Cuatro niveles, y cada uno con su equipo, su tiempo de respuesta y su tipo de
dato:

| Nivel | Qué hay | Tiempo de respuesta | Qué maneja |
|---|---|---|---|
| De campo | Sensores y actuadores | Milisegundos | La magnitud física |
| De control | Autómatas programables y controladores | Decenas de milisegundos | La lógica y los lazos |
| De supervisión | Puestos de operación, sinópticos | Segundos | El estado y la orden del operador |
| De gestión | Informes, históricos, gestión energética | Horas o días | La tendencia y el coste |

La correspondencia: campo es campo; control es el nivel de proceso del RITE; supervisión y gestión
caen en el nivel de gestión y telegestión del RITE; y el nivel de comunicaciones del RITE, que la
pirámide no dibuja como piso, es lo que une a los demás. En un examen sobre normativa española,
los nombres que valen son los del RITE.

La regla que ordena la pirámide y que hay que saber enunciar: cuanto más abajo, más rápido y más
concreto; cuanto más arriba, más lento y más agregado. Un lazo de temperatura se cierra en el nivel
de control, no en el de gestión, y un sistema que suba cada lectura al nivel de gestión para
decidir se cae solo.

Y el principio de autonomía, que es el que decide si una instalación aguanta un fallo: cada nivel
debe seguir funcionando si el de arriba desaparece. Un autómata sin supervisión sigue regulando;
una válvula con posicionador local sigue en su última consigna. Ésa es la diferencia entre un
sistema robusto y uno que deja el edificio a oscuras cuando cae un servidor.

### 1.5 Puesta en servicio y quién mantiene los programas

La IT 2.3.4, «Control automático», es la prueba de la empresa instaladora antes de entregar:

1. «**Se ajustarán los parámetros del sistema de control automático a los valores de diseño
   especificados en el proyecto o memoria técnica y se comprobará el funcionamiento de los
   componentes que configuran el sistema de control.**»
2. El seguimiento, por los cuatro niveles del epígrafe 1.4.
3. «**Los niveles de proceso serán verificados para constatar su adaptación a la aplicación, de
   acuerdo con la base de datos especificados en el proyecto o memoria técnica. Son válidos a estos
   efectos los protocolos establecidos en la norma UNE-EN-ISO 16484-3.**» El apéndice 2 del RITE
   la titula «**Sistemas de automatización y control de edificios (BACS). Parte 3: Funciones (ISO
   16484-3:2005).**»
4. «**Cuando la instalación disponga de un sistema de control, mando y gestión o telegestión basado
   en la tecnología de la información, su mantenimiento y la actualización de las versiones de los
   programas deberá ser realizado por personal cualificado o por el mismo suministrador de los
   programas.**»

El apartado 4 importa al puesto: el electricista mantiene el campo (sondas, actuadores, cableado,
cuadros de control, alimentaciones), pero cambiar la programación o actualizar el programa del
puesto central es tarea de personal cualificado para ello o del suministrador. Tocar una lógica
sin esa cualificación, aunque se tenga la contraseña, es salirse de la norma (lectura de oficio).

## 2. BMS/SCADA

### 2.1 BMS, SCADA y autómata: qué es cada uno

Ninguna norma española leída define el SCADA ni el BMS con esos nombres. El NIST, en su guía de
seguridad de sistemas de control industrial (SP 800-82, revisión 3), recoge esta definición de SCADA: «**A
generic name for a computerized system that is capable of gathering and processing data and
applying operational controls over long distances. Typical uses include power transmission and
distribution and pipeline systems.**» (Un nombre genérico para un sistema informático capaz de
recoger y procesar datos y de aplicar mandos de operación a grandes distancias; sus usos típicos
son el transporte y la distribución de electricidad y los oleoductos y gasoductos.) Y añade que
está pensado para comunicaciones con retardos y problemas de integridad de datos («**delays, data
integrity**») por líneas telefónicas, microondas o satélite.

La distinción práctica (oficio):

| | BMS | SCADA | Autómata (PLC) o controlador DDC |
|---|---|---|---|
| Qué es | El sistema de gestión técnica de un edificio o complejo | Un programa de supervisión y adquisición de datos, nacido para instalaciones dispersas | El equipo que ejecuta la lógica y cierra los lazos |
| Nivel del RITE | Todos, con el puesto central en gestión y telegestión | Gestión y telegestión | Proceso |
| Dónde se ve en una casa que emite | Climatización, alumbrado, contadores, cuadros de los edificios | Red de centros emisores y reemisores, subestaciones, redes de energía | Sala de calderas, UTA, cuadro de transferencia del grupo |
| Qué pasa si falta | Se pierde la vista de conjunto y los históricos | Se pierde la vista remota | Se pierde la regulación de ese equipo |

En la práctica las palabras se mezclan: muchos BMS usan un programa SCADA como interfaz del puesto
central, y muchos SCADA se usan en edificios. Por eso el enunciado los escribe juntos, BMS/SCADA.
Lo que no se mezcla es la función: el SCADA y el puesto central supervisan y ordenan; el autómata
regula. La interfaz con la persona (HMI) puede estar en el puesto central o en una pantalla local
del cuadro.

El puesto central se compone, en la guía técnica de mantenimiento del IDAE (familia 23, «Control
DDC (Computerizado)»), de ordenador central con discos, «**pantallas, teclados, impresoras y
periféricos**», alimentado por SAI (operación 63), conectado por «**buses de comunicación**» a los
«**controladores distribuidos microprocesados**», a los «**controladores de unidades terminales**» y
a las «**integraciones**» con otros sistemas. Ese índice es el de su gama de mantenimiento, que se
reparte por los epígrafes siguientes.

### 2.2 Los buses de campo y los protocolos

Lo que hay que saber decidir es si el sistema será ABIERTO o PROPIETARIO, y la decisión se toma
en el pliego, no después (oficio).

| Enfoque | Qué da | Qué cuesta |
|---|---|---|
| Protocolo abierto | Varios fabricantes pueden ampliar y mantener | Integración más trabajosa |
| Protocolo propietario | Integración perfecta y rápida | Dependencia de un solo suministrador para toda la vida de la instalación |

En los edificios no residenciales obligados a tener sistema (epígrafe 1.3), el RITE inclina la
balanza: la letra c) del apartado 1 de la IT 1.2.4.3.5 exige «**garantizar la interoperabilidad con
instalaciones técnicas del edificio de distintos tipos de tecnologías patentadas, dispositivos y
fabricantes.**»

Los grandes grupos de protocolos, sin entrar en producto (oficio):

| Grupo | Dónde se usa |
|---|---|
| Buses de campo de automatización de edificios | Climatización, alumbrado, persianas |
| Buses de campo industriales | Proceso, máquina, variadores |
| Protocolos sobre red de datos | Supervisión, integración entre sistemas, acceso remoto |
| Protocolos de instalación eléctrica | Contadores, analizadores de red, cuadros |

Tres protocolos con nombre que un electricista encuentra, con lo que de ellos se ha podido leer en
su fuente:

**BACnet.** Es la norma ISO 16484-5, «**Building automation and control systems (BACS) — Part 5:
Data communication protocol**», cuya edición vigente es la octava, de agosto de 2026 (ISO
16484-5:2026; como norma europea, EN ISO 16484-5:2026, que sustituye a la de 2022). Su objeto:
«**to define data communication services and protocols for computer equipment used for monitoring
and control of HVAC&R and other building systems and to define, in addition, an abstract,
object-oriented representation of information communicated between such equipment**» (definir
servicios y protocolos de comunicación de datos para los equipos informáticos de supervisión y
control de climatización, refrigeración y otros sistemas del edificio, y una representación
abstracta, orientada a objetos, de la información que intercambian). Cada equipo se modela como un
conjunto de objetos: el índice de la norma trae, entre otros, los tipos «**Analog Input**»,
«**Analog Output**», «**Analog Value**», «**Binary Input**», «**Binary Output**», «**Binary
Value**», «**Schedule**» (horario), «**Calendar**», «**Notification Class**» (clase de
notificación), «**Trend Log**» (registro de tendencias) y «**Event Log**». Tiene un
capítulo de servicios de alarma y evento («**ALARM AND EVENT SERVICES**», con el servicio
«**AcknowledgeAlarm**» de reconocimiento de alarma), una red serie propia, en bus multipunto con
paso de testigo («**MULTIDROP SERIAL BUS/TOKEN PASSING (MS/TP) LAN**») y su transporte sobre red
IP («**BACnet/IP**», anexo J; «**BACnet/IPv6**», anexo U).

**Modbus.** La especificación de la organización Modbus (versión V1.1b3, de 26 de abril de 2012)
lo define así: «**MODBUS is an application layer messaging protocol, positioned at level 7 of the
OSI model, which provides client/server communication between devices connected on different types
of buses or networks.**» (Protocolo de mensajería de capa de aplicación, nivel 7 del modelo OSI,
para comunicación cliente/servidor entre equipos conectados a distintos buses o redes.) Funciona
por pregunta y respuesta: «**MODBUS is a request/reply protocol and offers services specified by
function codes.**» Se implementa sobre TCP/IP por Ethernet, con el puerto reservado «**port 502**»,
y por transmisión serie asíncrona por cable, fibra o radio. Sus datos se ordenan en
cuatro tablas primarias:

| Tabla | Tipo | Acceso |
|---|---|---|
| «**Discretes Input**» (entradas discretas) | «**Single bit**» | «**Read-Only**» (sólo lectura) |
| «**Coils**» (bobinas) | «**Single bit**» | «**Read-Write**» (lectura y escritura) |
| «**Input Registers**» (registros de entrada) | «**16-bit word**» | «**Read-Only**» |
| «**Holding Registers**» (registros de retención) | «**16-bit word**» | «**Read-Write**» |

Es un protocolo frecuente en analizadores de red, contadores, SAI y grupos
electrógenos que se integran en el sistema de gestión (oficio): las magnitudes medidas se leen en
registros de entrada o de retención, y las órdenes se escriben en bobinas o en registros de
retención.

**KNX.** Su asociación lo presenta como «**an internationally recognised standard, not owned by a
single brand**» que conecta «**lighting, heating, blinds, security and energy management**»
(alumbrado, calefacción, persianas, seguridad y gestión de energía). Se usa sobre todo en el
mando de alumbrado y persianas de oficinas (oficio). El número de la norma internacional que lo
recoge no se ha confirmado en fuente primaria y este tema no lo da.

La tendencia que ordena los cuatro grupos (oficio): lo que antes era un bus dedicado hoy viaja
sobre red de datos. Es el mismo movimiento que ha seguido la señal de vídeo en las instalaciones
de televisión, y trae los mismos problemas: separación de redes, direccionamiento y seguridad.

El aviso de seguridad, que es la contrapartida de esa tendencia: un sistema de gestión técnica en
la misma red que la ofimática es una puerta al edificio. Los cuadros, las calderas y los grupos
de frío quedan a un clic de quien abra un correo con adjunto malicioso. La separación de redes no
es una comodidad de red: es una medida de seguridad física.

### 2.3 Las estrategias de control que se programan

Ésta es la parte que un examen puede pedir enumerada, y es lo que de verdad ahorra energía
(oficio):

| Estrategia | Qué hace |
|---|---|
| Programación horaria | Arrancar y parar por calendario, con festivos y excepciones |
| Arranque óptimo | Calcular a qué hora hay que arrancar para llegar a consigna justo a la de ocupación, aprendiendo de los días anteriores |
| Parada óptima | Parar antes del final de la jornada aprovechando la inercia del edificio |
| Enfriamiento gratuito | Usar aire exterior cuando sus condiciones son mejores que las de recirculación |
| Compensación por temperatura exterior | Mover la consigna de impulsión según la exterior, en vez de mantenerla fija |
| Control por ocupación | Regular caudal, alumbrado y consigna por presencia real |
| Limitación de potencia | Escalonar arranques para no superar la potencia contratada |
| Rotación de equipos | Igualar horas de funcionamiento entre bombas o enfriadoras redundantes |

Las dos primeras se confunden y no son lo mismo: la programación horaria arranca a una hora fija;
el arranque óptimo calcula esa hora cada día.

Varias de esas estrategias tienen apoyo en el RITE. El enfriamiento gratuito es obligatorio en
ciertos sistemas (IT 1.2.4.5.1): «**Los subsistemas de climatización del tipo todo aire, de
potencia útil nominal mayor que 70 kW en régimen de refrigeración, dispondrán de un subsistema de
enfriamiento gratuito por aire exterior.**» (La misma IT, en su apartado 5, admite justificar el
incumplimiento de alguno de sus aspectos por la dificultad de lograrlo.) Y el programa de funcionamiento de las instalaciones
de más de 70 kW (IT 3.7) comprende, entre otros, el «**horario de puesta en marcha y parada de la
instalación**», el «**orden de puesta en marcha y parada de los equipos**» y el «**programa y
régimen especial para los fines de semana y para condiciones especiales de uso del edificio o de
condiciones exteriores excepcionales**»: es lo que se carga en los horarios del sistema. Las
instrucciones de manejo y maniobra de esas instalaciones (IT 3.6) piden atender la «**limitación de
puntas de potencia eléctrica, evitando poner en marcha simultáneamente varios motores a plena
carga**», que es la limitación de potencia de la tabla.

La limitación de potencia evita una penalización en factura, y la rotación de equipos evita que la
bomba de reserva sea la que nunca ha girado y se gripe el día que hace falta (oficio).

El lazo de control clásico, con sus tres acciones, que hay que saber nombrar (oficio):

| Acción | Qué corrige |
|---|---|
| Proporcional | El error presente: cuanto mayor la desviación, mayor la corrección |
| Integral | El error acumulado: elimina la desviación permanente |
| Derivativa | La velocidad del error: anticipa y frena la oscilación |

El aviso de ajuste que se aprende en obra: en climatización la acción derivativa se usa poco y
suele desconectarse, porque las inercias térmicas son lentas y el ruido de la sonda la hace
oscilar. La mayoría de los lazos de un edificio son proporcional más integral.

### 2.4 Mantenimiento del puesto central y de los controladores

La guía del IDAE propone, para el control computerizado, una gama de mantenimiento con frecuencias
recomendadas (no obligatorias: el capítulo se titula «Programas genéricos de actuaciones y
frecuencias recomendadas»). Las claves de frecuencia de la guía: M mensual, T trimestral, 2.A dos
veces al año o dos veces por temporada, A anual. Lo que toca al puesto central y a los controladores (lo de
alarmas, históricos y telegestión va en los epígrafes 4, 5 y 6):

| Nº | Operación (literal de la guía) | Frecuencia |
|---|---|---|
| 50 | «**Comprobación del estado de cables de alimentación eléctrica y buses de comunicación y sus conexiones**» | T |
| 55 | «**Comprobación de las comunicaciones con los controladores periféricos**» | T |
| 62 | «**Comprobación del arranque del puesto central de gestión tras un fallo del suministro de tensión**» | 2.A |
| 63 | «**Verificación de funcionamiento de los Sistemas de Alimentación Ininterrumpida (SAI)**» | 2.A |
| 64 | «**Evaluación de la obsolescencia del hardware instalado, sistema operativo y software de aplicación**» | A |
| 66 | «**Verificación del estado de los cuadros de control. Limpieza interior, apriete de conexiones y protección antihumedad**» | A |
| 68 | «**Verificación general de estado de la instalación eléctrica. Comprobación de aislamientos y conexiones**» | T |
| 71 | «**Comprobación de tensiones de alimentación de a lazos de regulación y elementos actuadores**» | T |
| 72 | «**Inspección del estado y conexionado de los “buses” de comunicación**» | T |
| 73 | «**Verificación de estado y carga de las baterías de los controladores**» | T |
| 78 | «**Comprobación de la respuesta de los elementos de campo a los comandos de los controladores**» | T |
| 80 | «**Inspección de la estabilidad y precisión de los bucles de control, secuencias y horarios**» | 2.A |
| 83 | «**Realizar un backup general de la programación. Puesta al día y salvaguarda de la base de datos**» | T |
| 97 | «**Verificación de reglajes y valores de consigna. Ajuste y calibración de elementos de regulación**» | 2.A |

Lo eléctrico de esa lista (alimentaciones, SAI del puesto central, cuadros de control, buses,
baterías de los controladores, aislamientos) es lo que hace el electricista; la programación y las
copias de la base de datos, el personal cualificado del apartado 4 de la IT 2.3.4 (oficio). La operación 62 es
la prueba del principio de autonomía del epígrafe 1.4 vista desde arriba: tras un corte, el puesto
central tiene que volver solo, y entretanto los controladores tienen que haber seguido regulando.

## 3. Sensores

### 3.1 Los puntos: la unidad de cuenta del sistema

El «punto» es la unidad de cuenta de un sistema de gestión técnica, y es con lo que se presupuesta
(oficio). Las cuatro clases básicas:

| Tipo de punto | Qué es | Ejemplos |
|---|---|---|
| Entrada digital | Un contacto: abierto o cerrado | Estado de marcha, alarma, posición de un interruptor |
| Salida digital | Una orden de todo o nada | Arranque de bomba, mando de contactor |
| Entrada analógica | Una magnitud continua medida | Temperatura, presión, caudal, consumo |
| Salida analógica | Una consigna continua | Apertura de válvula, velocidad de variador |

La guía del IDAE recomienda que la ficha técnica de cada sistema de regulación y control recoja
«**la información relativa a las lógicas de control establecidas, listado de componentes de los
sistemas de regulación y control sujetos a mantenimiento y, como mínimo, de la relación de puntos
de control a supervisar**», y su ejemplo de listado clasifica los puntos en seis columnas, dos más
que las cuatro clases básicas:

- «**ED = Entrada Digital**»
- «**SD = Salida Digital**»
- «**SS = Salida de Supervisión**»
- «**EA = Entrada Analógica**»
- «**SA = Salida Analógica**»
- «**CT = Contador**»

El contador es una entrada que acumula impulsos (de un contador de energía, de agua o de gas), y
por eso se cuenta aparte (oficio). La misma ficha clasifica el tipo de sistema de control como
«**neumática, electromecánica, electrónica, DDC**».

Ejemplos literales de puntos del listado del IDAE, que dan la idea de qué se vigila en una
instalación térmica: «**Comando marcha/paro planta enfriadora GEA1**»; «**Estado/alarma general
planta enfriadora GEA1**»; «**Señal falta de presión/agua en circuito primario agua fría**»;
«**Señal temperatura de impulsión de agua fría**»; «**Comando regulación válvulas automáticas agua
fría**»; «**Fines de carrera válvulas automáticas agua fría**»; «**Alarma por filtros sucios**»;
«**Posición fines de carrera de compuertas cortafuegos**»; «**Contador general de energía
eléctrica**»; «**Contador de suministro de energía eléctrica a climatización**»; y, en el apartado
«Varios», uno muy del puesto: «**Alarma alta temperatura en sala de informática**».

Lo que un electricista conecta al sistema de gestión en un edificio audiovisual, además de la
climatización (oficio):

| Instalación | Puntos típicos |
|---|---|
| Cuadros generales y secundarios | Estado y disparo de interruptores (contacto auxiliar y de señalización de defecto), disparo de diferenciales, protección contra sobretensiones fuera de servicio |
| Medida | Analizadores de red y contadores de energía por línea: tensiones, intensidades, potencias, factor de potencia, energía (tema 14) |
| Grupo electrógeno | En marcha, en carga, avería, nivel de combustible, posición del conmutador de transferencia (tema 7) |
| SAI | En red, en batería, en bypass, batería baja, alarma general (tema 7) |
| Salas técnicas y CPD | Temperatura y humedad ambiente, fuga de agua, puerta abierta, estado de la climatización de precisión (temas 8 y 9) |
| Alumbrado | Mando de circuitos por horario o por nivel de luz, estado del alumbrado de emergencia si su sistema lo permite (tema 6) |
| Incendios | Alarma y avería de la central, sólo como señal recibida (epígrafe 1.1; tema 11) |

La regla de dimensionado que evita el error de proyecto más frecuente: el número de puntos se
cierra al final y siempre crece. Se deja reserva de puntos en cada controlador y de espacio en
cada cuadro (oficio).

### 3.2 Las señales de campo

Las señales que se encuentran en obra (oficio):

| Señal | Rango | Rasgo |
|---|---|---|
| Corriente | 4-20 miliamperios | El cero está en 4: si llega 0, el lazo está roto y se sabe |
| Tensión | 0-10 voltios | Más barata y más sensible a la caída en el cable |
| Resistiva | Sondas de resistencia | Para temperatura; la longitud del cable falsea la lectura |
| Contacto libre de tensión | Abierto o cerrado | La más robusta de todas |

La ventaja del rango 4-20 es el dato de oficio más útil de este epígrafe: al no empezar en cero, un
cable cortado da una lectura imposible y el sistema lo detecta. En 0-10 voltios, un cable cortado
se lee como «cero grados» y nadie se entera.

Y además de las señales cableadas, la lectura por bus: un analizador de red o un SAI con puerto de
comunicaciones entrega decenas de magnitudes por un solo par de hilos o un cable de red, en vez de
un cable por punto (oficio). El precio es que, si se cae la comunicación, se pierden todas a la
vez; por eso el fallo de comunicación es en sí mismo una alarma (epígrafe 4.1).

Precauciones de cableado (oficio): las señales analógicas van en cable apantallado, con la pantalla
puesta a tierra como indique el fabricante del equipo, y separadas de los cables de potencia para no recoger
interferencias (la compatibilidad electromagnética es del tema 8); los contactos que el sistema
lee deben ser libres de tensión, o el sistema recibe la tensión de otro circuito; y cada punto se
identifica en las dos puntas con la misma referencia que en el listado de puntos y en el sinóptico.

### 3.3 Que el sensor diga la verdad: contraste y calibración

Un sensor que mide mal es peor que uno que no mide, porque el sistema decide con él (oficio). La
guía del IDAE incluye en su gama del control computerizado:

| Nº | Operación (literal de la guía) | Frecuencia |
|---|---|---|
| 37 | «**Verificación de estado y actuación de sensores y controles de temperatura y termostatos**» | 2.A |
| 39 | «**Verificación de estado y actuación de controles de humedad, sondas y humidostatos**» | 2.A |
| 42 | «**Comprobación de entradas analógicas y digitales en módulos y centralitas. Conexiones y señales**» | 2.A |
| 76 | «**Inspección de lecturas de elementos de campo y ajuste de elementos fuera de rango**» | T |
| 77 | «**Contraste de las lecturas obtenidas de los controladores con reales tomadas directamente en campo**» | T |
| 85 | «**Comprobación de rangos de señal de sensores y corrección de desviaciones. Verificación de respuesta de los reguladores**» | T |
| 92 | «**Comprobación de los valores reales en los equipos (en campo) con los presentados en el puesto de control**» | T |

(La 37, la 39 y la 42 son, en la guía, del «Control por autómata electrónico» de la misma familia
23; la 76, la 77, la 85 y la 92, del control computerizado. La guía numera dos operaciones con el
85.)

Cómo se hace el contraste (oficio): se mide la magnitud en campo con un instrumento propio,
calibrado y de mejor precisión que la sonda (termómetro de contacto o de ambiente, higrómetro,
pinza amperimétrica o analizador para las magnitudes eléctricas, tema 14), en el mismo punto y al
mismo tiempo que se lee el valor en el puesto central; si la diferencia supera la tolerancia de la
sonda se busca la causa por este orden: sonda mal situada (al sol, junto a una impulsión, en un
rincón sin aire), cableado y conexiones, escalado mal configurado en el controlador, y por último
la propia sonda. Y la prueba al revés para las salidas: se manda una orden desde el puesto y se
comprueba en campo que la válvula, la compuerta o el contactor responden (operación 78 del
epígrafe 2.4).

## 4. Alarmas

### 4.1 Qué es una alarma y de dónde sale

Una alarma es un aviso que el sistema genera cuando un punto entra en un estado que pide atención,
y que queda registrado hasta que alguien lo reconoce (oficio). Sale de cuatro sitios:

| Origen | Cómo se produce | Ejemplo |
|---|---|---|
| Alarma de equipo | El propio equipo la da por un contacto o por bus | «Estado/alarma general» de una enfriadora; SAI en batería; disparo de un interruptor |
| Alarma por umbral | El sistema compara una medida con un límite | Temperatura de sala técnica por encima del máximo; humedad fuera de margen |
| Alarma por discrepancia | La orden y el estado no coinciden pasado un tiempo | Se manda arrancar una bomba y su contacto de marcha no llega |
| Alarma del propio sistema | Falla la comunicación, la alimentación o la señal | Controlador sin comunicación; sonda 4-20 con lectura imposible (epígrafe 3.2) |

Dos ajustes evitan las falsas alarmas (oficio): la histéresis (la alarma salta en un valor y se
repone en otro algo más bajo, para que no se dispare y repongan sin parar alrededor del límite) y
el retardo (la condición tiene que durar un tiempo antes de avisar, para que un arranque o un pico
breve no generen aviso). La alarma por discrepancia sólo existe si el punto tiene a la vez orden y
estado: un «comando marcha/paro» sin su «estado/alarma» deja al sistema mandando a ciegas.

En la exigencia de eficiencia del RITE, la alarma va más allá del fallo: la letra b) del apartado 1 de la IT 1.2.4.3.5 pide que el sistema sepa «**detectar las pérdidas de eficiencia de sus instalaciones
técnicas e informar sobre las posibilidades de mejora**». Una enfriadora que funciona pero con un
EER que cae, o un consumo nocturno que crece, son avisos aunque ningún equipo esté averiado
(lectura de oficio).

### 4.2 Prioridades y notificación

Las alarmas se ordenan por prioridad, porque no todas piden lo mismo (oficio):

| Prioridad | Qué es | Respuesta |
|---|---|---|
| Crítica | Afecta a la seguridad de personas o a la continuidad de la emisión | Inmediata, con aviso fuera del horario de presencia |
| Alta | Pérdida de redundancia o equipo esencial averiado con reserva en marcha | En el turno |
| Media | Desviación de condiciones o de eficiencia | Programada |
| Baja o informativa | Mantenimiento por horas, filtro sucio, aviso de fin de vida | Con el preventivo |

Una alarma que no cambia nada se vuelve ruido: cuando el puesto central muestra cientos de avisos
permanentes nadie ve el importante. Se revisan y se depuran las alarmas que no piden ninguna
acción, y cada alarma activa debe tener dicho quién la atiende y qué hace (oficio).

Por encima de todas está la protección contra incendios: si sus señales llegan a un sistema
integrado, el RIPCI exige para ellas un «**nivel de prioridad máximo**» (epígrafe 1.1), y su
gestión sigue en la central de incendios.

La notificación, en el sistema: aviso en pantalla y en el registro del puesto central, impresión,
y reenvío fuera del edificio a otros terminales (correo, mensaje al móvil del retén o al centro de
control) para las que no pueden esperar al día siguiente (oficio). BACnet tiene para ello un tipo de objeto propio, la clase de notificación («**Notification
Class**»), y un capítulo de servicios de alarma y evento (epígrafe 2.2).

### 4.3 Reconocer no es resolver

El ciclo de una alarma tiene tres momentos distintos que el sistema registra por separado
(oficio): aparece (fecha y hora de la activación), se reconoce (alguien dice que la ha visto) y
desaparece (la condición vuelve a lo normal). Reconocer una alarma no la resuelve: sólo deja
constancia de que alguien se ha hecho cargo. Y una alarma que desaparece sola no está resuelta si
no se sabe por qué apareció; si se repite, es una avería intermitente.

El servicio «**AcknowledgeAlarm**» de BACnet (epígrafe 2.2) es ese reconocimiento hecho protocolo.

Ningún dispositivo de seguridad se rearma desde el puesto central si la norma no lo permite. El apartado 3 de la IT 1.2.4.3.1 del RITE: «**El rearme automático de los dispositivos de seguridad sólo se permitirá
cuando se indique expresamente en estas Instrucciones técnicas.**» El rearme remoto de un equipo
que ha parado por su seguridad sin saber por qué ha parado es repetir la causa (oficio).

### 4.4 Las alarmas también se mantienen

La guía del IDAE pone la gama de alarmas del control computerizado con frecuencia mensual, la más
alta de toda la gama:

| Nº | Operación (literal de la guía) | Frecuencia |
|---|---|---|
| 86 | «**Inspección del estado de los elementos emisores y receptores de alarmas**» | M |
| 87 | «**Simulación de alarmas y comprobación de su notificación sobre los terminales o impresoras predefinidas**» | M |
| 88 | «**Comprobación de la notificación remota de alarmas a impresoras u otros terminales**» | M |
| 82 | «**Inspección y análisis de mensajes de alarmas y defectos de funcionamiento**» | T |

La simulación (operación 87) es la única forma de saber que una alarma llega antes de que haga
falta: se provoca la condición en campo (se abre el contacto, se calienta la sonda, se corta la
comunicación de un controlador) y se comprueba que el aviso aparece donde debe y llega a quien debe
(oficio). Una alarma de temperatura de CPD que nunca se ha probado no se sabe si funciona.

## 5. Históricos

### 5.1 Qué se registra

Un histórico es la serie de valores de un punto guardada con su fecha y hora (tendencia), más el
registro de eventos: alarmas, órdenes de operador, cambios de consigna y de programa, y quién los
hizo (oficio). En BACnet son los objetos «**Trend Log**» y «**Event Log**» (epígrafe 2.2).

El RITE obliga a registrar ciertos datos, tenga o no el edificio un sistema centralizado. El
sistema de gestión es el sitio natural donde se reúnen (lectura de oficio). IT 1.2.4.4:

- Apartado 2: las instalaciones de más de 70 kW «**dispondrán de dispositivos que permitan efectuar
  la medición y registrar el consumo de combustible y energía eléctrica, de forma separada del
  consumo debido a otros usos del resto del edificio.**»
- Apartado 3: medición de la energía térmica en centrales de más de 70 kW; el dispositivo «**se
  podrá emplear también para modular la producción de energía térmica en función de la
  demanda.**»
- Apartado 4: en refrigeración de más de 70 kW, medir y registrar el consumo eléctrico de la
  central frigorífica «**de forma diferenciada**» del resto de equipos del sistema.
- Apartado 5: «**Los generadores de calor y de frío de potencia útil nominal mayor que 70 kW
  dispondrán de un dispositivo que permita registrar el número de horas de funcionamiento del
  generador.**»
- Apartado 6: «**Las bombas y ventiladores de potencia eléctrica del motor mayor que 20 kW
  dispondrán de un dispositivo que permita registrar las horas de funcionamiento del equipo.**»
- Apartado 7: «**Los compresores frigoríficos de más de 70 kW de potencia útil nominal dispondrán
  de un dispositivo que permita registrar el número de arrancadas del mismo.**»

Las medidas periódicas de los generadores de frío de más de 70 kW (IT 3.4.2, tabla 3.3) son otra
lista de lo que conviene tener en histórico: temperaturas del fluido en entrada y salida del
evaporador y del condensador, pérdidas de presión en evaporador y condensador en las plantas enfriadas por agua, temperatura y presión de evaporación y de
condensación, «**Potencia eléctrica absorbida**», «**Potencia térmica instantánea del generador,
como porcentaje de la carga máxima**», «**EER instantáneo**» y caudales de agua en evaporador y
condensador. La tabla fija la periodicidad: cada tres meses entre 70 y 1.000 kW, y mensual por
encima de 1.000 kW, en los dos casos con la primera medida al inicio de la temporada.

### 5.2 Cuánto se conserva y a quién se enseña

- IT 3.4.4, apartado 2: en instalaciones de más de 70 kW, la empresa mantenedora sigue la evolución del
  consumo y de la energía aportada, desglosada por uso, «**con el fin de poder detectar posibles
  desviaciones y tomar las medidas correctoras oportunas. Esta información se conservará por un
  plazo de, al menos, cinco años y deberá entregarse al propietario del edificio e incorporarse al
  ‘‘Libro del Edificio’’.**»
- IT 3.4.5: esa evolución «**será puesta a disposición de los usuarios y titulares del edificio con
  una periodicidad anual e incluirá el consumo de la energía registrada en los últimos 5 años.**»
  Esa información estará disponible en un sitio visible y frecuentado por quienes usan el recinto, y su
  publicidad es obligatoria en los recintos destinados a los usos del «**apartado 2 de la I.T.
  3.8.1.2**» (así lo escribe el RITE) cuya superficie sea superior a 1.000 m² (tema 10).

### 5.3 Para qué sirve un histórico

Cuatro usos (oficio):

1. Diagnóstico de averías: ver qué pasó antes de la alarma (qué subió primero, qué orden se dio,
   a qué hora cayó la comunicación). Una avería sin histórico se diagnostica por suposición.
2. Mantenimiento por condición: las horas de funcionamiento y el número de arranques deciden
   cuándo toca la revisión, y la tendencia de una magnitud (consumo de un motor, salto térmico de
   una batería, presión diferencial de un filtro) avisa del desgaste antes del fallo. Es el puente
   con el mantenimiento predictivo del tema 13.
3. Eficiencia: comparar consumos con el año anterior y con la ocupación; detectar consumos
   fuera de horario (letra b del apartado 1 de la IT 1.2.4.3.5).
4. Prueba: demostrar que una sala técnica estuvo dentro de sus condiciones, o cuándo dejó de
   estarlo.

La guía del IDAE recomienda, al cumplimentar las fichas, anotar los datos nominales de diseño,
porque «**La comparación entre los datos nominales y los actuales obtenidos en cada toma de datos
periódica hará posible la detección de desviaciones y sus tendencias y permitirá plantear medidas
para corregir las causas que las originan**».

### 5.4 Que el histórico sirva: hora, copia y capacidad

Un histórico con la hora equivocada no sirve para reconstruir una avería, y uno que se ha perdido
tampoco. La gama del IDAE:

| Nº | Operación (literal de la guía) | Frecuencia |
|---|---|---|
| 53 | «**Verificación de la fecha y la hora**» | T |
| 54 | «**Verificación del cambio de horario invierno/verano**» | 2.A |
| 57 | «**Verificación de funcionamiento general. Análisis de históricos y tendencias de datos**» | T |
| 60 | «**Realización de backup general de las bases de datos del puesto central**» | T |
| 61 | «**Realización de backup de ficheros históricos y reinicio de secuencias de almacenamiento, si procede**» | T |
| 52 | «**Verificación de espacios ocupados en discos duros y disponibilidades de memoria**» | A |
| 75 | «**Inspección del histórico de fallos de comunicación**» | T |

Dos detalles de oficio: los controladores y el puesto central deben tener la misma hora, o la
secuencia de eventos de dos equipos no se puede ordenar; y la copia de seguridad se guarda fuera
del puesto central, o se pierde con él.

## 6. Telemedida

### 6.1 Telemedida, telemando y telegestión

Telemedida es la medida hecha en un sitio y leída en otro; telemando, la orden dada a distancia;
telegestión, las dos juntas más el registro y la alarma, es decir, el sistema de gestión manejado
desde fuera del edificio (oficio; ninguna norma leída define las tres palabras). El RITE recoge la
telegestión en el nombre de su cuarto nivel, el «**Nivel de gestión y telegestión**», cuyos
periféricos incluyen «**módems, routers**» (epígrafe 1.4), y en el apartado 4 de la IT 2.3.4, que habla de un
«**sistema de control, mando y gestión o telegestión basado en la tecnología de la
información**».

Dónde la usa una radiotelevisión (oficio): los centros emisores y reemisores, que no tienen a nadie
delante, mandan al centro de control la telemedida y las alarmas de red, grupo, SAI, temperatura y
puerta (tema 8); los edificios de producción, la de sus cuadros, contadores y climatización al
puesto central; y la empresa mantenedora de la climatización puede vigilar a distancia sus
equipos. En el RITE, la supervisión remota en continuo es lo que permite espaciar hasta 2 años el
mantenimiento de las instalaciones de hasta 70 kW, siempre que estén garantizadas la seguridad y la
eficiencia energética (epígrafe 1.3).

Telemedida de energía (oficio): los contadores y analizadores de red de los cuadros, leídos por
bus, dan el consumo por línea y por uso que la IT 1.2.4.4 pide separar (epígrafe 5.1), y avisan de
desequilibrios, de factor de potencia bajo o de una potencia que se acerca a la contratada (temas 1
y 14). La lectura remota de los contadores de la compañía eléctrica para facturación es otra cosa,
con su propia regulación, que este tema no da.

### 6.2 Lo que hay que comprobar en una telemedida

Una lectura remota puede estar congelada: el puesto central sigue mostrando el último valor
recibido aunque el equipo haya dejado de comunicar (oficio). Por eso se vigila el tiempo de refresco
y la comunicación, y se contrasta el valor remoto con el de campo. La gama del IDAE:

| Nº | Operación (literal de la guía) | Frecuencia |
|---|---|---|
| 90 | «**Comprobación de los tiempos de refresco**» | T |
| 91 | «**Comprobación del mando sobre los diferentes equipos controlados desde el puesto de control**» | T |
| 92 | «**Comprobación de los valores reales en los equipos (en campo) con los presentados en el puesto de control**» | T |
| 93 | «**Inspección de la alimentación y conexionado de MODEM u otros dispositivos de comunicación remota**» | T |
| 94 | «**Comprobación del establecimiento de la comunicación y de la actuación remota del sistema**» | T |

Las operaciones 90 a 92 son, en la guía, de las «Integraciones» (otros sistemas que se leen desde
el de gestión); la 93 y la 94, de la «Telegestión».

La comunicación remota alimentada desde el mismo cuadro que vigila se cae con él, y entonces el
centro de control se queda sin la alarma que más necesitaba (oficio). El módem o el equipo de
comunicaciones de un centro sin personal va alimentado desde el SAI, y la falta de comunicación se
trata en el otro extremo como alarma.

Y la seguridad del acceso remoto (oficio): cada acceso desde fuera es una entrada al sistema que
manda cuadros y equipos. Va por canal cifrado y con usuarios nominales, se cierra cuando no se usa
y se registra quién entró y qué hizo (epígrafe 2.2).

## 7. Actuación ante avisos

### 7.1 Lo que dice la norma

Ninguna norma leída fija un protocolo de respuesta a las alarmas de un sistema de gestión técnica.
Lo que hay son obligaciones sueltas que lo enmarcan:

- RITE, artículo 25.3, para titulares y usuarios: «**Se pondrá en conocimiento del responsable de
  mantenimiento cualquier anomalía que se observe en el funcionamiento normal de las instalaciones
  térmicas.**»
- RITE, IT 1.3.4.1.2.2, letra p): en el interior de la sala de máquinas deben figurar, visibles y
  protegidas, las «**instrucciones para efectuar la parada de la instalación en caso necesario, con
  señal de alarma de urgencia y dispositivo de corte rápido**».
- RITE, IT 1.2.4.3.1, apartado 3: el rearme automático de los dispositivos de seguridad sólo donde las
  instrucciones técnicas lo indiquen expresamente (epígrafe 4.3).
- RIPCI: la alarma de incendio la gestiona la central de incendios, con prioridad máxima en el
  sistema integrado (epígrafe 1.1); la respuesta es la del plan de autoprotección (tema 11).

### 7.2 El procedimiento diario del técnico de mantenimiento

La guía del IDAE trae, en su ejemplo de plan de mantenimiento, un procedimiento diario que encaja
con el enunciado. Recomienda incluir en el plan «**las instrucciones de procedimiento diario que
deberá seguir el personal de mantenimiento destacado en el edificio**», acordadas previamente con la propiedad o el usuario,
y propone:

> «**El técnico de mantenimiento efectuará diariamente, a su llegada al edificio, una comprobación,
> a través de la pantalla de comunicación del sistema de control centralizado, de la existencia de
> alarmas registradas por el sistema.**
>
> **En el caso de observar en pantalla la presencia de alguna alarma procederá a la comprobación del
> elemento, equipo o componente emisor de la señal de alarma, y actuará en consecuencia para que
> sean tomadas las medidas necesarias que conduzcan a la normalización de la instalación.**
>
> **Los resultados de las intervenciones anteriores serán anotados en el registro diario de
> incidencias.**
>
> **Una vez solventadas las situaciones de alarma, el técnico procederá a la realización de las
> tareas de mantenimiento preventivo programadas** […]»

Cuatro ideas en ese texto: se mira el sistema lo primero; la alarma se comprueba en el equipo, no
sólo en la pantalla; todo se anota; y el correctivo va antes que el preventivo.

### 7.3 Los pasos ante un aviso

Desarrollo de oficio de ese procedimiento, para cualquier aviso:

1. Leer el aviso entero: qué punto, qué equipo, qué valor, desde qué hora, si es nuevo o
   repetido. El histórico de los minutos anteriores (epígrafe 5.3) dice a menudo la causa.
2. Clasificar: ¿afecta a personas, a la emisión, a la redundancia, o es informativo?
   (epígrafe 4.2). Si afecta a personas o hay indicio de incendio, primero el plan de emergencia
   (tema 11); el sistema de gestión pasa a segundo plano.
3. Reconocer la alarma en el puesto, para que conste que alguien se ha hecho cargo
   (epígrafe 4.3), y avisar a quien deba saberlo: el responsable de mantenimiento, y producción o el
   centro de control si el aviso afecta a una sala en uso o a la emisión.
4. Comprobar en campo: ir al equipo y ver si la alarma es real o es fallo de la señal (sonda,
   cableado, comunicación). Una alarma falsa también es una avería, la del sistema de vigilancia.
5. Actuar con la consignación que corresponda (tema 15). En un edificio con gestión técnica
   que puede arrancar, parar, abrir o cerrar equipos a distancia, bloquear el aparato en campo no
   basta si el sistema puede volver a mandarlo: hay que dejar el punto fuera de servicio también en
   el puesto central, o en manual local, y señalizarlo en los dos sitios.
6. No rearmar a ciegas: un equipo parado por su seguridad no se rearma desde el puesto sin
   saber por qué paró (epígrafe 4.3).
7. Normalizar y probar: devolver los puntos que se pusieron en manual o fuera de servicio a
   automático, y comprobar que la alarma desaparece y que el equipo responde a la orden del sistema.
   Un punto olvidado en manual es una regulación que ya no existe.
8. Registrar: en el registro de incidencias, la hora, la causa, lo hecho, lo pendiente y los
   repuestos; si hace falta una reparación que no se puede hacer en el momento, abrir la orden de
   trabajo correctiva (tema 13).
9. Corregir el sistema si mintió: si la alarma no tenía causa real, ajustar el umbral, el
   retardo o la sonda; si faltó una alarma que debía haber saltado, crearla.

### 7.4 Casos del puesto

Tres situaciones típicas, con la respuesta de oficio:

| Aviso | Primera comprobación | Respuesta |
|---|---|---|
| Temperatura alta en sala técnica o CPD | Lectura de las demás sondas de la sala y estado de los equipos de climatización | Si la climatización ha disparado, ver por qué (protección eléctrica, alta presión del circuito frigorífico, falta de agua); arrancar la reserva si la hay; avisar a quien opera la sala por si hay que reducir carga; climatización de precisión, tema 9 |
| SAI en batería | Si hay tensión de red en la entrada del SAI y si el grupo ha arrancado | Si falta la red y el grupo no ha entrado, el tiempo que queda es la autonomía de la batería: transferencia manual o arranque del grupo según su procedimiento (tema 7) |
| Disparo de un interruptor de un cuadro | Qué línea alimenta y qué hay aguas abajo; si ha sido diferencial, magnetotérmico o sobretensiones | No se rearma hasta saber la causa (aislamiento, sobrecarga, cortocircuito); si alimenta un servicio en emisión, coordinar con producción antes de tocar (temas 3 y 17) |

### 7.5 La gestión técnica en una casa que emite

Cómo convive un sistema de gestión de edificios con una casa que emite: los cuatro conflictos
reales, y cómo se resuelven (oficio):

| Conflicto | Por qué ocurre | Cómo se resuelve |
|---|---|---|
| La parada óptima contra el directo | El sistema apaga la climatización antes del final de jornada; el plató sigue grabando a las once de la noche | Los espacios de producción se sacan del calendario general y se gobiernan por ocupación real o por reserva |
| La limitación de potencia contra el arranque de un plató | Escalonar arranques puede retrasar la iluminación de un decorado | La producción se declara carga no escalonable |
| El alumbrado por presencia contra la grabación | Un detector apaga la luz de un pasillo por el que no pasa nadie durante una toma | Las zonas contiguas a plató se excluyen del apagado automático mientras la luz roja esté encendida |
| El ruido de la climatización contra el sonido directo | El sistema sube el caudal para mantener consigna y el micrófono lo oye | Modo «silencio de plató»: consigna relajada y caudal limitado durante la toma |

Los cuatro se resuelven con la misma idea, y conviene enunciarla así: el sistema de gestión tiene
que conocer el estado de PRODUCCIÓN del edificio. Una señal de «en grabación» procedente del
control de realización vale más que veinte sensores de presencia.

Esa señal es una integración entre dos mundos que no se hablan —el de instalaciones y el de
producción—, y hay que pedirla en el pliego desde el principio.

Y la misma lógica para el mantenimiento (oficio): una prueba de alarmas, un cambio de programa o una
actualización del puesto central se hacen en una ventana pactada con producción (tema 17), porque
durante la prueba la vigilancia de las salas queda reducida.

## Normativa que el tema invoca

| Norma | Qué se usa | Redacción |
|---|---|---|
| Real Decreto 1027/2007, de 20 de julio, por el que se aprueba el Reglamento de Instalaciones Térmicas en los Edificios (BOE-A-2007-15820) | Artículos 2.1, 12.3 y 25.3; IT 1.2.4.3.1 (apartados 1 y 3), IT 1.2.4.3.5, IT 1.2.4.4 (apartados 2 a 7), IT 1.2.4.5.1, IT 1.3.4.1.2.2.p), IT 2.3.4, IT 3.3 (pie de la tabla 3.1), IT 3.4.2 (tabla 3.3), IT 3.4.4 (apartado 2), IT 3.4.5, IT 3.6, IT 3.7 e IT 4.3.4; apéndice 1 (definiciones del sistema de automatización y control y de los cuatro niveles); apéndice 2 (títulos de UNE-EN 15232-1 y UNE-EN ISO 16484-3) | Vigente a 05/10/2026; sin cambios desde el 01/07/2021 |
| Real Decreto 513/2017, de 22 de mayo, por el que se aprueba el Reglamento de instalaciones de protección contra incendios (BOE-A-2017-6606) | Anexo I, sección 1.ª, apartado 1.7 | Vigente desde el 10/05/2025 (BOE-A-2025-7190) |

## Lo que este tema no da, y dónde está

- Los controles locales que el RITE exige a cada instalación térmica, la contabilización de
  consumos completa, las inspecciones de las que exime el sistema y el Manual de Uso y
  Mantenimiento: tema 10. La climatización de salas técnicas y CPD y su mantenimiento: tema 9.
- La detección, la central de incendios y el plan de autoprotección: tema 11. Grupos y SAI: tema
  7. Instalaciones de centros emisores, CPD y compatibilidad electromagnética: tema 8. Analizadores
  de red y medidas: tema 14. Consignación y trabajos: tema 15. Órdenes de trabajo, gamas y
  mantenimiento predictivo: tema 13. Ventanas de mantenimiento y coordinación con producción: tema
  17. Sensorización IoT, gemelo digital y telegestión energética: tema 18. Control del alumbrado:
  tema 6.
- El contenido de las normas UNE-EN 15232-1 y UNE-EN ISO 16484-3: el tema dice lo que el RITE dice
  de ellas. Si la UNE-EN 15232-1 ha sido sustituida en el catálogo de normas no se ha comprobado.
- De la ISO 16484-5 (BACnet) sólo se ha leído su objeto y su índice; de la especificación Modbus,
  la introducción y el modelo de datos. El número de la norma internacional de KNX no se ha
  confirmado en fuente primaria; LonWorks y otros protocolos no se han investigado y no se nombran.
- Una definición normativa de SCADA, de telemedida, de telegestión o de las señales 4-20 mA y
  0-10 V: no se ha encontrado en las fuentes leídas; lo que dice el tema de ellas es oficio, salvo
  la definición del NIST. La seguridad de las redes de control (series de normas específicas y
  guías de organismos de ciberseguridad) no se ha investigado: lo que se dice es oficio.
- La lectura remota de contadores de la compañía eléctrica y su regulación: no se ha leído.
- El sistema de gestión técnica de los edificios de la RTVA, su fabricante, su protocolo, si los
  edificios superan los 290 kW, quién atiende las alarmas fuera de horario y con qué procedimiento:
  no constan en documento publicado.

## Trazabilidad

| Fuente | Qué se ha tomado | Leída |
|---|---|---|
| Real Decreto 1027/2007, RITE (BOE-A-2007-15820), redacción vigente | Los preceptos de la tabla anterior | 05/10/2026 |
| Real Decreto 513/2017, RIPCI (BOE-A-2017-6606), redacción vigente | Anexo I, sección 1.ª, apartado 1.7 | 05/10/2026 |
| IDAE, *Guía técnica de mantenimiento de instalaciones térmicas*, redactada por ATECYR y AMICYF, febrero de 2007 (ISBN 978-84-96680-06-7) | Familia 23: ficha técnica y ejemplo de listado de puntos de control con sus claves; gama «Control DDC (Computerizado)» (operaciones 50 a 97) y operaciones 37, 39 y 42 del control por autómata; claves de frecuencia del apéndice III; procedimiento diario del ejemplo de plan (capítulo 5); comparación entre datos nominales y actuales | 05/10/2026 |
| ISO 16484-5:2026, *Building automation and control systems (BACS) — Part 5: Data communication protocol*, octava edición (muestra pública con portada e índice en el catálogo de iTeh Standards; ficha del catálogo con el objeto y la sustitución de la EN ISO 16484-5:2022) | Objeto, edición, tipos de objeto, servicios de alarma, MS/TP, BACnet/IP | 05/10/2026 |
| Modbus Organization, *MODBUS Application Protocol Specification V1.1b3*, 26-04-2012 (modbus.org) | Apartados 1.1 y 4.3 | 05/10/2026 |
| NIST, glosario del Computer Security Resource Center, entrada «Supervisory Control and Data Acquisition (SCADA)», tomada de NIST SP 800-82r3 | Definición de SCADA | 05/10/2026 |
| KNX Association, página «What is KNX» (knx.org) | Las dos expresiones citadas | 05/10/2026 |

Lo que va como oficio y así se declara: la tabla que separa la gestión técnica del control de
proceso y de la seguridad, la regla de que supervisa pero no manda, las cuatro razones para
instalarlo y la observación sobre el mantenimiento por condición; la pirámide de automatización,
su regla de velocidad y el principio de autonomía, y su correspondencia con los niveles del RITE;
la lectura de que un sistema que sólo arranca y para no exime de inspección y de que la
programación es del personal cualificado del apartado 4 de la IT 2.3.4; la tabla que distingue BMS, SCADA y
autómata; la elección entre protocolo abierto y propietario, los grupos de protocolos, la
tendencia hacia la red de datos y el aviso de seguridad; el uso de Modbus en analizadores, SAI y
grupos y el de KNX en alumbrado; las estrategias de control y el lazo proporcional, integral y
derivativo; las clases básicas de punto, los puntos típicos del puesto, la reserva de puntos, las
señales de campo y la ventaja del 4-20 mA, las precauciones de cableado y el método de contraste;
los orígenes de alarma, la histéresis y el retardo, las prioridades, la depuración de alarmas, el
ciclo aparición-reconocimiento-desaparición y la simulación; los usos de los históricos y la
sincronización de hora; las definiciones de telemedida, telemando y telegestión, sus usos en una
radiotelevisión, la lectura congelada, la alimentación de la comunicación remota y la seguridad del
acceso; los nueve pasos ante un aviso, los tres casos del puesto y los cuatro conflictos con la
producción y su resolución. Ninguna fuente leída lo dice con esas palabras.
