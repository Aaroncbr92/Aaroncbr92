# Tema 1 del específico de Edición, Montaje y Procesos Audiovisuales · Conocimientos básicos de electrónica e informática aplicadas

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 1 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia son conceptos de electrónica e informática aplicados a una sala de edición —niveles de RAID, almacenamiento y redes—, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Aviso de reparto** | **Las cuatro preguntas de este punto son de informática y ninguna de electrónica**, aunque el anexo dedique un subpunto a cada una. **Tres de las cuatro son de RAID** |
| **Extensión** | **2.258 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el conjunto redundante de discos independientes
(**RAID**, *redundant array of independent disks*); la red de área local (**LAN**) y la red de área
extensa (**WAN**); el protocolo de internet (**IP**); el control de acceso al medio (**MAC**); la
unidad central de proceso (**CPU**); la memoria de acceso aleatorio (**RAM**); el disco de estado
sólido (**SSD**) frente al disco duro mecánico (**HDD**); el almacenamiento conectado a la red
(**NAS**) y la red de almacenamiento (**SAN**); la interfaz digital de vídeo serie (**SDI**); y el
sistema de alimentación ininterrumpida (**SAI**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, puntos 1.1 y 1.2):
> «Conocimientos básicos de electrónica aplicada.»
> «Conocimientos básicos de informática aplicada.»

**Cuatro preguntas.** Y las cuatro son de informática, no de electrónica: **tres de RAID y una de
redes**. El tribunal ha entendido «informática aplicada» como **la infraestructura sobre la que corre
una sala de edición**, y ahí es donde hay que estudiar.

<!-- indice -->

## Índice

- [1. Por qué una sala de edición es un problema de informática](#1-por-qué-una-sala-de-edición-es-un-problema-de-informática)
- [2. Qué es un RAID](#2-qué-es-un-raid)
- [3. Los niveles de RAID](#3-los-niveles-de-raid)
- [4. RAID 5, que es el que el examen destaca](#4-raid-5-que-es-el-que-el-examen-destaca)
- [5. El almacenamiento de una sala: local, NAS y SAN](#5-el-almacenamiento-de-una-sala-local-nas-y-san)
- [6. La red: los cuatro aparatos y para qué sirve cada uno](#6-la-red-los-cuatro-aparatos-y-para-qué-sirve-cada-uno)
- [7. La electrónica que el montador sí necesita](#7-la-electrónica-que-el-montador-sí-necesita)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Por qué una sala de edición es un problema de informática

**Un montador trabaja sobre ficheros que ni caben ni corren en un ordenador corriente.** Una hora de
material en alta definición sin comprimir pasa de los cien gigabytes, y un montaje de informativos
necesita **que varias salas lean el mismo material a la vez** mientras la ingesta sigue escribiendo.

De ahí salen los tres problemas que este tema resuelve:

1. **Capacidad**: dónde cabe el material.
2. **Velocidad**: si el disco no da el caudal que pide el códec, **el vídeo se corta en la
   reproducción**.
3. **Seguridad**: **un disco se rompe**, y el material de una jornada no se vuelve a grabar.

**El RAID resuelve los tres a la vez**, y por eso es lo que el examen pregunta.

## 2. Qué es un RAID

**Un RAID es un tipo de almacenamiento en el que los datos se escriben en varios discos dentro de un
mismo sistema.** Ésa es la respuesta oficial a la pregunta 26, y es la definición correcta: lo que
define un RAID **no es qué se guarda ni para qué, sino que el conjunto de discos se comporta como uno
solo**.

**Las siglas**: *redundant array of independent disks*, **conjunto redundante de discos
independientes**. Las tres palabras dicen lo esencial: **redundante** —hay información de más, para
poder reconstruir—, **conjunto** —varios discos vistos como uno— e **independientes** —cada disco es
una unidad completa—.

**Las tres opciones falsas de la pregunta 26 confunden el RAID con el uso que se le da:**

| Opción | Por qué no |
|---|---|
| «Varios proyectos de edición en un disco duro» | **Eso es simplemente usar un disco.** No hay conjunto |
| «Discos de diferente formato por seguridad» | **El RAID no exige formatos distintos**; al contrario, **pide discos iguales** |
| «Un solo proyecto en varios discos duros» | **Confunde el RAID con el reparto manual de un proyecto.** El RAID reparte **bloques de datos**, no proyectos |

**La distinción que resuelve la pregunta**: **el RAID es una forma de escribir, no una forma de
organizar el trabajo.** Quien la tenga clara no cae en ninguna de las tres.

## 3. Los niveles de RAID

**Cada nivel de RAID reparte los datos de una manera distinta**, y cada uno cambia el equilibrio entre
capacidad, velocidad y seguridad.

| Nivel | Cómo escribe | Qué gana | Qué pierde |
|---|---|---|---|
| **RAID 0** | ***Striping***: **distribuye los datos entre discos, sin redundancia** | **Velocidad** y **toda la capacidad** | **Ninguna seguridad**: si cae un disco, se pierde todo |
| **RAID 1** | ***Mirroring***: **duplica los datos de un disco en otro** | **Seguridad**: aguanta la caída de un disco | **La mitad de la capacidad** |
| **RAID 5** | *Striping* **con paridad distribuida** entre todos los discos | **Velocidad y tolerancia a fallo** con poca pérdida de capacidad | Necesita **tres discos como mínimo**; la reconstrucción es lenta |
| **RAID 6** | Como el 5, **con doble paridad** | **Aguanta la caída de dos discos** | Más pérdida de capacidad y de velocidad de escritura |
| **RAID 10** | **Espejos agrupados en *striping*** | **Velocidad y seguridad juntas** | **La mitad de la capacidad**, y hacen falta cuatro discos |

**La pregunta 4 pide identificar la afirmación correcta**, y la correcta es que **en el nivel RAID 1,
también conocido como sistema espejo, se duplican los datos de un disco en otro disco.**

**Las tres opciones falsas son la misma trampa repetida: cambian el número del nivel.**

| Opción | Qué dice | Por qué es falsa |
|---|---|---|
| a) | «El RAID 0 es el de mayor fiabilidad» | **El RAID 0 es el de menor fiabilidad**: no tiene ninguna redundancia |
| b) | «El RAID 0 es el sistema espejo» | **El espejo es el RAID 1** |
| c) | «En el RAID 1 se distribuyen los datos sin redundancia» | **Eso es el RAID 0** |

**La regla mnemotécnica que no falla**: **RAID 0, cero seguridad.** **RAID 1, un disco copiado en
otro.** Con esas dos frases se contestan las cuatro opciones.

## 4. RAID 5, que es el que el examen destaca

**La principal ventaja del RAID 5 es que su tolerancia a errores aporta velocidad y protección de los
datos.** Ésa es la respuesta oficial a la pregunta 92, y describe exactamente por qué el RAID 5 es el
que se monta en las salas de edición: **es el único de los niveles básicos que da las dos cosas a la
vez sin gastar la mitad del espacio.**

**Cómo lo consigue: la paridad.** El RAID 5 **reparte los datos entre todos los discos, como el RAID
0**, pero **añade en cada franja un bloque de paridad**, calculado a partir de los demás y **guardado
en un disco distinto cada vez**. Si un disco cae, **el sistema reconstruye lo que había en él a partir
de los otros y de la paridad**.

| | Con tres discos |
|---|---|
| **Capacidad útil** | **Dos discos de tres**: se pierde el equivalente a uno en paridad |
| **Discos que puede perder** | **Uno** |
| **Velocidad de lectura** | **Alta**: lee de varios discos a la vez |
| **Velocidad de escritura** | Menor que la de lectura: **hay que calcular la paridad** |

**Las tres opciones falsas de la pregunta 92, y por qué se caen:**

| Opción | Por qué no |
|---|---|
| «Sólo es necesario un sistema de un máximo de dos discos» | **Al revés: el RAID 5 exige tres discos como mínimo.** Con dos no hay dónde repartir la paridad |
| «No ofrece redundancia de datos» | **Precisamente la ofrece**: la paridad *es* la redundancia |
| «Sus prestaciones son superiores a cualquier otro nivel» | **Falso**: el RAID 0 es más rápido y el RAID 6 es más seguro. **El 5 es el equilibrio, no el máximo** |

**El aviso de oficio**: **un RAID no es una copia de seguridad.** Protege del fallo de un disco, **no
del borrado accidental ni del incendio de la sala**. En una casa de televisión el RAID mantiene el
trabajo vivo, y la copia se hace aparte.

## 5. El almacenamiento de una sala: local, NAS y SAN

**Dónde vive el material determina cómo se monta**, y el vocabulario aparece en los enunciados:

| Sistema | Qué es | Dónde se usa |
|---|---|---|
| **Almacenamiento local** | Discos dentro de la estación de edición | Proyectos de una sola sala |
| **NAS** | Un armario de discos **que sirve ficheros por la red**, con su propio sistema de ficheros | Trabajo compartido ligero, archivo |
| **SAN** | Una red dedicada que ofrece a cada estación **bloques de disco, como si fueran suyos** | **Edición compartida en tiempo real**: informativos, deportes |

**La diferencia que importa al montador**: **en un NAS se pide un fichero; en una SAN se pide un
bloque de disco.** Por eso **la SAN da el caudal sostenido que la reproducción de vídeo necesita** y
es la que se monta donde varias salas trabajan sobre el mismo material.

**Y en cualquiera de los tres, debajo hay un RAID.** No son alternativas al RAID: son **maneras de
presentar el RAID a las estaciones**.

## 6. La red: los cuatro aparatos y para qué sirve cada uno

**El aparato necesario para conectar una red local con una red de área extensa es el router o
enrutador.** Ésa es la respuesta oficial a la pregunta 32.

| Aparato | Qué hace | En qué nivel trabaja |
|---|---|---|
| **Hub** o concentrador | **Repite la señal por todos los puertos**, sin mirar a quién va | El más bajo: sólo eléctrico. **Está obsoleto** |
| **Switch** o conmutador | **Envía cada trama al puerto del destinatario**, mirando su dirección MAC | **Dentro de una misma red local** |
| **Router** o enrutador | **Une redes distintas y decide por qué camino sale cada paquete**, mirando su dirección IP | **Entre redes**: es el que saca la local a la extensa |
| «Interconectador» | **No existe** como aparato de red | — |

**La regla que resuelve la pregunta**: **el switch mueve dentro; el router mueve entre.** Una red
local y una red de área extensa **son dos redes distintas**, así que hace falta el que trabaja entre
redes.

**Por qué las otras tres se caen**: el **switch** es el aparato correcto **dentro** de la sala, pero
no sale de ella; el **hub** hace lo mismo que el switch pero peor y tampoco sale; y el
**«interconectador»** es una palabra inventada, del tipo que este cuadernillo usa a menudo como
relleno.

**Lo que el montador necesita saber de la red, más allá de la pregunta**: **el vídeo por red no
perdona la congestión**. Una sala de edición sobre red compartida **da cortes en la reproducción**
cuando otro tráfico satura el enlace, y por eso **la red de producción va separada de la ofimática**.

## 7. La electrónica que el montador sí necesita

**El punto 1.1 del anexo dice «electrónica aplicada» y el examen no ha preguntado nada de ella**, pero
el temario la desarrolla porque el programa la manda y porque **su vocabulario aparece en los otros
temas**.

| Concepto | Qué es | Dónde aparece en el oficio |
|---|---|---|
| **Señal analógica** | Varía de forma continua | El vídeo antes de la digitalización |
| **Señal digital** | Toma valores discretos, muestreados y cuantificados | **Todo lo que se edita hoy** |
| **Muestreo** | Cuántas veces por segundo se mide la señal | **Tema 4**: 4:2:2, 4:2:0 |
| **Cuantificación** | Con cuántos niveles se anota cada muestra | **Tema 2**: 8 bits frente a 10 bits |
| **Relación señal-ruido** | Cuánto ruido acompaña a la señal útil | **Tema 6**: los equipos de medida |
| **Impedancia** | La oposición del circuito al paso de la señal | **75 Ω** en las líneas de vídeo |
| **Alimentación y SAI** | Continuidad, filtrado y regulación | La sala no se apaga a mitad de un volcado |

**La conversión analógico-digital, en una frase**: **se mide la señal muchas veces por segundo
(muestreo) y cada medida se anota con un número de niveles limitado (cuantificación)**. **De la
primera depende qué frecuencias se conservan; de la segunda, cuántos matices.** Esas dos frases
explican, sin más aparato, por qué diez bits dan mejor degradado que ocho y por qué un audio a 48 kHz
llega hasta los 24 kHz.

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 4 | Afirmación correcta sobre los niveles RAID | d) En RAID 1, sistema espejo, se duplican los datos ✔ |
| 26 | Qué es el almacenamiento RAID | d) Los datos se escriben en varios discos de un mismo sistema ✔ |
| 32 | Aparato para conectar una red local con una extensa | a) Router o enrutador ✔ |
| 92 | Principal ventaja de RAID 5 | c) Su tolerancia a errores aporta velocidad y protección ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla**: las
cuatro son definiciones estándar de informática, verificables en cualquier manual de sistemas.

**El aviso de reparto**: **las cuatro preguntas de este punto son de informática y ninguna de
electrónica**, aunque el anexo dedique un subpunto a cada una. **Tres de las cuatro son de RAID**: es,
con diferencia, lo que más renta de este tema.

## 9. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son conceptos de informática y de electrónica
aplicados a una sala de edición, y **va entera como oficio**.

**Ninguna de sus cuatro respuestas descansa sólo en la plantilla.** Los niveles de RAID, la función
del router y la diferencia entre conmutar y enrutar **son definiciones estándar**, y el tema las
presenta como lo que son: **vocabulario técnico asentado, no doctrina de una fuente concreta**.

**Una advertencia de vocabulario**: **el examen usa «interconectador» como opción falsa**, y no es un
aparato de red. Este cuadernillo construye varios distractores así, **con palabras que suenan técnicas
y no designan nada**; conviene reconocerlos, porque **son la opción más fácil de descartar de toda la
pregunta**.
