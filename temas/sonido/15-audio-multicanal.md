# Tema 15 del específico de Sonido · Audio multicanal

Las siglas y términos de este tema, presentados de entrada: el canal de efectos de baja frecuencia
(**LFE**, *low-frequency effects*), que es el «punto uno» de todos los formatos; la codificación
**Dolby E** para transporte en producción; el audio basado en objetos y su cama de canales fijos
(*bed*); las mezclas reducidas compatibles (*downmix*) en sus dos variantes, la de estéreo puro
(**Lo/Ro**, *left only / right only*) y la codificada en matriz (**Lt/Rt**, *left total / right
total*); y la notación de los formatos por tres cifras —canales del plano horizontal, de baja
frecuencia y de altura—.

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 13):
> «AUDIO MULTICANAL. Conocimientos necesarios para la producción de una señal multicanal, 5.1,
> conocimientos básicos de los estándares, codificación DOLBY E.»

**Cuatro preguntas.** **Y el punto que mejor muestra cómo ha cambiado el sonido de televisión**:
**dos de sus cuatro preguntas van de audio basado en objetos, que hace quince años no existía.**

<!-- indice -->

## Índice

- [1. Cómo se lee un formato multicanal](#1-cómo-se-lee-un-formato-multicanal)
- [2. Canales frente a objetos](#2-canales-frente-a-objetos)
- [3. Las mezclas reducidas](#3-las-mezclas-reducidas)
- [4. El Dolby E](#4-el-dolby-e)
- [5. Producir una señal multicanal](#5-producir-una-señal-multicanal)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Cómo se lee un formato multicanal

**La notación de tres cifras es la que ordena todo el punto**, y **se lee siempre igual:**

> **Canales del plano horizontal · Canales de baja frecuencia · Canales de altura**

**La pregunta 54**: **una escucha de formato 5.1.4 significa 5 en plano horizontal, uno de efectos en
baja frecuencia y 4 en vertical.** Ésa es la respuesta oficial.

| Formato | Horizontal | Baja frecuencia | Altura | Dónde |
|---|---|---|---|---|
| **2.0** | **2** | — | — | **Estéreo** |
| **5.1** | **5** | **1** | — | **El envolvente clásico de televisión y cine** |
| **7.1** | **7** | **1** | — | **Cine y disco** |
| **5.1.4** ✔ | **5** | **1** | **4** | **Escucha inmersiva doméstica y de sala pequeña** |
| **9.1.6** | **9** | **1** | **6** | **Salas de mezcla inmersiva** |

**Y los cinco canales del 5.1, que hay que saber nombrar**: **izquierdo, central, derecho, envolvente
izquierdo y envolvente derecho**, más **el LFE.**

**El LFE merece una precisión que casi nadie hace**: **no es «el altavoz de graves».** **Es un canal
INDEPENDIENTE, de banda limitada —hasta unos 120 hercios— pensado para efectos de mucha energía.**
**Los graves de los otros cinco canales no van por ahí: van por sus propios canales, y es el sistema
de reproducción el que decide si los redirige al subgrave.** **Por eso se llama «punto uno»: porque no
es un canal completo.**

**Las tres opciones falsas de la pregunta 54 y por qué caen:**

1. **«5 altavoces frontales, uno de graves y 4 traseros»** **pone los cinco delante**, cuando **dos de
   los cinco son envolventes**, y **convierte los de altura en traseros.**
2. **«Ese formato no es estándar»** **es falsa**: **el 5.1.4 es una configuración corriente.**
3. **«Envolvente con 4 objetos»** **confunde CANALES con OBJETOS**, que es exactamente la distinción
   del epígrafe 2.

## 2. Canales frente a objetos

**Ésta es la idea central del punto y la que dos preguntas miden.**

**La pregunta 81**: **lo que caracteriza a Dolby Atmos frente a otros formatos envolventes es que
utiliza un enfoque basado en objetos de audio, permitiendo que los sonidos se coloquen y se muevan en
cualquier parte tridimensional del espacio, incluidos los canales superiores.** Ésa es la respuesta
oficial.

| | **Basado en CANALES** | **Basado en OBJETOS** |
|---|---|---|
| **Qué se manda** | **Una señal POR ALTAVOZ** | **Una señal MÁS SUS COORDENADAS** |
| **Quién decide dónde suena** | **El mezclador, al mezclar** | **El decodificador de cada sala, al reproducir** |
| **Si la sala tiene otro número de altavoces** | **Hay que hacer otra mezcla** | **La misma mezcla se adapta** |

**La consecuencia práctica es la que justifica el sistema**: **una mezcla basada en objetos suena
correctamente en una sala de cine con sesenta altavoces y en una barra de sonido de salón.** **No
porque se degrade con gracia, sino porque el decodificador RECALCULA el reparto con los altavoces que
hay.**

**Las tres opciones falsas de la 81 son tres afirmaciones falsas y comprobables**: **que envía a cinco
canales específicos —eso es el 5.1—, que se limita a altavoces de pared excluyendo el techo —justo lo
contrario: la altura es su aportación— y que funciona exclusivamente en salas de cine —hay
implantación doméstica—.**

**La pregunta 10**: **el tamaño máximo del bed permitido en Dolby Atmos es 7.1.2.** Ésa es la
respuesta oficial.

**Qué es el bed y por qué tiene un máximo**: **una mezcla basada en objetos no renuncia del todo a los
canales.** **Lo que no se mueve —el ambiente, la música, a menudo el diálogo— se pone en una CAMA de
canales fijos**, y **sólo lo que tiene que viajar por la sala se hace objeto.** **El sistema reserva
una parte de su capacidad para esa cama, y esa parte tiene un tope: 7.1.2**, es decir, **siete
canales horizontales, uno de baja frecuencia y dos de altura.**

**Y la opción d), «118», es un distractor bien puesto**: **es del orden del número total de elementos
que el sistema maneja**, y **quien recuerde una cifra grande asociada a Atmos puede marcarla.** **La
pregunta no pregunta por el total: pregunta por la cama.**

## 3. Las mezclas reducidas

**La pregunta 96**: **si se quiere hacer un downmix y poder decodificar después la señal trasera y la
central, hay que hacer un downmix Lt/Rt.** Ésa es la respuesta oficial.

**Las dos maneras de bajar un multicanal a dos canales, y no son intercambiables:**

| Downmix | Qué hace | Qué se puede recuperar |
|---|---|---|
| **Lo/Ro** | **Suma los canales a izquierda y derecha SIN codificar nada** | **Nada**: es una mezcla estéreo normal y lo envolvente se pierde |
| **Lt/Rt** ✔ | **Codifica en MATRIZ el central y los envolventes** dentro de los dos canales | **Un decodificador de matriz puede volver a separar central y traseros** |

**Cómo funciona la matriz, en una línea**: **el central se reparte por igual entre los dos canales, y
los envolventes se meten desfasados 180 grados entre uno y otro.** **Un decodificador que sume
recupera el centro; uno que reste, los traseros.** **Es la misma aritmética de suma y resta de la
conexión balanceada del tema 11, aplicada aquí a la espacialidad.**

**Y el precio de esa compatibilidad, que hay que conocer**: **una mezcla Lt/Rt escuchada en estéreo
puro no suena idéntica a una Lo/Ro.** **El desfase de los envolventes se nota.** **Por eso las
entregas de emisión suelen pedir las dos, o pedir Lt/Rt sabiendo lo que implica.**

## 4. El Dolby E

**El enunciado lo nombra expresamente y el examen no lo pregunta.** **El tema lo desarrolla porque el
programa lo pide y porque resuelve un problema muy concreto de las instalaciones de televisión.**

**Cuál es el problema**: **una instalación de televisión transporta audio en pares AES3, dos canales
por par.** **Un 5.1 son seis canales: tres pares.** **Y en el momento en que hay que pasar por un
equipo que sólo lleva un par —un enlace, un servidor antiguo, una matriz— el 5.1 no cabe.**

**Qué hace el Dolby E**: **empaqueta hasta ocho canales de audio, con sus metadatos, DENTRO de un solo
par AES3**, y **lo hace troceado en fotogramas de vídeo**, de modo que **se puede editar y conmutar en
los cortes de imagen sin producir ruido.**

**Y ésa es su virtud y su límite**: **está pensado para PRODUCCIÓN y contribución, no para emisión al
público.** **Es una codificación de transporte interno.** **Lo que sale al aire va en el sistema de
emisión que corresponda.**

## 5. Producir una señal multicanal

**El enunciado pide «conocimientos necesarios para la producción de una señal multicanal», y son
cinco:**

1. **Monitorización correcta.** **No se puede mezclar en 5.1 sin cinco altavoces bien colocados y
   calibrados en nivel.** **Es la parte que más se descuida y la que más caro sale.**
2. **Decidir qué va al central.** **En televisión, el diálogo.** **Un central mal usado descoloca todo
   lo demás.**
3. **Gestionar el LFE con criterio.** **Es efectos, no graves de todo.**
4. **Comprobar el downmix.** **La mayoría del público oirá la mezcla en estéreo o en una barra**, así
   que **la mezcla tiene que sobrevivir a la reducción.** **Es el epígrafe 3.**
5. **Cuidar los metadatos.** **La sonoridad del tema 14 y el tipo de downmix viajan como metadatos**,
   y **una entrega sin ellos o con ellos mal puestos suena mal sin que nada esté técnicamente roto.**

## 6. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 10 | Tamaño máximo del bed en Dolby Atmos | a) 7.1.2 ✔ **·** sólo con la plantilla |
| 54 | Qué significa una escucha 5.1.4 | a) 5 horizontales, 1 de baja frecuencia y 4 en vertical ✔ |
| 81 | Qué caracteriza a Dolby Atmos | b) Un enfoque basado en objetos de audio ✔ |
| 96 | Downmix del que se puedan decodificar trasera y central | b) Lt/Rt ✔ |

**Las cuatro respuestas oficiales son correctas.**

**Una de las cuatro descansa sólo en la plantilla**: **la cifra del tamaño máximo de la cama.**

**Y el aviso de estudio**: **tres de las cuatro se contestan con la notación de tres cifras y la
distinción canal/objeto.** **La cuarta es un dato de especificación de fabricante y hay que
memorizarla.**

## 7. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es el audio multicanal, y **va como oficio**, salvo una
afirmación que descansa en la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Una afirmación**: el tamaño máximo de la cama de canales de un sistema de audio basado en objetos | Pregunta 10 |

**Tres declaraciones expresas:**

1. **La documentación técnica de Dolby Laboratories no se ha consultado en este proyecto.** **La cifra
   de 7.1.2 como cama máxima descansa en la plantilla oficial**, y **lo que el tema sostiene por su
   cuenta es el CONCEPTO de cama frente a objeto**, que **es lo que hace la pregunta legible.** **Es la
   misma declaración que este proyecto hizo con las 128 pistas en el temario de Realización
   Televisión.**
2. **Las cifras del canal de efectos de baja frecuencia —banda limitada hasta unos 120 hercios— son de
   uso corriente y varían según el sistema.** **El tema las da como orden de magnitud**, y **ninguna
   respuesta depende de ellas.**
3. **El mecanismo de la codificación en matriz del downmix Lt/Rt se describe aquí de forma
   conceptual.** **Los coeficientes exactos de mezcla están en las especificaciones de los sistemas de
   matriz, que no se han consultado.** **Lo que la pregunta 96 mide es cuál de los dos downmix conserva
   la información espacial**, y **eso el tema lo sostiene.**

**El resto del tema va como oficio y así se declara**: la notación de tres cifras, la naturaleza del
canal de efectos de baja frecuencia, la diferencia entre audio basado en canales y basado en objetos,
la aritmética de la matriz de downmix, el problema que el Dolby E resuelve y los cinco requisitos de
una producción multicanal. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
