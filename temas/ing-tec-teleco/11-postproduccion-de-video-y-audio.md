# Tema 11 del específico de Ingeniería Técnica · Telecomunicación · Postproducción de vídeo y audio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 15 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el código de tiempo y el equipamiento de postproducción, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Desajuste declarado** | **El enunciado pide equipamiento y diagrama a bloques**, y **lo que ha caído es aritmética en base sesenta con un resto de veinticinco** |
| **Extensión** | **1.553 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el código de tiempo (**TC**, *timecode*); los
fotogramas por segundo (**fps**); el código de tiempo longitudinal (**LTC**) y el vertical
(**VITC**); la lista de decisiones de edición (**EDL**); el formato de intercambio de material
(**MXF**); la unidad central de proceso (**CPU**) y la de proceso gráfico (**GPU**); y la Sociedad de
Ingenieros de Cine y Televisión (**SMPTE**), que normaliza el código de tiempo.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 15):
> «Postproducción video y audio: Equipamiento. Diagrama a bloques. Interconexión.»

**Una pregunta.** **Y es de cálculo, no de equipamiento**: **una resta de códigos de tiempo.**

**Ese desajuste conviene decirlo**: **el enunciado pide equipamiento y diagrama a bloques, y lo que ha
caído es aritmética en base sesenta con un resto de veinticinco.**

<!-- indice -->

## Índice

- [1. El código de tiempo](#1-el-código-de-tiempo)
- [2. Cómo se opera con códigos de tiempo](#2-cómo-se-opera-con-códigos-de-tiempo)
- [3. El equipamiento que el enunciado pide](#3-el-equipamiento-que-el-enunciado-pide)
- [4. La interconexión](#4-la-interconexión)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. El código de tiempo

**Qué es**: **una etiqueta que identifica cada imagen de forma única**, con cuatro campos:

```
horas : minutos : segundos : fotogramas
```

**Y la clave para operar con él es que los cuatro campos NO son decimales:**

| Campo | Base | Va de |
|---|---|---|
| **Horas** | **24** | **00 a 23** |
| **Minutos** | **60** | **00 a 59** |
| **Segundos** | **60** | **00 a 59** |
| **Fotogramas** | **La cadencia** | **00 a la cadencia menos uno** ✔ |

**Con 25 imágenes por segundo, el campo de fotogramas va de 00 a 24**, y **al llegar a 25 se convierte
en un segundo.** **Ésa es la única base que cambia según la cadencia**, y es donde están los errores.

**Los dos formatos de transporte que conviene distinguir:**

| Formato | Cómo viaja | Cuándo se puede leer |
|---|---|---|
| **Longitudinal** | **Como una señal de audio, por una pista propia** | **Sólo con la cinta en movimiento** |
| **Vertical** | **Dentro del intervalo de borrado de la propia imagen** | **También con la imagen parada** ✔ |

**Y el que hoy se usa**: **el código incrustado en la trama digital**, que es la evolución del
segundo. **La razón de que los tres coexistan en el vocabulario es que las instalaciones conservan
equipos de las tres épocas.**

**El aviso que conviene llevar y que el examen puede pedir**: **con cadencias fraccionarias existe el
código con salto de cuenta**, que **omite números —no imágenes— para que el reloj no derive respecto
al tiempo real.** **Con 25 imágenes por segundo eso no ocurre**, porque la cadencia es exacta, y por
eso la pregunta de este examen es limpia.

## 2. Cómo se opera con códigos de tiempo

**La pregunta 18**: **la resta de 01:13:56:15 menos 00:45:15:10, a 25 imágenes por segundo, da
00:28:41:05.** Ésa es la respuesta oficial.

---

**Y se hace campo a campo, de derecha a izquierda, tomando prestado cuando hace falta:**

| Campo | Cuenta | Resultado |
|---|---|---|
| **Fotogramas** | **15 − 10** | **05** |
| **Segundos** | **56 − 15** | **41** |
| **Minutos** | **13 − 45**: hay que tomar prestada una hora, que son 60 minutos → **73 − 45** | **28** |
| **Horas** | **1 − 0**, menos la hora prestada → **0** | **00** |

**Resultado: 00:28:41:05**, que es la respuesta oficial.

**Las tres opciones falsas son los tres errores típicos**, y **conviene verlos porque enseñan más que
el resultado:**

| Opción | Qué error comete |
|---|---|
| **00:29:43:00** | **Restar mal los minutos y perder el préstamo** |
| **01:59:12:00** | **Sumar los dos códigos en vez de restarlos** |
| **00:27:36:05** | **Tomar prestado dos veces, o usar base 100 en los minutos** |

**La regla que evita los tres**: **sólo el campo de fotogramas usa la cadencia; los otros dos usan
sesenta.** **Nadie se equivoca en la base sesenta de los minutos y muchos se equivocan en la de los
fotogramas**, y **en este caso concreto ni siquiera hizo falta prestar en fotogramas.**

**Y el atajo de comprobación que un ingeniero usa**: **el resultado tiene que ser menor que el
minuendo y coherente en orden de magnitud.** **Una hora y catorce menos cuarenta y cinco minutos son
algo menos de media hora**: **de las cuatro opciones, dos rondan la media hora y dos no.** **Eso deja
la elección entre dos antes de hacer ninguna cuenta.**

## 3. El equipamiento que el enunciado pide

**El enunciado pide equipamiento y diagrama a bloques, y no ha dado ninguna pregunta.** **Lo que
conviene llevar visto:**

| Bloque | Qué contiene |
|---|---|
| **Puestos de edición** | **Estaciones de trabajo con proceso gráfico dedicado, monitor de referencia y superficie de control** |
| **Almacenamiento compartido** | **Que varios montadores trabajen sobre el mismo material a la vez** |
| **Sala de sonido** | **Mesa, monitores de escucha calibrados y tratamiento acústico** |
| **Sala de etalonaje** | **Monitor de referencia calibrado y panel de control de color** |
| **Sala de gráficos** | **Estaciones de tres dimensiones y de composición** |
| **Cabina de sonorización** | **Locución y doblaje** |

**Los tres principios de diseño de una sala de postproducción, que es lo preguntable:**

1. **El monitor de referencia manda.** **Todo lo que se decide de imagen se decide mirando el monitor
   calibrado, no la pantalla de trabajo.**
2. **La escucha tiene que ser fiable ANTES que potente.** **Es la razón de los monitores de campo
   cercano del tema 12.**
3. **El almacenamiento compartido es el cuello de botella.** **Varios montadores leyendo material sin
   comprimir a la vez piden un caudal que un almacenamiento corriente no da.**

**Y la observación que ordena el epígrafe**: **una sala de postproducción es una instalación de
informática con requisitos de tiempo real.** **Lo que la distingue de una oficina no es el vídeo: es
que no admite esperas.**

## 4. La interconexión

**El enunciado termina con esa palabra, y en postproducción tiene un sentido concreto**: **cómo entra y
sale el material de las salas.**

| Vía | Qué lleva | Cuándo se usa |
|---|---|---|
| **Almacenamiento compartido** | **Los ficheros de trabajo** | **Entre salas del mismo centro** ✔ |
| **Transferencia por red** | **Ficheros entregados o recibidos** | **Con productoras y con otros centros** |
| **Señal por matriz o por red** | **Vídeo y audio en tiempo real** | **Para monitorizar y para grabar de una fuente en directo** |
| **Soporte físico** | **Discos y tarjetas** | **Lo que llega de rodaje** |

**Y las dos operaciones que ocurren en cada frontera de esas y que dan casi todos los problemas:**

| Operación | Qué puede salir mal |
|---|---|
| **Transcodificación** | **Que el formato de entrega no sea el que la sala trabaja**, y haya que convertir |
| **Conformado** | **Que el código de tiempo del material de baja resolución no case con el del original** |

**El aviso de oficio que este punto deja**: **la lista de decisiones de edición es un fichero de texto
con códigos de tiempo.** **Si esos códigos no son los mismos en las dos copias del material, el
conformado sale desplazado**, y **el desplazamiento es constante y no salta a la vista.** **Es el
fallo más caro de la cadena, porque se detecta al final.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 18 | Resta de dos códigos de tiempo a 25 imágenes por segundo | b) 00:28:41:05 ✔ |

**La única respuesta oficial es correcta**, y **no descansa en la plantilla**: **es un cálculo, y queda
escrito paso a paso.**

**El aviso de estudio**: **el enunciado pide equipamiento y ha caído aritmética.** **Lo rentable es
saber operar con códigos de tiempo, que se aprende en cinco minutos y se olvida si no se practica**;
**lo enunciado se lee una vez.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Tres declaraciones expresas:**

1. **La norma que define el código de tiempo no se ha consultado**: su texto está tras un muro de
   pago. **La estructura de cuatro campos, las bases de cada uno y la existencia del código con salto
   de cuenta son de uso universal**, y **el cálculo de la pregunta 18 no depende de la norma: se
   hace**, y queda escrito para que se pueda comprobar.
2. **El equipamiento del epígrafe 3 y las vías de interconexión del 4 son oficio de postproducción**,
   escritos a partir del propio enunciado del anexo. **No describen la instalación de ninguna casa
   concreta**, que no se ha consultado.
3. **Ninguna respuesta oficial depende de los epígrafes 3 y 4**: **el examen no ha entrado por ahí**, y
   se desarrollan por estar en el enunciado.

**El resto del tema va como oficio y así se declara**: la observación de que sólo el campo de
fotogramas cambia de base, el desmontaje de los tres errores típicos, el atajo de comprobación por
orden de magnitud, los tres principios de diseño de una sala y el aviso sobre el conformado
desplazado. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el
tema no lo presenta como si lo estuviera.
