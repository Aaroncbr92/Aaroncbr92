# Tema 18 del específico de Oficial Técnico Electricista · Innovación aplicada al mantenimiento: sensorización IoT, mantenimiento predictivo, gemelo digital, telegestión energética, baterías, autoconsumo y automatización de edificios

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Oficial Técnico Electricista · punto 18 |
| **Sirve para** | Puesto 2.27, Oficial Técnico Electricista (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Real Decreto 244/2019, de 5 de abril, de autoconsumo de energía eléctrica (artículos 2, 3, 4, 5 y 14). Real Decreto 842/2002, de 2 de agosto, Reglamento electrotécnico para baja tensión (ITC-BT-40, apartados 2 y 4). Reglamento (UE) 2023/1542, de pilas y baterías (artículos 3, 12, 13, 14, 61, 95 y 96 y anexos V, VI y VII). Real Decreto 1027/2007, de 20 de julio, Reglamento de instalaciones térmicas en los edificios (apéndice 1, IT 1.2.4.3.5, IT 1.2.4.4, IT 2.3.4, nota a la tabla de la IT 3.3 e IT 4.3.4). Real Decreto 56/2016, de 12 de febrero, de auditorías energéticas (artículo 3). Fichas de catálogo de las normas ISO/IEC 30173:2023, ISO/IEC 30141:2024, ISO 17359:2018, UNE-EN ISO 52120-1:2022 y UNE-EN ISO 19650-1:2019; vistas previas oficiales de la ISO/IEC 30173, la ISO/IEC 30141, la ISO 19650-1 y la ISO 29821:2018. Fuente técnica: especificación LoRaWAN (LoRa Alliance), noticias técnicas del 3GPP sobre NB-IoT, norma MQTT 5.0 de OASIS y dos revisiones científicas sobre embalamiento térmico de baterías de litio. Lo demás es oficio, y así se declara |
| **Redacción que se estudia** | La vigente el 24/09/2026. Real Decreto 244/2019: artículos 3 y 4 en la redacción del Real Decreto-ley 7/2026, de 20 de marzo (desde el 22/03/2026); artículos 2, 5 y 14 en su redacción única (desde el 07/04/2019). ITC-BT-40 en la redacción del Real Decreto 244/2019 (desde el 07/04/2019). RITE: IT 1, IT 3, IT 4 y apéndice 1 en la del Real Decreto 178/2021 (desde el 01/07/2021); IT 2 en su redacción original (desde el 29/02/2008). Real Decreto 56/2016, redacción única. Reglamento (UE) 2023/1542 en su texto publicado en el Diario Oficial de la Unión Europea; sus cuatro correcciones de errores y sus modificaciones (artículo 77, artículo 48 y anexo I) no tocan los preceptos citados |
| **Extensión** | Unas 15.000 palabras |

<!-- /portada -->

Siglas y símbolos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); internet de las cosas
(**IoT**, *Internet of Things*); Reglamento electrotécnico para baja tensión (**REBT**) y sus
instrucciones técnicas complementarias (**ITC-BT**); Reglamento de instalaciones térmicas en los
edificios (**RITE**) y sus instrucciones técnicas (**IT**); sistema de gestión técnica del edificio
(**BMS**, *building management system*); control de supervisión y adquisición de datos
(**SCADA**, *supervisory control and data acquisition*); sistema de alimentación ininterrumpida (**SAI**); centro
de proceso de datos (**CPD**); orden de trabajo (**OT**); gestión del mantenimiento asistido por
ordenador (**GMAO**); Organización Internacional de Normalización (**ISO**) y Comisión
Electrotécnica Internacional (**IEC**); Asociación Española de Normalización (**UNE**) y norma
europea (**EN**); precio voluntario para el pequeño consumidor (**PVPC**); código de respuesta
rápida (**QR**); gemelo digital (**DTw**, *digital twin*, la abreviatura que usa la norma ISO/IEC
30173); modelado de información de la construcción (**BIM**, *building information modelling*); red de
área amplia y baja potencia (**LPWA**, *low power, wide area*); IoT de banda estrecha (**NB-IoT**,
*narrowband IoT*); proyecto de asociación de tercera generación (**3GPP**, *3rd Generation Partnership
Project*); litio-ferrofosfato (**LFP**, *lithium iron
phosphate*) y níquel-cobalto-manganeso (**NMC**, que las fuentes escriben también **NCM**), dos químicas
del cátodo de las baterías de ion litio. Unidades: voltio (**V**), voltamperio (**VA**) y kilovoltamperio (**kVA**), kilovatio
(**kW**), megavatio (**MW**), kilovatio hora (**kWh**), miliamperio (**mA**), hercio (**Hz**) y kilohercio (**kHz**),
kilogramo (**kg**).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.27, punto 18):
>
> Innovación aplicada al mantenimiento: sensorización IoT, mantenimiento predictivo, gemelo digital
> de instalaciones, telegestión energética, baterías, autoconsumo y automatización de edificios.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué es un gemelo digital según la norma ISO/IEC 30173, si un modelo BIM lo es, y qué norma da la
arquitectura de referencia del IoT; con qué redes y protocolos se comunican los sensores (LoRaWAN,
NB-IoT, MQTT); qué variables de una instalación eléctrica se sensorizan para
el predictivo y por qué lo que vale es el histórico; para qué sirve la inspección por ultrasonidos en
un cuadro; dónde encaja el predictivo en la terminología
normalizada; cuáles son los niveles de un sistema de control según el RITE (campo, proceso,
comunicaciones, gestión y telegestión) y quién mantiene sus programas; qué consumos obliga el RITE a
medir y registrar (70 kW, 20 kW) y qué dice de la energía de autoconsumo; qué exige el Real Decreto
56/2016 a los datos de consumo; qué es una batería industrial, un sistema estacionario de
almacenamiento de energía con baterías, un sistema de gestión de baterías y el estado de salud
según el Reglamento (UE) 2023/1542; qué química de litio es más estable frente al embalamiento
térmico; qué parámetros del estado de salud y de la vida útil prevista
debe guardar ese sistema y desde cuándo; qué riesgos prueba el anexo V; desde cuándo llevan las
baterías el símbolo de recogida separada y el código QR, y qué baterías tienen pasaporte; quién
recoge gratis una batería industrial usada; qué es autoconsumo, cuáles son sus modalidades y qué
instalaciones son «próximas» (500 metros; 5 MW y 5.000 metros); cuáles son las cinco condiciones
para acogerse a compensación (100 kW); qué potencia instalada tiene una instalación fotovoltaica;
cuándo se puede estar en dos modalidades a la vez; qué es el mecanismo antivertido; qué
diferencial exige la ITC-BT-40 al circuito de generación; dónde se instalan las baterías de un
autoconsumo; si un grupo de emergencia es autoconsumo; qué edificios tienen que tener un sistema de
automatización y control (290 kW), qué tiene que saber hacer, qué norma cita el RITE y cuál la ha
sustituido, y de qué inspecciones exime. En la prueba práctica: decidir la modalidad y el régimen de
una instalación fotovoltaica en una cubierta, comprobar el cuadro de un autoconsumo, montar el
seguimiento predictivo de una batería o de un cuadro, o leer los datos de un sistema de gestión
para decidir una actuación.

<!-- indice -->

## Índice

- [1. Innovación aplicada al mantenimiento](#1-innovación-aplicada-al-mantenimiento)
  - [1.1 Qué tienen en común las siete materias del enunciado](#11-qué-tienen-en-común-las-siete-materias-del-enunciado)
  - [1.2 Lo que el RITE llama ya «instalación técnica»](#12-lo-que-el-rite-llama-ya-instalación-técnica)
  - [1.3 Lo que este tema da y lo que da el resto del temario](#13-lo-que-este-tema-da-y-lo-que-da-el-resto-del-temario)
- [2. Sensorización IoT](#2-sensorización-iot)
  - [2.1 Qué es y qué norma lo describe](#21-qué-es-y-qué-norma-lo-describe)
  - [2.2 Qué cambia respecto al sistema de gestión clásico](#22-qué-cambia-respecto-al-sistema-de-gestión-clásico)
  - [2.3 Qué se sensoriza en una instalación eléctrica](#23-qué-se-sensoriza-en-una-instalación-eléctrica)
  - [2.4 Del sensor a la decisión: los niveles](#24-del-sensor-a-la-decisión-los-niveles)
  - [2.5 Las tres precauciones de un sistema sensorizado](#25-las-tres-precauciones-de-un-sistema-sensorizado)
  - [2.6 Cómo se comunican los sensores](#26-cómo-se-comunican-los-sensores)
- [3. Mantenimiento predictivo](#3-mantenimiento-predictivo)
  - [3.1 Qué es y dónde encaja](#31-qué-es-y-dónde-encaja)
  - [3.2 Lo que lo hace posible: medir siempre igual y guardar el histórico](#32-lo-que-lo-hace-posible-medir-siempre-igual-y-guardar-el-histórico)
  - [3.3 Las variables de un motor y de una batería](#33-las-variables-de-un-motor-y-de-una-batería)
  - [3.4 Lo que la norma exige que se parezca a un predictivo](#34-lo-que-la-norma-exige-que-se-parezca-a-un-predictivo)
  - [3.5 Una técnica más: los ultrasonidos](#35-una-técnica-más-los-ultrasonidos)
- [4. Gemelo digital de instalaciones](#4-gemelo-digital-de-instalaciones)
  - [4.1 La definición de la norma](#41-la-definición-de-la-norma)
  - [4.2 Lo que es y lo que no es](#42-lo-que-es-y-lo-que-no-es)
  - [4.3 Para qué sirve en mantenimiento](#43-para-qué-sirve-en-mantenimiento)
  - [4.4 Su condición: la documentación al día](#44-su-condición-la-documentación-al-día)
- [5. Telegestión energética](#5-telegestión-energética)
  - [5.1 Qué es](#51-qué-es)
  - [5.2 Lo que el RITE obliga a medir y registrar](#52-lo-que-el-rite-obliga-a-medir-y-registrar)
  - [5.3 Lo que la telegestión permite en el mantenimiento](#53-lo-que-la-telegestión-permite-en-el-mantenimiento)
  - [5.4 Los datos de consumo como prueba: el Real Decreto 56/2016](#54-los-datos-de-consumo-como-prueba-el-real-decreto-562016)
  - [5.5 Las actuaciones de la telegestión energética](#55-las-actuaciones-de-la-telegestión-energética)
- [6. Baterías](#6-baterías)
  - [6.1 Por qué las baterías están en un tema de innovación](#61-por-qué-las-baterías-están-en-un-tema-de-innovación)
  - [6.2 El Reglamento (UE) 2023/1542: qué es y desde cuándo se aplica](#62-el-reglamento-ue-20231542-qué-es-y-desde-cuándo-se-aplica)
  - [6.3 El sistema de gestión de baterías y el estado de salud](#63-el-sistema-de-gestión-de-baterías-y-el-estado-de-salud)
  - [6.4 La seguridad de los sistemas estacionarios](#64-la-seguridad-de-los-sistemas-estacionarios)
  - [6.5 Etiquetas, código QR y pasaporte](#65-etiquetas-código-qr-y-pasaporte)
  - [6.6 Cuando la batería se retira](#66-cuando-la-batería-se-retira)
  - [6.7 El mantenimiento de las baterías, con lo nuevo](#67-el-mantenimiento-de-las-baterías-con-lo-nuevo)
- [7. Autoconsumo](#7-autoconsumo)
  - [7.1 Qué es, y qué no](#71-qué-es-y-qué-no)
  - [7.2 Las modalidades](#72-las-modalidades)
  - [7.3 Qué potencia tiene una instalación fotovoltaica](#73-qué-potencia-tiene-una-instalación-fotovoltaica)
  - [7.4 Qué instalaciones son «próximas»](#74-qué-instalaciones-son-próximas)
  - [7.5 Cambiar de modalidad y estar en dos a la vez](#75-cambiar-de-modalidad-y-estar-en-dos-a-la-vez)
  - [7.6 Las baterías en el autoconsumo](#76-las-baterías-en-el-autoconsumo)
  - [7.7 Responsabilidad y corte de suministro](#77-responsabilidad-y-corte-de-suministro)
  - [7.8 La compensación simplificada](#78-la-compensación-simplificada)
  - [7.9 Lo que el electricista comprueba: la ITC-BT-40](#79-lo-que-el-electricista-comprueba-la-itc-bt-40)
  - [7.10 El mantenimiento de una fotovoltaica de autoconsumo](#710-el-mantenimiento-de-una-fotovoltaica-de-autoconsumo)
  - [7.11 Aplicación a un edificio técnico](#711-aplicación-a-un-edificio-técnico)
- [8. Automatización de edificios](#8-automatización-de-edificios)
  - [8.1 Quién tiene que tenerla y qué tiene que saber hacer](#81-quién-tiene-que-tenerla-y-qué-tiene-que-saber-hacer)
  - [8.2 La norma que cita el RITE, y la que la ha sustituido](#82-la-norma-que-cita-el-rite-y-la-que-la-ha-sustituido)
  - [8.3 Ponerla en marcha, documentarla y mantenerla](#83-ponerla-en-marcha-documentarla-y-mantenerla)
  - [8.4 Lo que se gana: la exención de inspecciones](#84-lo-que-se-gana-la-exención-de-inspecciones)
  - [8.5 Las estrategias que ahorran y las que cuidan los equipos](#85-las-estrategias-que-ahorran-y-las-que-cuidan-los-equipos)
  - [8.6 La automatización en un edificio que emite](#86-la-automatización-en-un-edificio-que-emite)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Innovación aplicada al mantenimiento

### 1.1 Qué tienen en común las siete materias del enunciado

El enunciado junta siete cosas que parecen de mundos distintos y que, en un edificio técnico, se
tocan en un mismo punto: el dato. Los sensores (IoT) producen el dato; el predictivo lo convierte
en una decisión de mantenimiento; el gemelo digital lo pone en el modelo de la instalación; la
telegestión energética lo lleva a un puesto remoto y lo convierte en consumo y coste; las baterías
y el autoconsumo son dos instalaciones nuevas que hay que mantener y que, además, generan sus
propios datos; y la automatización de edificios es el sistema que recoge todo eso y actúa (lectura
de oficio que ordena el tema; ninguna norma lo dice así).

Lo que separa cada materia es su apoyo normativo, y conviene saberlo antes de estudiar:

| Materia | Qué la regula o la define | Dónde está en este tema |
|---|---|---|
| Sensorización IoT | Ninguna norma obligatoria. Norma técnica de referencia: ISO/IEC 30141:2024 (arquitectura) | Epígrafe 2 |
| Mantenimiento predictivo | Terminología en la UNE-EN 13306 (tema 13). Apoyos normativos: RITE IT 1.2.4.3.5.1.b) y Reglamento (UE) 2023/1542, artículo 14 | Epígrafe 3 |
| Gemelo digital | Ninguna norma obligatoria. Norma técnica de terminología: ISO/IEC 30173:2023 | Epígrafe 4 |
| Telegestión energética | RITE (IT 1.2.4.4 e IT 2.3.4) y Real Decreto 56/2016 (datos de las auditorías) | Epígrafe 5 |
| Baterías | Reglamento (UE) 2023/1542, directamente aplicable | Epígrafe 6 |
| Autoconsumo | Real Decreto 244/2019 y REBT, ITC-BT-40 | Epígrafe 7 |
| Automatización de edificios | RITE, IT 1.2.4.3.5, IT 2.3.4 e IT 4.3.4 | Epígrafe 8 |

La consecuencia de estudio: en IoT, predictivo y gemelo digital no hay cifras de norma que
memorizar, y lo preguntable son definiciones y criterios; en baterías, autoconsumo y
automatización sí hay preceptos, con cifras y fechas.

### 1.2 Lo que el RITE llama ya «instalación técnica»

El RITE, en su apéndice 1 (términos y definiciones), recoge ya en una sola definición varias de las
materias del enunciado: **Instalación técnica del edificio: equipos técnicos destinados a
calefacción y refrigeración de espacios, ventilación, agua caliente sanitaria, iluminación
integrada, automatización y control de edificios, generación de electricidad in situ, o una
combinación de los mismos, incluidas las instalaciones que utilicen energía procedente de fuentes
renovables, de un edificio o de una unidad de este.**

Y en la definición de instalación térmica incluye **los sistemas de automatización y control**. Es
decir, el sistema de automatización es parte de la instalación térmica a efectos del reglamento, y
se le aplica lo que el RITE dice de ella (documentación, mantenimiento, inspección: tema 10).

### 1.3 Lo que este tema da y lo que da el resto del temario

Varias materias de este punto se desarrollan en otros temas del puesto. Para no repetirlas, aquí se
tratan desde el ángulo de la innovación y del mantenimiento, y se remite:

| Materia | Dónde está lo básico |
|---|---|
| Tipos de mantenimiento, gamas, OT, GMAO y el ciclo del predictivo | Tema 13 |
| Termografía, analizador de redes, medida de aislamiento | Tema 14 |
| BMS y SCADA: niveles, protocolos, puntos, señales, alarmas, históricos y telemedida | Tema 12 |
| SAI, baterías (parámetros, químicas, agrupación) y pruebas de autonomía | Tema 7 |
| Auditorías energéticas, contabilización de consumos y mantenimiento orientado a eficiencia | Tema 16 |
| Ventanas de mantenimiento y retorno al servicio | Tema 17 |

## 2. Sensorización IoT

### 2.1 Qué es y qué norma lo describe

Internet de las cosas es, en palabras de oficio, la conexión a una red de datos de sensores y
actuadores que miden y mandan sobre objetos físicos, de forma que sus datos se recogen, se guardan
y se analizan en otro sitio. La definición normativa de IoT está en la ISO/IEC 20924 (vocabulario
de IoT y gemelo digital), cuyo texto no se ha podido leer: este tema no la reproduce.

La norma de arquitectura es la ISO/IEC 30141:2024, **«Internet of Things (IoT) — Reference
architecture»**, con fecha de edición de 27 de agosto de 2024 y en vigor según la ficha de catálogo de AENOR, que la
resume así: **«This document provides a standardized IoT Reference Architecture using a common
vocabulary, reusable designs and industry best practices.»** La ficha añade: **«This second edition
cancels and replaces the first edition published in 2018.»** Es norma conjunta de la ISO y la IEC: según
su prólogo, la preparó el **«subcommittee 41: Internet of Things and Digital Twin, of ISO/IEC joint
technical committee 1: Information technology»**, el mismo subcomité que la norma del gemelo digital
(epígrafe 4.1). Está en inglés, sin versión UNE localizada y sin carácter obligatorio.

### 2.2 Qué cambia respecto al sistema de gestión clásico

Un edificio técnico ya tenía sensores: los del BMS (tema 12). Lo que la sensorización IoT añade,
como oficio, es:

| Rasgo | BMS clásico | Sensorización IoT |
|---|---|---|
| Cableado | Bus de campo o señal cableada a un controlador | A menudo inalámbrico, con batería propia en el sensor |
| Coste por punto | Alto: cable, tarjeta de entrada y programación | Bajo: se añaden puntos donde antes no compensaba |
| Dónde va el dato | Al puesto central del edificio | A una plataforma en red, propia o de un proveedor |
| Qué se mide | Lo necesario para regular | También lo que sólo sirve para vigilar el estado del equipo |
| Quién lo mantiene | El mantenedor del BMS | Además, la red, la plataforma y las baterías de los sensores |

La consecuencia práctica es la última fila: un sensor inalámbrico con pila es un equipo más que
mantener. Su pila se agota, su señal se pierde, y el sensor que deja de comunicar no avisa por sí
mismo. Por eso, igual que con cualquier telemedida (tema 12, epígrafe 6.2), la falta de
comunicación de un sensor se trata como alarma y la batería del sensor entra en la gama.

### 2.3 Qué se sensoriza en una instalación eléctrica

Las variables que un electricista quiere vigilar en continuo, porque anticipan una avería (oficio):

| Equipo | Variable | Qué anticipa |
|---|---|---|
| Conexiones de cuadros y embarrados | Temperatura (sensor fijo junto al punto de apriete) | Contacto flojo o sobrecarga antes de que se vea en la termografía anual |
| Líneas y receptores | Corriente por fase, tensión, factor de potencia, armónicos (analizadores fijos) | Desequilibrio, sobrecarga, degradación del factor de potencia |
| Diferenciales | Corriente de fuga de la línea | Degradación del aislamiento antes del disparo |
| Baterías de SAI y de almacenamiento | Tensión por bloque, temperatura, resistencia interna o los datos del sistema de gestión de baterías | Pérdida de capacidad; el elemento que limita la cadena (tema 7) |
| Salas técnicas, CPD, centros emisores | Temperatura, humedad, presencia de agua, apertura de puerta | Fallo de climatización; inundación; intrusión |
| Motores de bombas y ventiladores | Vibración, temperatura, horas de funcionamiento | Rodamiento, desalineación; vida consumida |
| Grupo electrógeno | Tensión de la batería de arranque, temperatura del refrigerante, nivel de combustible | Fallo de arranque el día que hace falta |

Ninguna de esas variables se mide «porque sí»: se mide la que tiene una relación conocida con un
modo de fallo. Una regla de oficio para elegir: si no se sabe qué decisión se tomaría con el dato,
el sensor sobra.

### 2.4 Del sensor a la decisión: los niveles

El RITE ordena un sistema de control por niveles, y el orden vale para cualquier sistema
sensorizado. IT 2.3.4, apartado 2: **se establecerán los criterios de seguimiento basados en la
propia estructura del sistema, en base a los niveles del proceso siguientes: nivel de unidades de
campo, nivel de proceso, nivel de comunicaciones, nivel de gestión y telegestión.**

Y su apéndice 1 los define:

| Nivel | Definición del RITE (apéndice 1) |
|---|---|
| Unidades de campo | **corresponde a los equipos de campo como: elementos primarios de medida, sondas, unidades de ambiente, termostatos, indicadores de estados y alarmas, así como elementos finales de control y mando, válvulas, actuadores, variadores de tensión/frecuencia, elementos finales de control, etc.** |
| Proceso | **corresponde a los controladores, tanto analógicos como digitales, que manejan los elementos del nivel de periferia.** |
| Comunicaciones | **corresponde a todos los controladores e interfaces de comunicación del sistema de gestión, así como a los buses de comunicación, drivers, redes, etc.** |
| Gestión y telegestión | **corresponde a los puestos centrales, programas residentes y periféricos asociados a los puestos centrales, tales como impresoras, pantallas de vídeo, módems, routers, etc.** |

Un sensor IoT es una unidad de campo que habla directamente con el nivel de comunicaciones; la
plataforma que guarda y analiza sus datos es nivel de gestión y telegestión. La regla de diseño de
oficio que sale de ahí: la decisión rápida y la de seguridad se toman abajo (en el controlador o en
la protección), y arriba sólo se toma la decisión de mantenimiento. Un disparo por sobretemperatura
no puede depender de que la nube conteste.

### 2.5 Las tres precauciones de un sistema sensorizado

Como oficio, y con el mismo fundamento que el tema 12 da para la telegestión:

1. *Alimentación.* El equipo de comunicaciones que transmite las alarmas de un cuadro no se
   alimenta del cuadro que vigila: va al SAI. Si no, el fallo que más importa es el que deja al
   sistema mudo.
2. *Seguridad de la red.* Cada sensor y cada pasarela conectados son una entrada a la red de
   instalaciones. Van en una red separada de la ofimática, con credenciales propias y sin las
   contraseñas de fábrica.
3. *Calidad del dato.* Un sensor se descalibra. Se contrasta periódicamente con un instrumento
   patrón (tema 12, epígrafe 3.3; tema 14), y un dato sin fecha y hora fiables no sirve para
   comparar.

La IT 2.3.4, apartado 4, fija además quién toca los programas: **Cuando la instalación disponga de
un sistema de control, mando y gestión o telegestión basado en la tecnología de la información, su
mantenimiento y la actualización de las versiones de los programas deberá ser realizado por
personal cualificado o por el mismo suministrador de los programas.**

### 2.6 Cómo se comunican los sensores

El sensor inalámbrico con pila del epígrafe 2.2 necesita dos cosas: una red radio que llegue lejos
gastando poca energía, y un protocolo para entregar sus lecturas a la plataforma. Ninguna norma
obligatoria elige una tecnología; lo que sigue es lo que dicen de sí mismas las especificaciones más
extendidas (fuente técnica, no reglamento).

| Tecnología | Qué es | Lo que dice su propia especificación |
|---|---|---|
| LoRaWAN | Red radio de área amplia y baja potencia (LPWA), especificación que **«is developed and maintained by the LoRa Alliance»** | **«a Low Power, Wide Area (LPWA) networking protocol designed to wirelessly connect battery operated 'things' to the internet in regional, national or global networks»**. Topología en **«star-of-stars»**: unas pasarelas (*gateways*) **«relay messages between end-devices and a central network server»** |
| NB-IoT | Tecnología radio celular para IoT, normalizada por el 3GPP | El 3GPP la presentó como **«the new narrowband radio technology developed for the Internet-of-Things (IoT)»**, incorporada a la versión 13 de sus especificaciones (**«Release 13 (LTE Advanced Pro)»**) y congelada en junio de 2016. Funciona en espectro con licencia: **«The operation in licensed spectrum also allows for a level of control and quality assurance, not possible to achieve by proprietary technologies operating in the unlicensed frequency domain.»** |
| MQTT | Protocolo de mensajería entre el sensor o la pasarela y la plataforma, norma de OASIS (versión 5.0, de 7 de marzo de 2019) | **«MQTT is a Client Server publish/subscribe messaging transport protocol. It is light weight, open, simple, and designed to be easy to implement.»** Pensado, entre otros, para **«Machine to Machine (M2M) and Internet of Things (IoT) contexts where a small code footprint is required and/or network bandwidth is at a premium»** |

Las dos primeras son la red; la tercera, el idioma en que el dato viaja por ella o por la red
de datos del edificio. No compiten entre sí: un sensor puede transmitir por LoRaWAN a una pasarela, y
la pasarela publicar las lecturas por MQTT en la plataforma (lectura de oficio).

Dos rasgos de esas especificaciones que importan a quien mantiene:

- *Clases de dispositivo LoRaWAN.* La especificación distingue tres. La clase A, **«Lowest power,
  bi-directional end-devices»**, es la que todo dispositivo debe soportar: la comunicación la empieza
  siempre el sensor, y tras cada envío abre dos ventanas cortas de recepción. La clase C mantiene el
  receptor abierto siempre que no transmite, con un consumo de hasta unos 50 mW, y por eso
  **«is suitable for applications where continuous power is available»**. Consecuencia práctica: un
  sensor de pila en clase A no puede recibir órdenes en cualquier momento; lo que haya que mandarle
  espera en el servidor de red hasta su siguiente envío. La clase B, también válida con pila según la
  especificación, añade ventanas de recepción a horas programadas, a costa de algo más de consumo.
- *Calidades de servicio de MQTT.* La norma da tres niveles de entrega: **«At most once»** (se puede
  perder un mensaje: la propia norma pone el ejemplo de **«ambient sensor data where it does not
  matter if an individual reading is lost as the next one will be published soon after»**), **«At least
  once»** (llega seguro, pero puede duplicarse) y **«Exactly once»**. Una alarma no se envía con el
  primer nivel (lectura de oficio): una lectura de temperatura perdida se repone con la siguiente; un
  aviso de disparo perdido, no.

Por qué todo esto es también mantenimiento: la red radio y la pasarela son equipos con su propia
avería (cobertura, interferencias, pasarela sin alimentación), y su fallo deja mudos a todos los
sensores que cuelgan de ella. La pasarela se trata como el equipo de comunicaciones del epígrafe 2.5:
alimentada desde el SAI y vigilada como un punto más (oficio).

## 3. Mantenimiento predictivo

### 3.1 Qué es y dónde encaja

El predictivo, o mantenimiento por condición, actúa cuando una medida dice que el equipo va a
fallar, no cuando lo dice el calendario. Frente a los otros dos:

| Tipo | Cuándo se actúa | Qué exige |
|---|---|---|
| Correctivo | Cuando ya ha fallado | Repuesto y gente disponibles a cualquier hora |
| Preventivo | Por calendario o por horas de uso | Un plan; se cambia lo que aún servía |
| Predictivo o por condición | Cuando una medida dice que va a fallar | Instrumentación, registro y criterio para leerlo |

Dos precisiones que el tema 13 desarrolla y que aquí se recuerdan porque se preguntan:

- En la terminología normalizada (UNE-EN 13306), el predictivo no es un tercer tipo al lado del
  preventivo: es una forma del preventivo basado en la condición. El enunciado lo nombra aparte y
  el oficio también, pero si una pregunta pide la clasificación de la norma, va dentro del
  preventivo. (El texto de la UNE-EN 13306 vigente no se ha leído: esta estructura procede de una
  reproducción secundaria de su edición de 2010; tema 13.)
- Que el predictivo salga más barato que el preventivo en instalaciones grandes es experiencia de
  oficio, no dato de norma. Lo que sí se puede afirmar es por qué compensa: evita a la vez la avería
  del correctivo y la sustitución prematura del preventivo.

Norma de referencia, sólo por catálogo (su texto no se ha leído): ISO 17359:2018, **«Condition
monitoring and diagnostics of machines — General guidelines»**, en vigor, cuyo resumen dice que
**«gives guidelines for the general procedures to be considered when setting up a condition
monitoring programme for machines»**.

### 3.2 Lo que lo hace posible: medir siempre igual y guardar el histórico

Tres medidas sostienen el predictivo de una instalación eléctrica: la termografía, el análisis de
red y la evolución de la resistencia de aislamiento (cómo se hacen, en el tema 14). Las tres tienen
en común que se comparan consigo mismas a lo largo del tiempo, y por eso lo que las hace útiles no
es la medida aislada: es el histórico.

Lo que la innovación añade es que esas medidas, que antes se hacían una o dos veces al año con un
instrumento portátil, pueden hacerse en continuo con sensores fijos (epígrafe 2.3), y que un
sistema que registra las horas de funcionamiento de cada equipo permite pasar de mantenimiento por
calendario a mantenimiento por condición. El RITE ya obliga a registrar algunas de esas horas
(epígrafe 5.2).

El ciclo, como oficio (tema 13, epígrafe 1.4):

1. Elegir la variable que anticipa el fallo.
2. Medirla siempre igual: mismo punto, mismo instrumento, carga comparable.
3. Registrarla con fecha y hora.
4. Fijar un umbral de aviso y uno de actuación.
5. Cuando la tendencia cruza el de aviso, generar una OT de preventivo antes de que llegue al fallo.

Una lectura fuera de tendencia vale más que una lectura alta: la caída clara del aislamiento de un
circuito respecto a sus medidas anteriores dice más que un valor absoluto que todavía cumple.

### 3.3 Las variables de un motor y de una batería

En los motores de bombas y ventiladores, las tres medidas que anticipan una avería (oficio):

1. El desequilibrio de corriente entre fases: un pequeño desequilibrio de tensión produce uno de
   corriente mucho mayor y calienta el devanado.
2. La evolución del aislamiento de cada devanado a masa, medida siempre en las mismas condiciones.
3. La vibración, que delata el rodamiento y la desalineación antes de que se oigan.

En las baterías, la innovación más clara es que la propia norma obliga a que el sistema de gestión
de ciertas baterías guarde los datos de su estado (epígrafe 6.3). Pero hay que saber qué mide y qué
no mide cada cosa (oficio, del tema 7):

| Medida | Qué dice | Qué no dice |
|---|---|---|
| Tensión en flotación | Que la batería está cargada | Su capacidad: una batería con la tensión correcta en flotación puede no tener capacidad ninguna |
| Resistencia interna o impedancia, en tendencia | Qué bloque se está degradando | La autonomía en minutos |
| Prueba de descarga controlada | La autonomía real | — |

La combinación útil es la del predictivo: se vigila la tendencia en continuo y se programa la prueba
de descarga cuando la tendencia lo pide, además de las periódicas.

### 3.4 Lo que la norma exige que se parezca a un predictivo

No hay una norma que obligue a hacer mantenimiento predictivo. Pero dos normas vigentes piden
capacidades que son, en la práctica, predictivo:

- El RITE, IT 1.2.4.3.5.1.b), exige a los sistemas de automatización y control obligatorios ser
  capaces de **detectar las pérdidas de eficiencia de sus instalaciones técnicas e informar sobre
  las posibilidades de mejora de la eficiencia energética a la persona responsable de la
  instalación o de la gestión técnica del edificio** (epígrafe 8.1).
- El Reglamento (UE) 2023/1542, artículo 14.1, exige que el sistema de gestión de los sistemas
  estacionarios de almacenamiento de energía con baterías recoja **los datos actualizados de los
  parámetros para determinar el estado de salud y la vida útil prevista** (epígrafe 6.3).

### 3.5 Una técnica más: los ultrasonidos

A las medidas del epígrafe 3.2 se suma una que el resto del temario sólo nombra para localizar fugas de
refrigerante (tema 9) y que sirve también en cuadros, celdas y transformadores: la inspección por
ultrasonidos. Su norma de referencia es la ISO 29821. Se ha leído la vista previa oficial de su edición de 2018 (**«Condition monitoring and
diagnostics of machines — Ultrasound — General guidelines, procedures and validation»**, preparada por
el subcomité 5 del comité técnico 108 de la ISO); según el catálogo de la distribuidora de normas del grupo del Instituto Alemán de Normalización
(**DIN**, *Deutsches Institut für Normung*), DIN Media, esa edición está
anulada y sustituida por la ISO 29821:2026, de abril de 2026, cuyo texto no se ha leído. Lo que sigue
es de la edición de 2018.

Qué es. La norma la define como un **«non-destructive test method used to inspect for airborne and
structure-borne ultrasound above 20 kHz created from or through a medium»**: se escucha el sonido de
alta frecuencia, por encima de 20 kHz, que viaja por el aire (*airborne*, con micrófono ultrasónico)
o por la estructura (*structure-borne*, con sensor de contacto). Las anomalías se detectan como
**«high frequency acoustic events caused by turbulent flow, ionization events, impacts and friction»**,
que proceden, entre otras causas, de **«electrical discharges»**.

Para qué la usa un electricista:

| Uso | Lo que dice la norma |
|---|---|
| Descargas eléctricas en equipos con la envolvente cerrada | Entre las aplicaciones eléctricas de su tabla 1 figuran **«Switchgear»**, **«Transformers»**, **«Insulators»**, **«Junction boxes»** y **«Circuit breaker»** |
| Seguridad antes de abrir un cuadro para la termografía | **«Airborne and structure-borne ultrasound are used to determine if an arc flash hazard is present before opening the cabinet for an infrared thermographic inspection.»** |
| Distinguir una descarga de una vibración | El análisis de la señal **«can also help distinguish the difference between “loose” or 50 Hz to 60 Hz vibrating components such as a transformer winding and the actual electrical discharges»** |
| Descargas parciales en un transformador | Con sensor de contacto, y con cuidado: **«a slight movement of a contact sensor can sound very similar to a partial discharge inside the transformer, which would cause a false indication of an anomaly»**; por eso la norma pone ese caso como ejemplo en el que conviene el sensor de acoplamiento magnético, que elimina la variación de la mano |
| Línea aérea o subestación | El sensor parabólico sirve para **«determining which phase in a high-voltage electrical tower has an electrical discharge»** |
| Rodamientos lentos y lubricación | A veces es el primer aviso, **«such as in the detection of faulty slow-speed bearings and/or insufficient lubrication in rolling element bearings»** |

Y cómo encaja en el predictivo: la norma dice que los equipos son **«typically hand-held, portable
and battery operated»**, pero que también se usan sistemas fijos en línea donde la anomalía
**«shall be addressed at the inception rather than when a route-based inspection is scheduled»**.
Es la misma evolución del epígrafe 3.2: de la ronda con instrumento portátil a la vigilancia en
continuo.

La lectura de oficio para un cuadro: la termografía ve el calor de una conexión floja; el
ultrasonido oye la descarga o el arco, que pueden no calentar todavía, y lo oye sin abrir la
puerta. Son complementarias, y el orden razonable es escuchar antes de abrir. La medida eléctrica
de las descargas parciales no se desarrolla en este tema.

## 4. Gemelo digital de instalaciones

### 4.1 La definición de la norma

La norma de terminología es la ISO/IEC 30173:2023, *Digital twin — Concepts and terminology*,
publicada el 8 de noviembre de 2023 y en vigor según la ficha de catálogo de AENOR, en inglés y sin
versión UNE localizada. Su definición 3.1.1 (vista previa oficial de la norma):

> **«digital twin DTw digital representation (3.1.8) of a target entity (3.1.3) with data
> connections that enable convergence between the physical and digital states at an appropriate
> rate of synchronization»**

Traducción de este temario, no oficial: gemelo digital es la representación digital de una entidad
objetivo con conexiones de datos que permiten la convergencia entre los estados físico y digital a
una tasa de sincronización adecuada.

Y dos notas de la misma definición:

- **«Note 1 to entry: Digital twin has some or all of the capabilities of connection, integration,
  analysis, simulation, visualization, optimization, collaboration, etc.»** (Tiene algunas o todas
  las capacidades de conexión, integración, análisis, simulación, visualización, optimización,
  colaboración, etc.)
- **«Note 2 to entry: Digital twin can provide an integrated view throughout the life cycle of the
  target entity.»** (Puede dar una visión integrada a lo largo de todo el ciclo de vida de la
  entidad objetivo.)

La ficha de catálogo resume el alcance: **«This document establishes terminology for digital twin
(DTw) and describes concepts in the field of digital twin»**. Según su prólogo, la preparó el
**«subcommittee 41: Internet of Things and Digital Twin»** del comité técnico conjunto 1 de la ISO
y la IEC: IoT y gemelo digital van de la mano también en la normalización.

### 4.2 Lo que es y lo que no es

De la definición salen los tres elementos que hay que poder nombrar: la entidad objetivo (la
instalación real), su representación digital (el modelo) y las conexiones de datos que los mantienen
sincronizados. La lectura de oficio que se deriva:

| Esto | ¿Es gemelo digital? | Por qué |
|---|---|---|
| Los planos y el esquema unifilar en papel o en PDF | No | No hay conexión de datos: es documentación |
| Un modelo tridimensional del edificio sin datos en vivo | No, por sí solo | Es la representación, pero le falta la conexión |
| El modelo BIM del edificio, con sus cuadros y líneas, entregado al acabar la obra | No, por sí solo | Es la mejor representación digital de partida, pero sin conexión de datos con la instalación en servicio no cumple la definición |
| El sinóptico del BMS con estados en tiempo real | En parte | Hay conexión y estado, pero no suele haber modelo de la instalación ni simulación |
| Un modelo de la instalación eléctrica (cuadros, líneas, protecciones, cargas) alimentado por las medidas reales y capaz de simular | Sí | Tiene los tres elementos |

El BIM merece párrafo propio, porque se confunde a menudo con el gemelo digital (oficio). La norma
que lo define es la ISO 19650-1:2018, adoptada en España como UNE-EN ISO 19650-1:2019 (en vigor según la ficha de AENOR,
idéntica a la EN ISO 19650-1:2018 y a la ISO 19650-1:2018). Su definición 3.3.14:

> **«building information modelling BIM use of a shared digital representation of a built asset (3.2.8) to
> facilitate design, construction and operation processes to form a reliable basis for decisions»**

Traducción de este temario, no oficial: modelado de información de la construcción es el uso de una
representación digital compartida de un activo construido para facilitar los procesos de diseño,
construcción y explotación y formar una base fiable para las decisiones. La misma norma llama
**«asset information model»** (AIM) al modelo de información **«relating to the operational
phase»**: el de la fase de explotación, que es la del mantenimiento.

Puestas una junto a otra, las dos definiciones responden a la pregunta: el BIM es una
**«digital representation»**, igual que la primera mitad de la definición de gemelo digital; lo que
le falta para ser gemelo son las **«data connections»** con la instalación real y la sincronización
entre ambos estados. Por eso, en la práctica, el BIM de la obra suele ser el punto de partida del
gemelo: se le conectan las medidas del BMS o de los sensores y se mantiene al día (lectura de oficio;
ninguna de las dos normas lo dice así).

La «tasa de sincronización adecuada» de la definición es la clave práctica: un gemelo de
mantenimiento no necesita datos de cada segundo; uno que se use para operar sí. Lo adecuado lo fija
el uso.

### 4.3 Para qué sirve en mantenimiento

Usos en una instalación eléctrica de un edificio técnico (oficio; ninguna norma leída los
enumera):

| Uso | Qué permite |
|---|---|
| Inventario vivo | Cada cuadro, protección y línea con su estado, su historial y sus OT, en el sitio en que está |
| Análisis de impacto antes de una intervención | Ver qué cuelga de un interruptor antes de abrirlo y qué se queda sin servicio (tema 17) |
| Simulación de cambios | Comprobar cargas, caídas de tensión o selectividad antes de añadir un receptor (temas 1 y 3) |
| Predictivo | Comparar el comportamiento medido con el esperado por el modelo y detectar la desviación |
| Formación y simulacros | Ensayar una maniobra o una contingencia sin tocar la instalación |

### 4.4 Su condición: la documentación al día

Un gemelo digital vale lo que valga su parecido con la instalación real. Un modelo que no recoge la
última reforma de un cuadro es peor que no tenerlo, porque da confianza a una información falsa.
Por eso el primer requisito no es tecnológico: es la disciplina de documentación del tema 13
(esquemas actualizados, inventario, cierre de cada OT con lo que se cambió). Sin esa disciplina, el
gemelo se separa de su entidad objetivo, y deja de cumplir la definición: ya no hay
«convergencia entre los estados físico y digital».

## 5. Telegestión energética

### 5.1 Qué es

Telemedida es la medida hecha en un sitio y leída en otro; telemando, la orden dada a distancia;
telegestión, las dos juntas más el registro y la alarma (tema 12, epígrafe 6.1; ninguna norma leída
define las tres palabras). Telegestión energética es esa telegestión aplicada a la energía: leer a
distancia contadores y analizadores, guardar los consumos, compararlos y actuar sobre los equipos
para consumir menos o en otro momento (oficio).

El RITE no la define, pero la nombra en dos sitios: en el nombre de su cuarto nivel de control, el
de **gestión y telegestión** (epígrafe 2.4), y en la IT 2.3.4, apartado 4, que exige personal cualificado
para mantener un **sistema de control, mando y gestión o telegestión basado en la tecnología de la
información**.

### 5.2 Lo que el RITE obliga a medir y registrar

Sin medida no hay telegestión. El RITE, IT 1.2.4.4 (contabilización de consumos), fija los
umbrales a partir de los cuales hay que medir y registrar:

| Apartado | Qué exige (literal) |
|---|---|
| 2 | **Las instalaciones térmicas de potencia útil nominal mayor que 70 kW, en régimen de refrigeración o calefacción, dispondrán de dispositivos que permitan efectuar la medición y registrar el consumo de combustible y energía eléctrica, de forma separada del consumo debido a otros usos del resto del edificio.** |
| 4 | **Las instalaciones térmicas de potencia útil nominal en refrigeración mayor que 70 kW dispondrán de un dispositivo que permita medir y registrar el consumo de energía eléctrica de la central frigorífica (maquinaria frigorífica, torres y bombas de agua refrigerada, esencialmente) de forma diferenciada de la medición del consumo de energía del resto de equipos del sistema de acondicionamiento.** |
| 5 | **Los generadores de calor y de frío de potencia útil nominal mayor que 70 kW dispondrán de un dispositivo que permita registrar el número de horas de funcionamiento del generador.** |
| 6 | **Las bombas y ventiladores de potencia eléctrica del motor mayor que 20 kW dispondrán de un dispositivo que permita registrar las horas de funcionamiento del equipo.** |
| 7 | **Los compresores frigoríficos de más de 70 kW de potencia útil nominal dispondrán de un dispositivo que permita registrar el número de arrancadas del mismo.** |

Las cifras se recuerdan así: 70 kW para todo lo térmico (generadores, centrales, compresores) y
20 kW para los motores de bombas y ventiladores.

Y el apartado 8, que une la telegestión con el autoconsumo y el almacenamiento: **Los generadores
de calor y de frío de potencia útil nominal mayor que 70 kW que dispongan de un suministro directo
de energía renovable eléctrica dispondrán de un dispositivo que permita contabilizar dicha
contribución de forma diferenciada al resto de su consumo eléctrico y, si es técnicamente viable,
se contabilizará la contribución de energía renovable eléctrica producida por instalaciones de
autoconsumo. Dicho dispositivo podrá permitir que se maximice el aprovechamiento energético de la
energía renovable eléctrica haciendo uso de las capacidades de comunicación e interoperabilidad de
las instalaciones técnicas conectadas y los sistemas de almacenamiento que puedan existir.**

Obsérvese el modo de los verbos: contabilizar la contribución renovable directa es obligatorio
(«dispondrán»); la de autoconsumo, sólo «si es técnicamente viable»; y aprovecharla con
comunicaciones y almacenamiento, potestativo («podrá permitir»).

### 5.3 Lo que la telegestión permite en el mantenimiento

El RITE premia la supervisión a distancia en las instalaciones pequeñas. Al pie de la tabla de
periodicidades del mantenimiento preventivo (IT 3.3): **En instalaciones de potencia útil nominal
hasta 70 kW, con supervisión remota en continuo, la periodicidad se puede incrementar hasta 2 años,
siempre que estén garantizadas las condiciones de seguridad y eficiencia energética.**

### 5.4 Los datos de consumo como prueba: el Real Decreto 56/2016

El Real Decreto 56/2016 obliga a **las grandes empresas o grupos de sociedades incluidos en el ámbito
de aplicación del artículo 2** a una auditoría energética cada cuatro años que cubra **al menos, el 85
por ciento del consumo total de energía final** de sus instalaciones en el territorio nacional, o a aplicar un sistema de
gestión energética o ambiental certificado que la incluya (artículo 3.1 y 3.2;
quién está obligado y si lo está la RTVA, en el tema 16). Lo que interesa aquí es lo que exige a
los datos, porque es lo que la telegestión tiene que producir. Artículo 3.3.a): las auditorías
**Deberán basarse en datos operativos actualizados, medidos y verificables, de consumo de energía
y, en el caso de la electricidad, de perfiles de carga siempre que se disponga de ellos.** Y el
artículo 3.5: **Los datos empleados en las auditorías energéticas deberán poderse almacenar para
fines de análisis histórico y trazabilidad del comportamiento energético.**

«Medidos y verificables», «perfiles de carga» y «análisis histórico»: tres exigencias que una
lectura manual de contadores una vez al mes no cumple y que un sistema de telemedida con registro
cumple sin esfuerzo (lectura de oficio).

### 5.5 Las actuaciones de la telegestión energética

Lo que un sistema de telegestión hace con los datos, como oficio (las estrategias de control
completas, en el tema 12, epígrafe 2.3):

| Actuación | Qué consigue |
|---|---|
| Separar consumos por uso y por línea | Saber cuánto gasta la climatización de un CPD frente a la de oficinas |
| Comparar con el mismo periodo anterior o con el de otro edificio | Detectar la desviación que no se ve en la factura total |
| Alarmar por consumo anómalo | Un equipo que no para de noche, una resistencia que se queda conectada |
| Limitar la potencia | Escalonar arranques para no superar la potencia contratada |
| Desplazar consumos | Cargar baterías o preenfriar en las horas en que la energía es más barata o hay excedente de autoconsumo |
| Rotar equipos | Igualar horas de funcionamiento entre bombas o enfriadoras redundantes, para que la de reserva no sea la que se gripa el día que hace falta |

Y la lectura de mantenimiento que esa tabla esconde: casi todas las anomalías de consumo son
averías. Un consumo nocturno que sube es un equipo que no obedece a su programa; un consumo de
bombeo que sube con el mismo caudal es una bomba que se degrada. La telegestión energética es, por
eso, también una herramienta de predictivo.

## 6. Baterías

### 6.1 Por qué las baterías están en un tema de innovación

Un edificio técnico siempre ha tenido baterías: las de los SAI y las de arranque de los grupos
(tema 7). Lo nuevo es triple (lectura de oficio): la química de ion litio, con más energía por kilo
y por litro y más ciclos, pero que exige sistema de gestión y tiene su propio régimen de seguridad;
el almacenamiento estacionario asociado al autoconsumo (epígrafe 7.6); y una norma europea que
regula la batería de la cuna a la tumba y obliga a que algunas guarden los datos de su propio
estado.

| Química | Rasgos de uso (tema 7) |
|---|---|
| Plomo-ácido abierta | Barata, robusta; desprende hidrógeno y exige mantenimiento de nivel |
| Plomo-ácido regulada por válvula | Sin mantenimiento de nivel; la de los SAI clásicos |
| Níquel-cadmio | Muy robusta a temperatura extrema y a descarga profunda; cara |
| Ion litio | Mucha más energía por kilo y por litro, más ciclos; exige sistema de gestión y tiene su propio régimen de seguridad |

«Ion litio» no es una sola química: hay varios materiales de cátodo, y el comportamiento ante el
embalamiento térmico cambia mucho de uno a otro. Lo que sigue sale de dos revisiones científicas de
2026 (fuente técnica: no son norma). Una de ellas nombra como cátodos **«frequently used and
studied»** el óxido de cobalto y litio (**LCO**), el NCM, el óxido de manganeso y litio (**LMO**) y el
LFP. Las dos familias que aquí interesan son el litio-ferrofosfato (LFP) y los óxidos laminares de
níquel, cobalto y manganeso (NMC):

| Rasgo | LFP | NMC |
|---|---|---|
| Estructura del cátodo | Olivino de fosfato, que retiene el oxígeno: **«LFP cathodes exhibit weaker oxygen-release contribution because the olivine phosphate framework stabilizes oxygen»** | Óxido laminar; los ricos en níquel **«exhibit the highest thermal reactivity among layered cathodes and are key drivers of thermal runaway propagation»** |
| Peligrosidad comparada | **«LFP is widely regarded as the safest commercial cathode»** | Una revisión de análisis calorimétricos de varios estudios con celdas comerciales 18650, citada por la segunda revisión, da, con el óxido de níquel, cobalto y aluminio (**NCA**) a la cabeza, **«a general hazard trend of NCA > LCO > NMC > LMO >> LFP»** |
| Propagación del embalamiento en un módulo | Más lenta y menos violenta | **«NCM modules exhibit significantly shorter propagation intervals, higher propagation speeds, and more severe thermal and combustion behavior than LFP modules»** |
| Cómo se manifiesta | **«LFP modules are more likely to release high-speed white smoke without any burning behavior»** | **«NCM-based modules often exhibit intense flaming and jetting»** |

Dos lecturas para quien mantiene una sala de baterías (oficio):

- La química es el primer dato que hay que saber de un sistema de almacenamiento, porque condiciona
  su riesgo. La etiqueta del anexo VI, parte A, del Reglamento (UE) 2023/1542 incluirá la
  **composición química** (epígrafe 6.5, con la fecha de esa etiqueta pendiente); mientras, se pide al
  fabricante.
- Que la LFP sea más estable no la hace inocua: el humo blanco de la tabla es gas que sale de la
  celda, y el anexo V del reglamento prueba precisamente la **emisión de gases** (epígrafe 6.4). La
  ventilación y la detección de la sala no se relajan por la química.

### 6.2 El Reglamento (UE) 2023/1542: qué es y desde cuándo se aplica

El Reglamento (UE) 2023/1542, de 12 de julio de 2023, relativo a las pilas y baterías y sus
residuos, deroga la Directiva 2006/66/CE **con efecto a partir del 18 de agosto de 2025**
(artículo 95), aunque algunas disposiciones de esta siguen aplicándose transitoriamente. Como todo
reglamento europeo, no necesita transposición: su fórmula final, a continuación del artículo 96,
dice que **será obligatorio en todos sus elementos y directamente aplicable en cada Estado
miembro.** Se aplica, con carácter general, **a partir del 18 de febrero de 2024** (artículo
96.2), con fechas propias para algunas partes; entre ellas, el capítulo de gestión de residuos,
**aplicable a partir del 18 de agosto de 2025** (artículo 96.2.c).

Las definiciones que un electricista necesita (artículo 3.1):

| Término | Definición (literal) |
|---|---|
| Batería industrial (punto 13) | **una batería que está específicamente diseñada para usos industriales, destinada a usos industriales tras ser objeto de preparación para la adaptación o de adaptación, o cualquier otra batería de peso superior a 5 kg que no sea una batería para vehículos eléctricos, una batería para medios de transporte ligeros, ni una batería para arranque, encendido o alumbrado** |
| Sistema estacionario de almacenamiento de energía con baterías (punto 15) | **una batería industrial con almacenamiento interno que está específicamente diseñada para almacenar energía eléctrica desde la red y suministrársela o para almacenar energía eléctrica para los usuarios finales y suministrársela, con independencia del lugar en el que se use y la persona que la use** |
| Sistema de gestión de baterías (punto 25) | **un dispositivo electrónico que controla o gestiona las funciones eléctricas y térmicas de una batería para asegurar su seguridad, rendimiento y vida útil, que gestiona y almacena los datos correspondientes a los parámetros para determinar el estado de salud y la vida útil prevista establecidos en el anexo VII y que se comunica con el vehículo, el medio de transporte ligero o el aparato en que se encuentra incorporada la batería, o con una infraestructura de recarga pública o privada** |
| Estado de carga (punto 27) | **la energía disponible en una pila o batería expresada como porcentaje de su capacidad asignada con arreglo a la declaración del fabricante** |
| Estado de salud (punto 28) | **una medición del estado general de una pila o batería recargable y de su capacidad para ofrecer el rendimiento especificado en comparación con su estado inicial** |

Dos lecturas de oficio de esas definiciones, que el reglamento no hace con estas palabras:

- Las baterías de un SAI de edificio o de un almacenamiento de autoconsumo pesan, como conjunto,
  bastante más de 5 kg y no son de vehículo ni de arranque: caen en «batería industrial». La
  batería de arranque del grupo electrógeno, en cambio, es «para arranque, encendido o alumbrado».
- No hay que confundir estado de carga (cuánta energía queda ahora) con estado de salud (cuánto
  queda de la batería que se compró). El primero sirve para operar; el segundo, para mantener.

### 6.3 El sistema de gestión de baterías y el estado de salud

El artículo 14.1 es el que convierte la batería en un equipo sensorizado por norma: **A partir del
18 de agosto de 2024, los datos actualizados de los parámetros para determinar el estado de salud y
la vida útil prevista de las baterías, según se establece en el anexo VII estarán recogidos en el
sistema de gestión de baterías de los sistemas estacionarios de almacenamiento de energía con
baterías, las baterías para medios de transporte ligeros y las baterías para vehículos
eléctricos.**

Qué parámetros son, del anexo VII:

| Parte A: estado de salud (sistemas estacionarios) | Parte B: vida útil prevista (sistemas estacionarios) |
|---|---|
| **1) capacidad restante;** | **1) fecha de fabricación y, si procede, fecha de puesta en servicio de la pila o batería;** |
| **2) en la medida de lo posible, capacidad de potencia restante;** | **2) rendimiento energético;** |
| **3) en la medida de lo posible, eficiencia de ida y vuelta restante;** | **3) rendimiento en términos de capacidad;** |
| **4) evolución de los índices de autodescarga;** | **4) seguimiento de los acontecimientos adversos, como el número de descargas profundas, el tiempo transcurrido en temperaturas extremas o el tiempo transcurrido en carga en temperaturas extremas;** |
| **5) en la medida de lo posible, resistencia óhmica.** | **5) número de ciclos completos de carga y descarga equivalentes.** |

Y quién puede leerlos, artículo 14.2: la persona que **haya adquirido legalmente la batería**,
incluidos los operadores independientes, tiene **en todo momento acceso de solo lectura, no
discriminatorio** a esos datos a través del sistema de gestión, entre otros fines para **evaluar el
valor residual o la vida útil restante de la batería y su capacidad de reutilización, a partir de
la estimación del estado de salud de la batería**.

Lo que eso significa para el mantenedor (oficio): el titular de un almacenamiento estacionario tiene
derecho a leer el estado de salud de su batería sin depender del fabricante, y esos datos son la
materia prima del predictivo (epígrafe 3.3). El seguimiento de los «acontecimientos adversos» de
la parte B (descargas profundas, horas a temperatura extrema) es exactamente lo que acorta la vida
de una batería: la temperatura de la sala de baterías es, en las de plomo, lo que más la acorta
(tema 7), y ahora queda registrada.

### 6.4 La seguridad de los sistemas estacionarios

Artículo 12.1: **Los sistemas estacionarios de almacenamiento de energía con baterías introducidos
en el mercado o puestos en servicio serán seguros durante su funcionamiento y uso normales.** Y su
documentación técnica, **A más tardar el 18 de agosto de 2024** (artículo 12.2), debe demostrarlo
con pruebas de los parámetros de seguridad del anexo V (que **solo se aplicarán en la medida en que
exista un peligro correspondiente** para ese sistema en las condiciones previstas por el fabricante) e incluir, letra d), **instrucciones de
mitigación en caso de que puedan producirse los peligros identificados, por ejemplo, un incendio o
una explosión.**

Los once parámetros de seguridad del anexo V, por sus títulos: **1. Choque térmico y ciclos**;
**2. Protección frente a cortocircuitos externos**; **3. Protección frente a la sobrecarga**;
**4. Protección frente a la descarga excesiva**; **5. Protección frente al sobrecalentamiento**;
**6. Protección frente a la propagación térmica**; **7. Daños mecánicos provocados por fuerzas
externas**; **8. Cortocircuito interno**; **9. Abuso térmico**; **10. Ensayo de exposición al
fuego**; **11. Emisión de gases**.

El que más importa a quien mantiene una sala de baterías de litio es el 6: **Un embalamiento
térmico en una celda puede provocar una reacción en cascada por toda la batería, que puede estar
compuesta por muchas celdas. Esto puede ocasionar consecuencias graves, incluida una liberación
importante de gas.** De ahí tres reglas de oficio: las instrucciones de mitigación del fabricante
(12.2.d) se tienen en la sala y se conocen antes de la emergencia; la alarma del sistema de gestión
por temperatura de celda es de prioridad máxima; y la protección contra incendios de la sala se
coordina con lo que diga esa documentación (tema 11).

### 6.5 Etiquetas, código QR y pasaporte

El artículo 13 escalona las obligaciones de marcado:

| Desde | Qué (artículo 13) |
|---|---|
| 18/08/2025 | **todas las pilas o baterías llevarán marcado el símbolo de recogida separada** (apartado 4) |
| 18/08/2026, o 18 meses después de la entrada en vigor del acto de ejecución del apartado 10, **si esta fecha es posterior** | Etiqueta con la información general del anexo VI, parte A (apartado 1) |
| 18/02/2027 | **todas las pilas o baterías llevarán marcado un código QR** (apartado 6) |

Ese acto de ejecución no se ha podido comprobar, así que este tema no afirma cuál de las dos fechas
rige para la etiqueta del apartado 1.

La etiqueta del anexo VI, parte A, incluye, entre otros datos, la **fecha de fabricación (mes y
año)**, la **capacidad**, la **composición química** y el **agente extintor utilizable**. Este
último es el dato de la etiqueta que más importa en mantenimiento: dice con qué se apaga esa
batería.

Y el código QR da acceso, en las **baterías industriales con una capacidad superior a 2 kWh**, al
**pasaporte para baterías** (artículo 13.6.a). Una batería de SAI o de almacenamiento de más de
2 kWh tendrá, por tanto, pasaporte. El pasaporte lo regulan los artículos 77 y 78, y este tema no da
su contenido.

### 6.6 Cuando la batería se retira

El capítulo VIII (residuos) es aplicable desde el 18 de agosto de 2025. Su artículo 61.1 obliga a
los productores de baterías industriales o, **de haber sido designadas con arreglo al artículo 57,
apartado 1, las organizaciones competentes en materia de responsabilidad del productor**, a aceptar
la devolución de los residuos de baterías industriales **de manera
gratuita y sin obligación para el usuario final de comprar una batería nueva ni de haberles comprado
a ellos la batería**, y a garantizar su recogida separada. Para el mantenedor, eso significa que la
batería de SAI retirada no va al contenedor general ni se acumula en un almacén: se entrega por el
sistema de recogida del productor (la gestión de residuos de la instalación, en el tema 16).

Si la norma española de adaptación a este reglamento existe y si el Real Decreto 106/2008, de pilas
y acumuladores, sigue vigente en todo o en parte, no se ha comprobado: el tema no lo afirma.

### 6.7 El mantenimiento de las baterías, con lo nuevo

Lo que no cambia (tema 7): inspección visual, temperatura de la sala, apriete de conexiones,
prueba de descarga como única medida de la autonomía real, y el aviso de seguridad de que una
batería no tiene interruptor: no se puede dejar sin tensión, y su corriente de cortocircuito es
enorme; se trabaja con herramienta aislada, sin anillos ni relojes y con protección facial.

Lo que añade la innovación (oficio):

| Tarea | Por qué |
|---|---|
| Leer y archivar los datos del sistema de gestión (estado de salud, ciclos, acontecimientos adversos) | Es el histórico del predictivo, y el reglamento garantiza el derecho a leerlo |
| Revisar las alarmas del sistema de gestión y su comunicación con el BMS | Una batería de litio que pierde la comunicación con su sistema de gestión no está vigilada |
| Comprobar que la ventilación y la climatización de la sala funcionan | La temperatura acorta la vida y es la condición del embalamiento |
| Tener a mano las instrucciones de mitigación y el agente extintor de la etiqueta | Artículo 12.2.d y anexo VI |
| No mezclar elementos nuevos con viejos | En una cadena en serie, el elemento más débil limita a toda la rama (tema 7) |

## 7. Autoconsumo

### 7.1 Qué es, y qué no

La norma es el Real Decreto 244/2019, de 5 de abril, por el que se regulan las condiciones
administrativas, técnicas y económicas del autoconsumo de energía eléctrica. Sus artículos 3 y 4
se han reformado varias veces; la redacción vigente es la del Real Decreto-ley 7/2026, de 20 de
marzo, en vigor desde el 22 de marzo de 2026.

La definición, artículo 3.l): **Autoconsumo: De acuerdo con lo previsto en el artículo 9.1 de la
Ley 24/2013, de 26 de diciembre, se entenderá por autoconsumo, el consumo por parte de uno o varios
consumidores de energía eléctrica proveniente de instalaciones de producción próximas a las de
consumo y asociadas a los mismos.**

El ámbito, artículo 2: se aplica a las instalaciones y sujetos de cualquier modalidad **que se
encuentren conectados a las redes de transporte o distribución**, y el apartado 2 excluye dos casos:

| Situación | ¿Es autoconsumo de este real decreto? |
|---|---|
| Instalación conectada a la red de transporte o distribución | Sí |
| **instalaciones aisladas** | No |
| **grupos de generación utilizados exclusivamente en caso de una interrupción de alimentación de energía eléctrica de la red eléctrica de acuerdo con las definiciones del artículo 100 del Real Decreto 1955/2000** | No |

La segunda exclusión es la que interesa a un edificio técnico: el grupo electrógeno de emergencia
no es autoconsumo, siempre que se use exclusivamente ante una interrupción. El artículo 2.2 remite,
para saber qué es ese grupo, a las definiciones del artículo 100 del Real Decreto 1955/2000, de 1 de
diciembre, **por el que se regulan las actividades de transporte, distribución, comercialización,
suministro y procedimientos de autorización de instalaciones de energía eléctrica**, que este tema
no reproduce. Si se arrancara para
recortar puntas de consumo o para otra cosa, dejaría de estar en la exclusión (lectura de oficio:
el uso decide el régimen, no el aparato; los matices los darían esas definiciones, no leídas).

Y qué es «aislada», artículo 3.d): **Aquella en la que no existe en ningún momento capacidad física
de conexión eléctrica con la red de transporte o distribución ni directa ni indirectamente a través
de una instalación propia o ajena. Las instalaciones desconectadas de la red mediante dispositivos
interruptores o equivalentes no se considerarán aisladas a los efectos de la aplicación de este real
decreto.** Abrir un interruptor no convierte una instalación en aislada.

En el REBT, la ITC-BT-40 (apartado 2) clasifica las instalaciones generadoras en aisladas,
asistidas e interconectadas (tema 7, epígrafe 4.1), y dice de las interconectadas: **Las
instalaciones generadoras interconectadas para autoconsumo, podrán pertenecer a las modalidades de
suministro con autoconsumo sin excedentes o modalidades de suministro con autoconsumo con
excedentes** definidas en la Ley 24/2013 y en el artículo 4 del Real Decreto 244/2019. Una
fotovoltaica de autoconsumo en la cubierta de un edificio es, por tanto, una instalación generadora
interconectada.

### 7.2 Las modalidades

El artículo 4 da la clasificación, y hay que saberla con sus nombres:

| Modalidad (artículo 4) | Qué la define (literal) | Sujetos |
|---|---|---|
| Sin excedentes (4.1.a) | **se deberá instalar un mecanismo antivertido que impida la inyección de energía excedentaria a la red de transporte o de distribución** | **un único tipo de sujeto**: **el sujeto consumidor** |
| Con excedentes (4.1.b) | **las instalaciones de producción próximas y asociadas a las de consumo podrán, además de suministrar energía para autoconsumo, inyectar energía excedentaria en las redes de transporte y distribución** | Dos: **el sujeto consumidor y el productor** |
| Con excedentes acogida a compensación (4.2.a) | **voluntariamente el consumidor y el productor opten por acogerse a un mecanismo de compensación de excedentes** | Dos |
| Con excedentes no acogida a compensación (4.2.b) | Las que **no cumplan con alguno de los requisitos** para la compensación **o que voluntariamente opten por no acogerse** | Dos |

La primera partición es técnica (hay antivertido o no lo hay); la segunda, voluntaria y
condicionada. De ahí que sólo haya un sujeto en la modalidad sin excedentes: si no se vierte, no
hay producción que vender.

El mecanismo antivertido, artículo 3.k): **Dispositivo o conjunto de dispositivos que impide en todo
momento el vertido de energía eléctrica a la red. Estos dispositivos deberán cumplir con la
normativa de calidad y seguridad industrial que le sea de aplicación y, en particular, en el caso de
la baja tensión con, lo previsto en la ITC-BT-40.**

Las cinco condiciones de la compensación, artículo 4.2.a), acumulativas:

1. **La fuente de energía primaria sea de origen renovable.**
2. **La potencia total de las instalaciones de producción asociadas no sea superior a 100 kW.**
3. **Si resultase necesario realizar un contrato de suministro para servicios auxiliares de
   producción, el consumidor haya suscrito un único contrato de suministro para el consumo asociado
   y para los consumos auxiliares de producción con una empresa comercializadora**.
4. **El consumidor y productor asociado hayan suscrito un contrato de compensación de excedentes de
   autoconsumo definido en el artículo 14 del presente real decreto.**
5. **La instalación de producción no tenga otorgado un régimen retributivo adicional o
   específico.**

La quinta se resume en que no se puede cobrar dos veces (lectura de oficio).

Además, el artículo 4.3 añade una clasificación que se cruza con la anterior: **individual o
colectivo en función de si se trata de uno o varios consumidores los que estén asociados a las
instalaciones de generación.** En el colectivo, todos los consumidores de la misma instalación
**deberán pertenecer a la misma modalidad de autoconsumo** y comunicar **de forma individual** a la
distribuidora **un mismo acuerdo firmado por todos los participantes que recoja los criterios de
reparto**. La comunicación es individual; el acuerdo, único.

### 7.3 Qué potencia tiene una instalación fotovoltaica

Para comprobar el límite de 100 kW hay que saber cómo se mide. Artículo 3.h): **En el caso de
instalaciones fotovoltaicas, la potencia instalada será la potencia máxima del inversor o, en su
caso, la suma de las potencias máximas de los inversores.**

Es decir, cuenta el inversor, no los paneles. Una cubierta con módulos que suman más de 100 kW pico
conectados a inversores cuya potencia máxima suma 100 kW o menos cumple la condición de potencia de
la compensación (ejemplo de aplicación de este temario, no de la norma).

Y la cifra de 100 kW reaparece en la definición de instalación de producción, artículo 3.c): aunque
no estén inscritas en el registro, también tienen esa consideración las instalaciones de
generación que **Tengan una potencia no superior a 100 kW**, **Estén asociadas a modalidades de
suministro con autoconsumo** y **Puedan inyectar energía excedentaria en las redes de transporte y
distribución**.

### 7.4 Qué instalaciones son «próximas»

El autoconsumo exige generación próxima. Artículo 3.g), en su redacción vigente, se cumple alguna
de estas condiciones:

| Condición | Texto (literal) |
|---|---|
| i | **Estén conectadas a la red interior de los consumidores asociados o estén unidas a éstos a través de líneas directas.** |
| ii | **Estén conectadas a cualquiera de las redes de baja tensión derivada del mismo centro de transformación.** |
| iii | **Se encuentren conectados a una distancia inferior a 500 metros de los consumidores asociados. A tal efecto se tomará la distancia entre los equipos de medida en su proyección ortogonal en planta.** |
| iii, segundo párrafo | **aquella instalación de generación que empleando tecnología fotovoltaica o eólica con una potencia de hasta 5 MW, esta se conecte al consumidor o consumidores a través de las líneas de transporte o distribución y siempre que estas se encuentren a una distancia inferior a 5.000 metros de los consumidores asociados.** |
| iv | **Estén ubicados, tanto la generación como los consumos, en una misma referencia catastral según sus primeros 14 dígitos** (o según la disposición adicional vigésima del Real Decreto 413/2014) |

El segundo párrafo del iii es el que más ha cambiado, y su redacción actual es la del Real
Decreto-ley 7/2026. La inmediatamente anterior (la del Real Decreto-ley 20/2022, que volvió a regir
tras la derogación del Real Decreto-ley 7/2025) lo limitaba a la planta **que empleando
exclusivamente tecnología fotovoltaica** estuviera **ubicada en su totalidad en la cubierta de una o
varias edificaciones, en suelo industrial o en estructuras artificiales existentes o futuras cuyo
objetivo principal no sea la generación de electricidad**, a una distancia **inferior a 2.000
metros**. Hoy alcanza a fotovoltaica o eólica de hasta 5 MW, sin exigencia de ubicación, y a menos de
5.000 metros. El primer párrafo sigue en 500 metros. Un temario anterior a marzo de 2026 dará otras
cifras.

Y los dos nombres que salen de esa lista: **Aquellas instalaciones próximas y asociadas que cumplan
la condición i de esta definición se denominarán instalaciones próximas de red interior. Aquellas
instalaciones próximas y asociadas que cumplan las condiciones ii, iii o iv de esta definición se
denominarán instalaciones próximas a través de la red.**

### 7.5 Cambiar de modalidad y estar en dos a la vez

Artículo 4.5: se puede pasar a cualquier otra modalidad, adecuando las instalaciones. **No
obstante lo anterior:**

- **a) En el caso de autoconsumo colectivo, dicho cambio deberá ser llevado a cabo simultáneamente
  por todos los consumidores participantes del mismo, asociados a la misma instalación de
  generación.**
- **b) En ningún caso un sujeto consumidor podrá estar asociado de forma simultánea a más de una de
  las modalidades de autoconsumo reguladas en el presente artículo con la única excepción de un
  autoconsumo individual sin excedentes combinado con un autoconsumo mediante instalaciones próximas
  y asociadas a través de la red.**
- **c) En aquellos casos en que se realice autoconsumo mediante instalaciones próximas y asociadas a
  través de la red, el autoconsumo deberá pertenecer a la modalidad de suministro con autoconsumo
  con excedentes.**

La excepción de la letra b) la introdujo la Ley 9/2025, de 3 de diciembre, de Movilidad
Sostenible (en vigor desde el 5 de diciembre de 2025), entonces como inciso «ii.»; el Real
Decreto-ley 7/2026 renombró los incisos como letras. Conviene no olvidarla: un centro de trabajo puede tener a la vez
su fotovoltaica de cubierta sin excedentes y participar en un autoconsumo a través de la red. Y la
c) dice que la proximidad a través de la red excluye el antivertido.

Y la comunidad de energías renovables no está en el apartado 5, sino en el 7: **Para la
realización del autoconsumo colectivo podrá constituirse una comunidad de energías renovables
siempre que se cumpla con los requisitos establecidos para las mismas.** Puede representar a los
consumidores **siempre que estos otorguen las correspondientes autorizaciones.**

### 7.6 Las baterías en el autoconsumo

El real decreto autoriza el almacenamiento y fija dónde va. Artículo 5.7: **Podrán instalarse
elementos de almacenamiento en las instalaciones de autoconsumo reguladas en este real decreto,
cuando dispongan de las protecciones establecidas en la normativa de seguridad y calidad industrial
que les sea de aplicación.** Y: **Los elementos de almacenamiento se encontrarán instalados de tal
forman que compartan equipo de medida que registre la generación neta, equipo de medida en el
punto frontera o equipo de medida del consumidor asociado.**

La condición de ubicación evita que la batería quede fuera del perímetro que se mide (lectura de
oficio). Y la batería de ese almacenamiento es, en el Reglamento (UE) 2023/1542, un sistema
estacionario de almacenamiento de energía con baterías, con todo lo del epígrafe 6.

### 7.7 Responsabilidad y corte de suministro

Artículo 5, lo que hay que saber:

| Regla | Texto |
|---|---|
| Titulares distintos (5.2) | **el consumidor y el propietario de la instalación de generación podrán ser personas físicas o jurídicas diferentes** |
| Sin excedentes (5.3) | **el titular del punto de suministro será el consumidor, el cual también será el titular de las instalaciones de generación conectadas a su red**; en el colectivo, la titularidad de la generación y del antivertido **será compartida solidariamente por todos los consumidores asociados** |
| Con excedentes que comparten conexión o están en red interior (5.4) | **los consumidores y productores responderán solidariamente por el incumplimiento** |
| Corte (5.6) | **Cuando por incumplimiento de requisitos técnicos existan instalaciones peligrosas o cuando se haya manipulado el equipo de medida o el mecanismo antivertido**, la distribuidora **podrá proceder a la interrupción de suministro** |

Para el mantenimiento, el 5.6 es el aviso: tocar el antivertido o el equipo de medida sin
procedimiento puede costar el suministro del edificio.

### 7.8 La compensación simplificada

El artículo 14.3 define el mecanismo: **un saldo en términos económicos de la energía consumida en
el periodo de facturación**. Se compensan euros, no kilovatios hora (lectura de oficio).

| Contrato de suministro | Energía consumida de la red | Energía excedentaria |
|---|---|---|
| Con comercializadora libre | **al precio horario acordado entre las partes** | **al precio horario acordado entre las partes** |
| PVPC, con comercializadora de referencia | Al coste horario de energía del PVPC en cada hora | Al precio medio horario del mercado diario e intradiario menos el coste de los desvíos |

Y los límites, del mismo apartado: **En ningún caso, el valor económico de la energía horaria
excedentaria podrá ser superior al valor económico de la energía horaria consumida de la red en el
periodo de facturación, el cual no podrá ser superior a un mes.** La factura de energía puede
llegar a cero, no a negativo (lectura de oficio). Y, si consumidor y productor se acogen a la
compensación, el productor **no podrá participar de otro mecanismo de venta de energía.**

El apartado 4: la energía excedentaria compensada **no tendrá consideración de energía incorporada
al sistema eléctrico** y por eso está exenta de los peajes de acceso de productores, **si bien el
comercializador será el responsable de balance de dicha energía.** Y el 2: el autoconsumo colectivo
sin excedentes también puede acogerse a compensación, y entonces **no será necesaria la existencia
de contrato de compensación de excedentes, al no existir productor**; basta **un acuerdo entre todos
los sujetos consumidores**.

### 7.9 Lo que el electricista comprueba: la ITC-BT-40

Lo técnico del autoconsumo está en el REBT, ITC-BT-40, apartado 4.3 (instalaciones generadoras
interconectadas), en la redacción que le dio el propio Real Decreto 244/2019:

- Alcance: **Las prescripciones de la ITC-BT-40 son aplicables a todas instalaciones de autoconsumo
  interconectadas, sea cual sea su potencia.**
- Protecciones frente a la red: **Todas las instalaciones de generación interconectadas a la red de
  distribución en baja tensión deben disponer de dispositivos que limiten la inyección de corriente
  continua y la generación de sobretensiones, así como impedir el funcionamiento en isla de dicha
  red de distribución**.
- Antivertido: las de autoconsumo sin excedentes **deberán disponer de un sistema que evite el
  vertido de energía a la red de distribución que cumpla los requisitos y ensayos del nuevo anexo I
  de la ITC-BT-40.**
- Documentación: las sin excedentes **se ajustarán a lo establecido en la ITC-BT-04 en cuanto a su
  documentación y puesta en servicio** (tema 2), y la documentación de evaluación de conformidad del
  anexo I **será entregada por el instalador junto con el certificado de la instalación.**
- Cuadro y diferencial: en las instalaciones próximas, **la conexión se realizará a través de un
  cuadro de mando y protección que incluya las protecciones diferenciales tipo A necesarias para
  garantizar que la tensión de contacto no resulte peligrosa para las personas.** Si son accesibles
  al público general o están en zonas residenciales o análogas, **la protección diferencial de los
  circuitos de generación será de 30 mA.**
- Circuito dedicado: **Todos los generadores para suministro con autoconsumo con excedentes
  independientemente de su potencia y los generadores para suministro con autoconsumo sin
  excedentes de potencia instalada superior a 800 VA, que se conecten a instalaciones interiores o
  receptoras de usuario, lo harán a través de un circuito independiente y dedicado desde un cuadro
  de mando y protección que incluya protección diferencial tipo A**.
- Potencia admisible en baja tensión (4.3.1): **Con carácter general la interconexión de centrales
  generadoras a las redes de baja tensión de 3x400/230 V será admisible cuando la suma de las
  potencias nominales de los generadores no exceda de 100 kVA, ni de la mitad de la capacidad de la
  salida del centro de transformación correspondiente a la línea de la Red de Distribución Pública a
  la que se conecte la central.** A las de autoconsumo sin excedentes **no les son de aplicación los
  apartados 4.3.1, 4.3.4** ni los requisitos relacionados con la empresa distribuidora del apartado 9
  (apartado 4.3).

Las dos cosas que el funcionamiento en isla esconde, como oficio y como seguridad: si la red de la
distribuidora cae y el inversor siguiera generando, la línea que el operario de la distribuidora
cree sin tensión la tendría. Por eso el anti-isla es una protección de personas, y por eso, al
consignar un cuadro que tiene un generador conectado, hay que contar con dos fuentes (cinco reglas
de oro, tema 15): la red y el inversor.

### 7.10 El mantenimiento de una fotovoltaica de autoconsumo

No hay periodicidades de mantenimiento fotovoltaico en las normas leídas para este tema. Lo que
sigue es oficio:

| Elemento | Qué se revisa |
|---|---|
| Módulos | Suciedad, sombras nuevas, roturas, puntos calientes (termografía con sol) |
| Cableado de corriente continua y conectores | Apriete, estado del aislamiento, conectores sin calentamiento |
| Inversores | Alarmas y registro de eventos, ventilación, rendimiento comparado entre inversores iguales |
| Cuadro de protecciones | Diferencial (prueba), protecciones, antivertido si lo hay |
| Producción | Comparación con la esperada para la irradiación del periodo: la caída de producción es el aviso del predictivo |

La última fila une el autoconsumo con el resto del tema: el inversor y el contador de generación
son sensores, y su dato, leído por telegestión y comparado con su histórico, es el que dice que algo
falla antes de que nadie suba a la cubierta.

### 7.11 Aplicación a un edificio técnico

Las decisiones que un electricista ve tomar con este epígrafe delante (oficio):

| Situación | Qué la gobierna |
|---|---|
| Fotovoltaica en la cubierta de un centro de trabajo que consume más de lo que produce | Suele bastar sin excedentes, con antivertido (ITC-BT-40, anexo I); un solo sujeto |
| La misma, si se quiere verter y compensar | Con excedentes acogida a compensación: renovable, inversores que sumen 100 kW o menos, contrato del artículo 14 |
| Más de 100 kW de inversores | Fuera de la compensación: si se quiere verter, con excedentes no acogida; si no, sin excedentes, con antivertido |
| Grupo electrógeno de emergencia | No es autoconsumo (artículo 2.2), si se usa sólo ante una interrupción |
| Baterías para aprovechar el excedente | Artículo 5.7 (dentro del perímetro de medida) y Reglamento (UE) 2023/1542 |

Y la observación de escala: un centro de producción con platós y CPD consume de día de forma
continua, así que la fotovoltaica de su cubierta se autoconsume casi entera; el excedente, y con él
la compensación, importan menos que en una vivienda (lectura de oficio; depende de cada edificio).

## 8. Automatización de edificios

### 8.1 Quién tiene que tenerla y qué tiene que saber hacer

La obligación está en el RITE, IT 1.2.4.3.5, apartado 1 (desarrollada en el tema 12, epígrafe
1.3): **Cuando sea técnica y económicamente viable, los edificios no residenciales con una
potencia nominal útil para instalaciones de calefacción, refrigeración, instalaciones combinadas de
calefacción y ventilación, o para instalaciones combinadas de refrigeración y ventilación de más de
290 kW deberán estar equipados con sistemas de automatización y control de edificios.**

Tres condiciones juntas: edificio no residencial, más de 290 kW y viabilidad técnica y económica.
Los residenciales no están obligados: el apartado 2 dice que **podrán** estar equipados.

Y lo que el sistema tiene que ser capaz de hacer, las tres letras del apartado 1, que son en sí
mismas un programa de innovación en el mantenimiento:

- **a) Monitorizar, registrar, analizar y permitir la adaptación del consumo de energía de forma
  continua;** (telegestión energética, epígrafe 5)
- **b) Efectuar una evaluación comparativa de la eficiencia energética del edificio, detectar las
  pérdidas de eficiencia de sus instalaciones técnicas e informar sobre las posibilidades de mejora
  de la eficiencia energética a la persona responsable de la instalación o de la gestión técnica del
  edificio;** (predictivo, epígrafe 3)
- **c) Permitir la comunicación con instalaciones técnicas conectadas y otros aparatos que estén
  dentro del edificio, así como garantizar la interoperabilidad con instalaciones técnicas del
  edificio de distintos tipos de tecnologías patentadas, dispositivos y fabricantes.**
  (sensorización e integración, epígrafe 2)

### 8.2 La norma que cita el RITE, y la que la ha sustituido

El mismo apartado remite a una norma técnica: **Será considerado, a efectos de esta exigencia, la
automatización y el control que tienen un impacto en la eficiencia energética del edificio, como
los recogidos en la norma UNE-EN 15232-1.**

Esa norma ya no está en vigor en el catálogo de normas. La ficha de AENOR de la
**UNE-EN ISO 52120-1:2022**, **Eficiencia energética de los edificios. Contribución de la
automatización, el control y la gestión de los edificios. Parte 1: Marco general y procedimientos.
(ISO 52120-1:2021, Versión corregida 2022-09).**, de **2022-10-19** y **En Vigor**, dice que
**Anula a UNE-EN 15232-1:2018**.

Cómo se contesta, por tanto: el RITE cita la UNE-EN 15232-1 (y eso es lo que dice la norma
reglamentaria, que no se ha modificado); en el catálogo de normas UNE, esa norma está anulada y
sustituida por la UNE-EN ISO 52120-1:2022. El contenido de ninguna de las dos se ha leído.

### 8.3 Ponerla en marcha, documentarla y mantenerla

El apartado 3 de la misma IT fija tres cosas que son de mantenimiento:

- Comprobar y ajustar en uso real: **Una vez instalado el sistema de automatización y control, será
  necesario realizar acciones de comprobación de que el sistema funciona con arreglo a sus
  especificaciones y acciones de ajuste, en su caso, en la instalación en condiciones de uso real.**
- Configurarla para el mínimo consumo, teniendo en cuenta **los periodos de inactividad del
  edificio, el uso de los espacios, los regímenes de operación en el punto de máximo rendimiento de
  los equipos y el máximo aprovechamiento de las energías renovables y residuales disponibles.**
- Documentarla: **Las indicaciones e instrucciones para la correcta operación del sistema de
  automatización y control deberán recogerse en el ''Manual de Uso y Mantenimiento''.**

La IT 2.3.4 añade las pruebas del control automático en la puesta en servicio (apartado 1: **Se
ajustarán los parámetros del sistema de control automático a los valores de diseño especificados en
el proyecto o memoria técnica y se comprobará el funcionamiento de los componentes que configuran el
sistema de control.**), su seguimiento por niveles (epígrafe 2.4), y que **Son válidos a estos
efectos los protocolos establecidos en la norma UNE-EN-ISO 16484-3.** Y el apartado 4, ya citado,
reserva el mantenimiento de los programas a **personal cualificado o** al **mismo suministrador de
los programas.**

### 8.4 Lo que se gana: la exención de inspecciones

La IT 4.3.4, párrafo segundo: **Los edificios no residenciales que cuenten con un sistema de
automatización y control que cumpla los requisitos establecidos en el apartado 1 de la IT
1.2.4.3.5, así como los edificios residenciales que cuenten con un sistema de automatización y
control que cumpla los requisitos establecidos en el apartado 2 de la IT 1.2.4.3.5, quedarán exentos
del cumplimiento de los requisitos establecidos en la IT 4.2.1, IT 4.2.2 y IT 4.2.3.** Es decir, de
las inspecciones periódicas de eficiencia energética de los sistemas de calefacción, ventilación y agua
caliente sanitaria, de los de aire acondicionado y ventilación, y de la instalación térmica completa
(tema 10).

La condición es «que cumpla los requisitos»: las tres capacidades a), b) y c). Un sistema que sólo
arranca y para equipos por horario no exime (lectura de oficio, como en el tema 12).

### 8.5 Las estrategias que ahorran y las que cuidan los equipos

Las estrategias de control (tema 12, epígrafe 2.3) se dividen, a efectos de este tema, en dos
grupos (oficio):

| Estrategia | Ahorra energía | Alarga la vida de los equipos |
|---|---|---|
| Programación horaria y arranque y parada óptimos | Sí | Menos horas de funcionamiento |
| Control por ocupación | Sí | Menos horas |
| Enfriamiento gratuito con aire exterior | Sí | Menos horas de compresor |
| Limitación de potencia | En factura | Evita arranques simultáneos |
| Rotación de equipos redundantes | No | Sí: iguala horas y prueba la reserva |
| Registro de horas y arranques | No | Sí: es el dato del mantenimiento por condición |

La diferencia entre programación horaria y arranque óptimo se pregunta: la programación horaria
arranca a una hora fija; el arranque óptimo calcula cada día a qué hora hay que arrancar para
llegar a la consigna justo a la hora de ocupación.

Y el principio de autonomía, que es el que decide si la automatización aguanta un fallo (oficio):
cada nivel debe seguir funcionando si el de arriba desaparece. Un controlador sin puesto central
sigue regulando; una válvula con posicionador local se queda en su última consigna. Un edificio
automatizado que queda a oscuras cuando cae un servidor está mal diseñado.

### 8.6 La automatización en un edificio que emite

Los conflictos entre la automatización y la producción audiovisual (la parada óptima contra el
directo, el ruido de la climatización contra el sonido directo, el apagado por presencia junto a un
plató) y su solución común, que el sistema conozca el estado de producción del edificio, están en
el tema 12, epígrafe 7.5.

Lo que añade este tema es la regla para las salas técnicas (oficio): en un CPD, un control de
emisión o un centro emisor, la automatización que ahorra energía nunca puede tener la última
palabra sobre la que mantiene la temperatura. Las estrategias de ahorro se aplican a oficinas y
zonas comunes; en las salas técnicas, la consigna la manda la continuidad del servicio (temas 8 y
9).

## Normativa que el tema invoca

| Norma | Preceptos usados | Redacción |
|---|---|---|
| Real Decreto 244/2019, de 5 de abril, de autoconsumo de energía eléctrica (BOE-A-2019-5089) | Artículos 2, 3 (letras c, d, g, h, k, l), 4 (apartados 1, 2, 3, 5 y 7), 5 (apartados 2, 3, 4, 6 y 7) y 14 (apartados 2, 3 y 4) | Artículos 3 y 4: Real Decreto-ley 7/2026 (desde 22/03/2026). Resto: original (desde 07/04/2019) |
| Real Decreto 842/2002, Reglamento electrotécnico para baja tensión (BOE-A-2002-18099) | ITC-BT-40, apartados 2, 4.3 y 4.3.1 | La del Real Decreto 244/2019 (desde 07/04/2019) |
| Reglamento (UE) 2023/1542, de pilas y baterías (DOUE L 191, de 28/07/2023) | Artículos 3.1 (puntos 13, 15, 25, 27 y 28), 12, 13, 14, 61.1, 95 y 96; anexos V, VI (parte A) y VII | Texto publicado; correcciones de errores de 2024, 2025 y 2026 y modificaciones (artículo 77 por el Reglamento (UE) 2024/1781, artículo 48 por el Reglamento (UE) 2025/1561, anexo I por el Reglamento (UE) 2026/1738) cotejadas: ninguna afecta a estos preceptos |
| Real Decreto 1027/2007, Reglamento de instalaciones térmicas en los edificios (BOE-A-2007-15820) | Apéndice 1 (definiciones de instalación técnica del edificio, instalación térmica y los cuatro niveles); IT 1.2.4.3.5; IT 1.2.4.4, apartados 2 y 4 a 8; IT 2.3.4; IT 3.3 (nota a la tabla de periodicidades); IT 4.3.4 | IT 1, IT 3, IT 4 y apéndice 1: la del Real Decreto 178/2021 (desde 01/07/2021). IT 2: original (desde 29/02/2008) |
| Real Decreto 56/2016, de auditorías energéticas (BOE-A-2016-1460) | Artículo 3, apartados 1, 3.a) y 5 | Original (desde 14/02/2016) |

## Lo que este tema no da, y dónde está

- La definición normativa de IoT (ISO/IEC 20924) no se ha podido leer: el tema no la da. Del gemelo
  digital da la definición de la ISO/IEC 30173 en inglés, con traducción propia; no hay versión UNE
  localizada.
- El texto de las normas ISO/IEC 30141, ISO 17359, UNE-EN 15232-1, UNE-EN ISO 52120-1 y UNE-EN ISO
  16484-3: sólo se han leído sus fichas de catálogo, las primeras páginas de su vista previa o lo que
  el RITE dice de ellas. De la UNE-EN ISO 19650-1 y de la ISO 29821:2018, sólo las primeras páginas
  de la vista previa; la ISO 29821:2026, que sustituye a la de 2018, no se ha leído.
- Las especificaciones completas de LoRaWAN, NB-IoT y MQTT: sólo se ha leído lo citado (la página
  de la especificación de la LoRa Alliance, dos noticias técnicas del 3GPP y la introducción de la
  norma MQTT 5.0). Ni bandas de frecuencia, ni alcances, ni duraciones de pila: ninguna de esas cifras
  se ha confirmado en la fuente, y el tema no las da. Tampoco otras tecnologías radio ni la
  seguridad de esas redes más allá del epígrafe 2.5.
- La medida eléctrica de descargas parciales y su norma; las cifras de temperatura de inicio del
  embalamiento térmico de cada química de litio, que varían de un estudio a otro.
- La fecha efectiva de la etiqueta del artículo 13.1 del Reglamento (UE) 2023/1542 (depende de un
  acto de ejecución no localizado); el contenido del pasaporte de baterías; la norma española de
  adaptación a ese reglamento y la vigencia del Real Decreto 106/2008.
- El contenido del anexo I de la ITC-BT-40 (requisitos y ensayos del antivertido) y del resto de la
  ITC-BT-40 (protecciones, puesta a tierra, medida): sólo se citan los apartados indicados.
- El artículo 100 del Real Decreto 1955/2000, al que remite el artículo 2.2 del Real Decreto 244/2019
  para definir los grupos de emergencia excluidos: no se ha leído.
- El Real Decreto 1699/2011, de conexión a red de instalaciones de pequeña potencia, y los trámites
  administrativos del autoconsumo (registro, acceso y conexión, contrato de acceso): no se
  desarrollan. El anexo I del Real Decreto 244/2019 (criterios de reparto) se nombra y no se
  reproduce. Ningún precio ni peaje se da.
- La Directiva (UE) 2024/1275, de eficiencia energética de los edificios, y el umbral de
  automatización que pueda fijar: no se ha leído ni consta transpuesta en el RITE vigente.
- Si la RTVA está obligada por el Real Decreto 56/2016 y por la IT 1.2.4.3.5 (si sus edificios
  superan los 290 kW): tema 16 y tema 12, que lo dejan sin confirmar.
- Lo básico de cada materia en el resto del temario: BMS y telemedida, tema 12; tipos de
  mantenimiento, gamas, OT y GMAO, tema 13; instrumentos de medida, tema 14; SAI y baterías, tema 7;
  eficiencia y residuos, tema 16; ventanas de mantenimiento, tema 17; trabajos y consignación, tema
  15; protección contra incendios, tema 11.
- Cualquier uso de sensorización IoT, predictivo, gemelo digital, telegestión, almacenamiento con
  baterías o autoconsumo en los edificios de la RTVA o de CSRTV: no consta en documento publicado.

## Trazabilidad

| Fuente | Qué se ha tomado | Leída |
|---|---|---|
| Real Decreto 244/2019 (BOE-A-2019-5089), redacción vigente, y redacciones a 21/12/2022, 01/01/2023, 01/07/2025, 01/08/2025, 01/11/2025, 10/12/2025 y 01/03/2026 de los artículos 3 y 4 | Los preceptos de la tabla de normativa; la evolución del artículo 3.g).iii y del 4.5 | 05/10/2026 |
| Real Decreto 842/2002, REBT (BOE-A-2002-18099), ITC-BT-40 | Apartados 2, 4.3 y 4.3.1 | 05/10/2026 |
| Reglamento (UE) 2023/1542 (DOUE-L-2023-81096) y sus correcciones DOUE-L-2024-80529, DOUE-L-2024-81259, DOUE-L-2025-81464 y DOUE-L-2026-80534; referencias posteriores de su ficha en el BOE (modificaciones) | Los preceptos de la tabla de normativa | 05/10/2026 |
| Real Decreto 1027/2007, RITE (BOE-A-2007-15820), redacción vigente | Los preceptos de la tabla de normativa | 05/10/2026 |
| Real Decreto 56/2016 (BOE-A-2016-1460) | Artículo 3 | 05/10/2026 |
| Metadatos del BOE (API de legislación consolidada) de BOE-A-2025-24545, BOE-A-2022-22685 y BOE-A-2026-6544 | Títulos de la Ley 9/2025 y de los Reales Decretos-leyes 20/2022 y 7/2026 | 05/10/2026 |
| Ficha de catálogo de AENOR de la UNE-EN ISO 52120-1:2022 | Título, fecha de edición, «En Vigor», «Anula a UNE-EN 15232-1:2018» | 05/10/2026 |
| Fichas de catálogo de AENOR de ISO/IEC 30173:2023, ISO/IEC 30141:2024 e ISO 17359:2018 | Fecha, estado, resumen y edición | 05/10/2026 |
| Vista previa oficial de la ISO/IEC 30173, edición 1.0, 2023-11 (primeras páginas: prólogo y apartado 3.1) | Definición 3.1.1 y sus dos notas; el nombre del subcomité 41 | 05/10/2026 |
| Vista previa oficial de la ISO/IEC 30141, edición 2.0, 2024-08 (prólogo) | El subcomité y el comité técnico conjunto que la prepararon | 05/10/2026 |
| Vista previa oficial de la ISO 19650-1:2018 (prólogo, apartado 3) y ficha de catálogo de AENOR de la UNE-EN ISO 19650-1:2019 | Definiciones 3.3.9 (AIM) y 3.3.14 (BIM); fecha de edición, «En Vigor», equivalencia idéntica | 05/10/2026 |
| Vista previa oficial de la ISO 29821:2018 (prólogo, introducción, apartados 3 a 5 y tabla 1) y ficha de DIN Media de esa edición | Definición 3.1, aplicaciones eléctricas, sensores, equipos portátiles y fijos; edición de 2018 anulada y sustituida por la ISO 29821:2026-04 | 05/10/2026 |
| LoRa Alliance, página «What is LoRaWAN® Specification» (lora-alliance.org) | Definición, topología, clases A, B y C | 05/10/2026 |
| 3GPP, noticias «Standardization of NB-IOT completed» (21/06/2016) y «The Cellular Internet of Things» (09/10/2017) | Qué es NB-IoT, versión 13, espectro con licencia | 05/10/2026 |
| OASIS, *MQTT Version 5.0*, OASIS Standard, 07/03/2019, apartado 1 | Definición, contextos de uso y las tres calidades de servicio | 05/10/2026 |
| Yang y otros, «A Review of Failure Modes and Safety Strategies of Lithium-Ion Batteries from Materials to Systems», *Advanced Science*, 13, 2026 (doi 10.1002/advs.76228); Su y otros, «Engineering Strategies to Suppress Thermal Runaway Propagation in Lithium-Ion Battery: Mechanisms, Metrics, Materials, and Evaluation Methods», *Advanced Science*, 13, 2026, e76502 (doi 10.1002/advs.76502); texto completo en Europe PMC | Comparación de LFP y NMC frente al embalamiento térmico | 05/10/2026 |
| Real Decreto 244/2019, artículo 2.2, y Real Decreto 56/2016, artículo 3.1; Reglamento (UE) 2023/1542, artículo 61.1 | Remisión al artículo 100 del Real Decreto 1955/2000; sujeto y alcance de la auditoría; condición de designación de las organizaciones de responsabilidad del productor | 05/10/2026 |

La redacción que se estudia es la vigente el 24/09/2026: ninguna de las fuentes cambió entre esa
fecha y la de lectura.

Lo que va como oficio y así se declara: la lectura que une las siete materias por el dato; la tabla
que compara el BMS clásico con la sensorización IoT y el aviso sobre las pilas de los sensores; la
tabla de variables que se sensorizan; la regla de que la decisión rápida y la de seguridad se toman
abajo; las tres precauciones de un sistema sensorizado; la comparación de los tipos de
mantenimiento, el ciclo del predictivo, las medidas de un motor y la tabla de medidas de una
batería; la tabla de lo que es y no es un gemelo digital, sus usos y su dependencia de la
documentación; las definiciones de telemedida, telemando y telegestión, la tabla de actuaciones de
la telegestión energética y la lectura de las anomalías de consumo como averías; las lecturas sobre
qué baterías son industriales y sobre estado de carga y de salud, las reglas de la sala de baterías
de litio y la tabla de tareas nuevas de mantenimiento; la lectura del uso del grupo de emergencia,
el ejemplo de potencia de inversores, la lectura de la condición de ubicación del almacenamiento,
el riesgo del funcionamiento en isla para la consignación, la tabla de mantenimiento fotovoltaico,
la tabla de decisiones y la observación de escala; la relación entre red radio y protocolo de
mensajería, la consecuencia práctica de la clase A, el nivel de servicio de las alarmas y el
tratamiento de la pasarela; la complementariedad entre termografía y ultrasonidos; el BIM como punto
de partida del gemelo; las dos lecturas sobre la química de la sala de baterías; la tabla de estrategias de automatización, el
principio de autonomía y la regla de las salas técnicas. Ninguna fuente leída lo dice con esas
palabras.
