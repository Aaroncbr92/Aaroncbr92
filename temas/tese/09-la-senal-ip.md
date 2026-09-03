# Tema 9 del específico de Técnica de Equipos y Sistemas Electrónicos · La señal audiovisual sobre redes

Las siglas de este tema, presentadas de entrada: el protocolo de internet (**IP**), que da nombre al
punto; las familias de normas de la Sociedad de Ingenieros de Cine y Televisión —**SMPTE ST 2110** y
**SMPTE ST 2022**— para medios sobre red gestionada; la interfaz digital serie (**SDI**, *serial
digital interface*) y la interfaz digital multicanal de audio (**MADI**, *multichannel audio digital
interface*), las dos del tema 8; la modulación por impulsos codificados (**PCM**, *pulse code
modulation*); la norma de audio en red de la Sociedad de Ingeniería de Audio (**AES67**); el
transporte seguro y fiable (**SRT**, *secure reliable transport*); el protocolo de datagramas de
usuario (**UDP**); la petición automática de repetición (**ARQ**, *automatic repeat request*); la
corrección de errores hacia adelante (**FEC**, *forward error correction*); el cifrado avanzado con
clave de 256 bits (**AES-256**, que **no** es la Sociedad de Ingeniería de Audio sino el *advanced
encryption standard*); el envío a varios destinos (*multicast*); el protocolo de tiempo de precisión
(**PTP**), que el tema 8 ya presentó; y los bits por segundo (**bps**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 11):
> «SEÑAL IP: Señal video IP y audio IP. SMPTE 2110. SMPTE 2022. Sincronización PTP»

**Siete preguntas.** **Y el punto donde esta ocupación se encuentra con el futuro de las
instalaciones**: **la matriz y el cable coaxial del tema 8 se están sustituyendo por una red.**

**Un aviso de nomenclatura antes de empezar, porque el propio examen lo provoca**: **en este punto
aparecen dos siglas «AES» que no tienen nada que ver.** **La AES67 es de la Sociedad de Ingeniería de
Audio; el AES-256 de la pregunta 14 es un algoritmo de cifrado.** **Coinciden las tres letras y no la
cosa.**

<!-- indice -->

## Índice

- [1. Por qué la señal audiovisual se pasa a IP](#1-por-qué-la-señal-audiovisual-se-pasa-a-ip)
- [2. La familia SMPTE ST 2110](#2-la-familia-smpte-st-2110)
- [3. La redundancia: SMPTE ST 2022-7](#3-la-redundancia-smpte-st-2022-7)
- [4. Los conceptos de red que el examen pide](#4-los-conceptos-de-red-que-el-examen-pide)
- [5. La corrección de errores y el transporte seguro](#5-la-corrección-de-errores-y-el-transporte-seguro)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Por qué la señal audiovisual se pasa a IP

| | **Infraestructura clásica** | **Infraestructura IP** |
|---|---|---|
| **Un cable lleva** | **Una señal** | **Todas las que quepan** |
| **Conmutar** | **Una matriz física con N × M cruces** | **Suscribirse a un flujo** |
| **Ampliar** | **Más bastidor** | **Más ancho de banda** |
| **Formatos** | **Cada uno con su interfaz** | **Todos por el mismo cable** |
| **Lo que hay que resolver** | **Nada: el cable garantiza el camino** | **Reloj, ancho de banda, prioridad y redundancia** |

**La última fila es la que ocupa el resto del tema.** **Una red no garantiza nada por sí sola**, y
**las normas de este punto existen precisamente para poner de acuerdo a los fabricantes en cómo se
resuelve cada garantía que se pierde.**

## 2. La familia SMPTE ST 2110

**Es la norma que descompone la señal audiovisual en flujos *separados***: **el vídeo por un lado, el
audio por otro y los datos por otro.** **Eso es lo que la distingue de todo lo anterior: en SDI iba
todo incrustado en la misma trama; en 2110, cada esencia va por su camino y se vuelven a juntar
gracias al reloj común.**

**Las partes publicadas, con sus títulos oficiales tomados del índice que la propia SMPTE publica en
su biblioteca abierta y que este proyecto tiene volcado:**

| Documento | Título oficial |
|---|---|
| **ST 2110-10** | «Professional Media Over Managed IP Networks — System Timing and Definitions» |
| **ST 2110-20** | «Professional Media Over Managed IP Networks — Uncompressed Active Video» |
| **ST 2110-21** | «Professional Media Over Managed IP Networks — Traffic Shaping and Delivery Timing for Video» |
| **ST 2110-22** | «Professional Media Over Managed IP Networks — Constant Bit-Rate Compressed Video» |
| **ST 2110-30** | «Professional Media Over Managed IP Networks — PCM Digital Audio» |

**La pregunta 41**: **el estándar que regula la transmisión basada en AES67 en una instalación de
televisión IP es SMPTE 2110-30.** Ésa es la respuesta oficial, **y no descansa en la plantilla: el
título oficial de esa parte es «PCM Digital Audio», y es la única de las cuatro opciones que trata de
audio.**

**Las tres opciones falsas son partes REALES de la misma familia y todas son de vídeo o de sistema**:
**la 2110-20 es vídeo activo sin comprimir, la 2110-21 es el conformado de tráfico de vídeo y la
2110-06 no figura entre las partes publicadas.** **La pregunta se contesta sabiendo que la treintena
es la del audio.**

**Y el aviso que el propio índice de la SMPTE deja anotado**: **en esta familia no existe una parte
«ST 2110-50».** **Las publicadas son las de la tabla más las partes 31, 40, 41 y 43, la hoja de ruta y
tres prácticas recomendadas.**

## 3. La redundancia: SMPTE ST 2022-7

**El principal objetivo del estándar SMPTE 2022-7 en la transmisión de contenido multimedia sobre
redes IP es proporcionar conmutación sin interrupciones entre rutas redundantes para garantizar la
continuidad de la transmisión.** Ésa es la respuesta oficial a la pregunta 38.

**Cómo funciona, y es una idea elegante**: **el emisor manda *dos copias idénticas* del mismo flujo por
*dos caminos de red distintos*.** **El receptor recibe las dos y va tomando de cada una los paquetes que
le lleguen bien.** **Si un camino se cae, no hay que conmutar nada: los paquetes siguen llegando por
el otro.**

**Y de ahí el nombre que el sector le da: conmutación sin costuras.** **No es una conmutación de
reserva que tarda en entrar; es que las dos rutas están siempre activas.**

**Las tres opciones falsas trasladan el estándar a terrenos que no le tocan**: **compresión avanzada,
alta definición para móviles y — la cuarta— otra función distinta.** **La palabra que decide es
«redundantes».**

**Y el contraste con el tema 8, que es lo que ordena las dos maneras de protegerse:**

| Tecnología | Cómo se protege |
|---|---|
| **MADI y SDI** | **Duplicando el *cable***: dos caminos físicos y un conmutador que elige |
| **ST 2110 sobre IP** | **Duplicando el *flujo***: la 2022-7, sin conmutador y sin corte |

## 4. Los conceptos de red que el examen pide

**Tres preguntas son de vocabulario básico de transmisión, y las tres se contestan con la definición.**

**La pregunta 19**: **la latencia en la transmisión de vídeo en directo es el retraso entre la captura
y la visualización.** Ésa es la respuesta oficial.

**La pregunta 30**: **el bit rate describe el número de bits que se transmiten por unidad de tiempo,
generalmente medido en bits por segundo.** Ésa es la respuesta oficial.

**Y las opciones falsas de las dos preguntas cambian la magnitud por otra del mismo mundo**: **calidad
de imagen, velocidad de transmisión, resolución, capacidad de un disco, tamaño de un archivo.**
**Ninguna es tiempo de retraso ni cantidad de bits por segundo.**

**La pregunta 75**: **las transmisiones en multicast utilizan el rango de direcciones 224.0.0.0/4.**
Ésa es la respuesta oficial.

**Y las tres opciones falsas son rangos reales con otro uso, lo que hace la pregunta buena:**

| Rango | Para qué es de verdad |
|---|---|
| **224.0.0.0/4** ✔ | **Multicast**: es la clase D |
| **10.0.0.0/8** | **Direccionamiento privado**: redes internas grandes |
| **169.254.0.0/16** | **Autoconfiguración**: la dirección que un equipo se pone solo cuando NO encuentra servidor. **Verla en un equipo es el síntoma de que no está recibiendo configuración** |
| **192.168.0.0/16** | **Direccionamiento privado**: el de las redes pequeñas |

**El tercer rango merece la nota porque es diagnóstico puro**: **un equipo con una dirección
169.254.x.x no tiene un problema de dirección: tiene un problema de servidor o de cable.** **Es el
tema 15.**

## 5. La corrección de errores y el transporte seguro

**La pregunta 90**: **el FEC, en español corrección de errores hacia delante, es un mecanismo que
mediante la agregación de bits adicionales a la información puede corregir los errores de forma
automática.** Ésa es la respuesta oficial.

**Y la palabra que lo define es «hacia delante»**: **el receptor corrige *sin pedir nada*.** **No hay
vuelta atrás, no hay retransmisión, no hay espera.** **Se paga con ancho de banda —los bits
adicionales— y se cobra en latencia constante.**

**Las dos maneras de sobrevivir a la pérdida de paquetes, que es lo que separa los dos mecanismos de
este epígrafe:**

| Mecanismo | Cómo recupera | Coste |
|---|---|---|
| **FEC** | **Con redundancia enviada por adelantado** | **Más ancho de banda**, latencia *fija* |
| **ARQ** | **Pidiendo la retransmisión** del paquete perdido | **Menos ancho de banda**, latencia *variable* |

**La pregunta 14 es negativa y va del segundo**: **la característica que *no* es del protocolo SRT es que
sea «un protocolo de transmisión de alta latencia basado en UDP con recuperación de pérdida de
paquetes ARQ».** Ésa es la respuesta oficial.

**Y hay que ser preciso sobre qué es lo que falla en esa afirmación, porque casi todo lo que dice es
cierto**: **el SRT SÍ está basado en UDP y SÍ usa recuperación por retransmisión.** **Lo que es falso
es «de alta latencia»**: **el SRT existe precisamente para conseguir transmisión FIABLE con BAJA
latencia sobre redes no gestionadas.** **Es su razón de ser y lo que lo hace útil para contribución
por internet pública.**

**Las tres afirmaciones verdaderas que la pregunta ofrece son**: **que admite cifrado AES-256, que
tiene mecanismo contra la pérdida de paquetes y que es de código abierto.**

**La lección de método que deja esta pregunta**: **en una opción larga con varios datos, basta con que
UNO sea falso para que la opción lo sea.** **Hay que leer los adjetivos, no sólo los sustantivos.**

## 6. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 14 | Cuál NO es característica del protocolo SRT | a) Que sea de alta latencia ✔ |
| 19 | Qué significa latencia en directo | b) El retraso entre captura y visualización ✔ |
| 30 | Qué describe el término bit rate | b) Bits transmitidos por unidad de tiempo ✔ |
| 38 | Objetivo del estándar SMPTE 2022-7 | c) Conmutación sin interrupciones entre rutas redundantes ✔ |
| 41 | Qué estándar regula la transmisión basada en AES67 | b) SMPTE 2110-30 ✔ **·** verificado en el índice de la SMPTE |
| 75 | Rango de direcciones del multicast | d) 224.0.0.0/4 ✔ |
| 90 | Qué es el FEC | b) Corrección de errores hacia delante ✔ |

**Las siete respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Un aviso de reparto**: **una de las siete es negativa** —la 14—, **y su opción falsa es larga y
mayoritariamente cierta.** **Es la pregunta que mejor castiga la lectura en diagonal de todo el
cuadernillo.**

## 7. Trazabilidad

**Este tema no cita ninguna norma articulada**, y **cita el índice oficial de una familia de normas.**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Índice de la familia SMPTE ST 2110**, publicado por la propia SMPTE en su biblioteca abierta (`fuentes/normas-tecnicas/SMPTE-ST-2110-indice.md`) | **Los títulos oficiales de las partes 10, 20, 21, 22 y 30**, citados literales, y **el aviso de que no existe una parte 2110-50**. **Nada del contenido interno de ninguna parte** |

**Cuatro declaraciones expresas:**

1. **El texto de las partes de la SMPTE ST 2110 no se ha leído**: **este proyecto tiene volcado su
   ÍNDICE con los títulos oficiales, no los documentos.** **La respuesta a la pregunta 41 se sostiene
   con el título de la parte 30 —«PCM Digital Audio»—, que es lo que la hace verificable**, y **no con
   ninguna afirmación sobre su articulado.**
2. **El texto de la SMPTE ST 2022-7 no se ha consultado.** **Lo que este tema sostiene sobre ella es
   el CONCEPTO de conmutación sin costuras por flujo duplicado**, que **es lo que la pregunta 38 mide**,
   y **coincide con la respuesta oficial.**
3. **La especificación del protocolo SRT no se ha consultado.** **Lo que el tema sostiene —que se apoya
   en UDP, que recupera por retransmisión y que su objetivo es baja latencia— es conocimiento común
   del sector**, y **es lo que hace la pregunta 14 contestable.**
4. **Los rangos de direccionamiento del epígrafe 4 están normalizados por documentos de la Autoridad de
   Números Asignados en Internet que no se han consultado.** **Los valores que este tema da son de uso
   universal y coinciden con la respuesta oficial**, y **no se atribuyen a un articulado.**

**El resto del tema va como oficio y así se declara**: la comparación entre infraestructura clásica e
IP y lo que hay que resolver al pasar a red, la idea de esencias separadas de la ST 2110, la diferencia
entre duplicar cable y duplicar flujo, la distinción entre corrección hacia delante y retransmisión, y
el valor diagnóstico de una dirección de autoconfiguración. **Nada de eso está en un boletín oficial ni
en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
