# Tema 10 del específico de Ingeniería Técnica · Telecomunicación · Sistemas de redacción digital

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 14 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el flujo de trabajo de una redacción digital, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Aviso de estudio** | **Una redacción digital es un sistema informático que produce televisión.** Quien lo estudie como equipamiento de vídeo falla; quien lo estudie como flujo, acierta |
| **Extensión** | **1.925 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la gestión de activos de medios (**MAM**, *media
asset management*) y la de activos digitales (**DAM**); el sistema de gestión de contenido de
noticias (**NRCS**, *newsroom computer system*); el intercambio de material de noticias (**MOS**,
*media object server*); el formato de intercambio de material (**MXF**); la interfaz digital serie
(**SDI**) del tema 3; y la red de área de almacenamiento (**SAN**) y el almacenamiento conectado a la
red (**NAS**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 14):
> «Sistemas de redacción: Ingesta. Edición. Emisión. Equipamiento. Diagrama a bloques. Interconexión.
> Conexión con otras salas (Controles, Intercambios, Continuidades, etc.). Red Informática»

**Tres preguntas.** **Y las tres son de la misma mitad del enunciado**: **la ingesta y la gestión del
material.** **De la edición, de la emisión y de la conexión con otras salas no ha caído ninguna.**

**El aviso que ordena el punto**: **una redacción digital es un sistema informático que produce
televisión.** **Quien lo estudie como equipamiento de vídeo falla; quien lo estudie como flujo de
trabajo, acierta.**

<!-- indice -->

## Índice

- [1. Las cuatro etapas del flujo](#1-las-cuatro-etapas-del-flujo)
- [2. La ingesta](#2-la-ingesta)
- [3. La gestión del material](#3-la-gestión-del-material)
- [4. La edición y la emisión](#4-la-edición-y-la-emisión)
- [5. El almacenamiento y la red](#5-el-almacenamiento-y-la-red)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Las cuatro etapas del flujo

| Etapa | Qué hace | Quién trabaja ahí |
|---|---|---|
| **Ingesta** | **Meter el material en el sistema**: grabar señales de entrada y volcar tarjetas ✔ | **Operadores de ingesta** |
| **Gestión** | **Catalogar, buscar y controlar el material y sus versiones** | **Documentación y todos los demás** |
| **Edición** | **Montar las piezas** | **Redactores y montadores** |
| **Emisión** | **Poner la pieza en antena en el momento previsto** | **Control de emisión** |

**Y el archivo atraviesa las cuatro**, no es una quinta: **lo que se conserva se decide en la primera y
se ejecuta después.**

**La regla que ordena el punto**: **cada etapa mete el material en un sitio y las demás lo encuentran
por sus DATOS DESCRIPTIVOS, no por su nombre de fichero.** **Ésa es toda la diferencia entre un
sistema de redacción y una carpeta compartida.**

## 2. La ingesta

**La pregunta 50**: **el sistema de ingesta se encarga de la grabación de las señales de entrada que se
transfieren al almacenamiento para edición.** Ésa es la respuesta oficial.

**La pregunta 6**: **en una redacción digital integrada, la señal de una agencia de noticias se graba
en ingesta.** Ésa es la respuesta oficial.

---

**Las dos son la definición y su aplicación**, y **las opciones falsas de las dos son las otras
etapas del flujo:**

| Opción falsa de la 50 | De qué etapa es |
|---|---|
| **La ingesta de metadatos para la catalogación** | **De la gestión** |
| **La transferencia de ficheros de edición a emisión** | **Del conformado y la emisión** |
| **La incrustación de rótulos** | **De la edición y del grafismo** |

| Opción falsa de la 6 | Por qué no |
|---|---|
| **Archivo** | **Guarda lo que ya está dentro, no mete lo que llega** |
| **Redacción** | **Escribe y monta, no captura señal** |
| **Continuidad** | **Articula la emisión, y es materia del tema 9 de Diseño Gráfico** |

**Los tres tipos de ingesta que conviene distinguir, porque el enunciado da la materia por sabida:**

| Tipo | De dónde entra | Rasgo |
|---|---|---|
| **En directo, desde señal** | **Una entrada de vídeo: agencia, satélite, unidad móvil** ✔ | **Ocurre en tiempo real y no se puede repetir** |
| **Desde soporte** | **Una tarjeta o un disco de cámara** | **Va más deprisa que en tiempo real** |
| **Desde fichero** | **Una entrega por red o por transferencia** | **La más rápida, y la que más problemas de formato da** |

**Y la razón por la que la ingesta en directo es la crítica**: **es la única que no se puede
repetir.** **Si falla la grabación de una señal de agencia mientras ocurre, no hay segunda
oportunidad**, y **por eso se graba por partida doble en dos sistemas independientes.**

**Los tres datos que se capturan en la ingesta y que deciden si el material se encontrará después:**
**quién lo trae, de qué es y qué derechos tiene.** **Un material sin esos tres datos está dentro del
sistema y está perdido.**

## 3. La gestión del material

**La pregunta 90**: **la gestión de activos de medios posibilita la gestión del vídeo y los ficheros
multimedia en el sistema de redacción.** Ésa es la respuesta oficial.

---

**Qué hace de verdad, en cinco funciones**, que es lo que la respuesta oficial resume:

| Función | Qué resuelve |
|---|---|
| **Catálogo** | **Que cada material tenga sus datos descriptivos y se pueda buscar** |
| **Versiones** | **Que se sepa cuál es la buena y de dónde sale cada una** |
| **Baja resolución** | **Que se pueda ver y marcar el material sin mover el fichero grande** |
| **Ciclo de vida** | **Cuánto se guarda cada cosa y cuándo se borra o se archiva** |
| **Permisos** | **Quién puede ver, usar y borrar qué** |

**Las tres opciones falsas son tres funciones reales del sistema, cada una de otro módulo**: **el
planificador de ingestas, el transferidor a los servidores de emisión y el conformador de ediciones.**
**La palabra que decide es «gestión»**: **de las cuatro, sólo una nombra una función transversal y no
un paso concreto.**

**Y la pieza que hace posible todo lo anterior, aunque el examen no la pregunte**: **la copia de baja
resolución.** **Cada material se transcodifica al entrar a una versión ligera**, y **es esa versión la
que viaja por la red ofimática, se ve en el navegador y se marca.** **El fichero grande no se mueve
hasta el conformado final.** **Sin esa pieza, una redacción de doscientas personas necesitaría una red
de vídeo en cada mesa.**

**Y la distinción de vocabulario que conviene tener**: **la gestión de activos DIGITALES es el término
general —vale para fotos, documentos y audio—**; **la de activos de MEDIOS es la especializada en
audiovisual**, con lo que eso añade: código de tiempo, subclips, versiones de montaje y derechos por
ventana de explotación.

## 4. La edición y la emisión

**El enunciado las nombra y el examen no ha entrado.** **Lo que conviene llevar visto:**

**La edición en una redacción se hace en dos niveles:**

| Nivel | Quién lo usa | Sobre qué material |
|---|---|---|
| **Edición ligera, en el propio puesto** | **El redactor** | **La copia de baja resolución** |
| **Edición completa, en sala** | **El montador** | **El material de alta resolución** |

**Y el conformado es la operación que une los dos**: **la lista de decisiones tomada sobre la copia
ligera se aplica al material grande.** **Es automático, y es donde aparecen los fallos si los códigos
de tiempo no coinciden.**

**La emisión, en tres piezas:**

| Pieza | Qué hace |
|---|---|
| **Escaleta de emisión** | **Dice qué sale y en qué orden**, y viene del sistema de redacción |
| **Servidor de emisión** | **Reproduce las piezas en el instante previsto** |
| **Automatización** | **Ejecuta la escaleta: dispara servidor, grafismo y conmutación** |

**El principio de diseño que gobierna esa parte**: **la emisión se separa de todo lo demás.** **Sus
servidores son propios, su almacenamiento es propio y su red es propia**, porque **es el único punto
del sistema donde un fallo se ve en antena.**

**Y la conexión con otras salas que el enunciado pide**: **con controles, intercambios y
continuidades.** **Hoy esa conexión es de dos clases**: **la de SEÑAL, por matriz o por red del tema
7**, y **la de DATOS, por la red informática.** **La segunda es la que lleva las escaletas, los estados
y las órdenes**, y **es la que más ha crecido.**

## 5. El almacenamiento y la red

**El enunciado termina con «red informática», y eso no es un detalle**: **es lo que distingue esta
ocupación de una de vídeo.**

**Los dos almacenamientos de una redacción, y por qué son dos:**

| | **Almacenamiento de producción** | **Almacenamiento de archivo** |
|---|---|---|
| **Qué guarda** | **Lo que está en uso** | **Lo que se conserva** |
| **Cómo se accede** | **Inmediato, por red de bloques** | **Diferido: puede estar en cinta** |
| **Coste por terabyte** | **Alto** | **Bajo** |
| **Qué lo dimensiona** | **Cuánto material vivo hay a la vez** | **Cuánto hay que conservar y cuánto tiempo** |

**Las tres redes que conviven en una redacción, que es lo más preguntable de lo que no ha caído:**

| Red | Qué lleva | Por qué va separada |
|---|---|---|
| **De señal** | **Vídeo y audio en tiempo real** | **Caudal enorme y sensible al retardo** |
| **De producción** | **Ficheros, baja resolución, control del sistema** | **Caudal alto a ráfagas** |
| **Ofimática** | **Correo, navegación, gestión** | **Es la que está expuesta a internet** |

**Y la razón de la separación, dicha sin rodeos**: **la red ofimática es la que recibe el correo con
el adjunto malicioso.** **Si la producción cuelga de ella, un incidente de seguridad puede parar la
emisión.**
**Es la misma lógica de la zona perimetral del tema 18.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 6 | Dónde se graba la señal de una agencia de noticias | c) Ingesta ✔ |
| 50 | De qué se encarga el sistema de ingesta | a) Grabar las señales de entrada para edición ✔ |
| 90 | Qué hace la gestión de activos de medios | b) Gestionar el vídeo y los ficheros multimedia ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la tabla de las cuatro etapas contesta las tres preguntas**, porque **las
nueve opciones falsas son, todas, funciones de otra etapa.** **Es el punto que mejor se contesta
entendiendo el flujo entero.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **No se ha consultado la documentación de ningún sistema de redacción comercial.** **Lo que el tema
   describe es la arquitectura habitual de una redacción digital**, escrita a partir del propio
   enunciado del anexo y de las tres respuestas oficiales.
2. **Este temario no describe la redacción de RTVE**, cuyos sistemas no se han consultado. **Lo que
   contiene vale para cualquier instalación de esa clase.**
3. **La distinción entre gestión de activos digitales y de activos de medios es de uso corriente en el
   sector**, y **ninguna respuesta oficial depende de ella.**
4. **El protocolo de intercambio entre el sistema de redacción y los equipos de producción se nombra
   por sus siglas y no se desarrolla**: **el examen no ha entrado por ahí** y su especificación no se
   ha consultado.

**El resto del tema va como oficio y así se declara**: la regla de que el material se encuentra por sus
datos descriptivos, la razón de que la ingesta en directo sea la crítica y se duplique, los tres datos
que deciden si un material se encontrará, el papel de la copia de baja resolución, el principio de
separar la emisión y la razón de seguridad para separar las tres redes. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
