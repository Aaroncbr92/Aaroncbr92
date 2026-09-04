# Esquema · Tema 18 del específico de Ingeniería Superior · Telecomunicación · Almacenamiento de datos y servidores

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de almacenamiento audiovisual ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: el bit
y el byte (**B**), con los múltiplos decimales **kB**, **MB**, **GB**, **TB** y **PB** y los binarios
**KiB**, **MiB**, **GiB** y **TiB**; el disco magnético (**HDD**) y el de estado sólido (**SSD**); el
conjunto redundante de discos independientes (**RAID**) y el conjunto sin redundancia (**JBOD**); la
cinta lineal abierta (**LTO**) y su sistema de ficheros (**LTFS**); el almacenamiento de conexión
directa (**DAS**), el conectado a la red (**NAS**) y la red de almacenamiento (**SAN**); las interfaces
**SAS**, **SATA**, **PCIe** y **NVMe**; el canal de fibra (**FC**) y el protocolo **iSCSI**; los
sistemas de ficheros en red (**NFS**) y de bloque de mensajes (**SMB**); las operaciones por segundo
(**IOPS**); y la gestión de activos de medios (**MAM**).

**Cabecera.** Enunciado: punto 20 del anexo · **cuatro preguntas** · **sin norma del boletín**.

**La idea que lo ordena** · `[of]` · **En una casa de televisión el almacenamiento no se dimensiona por
lo que cabe, sino por lo que SALE POR SEGUNDO sin fallar ni una vez.** **Capacidad, caudal y tolerancia
a fallo son tres exigencias distintas y se resuelven con piezas distintas.**

<!-- indice -->

## Índice

- [Las unidades](#las-unidades)
- [Los soportes](#los-soportes)
- [La cinta y las bibliotecas](#la-cinta-y-las-bibliotecas)
- [La redundancia](#la-redundancia)
- [La consolidación](#la-consolidación)
- [Arquitectura, protocolos e interfaces](#arquitectura-protocolos-e-interfaces)
- [Servidores](#servidores)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las unidades

- **las tres igualdades de memoria** · `[of]` · **un byte son ocho bits** · **un kibibyte son mil
  veinticuatro bytes** · **por tanto un kibibyte son ocho mil ciento noventa y dos bits.**
- **EL EJEMPLO QUE LA PLANTILLA CONFIRMA** · `[exam]` · **Cuatro kibibytes son cuatro mil noventa y
  seis bytes, y por ocho, TREINTA Y DOS MIL SETECIENTOS SESENTA Y OCHO bits.**
- **las dos trampas** · `[exam]` · **contar en base mil** da treinta y dos mil, **que es otra de las
  opciones**; **responder en bytes cuando se piden bits** da cuatro mil noventa y seis, **que también
  estaba puesta.**
- **regla de examen** · `[of]` · **Subrayar la unidad del enunciado antes de mirar las opciones.**
  **Casi todas estas preguntas se fallan por la unidad, no por la cuenta.**

## Los soportes

| Soporte | Para qué sirve aquí |
|---|---|
| **disco magnético** | **el grueso de la capacidad en línea: mucho espacio a coste bajo** |
| **disco de estado sólido** | **lo que exige acceso inmediato: bases de datos, caché, edición viva** |
| **cinta** | **el archivo a largo plazo y la copia de seguridad** |
| **óptico** | **residual; se conserva por compatibilidad con fondos antiguos** |

- **la diferencia que de verdad importa** · `[of]` · **No es la velocidad de transferencia: es el
  TIEMPO DE ACCESO.** **El magnético mueve una cabeza y espera al plato; el de estado sólido no espera
  a nada.**
- **las dos magnitudes con que se dimensiona** · `[of]` · **el CAUDAL** —manda al reproducir o grabar
  vídeo— y **las OPERACIONES POR SEGUNDO** —manda cuando muchos puestos pinchan a la vez sobre el
  mismo material—. **Un sistema puede ahogarse por las segundas teniendo el primero de sobra**:
  **dimensionar sólo por terabytes es el error clásico.**

## La cinta y las bibliotecas

- **las tres razones por las que sigue viva** · `[of]` · **cuesta menos por unidad de capacidad que
  cualquier disco** · **se guarda sin consumir energía** · **el soporte se separa del lector**, lo que
  la convierte en **la única copia que un fallo del sistema no puede borrar.**
- **las tres piezas** · `[of]` · **cartuchos, lectores y brazo robótico.** **La capacidad la dan los
  cartuchos; el caudal, el número de lectores.** **Son dos decisiones independientes y se confunden a
  menudo.**
- **CÓMO SE RAZONA LA COMPATIBILIDAD** · `[exam]` · **1)** un lector escribe siempre **en su propia
  generación**; **2)** la compatibilidad hacia atrás es **asimétrica**: se lee más generaciones de las
  que se escribe, y **una opción con la misma cobertura para leer y escribir es sospechosa por
  construcción**; **3)** entre las que quedan gana **la de mayor alcance de lectura con alcance de
  escritura menor.**
- **lo que este temario NO dice** · `[of]` · **Ni capacidad, ni velocidad, ni alcance de compatibilidad
  de ninguna generación en abstracto**: **son dato de especificación del consorcio que publica el
  formato.**
- **el sistema de ficheros de cinta** · `[of]` · **Presenta el cartucho como una carpeta, legible sin
  la aplicación que lo escribió.** **Es lo que hace que una cinta de archivo no dependa para siempre
  del programa que la grabó.**

## La redundancia

| Nivel | Mínimo | Capacidad útil | Aguanta |
|---|---|---|---|
| **reparto sin redundancia** | **dos** | **toda** | **ningún fallo** |
| **espejo** | **dos** | **la mitad** | **un disco de cada pareja** |
| **paridad simple** | **tres** | **la de todos menos uno** | **un disco** |
| **doble paridad** | **cuatro** | **la de todos menos dos** | **dos discos** |
| **espejo repartido** | **cuatro** | **la mitad** | **un disco de cada pareja** |

- **POR QUÉ EL MÍNIMO DE LA PARIDAD SIMPLE ES TRES** · `[exam]` · **Hacen falta al menos dos discos con
  datos para que la paridad sirva de algo, más el espacio de la propia paridad.** **Con dos discos, la
  paridad de un solo dato es una copia del dato, y eso ya tiene nombre: es el espejo.**
- **LA CUENTA CON CUATRO DISCOS** · `[exam]` · **De las tres opciones que protegen, la de paridad
  simple deja TRES discos útiles y las otras dos dejan dos.** **La pregunta pedía máxima capacidad con
  alguna protección: es esa.**
- **las dos advertencias de oficio** · `[of]` · **1)** la RECONSTRUCCIÓN es el momento peligroso:
  **mientras se reconstruye, el conjunto lee todos los demás de cabo a rabo y está sin protección**, y
  **cuanto mayores son los discos más dura esa ventana.** **2)** escribir una paridad **obliga a leer
  antes**, lo que penaliza la escritura frente al espejo.
- **el conjunto que no es un conjunto** · `[of]` · **Agrupar discos sin redundancia sólo para verlos
  como un volumen no es un nivel**, y **cuando en un pliego aparece como si lo fuera hay que decirlo.**

## La consolidación

| Arquitectura | Qué ve el equipo |
|---|---|
| **conexión directa** | **un disco suyo, por un cable de la propia máquina** |
| **conectado a la red** | **una carpeta compartida: FICHEROS** |
| **red de almacenamiento** | **un disco suyo aunque esté lejos: BLOQUES** |

- **la frontera que hay que saber explicar** · `[of]` · **Quien sirve ficheros decide él cómo se
  guardan y arbitra entre clientes; quien sirve bloques entrega trozos de disco y es el cliente el que
  pone encima su sistema de ficheros.**
- **el error caro** · `[of]` · **Montar un volumen de bloques corriente en dos máquinas a la vez
  CORROMPE los datos.** **Compartirlo exige un sistema de ficheros preparado para ello.**
- **la tercera forma** · `[of]` · **El almacenamiento por OBJETOS**: ni bloques ni árbol de carpetas,
  **objetos con identificador y datos descriptivos**, servidos por peticiones de red. **Es la base del
  archivo profundo.**
- **la jerarquía** · `[of]` · **en línea** —disco, al instante— · **casi en línea** —biblioteca con el
  robot montado, minutos— · **fuera de línea** —cinta en la estantería—. **Quien la gobierna es la
  gestión de activos de medios**: **sin catálogo, un archivo grande es material perdido con orden
  alfabético.**

## Arquitectura, protocolos e interfaces

| Interfaz | Qué la caracteriza |
|---|---|
| **serie avanzada** | **sencilla y barata; una cola de órdenes corta** |
| **serie conectada** | **doble camino a cada disco, colas largas, para funcionar sin parar** |
| **memoria no volátil sobre el bus del procesador** | **muchas colas en paralelo** |

- **la idea que ordena la tabla** · `[of]` · **Cada interfaz nació para un tipo de disco.** **La
  ganancia de la más moderna no está en el cable sino en dejar de fingir que hay una cabeza que
  mover.**
- **la regla para no equivocarse** · `[of]` · **Si el nombre del protocolo apunta a ÓRDENES DE DISCO,
  sirve bloques; si apunta a ficheros o carpetas compartidas, sirve ficheros.** **La red de
  almacenamiento va con los primeros; el almacenamiento conectado a la red, con los segundos.**
- **el sistema de ficheros compartido** · `[of]` · **Permite que varios puestos de edición monten el
  mismo volumen de bloques sin pisarse, porque un gestor arbitra quién escribe qué.**

## Servidores

| Sentido | Qué se le pide |
|---|---|
| **servidor de datos** | **disponibilidad, memoria, red** |
| **servidor de vídeo** | **caudal garantizado y arranque inmediato del primer fotograma** |

- **lo que hace especial al de vídeo** · `[of]` · **No puede llegar tarde.** **Uno de datos que tarda
  medio segundo más es lento; uno de vídeo que tarda medio segundo más ha dejado la emisión en
  negro.** **Por eso se dimensiona por caudal sostenido en el peor caso y no por capacidad.**
- **sus cuatro funciones** · `[of]` · **ingesta** · **reproducción para edición mientras se sigue
  grabando** · **emisión con el arranque exacto** · **trasiego con el archivo.**
- **las formas de no ser un punto único de fallo** · `[of]` · **duplicar componentes dentro de la
  máquina** —lo primero y lo más barato— · **una máquina en espera** · **agrupar máquinas en conjunto**
  —permite además mantener sin parar el servicio— · **virtualizar**, que hace que la máquina deje de
  ser un sitio y pase a ser un recurso.
- **EL AVISO CON EL QUE SE CIERRA** · `[of]` · **Un conjunto redundante NO es una copia de seguridad.**
  **Protege del fallo de un disco y de nada más: ni del borrado por error, ni del programa que cifra
  los ficheros, ni del incendio de la sala.** **Confundirlos es el error que más material ha destruido
  en esta industria.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 3 | Con cuatro discos, máxima capacidad útil con alguna redundancia | **Paridad simple** ✔ **·** deja tres discos útiles frente a dos de las otras |
| 14 | Qué se puede hacer con dos lectores de cinta de novena generación | **La opción oficial** ✔ **·** escritura en su generación y la anterior, con lectura más amplia |
| 20 | Mínimo de discos de un conjunto de paridad simple | **Tres** ✔ **·** con dos, la paridad es una copia y eso es el espejo |
| 70 | Cuántos bits hay en cuatro kibibytes | **32.768** ✔ **·** base mil veinticuatro, y en bits, no en bytes |
