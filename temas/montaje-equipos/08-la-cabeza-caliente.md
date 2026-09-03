# Tema 8 del específico de Montaje de Equipos Audiovisuales · La cabeza caliente

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Montaje de Equipos Audiovisuales · punto 8 |
| **Sirve para** | **Montaje de Equipos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los módulos de una cabeza caliente y su cableado, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Una pregunta** —la longitud máxima del par trenzado hacia el control remoto— **no se ha podido contrastar en documentación de fabricante ni en norma técnica**, y así se declara en el tema |
| **Extensión** | **1.999 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la panorámica horizontal (***pan***) y la vertical
(***tilt***), y el balanceo sobre el eje óptico (***roll***), que rotulados en mayúsculas —**PAN**,
**TILT** y **ROLL**— dan nombre a los tres módulos de la máquina; el par trenzado apantallado (**STP**) y
el par trenzado sin apantallar (**UTP**); la norma de transmisión serie diferencial de la
*Electronic Industries Alliance* (**EIA**) conocida como **RS-422**; el conector circular multipolo
**LEMO**, que es una marca; el conector de vídeo *Bayonet Neill-Concelman* (**BNC**); el conector de
audio profesional de tres polos (**XLR**); el conector de red (**RJ45**); la fibra óptica de la
*Society of Motion Picture and Television Engineers* (**SMPTE**); y la unidad de control de cámara
(**CCU**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Montaje de Equipos Audiovisuales,
> punto 4.4):
> «Cabeza caliente: Componentes y cableado.»

**Dos preguntas.** Es el punto más corto del cuadernillo y el más específico: una pregunta sobre el
cableado y otra sobre los módulos de la máquina.

<!-- indice -->

## Índice

- [1. Qué es una cabeza caliente](#1-qué-es-una-cabeza-caliente)
- [2. Los tres ejes y los tres módulos](#2-los-tres-ejes-y-los-tres-módulos)
- [3. El módulo PAN: la unión al soporte y la entrada de conectores](#3-el-módulo-pan-la-unión-al-soporte-y-la-entrada-de-conectores)
- [4. El control remoto y el cableado](#4-el-control-remoto-y-el-cableado)
- [5. El montaje paso a paso](#5-el-montaje-paso-a-paso)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Qué es una cabeza caliente

**Una cabeza caliente es una cabeza de cámara motorizada que se maneja a distancia**, sin que haya
nadie tocándola. El operador no está detrás de la cámara: está en un puesto de control, a veces en el
plató, a veces en el control de realización, a veces en la unidad móvil.

**Se llama «caliente» porque va en el extremo de una máquina** —la punta de una grúa, el carro de un
travelling, un pedestal robotizado, un raíl de techo— **donde una persona no cabe o no debe estar**.
El nombre inglés que aparece en los catálogos es *remote head* o *hot head*, y las dos expresiones
designan lo mismo.

**Lo que la distingue de una cabeza de fluido** es que en la de fluido el movimiento lo hace el brazo
del operador contra una resistencia mecánica, y en la caliente lo hacen **motores gobernados por un
control remoto**. La consecuencia práctica para el montaje es que **una cabeza caliente no se instala
sola: se instala con su cableado y con su puesto de control**, y si falta cualquiera de las tres
partes la máquina no sirve.

| | Cabeza de fluido | Cabeza caliente |
|---|---|---|
| **Quién mueve** | El operador, con el brazo | **Motores** |
| **Dónde está el operador** | Detrás de la cámara | **En un puesto de control remoto** |
| **Qué necesita** | Nivelado y equilibrado | **Nivelado, equilibrado, alimentación y línea de control** |
| **Dónde se usa** | Trípode, pedestal, hombro | **Grúa, travelling, raíl, punto inaccesible** |

**Las tres ventajas de oficio.** **Alcanza sitios donde no cabe una persona**, **quita peso del
extremo de la máquina** —una cabeza y una cámara pesan mucho menos que una cabeza, una cámara y un
operador— y **permite que un solo operador gobierne varias cámaras** desde un mismo puesto.

## 2. Los tres ejes y los tres módulos

**Una cabeza caliente se construye por módulos, y cada módulo es un eje de giro.** Ésta es la
arquitectura que hay que tener en la cabeza, porque es de donde sale la pregunta del examen.

| Módulo | Eje | Qué hace |
|---|---|---|
| **Módulo PAN** | Vertical | **Gira la cámara a izquierda y derecha.** Es el módulo de abajo: **el que une la cabeza al soporte** |
| **Módulo TILT** | Horizontal transversal | **Inclina la cámara arriba y abajo** |
| **Módulo ROLL** | Longitudinal, el del eje óptico | **Balancea la cámara**, inclinando el horizonte. No lo llevan todas |
| **Plataforma porta cámara** | — | **Sostiene la cámara** y la fija a la cabeza. No es un eje: es la bandeja |

**El orden de abajo arriba es siempre el mismo**: soporte → **PAN** → **TILT** → plataforma porta
cámara → cámara. **El ROLL, cuando existe, va entre el TILT y la plataforma**, y es el módulo que
convierte una cabeza de dos ejes en una de tres.

**La regla que ordena todo esto**: **el módulo que va abajo es el que carga con el peso de todo lo que
tiene encima**. Por eso el PAN es el módulo grande, el que lleva el anclaje al soporte y el que
concentra la conectividad.

## 3. El módulo PAN: la unión al soporte y la entrada de conectores

**El módulo de la cabeza caliente que permite la unión al soporte y en el que se sitúan todos los
conectores de la entrada de la cabeza al equipo es el módulo PAN.** Ésa es la respuesta oficial a la
pregunta 90, y es coherente con la arquitectura: **el módulo de abajo es el que toca el soporte y el
que recibe el cableado que sube desde el suelo**.

**Por qué los conectores van ahí y no arriba.** Un cable que entrase por el módulo TILT tendría que
cruzar la articulación del PAN colgando, y **el giro panorámico lo enrollaría en la columna** hasta
arrancarlo. Entrando por el PAN, **el cable llega a la parte que gira menos y se reparte hacia arriba
por dentro de la máquina**, con las holguras ya calculadas por el fabricante.

**Las tres opciones falsas de la pregunta 90 son piezas reales que hacen otra cosa**: la **plataforma
porta cámara** sostiene la cámara pero no une la cabeza al soporte y no lleva la entrada de
conectores; el **módulo ROLL** balancea; y el **módulo TILT** inclina.

**Lo que hay en el panel del módulo PAN**, en las cabezas al uso: la entrada de **alimentación**, la
entrada de la **línea de control** que viene del puesto remoto, y las entradas y salidas de la señal
de la cámara —**vídeo por BNC o por fibra SMPTE**, **audio por XLR**, **datos y red por RJ45**, y los
multipolo tipo **LEMO** para el objetivo y los servos de zoom y foco.

## 4. El control remoto y el cableado

**Una cabeza caliente necesita tres líneas**, y conviene no confundirlas porque se montan por
separado y fallan por separado:

1. **La alimentación.** Corriente para los motores de la cabeza y, muchas veces, para la propia
   cámara.
2. **La línea de control.** El camino de ida y vuelta entre el **puesto de control remoto** y la
   cabeza: las órdenes de *pan*, *tilt*, *roll*, zoom, foco e iris van por aquí, y por aquí vuelven
   las posiciones de los ejes.
3. **La línea de señal.** El vídeo y el audio de la cámara hacia el control, y el retorno y la
   intercomunicación hacia la cámara.

**Cómo se lleva la línea de control.** Las cabezas al uso admiten tres caminos: **par trenzado**,
**fibra óptica** y **enlace inalámbrico**. El par trenzado es el más común en instalación fija porque
es barato, se remata en obra y admite tiradas largas; la fibra se usa cuando la distancia o el ruido
eléctrico lo exigen; y el inalámbrico, cuando la máquina se mueve y no puede arrastrar cable.

**Por qué par trenzado y no coaxial.** La línea de control es **una transmisión serie diferencial**,
del tipo **RS-422**: la señal viaja como la **diferencia de tensión entre los dos hilos de un par**, de
modo que **el ruido que se cuela lo hace igual en los dos hilos y la diferencia lo cancela**. Ése es
el motivo de que el par vaya **trenzado**: el trenzado hace que los dos hilos recojan la misma
interferencia. Y ése es el motivo de que se llegue lejos con un cable barato.

**En caso de utilizar un cable de par trenzado para la comunicación de una cabeza caliente con su
control remoto, la longitud máxima que podemos utilizar es de 1.000 metros.** Ésa es la respuesta
oficial a la pregunta 72. **Las tres opciones falsas** —2.000, 500 y 300 metros— **son cifras
plausibles y sólo una es la de la plantilla**.

**Lo que el montador tiene que saber de esa cifra**, más allá de memorizarla: **el límite de una línea
diferencial sobre par trenzado no es un número absoluto, sino un compromiso entre distancia y
velocidad**. A más metros, menos velocidad de datos admisible, porque la atenuación y el retardo del
cable degradan el flanco de la señal. **Por eso el fabricante da una longitud máxima y no una
longitud recomendada**: por encima de ella, la cabeza responde tarde o no responde.

**Los tres cuidados del cableado de control en montaje.** **No compartir canaleta con líneas de
fuerza** —la interferencia que el par cancela es la que entra por igual en los dos hilos, no la que
entra por acoplamiento fuerte a un solo tramo—; **rematar el apantallado en un solo extremo** para no
cerrar un bucle de masa; y **dejar el bucle de servicio en la base**, no en la punta, porque la punta
es la que gira.

## 5. El montaje paso a paso

**El orden de montaje de una cabeza caliente es el orden inverso del desmontaje**, y se hace siempre
de abajo arriba:

1. **Preparar el soporte.** Trípode, pedestal, carro o pluma: **nivelado antes de nada**, porque una
   cabeza caliente no tiene bola niveladora propia en muchos modelos y hereda el nivel de lo que hay
   debajo.
2. **Anclar el módulo PAN al soporte.** Es la unión que sostiene el conjunto; se aprieta con la
   máquina descargada.
3. **Montar el TILT y, si lo hay, el ROLL.**
4. **Colocar la plataforma porta cámara y encima la cámara**, con la óptica y los accesorios que va a
   llevar en plano: el equilibrado se hace con la máquina completa, no con el cuerpo desnudo.
5. **Equilibrar el eje de TILT** desplazando la cámara adelante o atrás sobre la plataforma, hasta que
   se quede quieta en cualquier inclinación.
6. **Cablear por el módulo PAN**: alimentación, control y señal, en ese orden, dejando el bucle de
   servicio.
7. **Comprobar recorridos en vacío**, a mano y luego desde el control, buscando el punto en que el
   cable se tensa. **Ése es el límite real de la máquina**, y hay que conocerlo antes del directo.
8. **Encender y hacer el reglaje** con el operador remoto: sentido de los ejes, velocidades y topes.

**El error clásico**: dar por bueno el recorrido con la cámara apagada y sin cables. **Con el
cableado puesto, el recorrido útil siempre es menor**, y el momento de descubrirlo no es en el
directo.

## 6. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 72 | Longitud máxima del par trenzado hacia el control remoto | a) 1.000 metros ✔ **·** sólo con la plantilla |
| 90 | Módulo que une la cabeza al soporte y lleva los conectores | d) Módulo PAN ✔ |

**Las dos respuestas oficiales son correctas.**

**Y una de las dos descansa sólo en la plantilla**: la longitud máxima del par trenzado.

## 7. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es una máquina y su cableado, y va como oficio: los
módulos de la cabeza, el orden en que se apilan, el papel del módulo de abajo, las tres líneas que
suben hasta ella y el procedimiento de montaje.

**Una declaración expresa sobre lo que no se ha podido contrastar**: **la longitud máxima de 1.000
metros del par trenzado hacia el control remoto no se ha verificado en documentación de fabricante ni
en norma técnica**. Es un dato de catálogo, y descansa en la plantilla oficial, que es el quinto nivel
de la jerarquía de fuentes de este proyecto.

**Lo que este tema sí sostiene sobre ese dato** es el porqué: que la línea de control es una
transmisión serie diferencial sobre par trenzado, que el trenzado sirve para que el ruido entre por
igual en los dos hilos y la diferencia lo cancele, y que el alcance de una línea así es un compromiso
entre distancia y velocidad, no una constante. **Eso es oficio, y es lo que hace la cifra legible.**
