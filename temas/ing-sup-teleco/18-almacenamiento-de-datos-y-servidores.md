# Tema 18 del específico de Ingeniería Superior · Telecomunicación · Almacenamiento de datos y servidores

Las siglas y símbolos de este tema, presentados de entrada: el bit y el byte (**B**), con los
múltiplos decimales kilobyte (**kB**), megabyte (**MB**), gigabyte (**GB**), terabyte (**TB**) y
petabyte (**PB**) y los binarios kibibyte (**KiB**), mebibyte (**MiB**), gibibyte (**GiB**) y tebibyte
(**TiB**); el disco duro magnético (**HDD**) y el disco de estado sólido (**SSD**); el conjunto
redundante de discos independientes (**RAID**); el conjunto de discos sin más (**JBOD**); la cinta
lineal abierta (**LTO**) y su sistema de ficheros (**LTFS**); el almacenamiento de conexión directa
(**DAS**), el conectado a la red (**NAS**) y la red de almacenamiento (**SAN**); las interfaces serie
conectada (**SAS**), serie avanzada (**SATA**), el bus **PCIe** y la memoria no volátil **NVMe**; el
canal de fibra (**FC**) y el protocolo de órdenes de dispositivo sobre red (**iSCSI**); el sistema de
ficheros en red (**NFS**) y el bloque de mensajes del servidor (**SMB**); las operaciones de entrada y
salida por segundo (**IOPS**); y la gestión de activos de medios (**MAM**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 20):
> «Almacenamiento de datos. Sistemas. Redundancia. Consolidación. Arquitectura, protocolos e
> interfaces. Servidores.»

**El enunciado tiene seis palabras y cada una es un epígrafe**, así que el tema las recorre en el orden
en que están escritas y no inventa ninguna más.

**Y la idea que ordena el punto**: **en una casa de televisión el almacenamiento no se dimensiona por
lo que cabe, sino por lo que sale por segundo sin fallar ni una vez.** **Un disco que guarda todo el
archivo y se atasca medio segundo durante una emisión es un disco inservible.** **Capacidad, caudal y
tolerancia a fallo son tres exigencias distintas y se resuelven con piezas distintas.**

<!-- indice -->
<!-- /indice -->

## 1. Las unidades: lo que se cuenta antes de comprar nada

**Todo lo demás depende de tener clara la aritmética**, y **es donde más se falla**, porque hay dos
familias de múltiplos y se parecen.

| Familia | Base | Ejemplo |
|---|---|---|
| **Decimal** | **potencias de mil** | **un kilobyte son mil bytes; un terabyte, un billón de bytes** |
| **Binaria** | **potencias de mil veinticuatro** | **un kibibyte son mil veinticuatro bytes** |

**Las tres igualdades que hay que saber de memoria:**

1. **Un byte son ocho bits.**
2. **Un kibibyte son mil veinticuatro bytes.**
3. **Por tanto un kibibyte son ocho mil ciento noventa y dos bits.**

**El ejemplo que la plantilla oficial confirma**: **cuatro kibibytes son cuatro mil noventa y seis
bytes, y cuatro mil noventa y seis por ocho son treinta y dos mil setecientos sesenta y ocho bits.**
**La pregunta 70 del cuadernillo de esta ocupación pide exactamente eso y la plantilla da como buena
esa cifra.**

**Las dos trampas del enunciado, porque las cuatro opciones estaban puestas para caer en ellas:**

- **Contar en base mil y no en base mil veinticuatro** da treinta y dos mil, que es otra de las
  opciones. **La unidad estaba escrita con la i intercalada: es binaria.**
- **Responder en bytes cuando la pregunta pide bits** da cuatro mil noventa y seis, que también estaba
  puesta. **Hay que leer si la pregunta dice bit o byte.**

**Regla de examen**: **subrayar la unidad del enunciado antes de mirar las opciones.** **Casi todas las
preguntas de aritmética de almacenamiento se fallan por la unidad, no por la cuenta.**

## 2. Los sistemas: de qué está hecho el almacenamiento

**Los cuatro soportes que conviven en una instalación de televisión, con lo que aporta cada uno:**

| Soporte | Cómo guarda | Para qué sirve aquí |
|---|---|---|
| **Disco magnético (HDD)** | **platos que giran y una cabeza que se desplaza** | **el grueso de la capacidad en línea: mucho espacio a coste bajo** |
| **Disco de estado sólido (SSD)** | **memoria no volátil, sin partes móviles** | **lo que exige acceso inmediato: bases de datos, caché, edición sobre material vivo** |
| **Cinta magnética (LTO)** | **acceso secuencial, soporte extraíble** | **el archivo a largo plazo y la copia de seguridad** |
| **Soporte óptico** | **lectura por haz luminoso** | **residual en explotación; se conserva por compatibilidad con fondos antiguos** |

**La diferencia que de verdad importa entre el disco magnético y el de estado sólido no es la
velocidad de transferencia: es el tiempo de acceso.** **El magnético tiene que mover una cabeza y
esperar a que el plato pase por debajo; el de estado sólido no espera a nada.** **Por eso el magnético
sigue siendo excelente para leer un fichero grande de corrido —una emisión— y malo para atender mil
peticiones pequeñas a la vez.**

**Y de ahí salen las dos magnitudes con las que se dimensiona:**

- **El caudal**: **cuántos bits por segundo salen de corrido.** **Es lo que manda cuando se reproduce
  o se graba vídeo.**
- **Las operaciones por segundo**: **cuántas peticiones independientes atiende.** **Es lo que manda
  cuando hay muchos puestos de edición pinchando a la vez sobre el mismo material.**

**Un sistema puede tener capacidad de sobra y caudal de sobra y aun así ahogarse por operaciones por
segundo.** **Dimensionar sólo por terabytes es el error clásico.**

## 3. La cinta y las bibliotecas: el archivo

**La cinta no ha desaparecido y no va a desaparecer**, por tres razones que hay que saber decir:
**cuesta menos por unidad de capacidad que cualquier disco**, **se guarda sin consumir energía** y
**el soporte se separa del lector**, lo que la convierte en la única copia que un fallo del sistema no
puede borrar.

**Una biblioteca de cintas tiene tres piezas**: **los cartuchos**, **las unidades de lectura y
escritura** —los lectores— y **el brazo robótico** que lleva un cartucho de su hueco al lector. **La
capacidad de la biblioteca la dan los cartuchos; el caudal, el número de lectores.** **Son dos
decisiones independientes y se confunden a menudo.**

**La compatibilidad entre generaciones es la pregunta de examen de este epígrafe**, y va con cuidado
porque cada generación redefine la regla. **La pregunta 14 del cuadernillo de esta ocupación plantea
una biblioteca con dos lectores de novena generación y pregunta qué se puede hacer con ellos.** **La
plantilla oficial da como buena la opción que combina escritura en novena y octava generación con
lectura en séptima, octava y novena.**

**Cómo se razona la respuesta sin haberla memorizado:**

1. **Un lector escribe siempre en su propia generación.** **Eso descarta cualquier opción que se lo
   niegue.**
2. **La compatibilidad hacia atrás es asimétrica**: **se lee más generaciones de las que se escribe.**
   **Una opción que ofrezca la misma cobertura para leer y para escribir es sospechosa por
   construcción.**
3. **Entre las que quedan, la buena es la que da el alcance de lectura más amplio compatible con un
   alcance de escritura menor.** **Es la única que respeta a la vez las dos reglas anteriores.**

**Lo que este tema no dice**: **ni la capacidad en terabytes de ninguna generación, ni su velocidad,
ni cuántas generaciones hacia atrás alcanza cada una en abstracto.** **Son dato de especificación del
consorcio que publica el formato**, **cambian de una generación a otra** y **aquí sólo se recoge lo
que la plantilla oficial confirma para el caso que pregunta.**

**Y una pieza más, porque el enunciado del punto habla de protocolos**: **el sistema de ficheros de
cinta lineal (LTFS) presenta el cartucho como si fuera una carpeta**, con nombres de fichero y
directorios legibles sin la aplicación que los escribió. **Es lo que hace que una cinta de archivo no
dependa para siempre del programa que la grabó.**

## 4. La redundancia: los conjuntos de discos

**El principio**: **un disco falla, y con suficientes discos la pregunta no es si fallará alguno, sino
cuándo.** **La redundancia consiste en guardar información sobrante para que la pérdida de un disco no
sea la pérdida de los datos.**

**Los niveles que hay que saber, con lo que cada uno hace y lo que cuesta:**

| Nivel | Qué hace | Mínimo de discos | Capacidad útil | Aguanta |
|---|---|---|---|---|
| **Conjunto sin redundancia** | **reparte los datos en trozos entre todos los discos** | **dos** | **toda** | **ningún fallo** |
| **Espejo** | **escribe lo mismo en dos discos** | **dos** | **la mitad** | **un disco de cada pareja** |
| **Paridad simple** | **reparte los datos y una paridad distribuida** | **tres** | **la de todos menos uno** | **un disco** |
| **Doble paridad** | **reparte los datos y dos paridades distintas** | **cuatro** | **la de todos menos dos** | **dos discos** |
| **Espejo repartido** | **primero espeja y luego reparte** | **cuatro** | **la mitad** | **un disco de cada pareja** |

**Los dos números que la plantilla oficial confirma en este epígrafe:**

**El primero, la pregunta 20**: **el mínimo de discos de un conjunto de paridad simple es tres**, y
**la plantilla lo da como bueno.** **La razón se ve sin memorizar nada**: **hacen falta al menos dos
discos con datos para que la paridad sirva de algo, más el espacio de la propia paridad.** **Con dos
discos, la paridad de un solo dato es una copia del dato, y eso ya tiene nombre y es el espejo.**

**El segundo, la pregunta 3**: **con cuatro discos, queriendo máxima capacidad útil y algún mecanismo
de redundancia, el conjunto que se elige es el de paridad simple**, y **la plantilla lo da como
bueno.** **La cuenta con cuatro discos, que es lo que decide entre las opciones:**

| Opción del enunciado | Capacidad útil con cuatro discos | ¿Redundancia? |
|---|---|---|
| **Reparto sin redundancia** | **cuatro discos** | **no: es la opción que hay que descartar primero** |
| **Espejo** | **dos discos** | **sí** |
| **Espejo repartido** | **dos discos** | **sí** |
| **Paridad simple** | **tres discos** | **sí** |

**El razonamiento en una línea**: **de las tres que sí protegen, la de paridad simple deja tres discos
útiles y las otras dos dejan dos.** **La pregunta pedía máxima capacidad con alguna protección: es
esa.**

**Dos advertencias de oficio sobre la paridad, que no salen en el examen pero se preguntan en la
entrevista:**

- **La reconstrucción es el momento peligroso.** **Mientras se reconstruye el disco sustituido, el
  conjunto lee todos los demás de cabo a rabo y está sin protección.** **Cuanto mayores son los
  discos, más dura esa ventana.** **Es el argumento de la doble paridad en conjuntos grandes.**
- **La escritura de una paridad obliga a leer antes.** **Modificar un trozo pequeño exige recalcular
  la paridad, lo que penaliza la escritura frente al espejo.** **Por eso el espejo sigue usándose
  donde manda la escritura y no la capacidad.**

**Y el conjunto que no es un conjunto**: **agrupar discos sin redundancia ninguna, sólo para verlos
como un volumen.** **Sirve para capacidad bruta y no protege nada.** **Cuando en un pliego aparece
como si fuera un nivel más, hay que decir que no lo es.**

## 5. La consolidación: dejar de tener el disco dentro del equipo

**Consolidar es sacar el almacenamiento de dentro de cada máquina y ponerlo en un sitio común.** **La
razón no es la elegancia: es que el disco de dentro de un equipo sólo lo aprovecha ese equipo, y en una
instalación con decenas de puestos eso significa comprar diez veces lo que se usa una.**

**Las tres arquitecturas, que es la pregunta clásica:**

| Arquitectura | Qué ve el equipo | Por dónde va |
|---|---|---|
| **Conexión directa (DAS)** | **un disco suyo** | **un cable de la propia máquina** |
| **Conectado a la red (NAS)** | **una carpeta compartida: ficheros** | **la red de datos general** |
| **Red de almacenamiento (SAN)** | **un disco suyo, aunque esté lejos: bloques** | **una red dedicada al almacenamiento** |

**La frontera que hay que saber explicar es la del medio**: **el almacenamiento conectado a la red
sirve ficheros y la red de almacenamiento sirve bloques.** **Quien sirve ficheros decide él cómo se
guardan y arbitra entre clientes; quien sirve bloques entrega trozos de disco y es el cliente el que
pone encima su sistema de ficheros.** **De ahí se derivan las dos consecuencias prácticas:**

- **Compartir un mismo volumen de bloques entre varios equipos exige un sistema de ficheros preparado
  para ello.** **Montar un volumen de bloques corriente en dos máquinas a la vez corrompe los datos.**
  **Es un error caro y se comete.**
- **Servir ficheros añade una capa y con ella algo de retardo**, **a cambio de que compartir sea
  natural.**

**La tercera forma, más reciente y ya presente en las casas de televisión**: **el almacenamiento por
objetos**, donde **no hay ni bloques ni árbol de carpetas, sino objetos con un identificador y sus
datos descriptivos**, servidos por peticiones de red. **Escala sin límite práctico y es la base del
archivo profundo y del almacenamiento contratado a un tercero.**

**Y la jerarquía, que es la consolidación llevada al ciclo de vida del material:**

1. **En línea**: **disco, disponible al instante.** **El material que se está tocando.**
2. **Casi en línea**: **disco lento o biblioteca de cintas con el robot montado.** **Minutos.**
3. **Fuera de línea**: **cinta en la estantería.** **Requiere que alguien la traiga.**

**Quien gobierna ese ciclo es la gestión de activos de medios (MAM)**: **el catálogo que sabe qué hay,
dónde está cada copia y con qué derechos**, y **que ordena bajar a cinta lo que no se toca y subir a
disco lo que se va a necesitar.** **Sin catálogo, un archivo grande es material perdido con orden
alfabético.**

## 6. Arquitectura, protocolos e interfaces

**El enunciado los nombra juntos y conviene separarlos**, porque **la interfaz es el cable y el
conector; el protocolo, el idioma que va por dentro.**

**Las interfaces de dentro de la máquina y de la cabina:**

| Interfaz | Dónde vive | Qué la caracteriza |
|---|---|---|
| **Serie avanzada (SATA)** | **equipos de escritorio y discos de capacidad** | **sencilla y barata; una cola de órdenes corta** |
| **Serie conectada (SAS)** | **cabinas y servidores** | **doble camino a cada disco, colas largas, pensada para funcionar sin parar** |
| **Memoria no volátil sobre PCIe (NVMe)** | **discos de estado sólido rápidos** | **habla directamente con el bus del procesador; muchas colas en paralelo** |

**La idea que ordena la tabla**: **cada interfaz nació para un tipo de disco.** **La serie avanzada se
diseñó para un disco que gira y no puede atender más de una cosa a la vez; la memoria no volátil, para
un disco que sí puede, y por eso su ganancia no está en el cable sino en dejar de fingir que hay una
cabeza que mover.**

**Los protocolos de red de almacenamiento, que sirven bloques:**

- **Canal de fibra (FC)**: **red dedicada, propia, con sus conmutadores y su direccionamiento.**
  **Es la solución tradicional de las cabinas grandes y su virtud es que no comparte camino con nada
  más.**
- **Órdenes de dispositivo sobre red de datos (iSCSI)**: **las mismas órdenes de disco encapsuladas
  para viajar por la red general.** **Ahorra una red entera a cambio de compartirla.**

**Los protocolos de ficheros, que sirven carpetas:**

- **Sistema de ficheros en red (NFS)**: **el compartido de tradición de los sistemas de tipo unix.**
- **Bloque de mensajes del servidor (SMB)**: **el compartido de tradición de los sistemas de
  escritorio de oficina.**

**La regla para no equivocarse en un examen**: **si el nombre del protocolo apunta a órdenes de disco,
sirve bloques; si apunta a ficheros o a carpetas compartidas, sirve ficheros.** **Y la red de
almacenamiento va con los primeros; el almacenamiento conectado a la red, con los segundos.**

**Una última pieza de arquitectura, propia de las casas de televisión**: **el sistema de ficheros
compartido**, que **permite que varios puestos de edición monten el mismo volumen de bloques a la vez
sin pisarse**, porque **un gestor arbitra quién escribe qué.** **Es lo que hace posible que dos
montadores trabajen sobre el mismo material sin copiarlo dos veces.**

## 7. Servidores

**El enunciado cierra con la palabra servidores y en esta ocupación tiene dos sentidos que hay que
distinguir**, porque **se llaman igual y no son lo mismo:**

| Sentido | Qué es | Qué se le pide |
|---|---|---|
| **Servidor de datos** | **una máquina que ofrece un servicio a otras** | **disponibilidad, memoria, red** |
| **Servidor de vídeo** | **un equipo que graba y reproduce vídeo en tiempo real por sus salidas** | **caudal garantizado y arranque inmediato del primer fotograma** |

**Lo que hace especial al servidor de vídeo, y es lo que se pregunta**: **no puede llegar tarde.**
**Un servidor de datos que tarda medio segundo más es un servidor lento; un servidor de vídeo que
tarda medio segundo más ha dejado la emisión en negro.** **Por eso su almacenamiento se dimensiona por
caudal sostenido en el peor caso, con todos los canales grabando y reproduciendo a la vez, y no por
capacidad.**

**Sus funciones en la instalación, que son cuatro y suelen ir en el mismo equipo:**

1. **Ingesta**: **entrar el material, de una cámara, de una línea o de un fichero.**
2. **Reproducción para edición**: **servir el material a los puestos mientras se sigue grabando.**
3. **Emisión**: **sacar la escaleta al aire con el arranque exacto.**
4. **Trasiego con el archivo**: **subir y bajar material del almacenamiento profundo.**

**Y las formas de que un servidor no sea un punto único de fallo:**

- **Duplicar componentes dentro de la máquina**: **fuentes de alimentación, ventilación, tarjetas de
  red, discos de sistema en espejo.** **Es lo primero y lo más barato.**
- **Duplicar la máquina en espera**: **una segunda que arranca cuando la primera cae.**
- **Agrupar máquinas en conjunto**: **varias trabajan a la vez y el trabajo de la que cae se reparte
  entre las demás.** **Es lo que permite además mantener sin parar el servicio.**
- **Virtualizar**: **separar el servicio de la máquina concreta, de modo que el servicio se pueda
  mudar a otro hierro.** **Es la forma moderna de la consolidación aplicada al cómputo, y la que hace
  que la máquina deje de ser un sitio y pase a ser un recurso.**

**El aviso de oficio con el que se cierra el tema**: **la redundancia interna de un conjunto de discos
protege del fallo de un disco y de nada más.** **No protege del borrado por error, ni del programa
malicioso que cifra los ficheros, ni del incendio de la sala.** **Un conjunto redundante no es una
copia de seguridad**, y **confundir las dos cosas es el error que más material ha destruido en esta
industria.**

## 8. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cuatro declaraciones expresas:**

1. **Las tres cifras del tema vienen de la plantilla oficial de esta ocupación y se citan con su
   número de pregunta**: **los treinta y dos mil setecientos sesenta y ocho bits de cuatro kibibytes,
   en la pregunta 70**; **el mínimo de tres discos del conjunto de paridad simple, en la pregunta
   20**; y **la elección del conjunto de paridad simple para cuatro discos con máxima capacidad útil y
   redundancia, en la pregunta 3.** **La cuenta de capacidad útil con cuatro discos que acompaña a esa
   última se deriva de la definición de cada nivel y así se presenta.**
2. **La regla de compatibilidad entre generaciones de cinta se recoge sólo para el caso que la
   plantilla confirma —dos lectores de novena generación, en la pregunta 14— y con el razonamiento que
   lleva a esa opción.** **El tema no da la capacidad, la velocidad ni el alcance de compatibilidad de
   ninguna generación en abstracto**: **son dato de especificación del consorcio que publica el
   formato**, y **una cifra que no se ha leído en su fuente no se escribe.**
3. **Este tema no da ningún caudal en bits por segundo, ninguna cifra de operaciones por segundo,
   ninguna capacidad de cabina, ninguna velocidad de interfaz y ningún tiempo de reconstrucción.**
   **Todos ellos son dato de fabricante y de dimensionado**, y **no hay fuente en este proyecto que
   los sostenga.**
4. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la
   producción sobre infraestructura de red y sus formatos de señal, al tema 19**; **las redes, sus
   modelos de referencia y su conmutación, al tema 20**; **la ingesta, la edición y la emisión como
   flujo de producción, a los temas 11 y 14**; **la postproducción y sus formatos de fichero, al tema
   15**; y **la seguridad de la información y las copias, al tema 25.**

**El resto del tema va como oficio y así se declara**: la idea de que el almacenamiento de televisión
se dimensiona por lo que sale por segundo y no por lo que cabe, la distinción entre caudal y
operaciones por segundo con el aviso de que un sistema puede ahogarse por las segundas teniendo el
primero de sobra, la lectura de que la diferencia decisiva entre disco magnético y de estado sólido es
el tiempo de acceso y no la transferencia, las tres razones por las que la cinta sigue viva, la
separación entre capacidad y caudal en una biblioteca según cartuchos y lectores, las dos reglas de
compatibilidad de generaciones con las que se razona la respuesta, las dos advertencias sobre la
reconstrucción y sobre la penalización de escritura de la paridad, la aclaración de que agrupar discos
sin redundancia no es un nivel, la frontera entre servir bloques y servir ficheros con sus dos
consecuencias prácticas, el aviso de que montar un volumen de bloques corriente en dos máquinas
corrompe los datos, la jerarquía en línea, casi en línea y fuera de línea con el papel del catálogo, la
observación de que cada interfaz nació para un tipo de disco, la regla de examen para distinguir
protocolos de bloques y de ficheros, la distinción entre servidor de datos y servidor de vídeo con las
cuatro funciones de este último, las cuatro formas de evitar el punto único de fallo y el aviso final
de que un conjunto redundante no es una copia de seguridad. **Nada de eso está en un boletín oficial ni
en ninguna fuente consultada para este proyecto**, y el tema no lo presenta como si lo estuviera.
