# Tema 11 del específico de Técnica de Equipos y Sistemas Electrónicos · Control de iluminación escénica

Las siglas de este tema, presentadas de entrada: el multiplexado digital de la Asociación de
Tecnología y Producción de Espectáculos (**DMX**, y en su nombre completo **DMX512**); el diodo emisor
de luz (**LED**, *light emitting diode*); el conector de audio profesional de tres o cinco contactos
(**XLR**), que aquí se usa para datos; el protocolo de red para control de iluminación (**Art-Net**);
la protección de las personas frente a contactos indirectos por dispositivo de corriente diferencial
residual (**DDR**); y los grados Kelvin (**K**) de la temperatura de color.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 13):
> «CONTROL DE ILUMINACIÓN ESCÉNICA: consola de control, señal DMX. Proyectores LED. Iluminación
> robotizada.»

**Una pregunta.** **Es el punto más pequeño de la ocupación y el enunciado más corto de su anexo**,
y **las dos cosas son coherentes: en esta convocatoria la iluminación escénica se examina de refilón**,
porque tiene su propia ocupación.

**Aun así el punto está en el temario y el tema se escribe entero**, por el motivo que el manual de
este proyecto fija: **un punto con una pregunta puede tener cuatro en la convocatoria siguiente**, y
**el opositor que sólo estudia lo preguntado estudia el examen pasado.**

**La pregunta que ha caído es la definición del atenuador**, que es la pieza central del punto.

<!-- indice -->

## Índice

- [1. Qué es un dimmer](#1-qué-es-un-dimmer)
- [2. La consola y la señal DMX](#2-la-consola-y-la-señal-dmx)
- [3. Los proyectores de diodos y la iluminación robotizada](#3-los-proyectores-de-diodos-y-la-iluminación-robotizada)
- [4. Lo que el mantenimiento de este punto revisa](#4-lo-que-el-mantenimiento-de-este-punto-revisa)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Qué es un dimmer

**La pregunta 79**: **un dimmer es un dispositivo electrónico o mecánico cuya función es controlar la
intensidad de una o varias fuentes de luz.** Ésa es la respuesta oficial.

---

**Las tres opciones falsas son las otras tres cosas que se pueden hacer con una luz**, y **conviene
verlas juntas porque cada una tiene su propio aparato:**

| Qué se quiere cambiar | Con qué se hace | Cómo se llama |
|---|---|---|
| **La intensidad** | **Regulando la potencia que llega al proyector** | **El dimmer o atenuador** |
| **El color** | **Con un filtro, una rueda de color o los canales de un proyector de diodos** | **El gelatinado o el mezclador de color** |
| **La temperatura de color** | **Cambiando la lámpara, filtrando o mezclando dos blancos** | **La corrección de color** |
| **El momento del encendido** | **Con la memoria de la consola o un temporizador** | **La programación de la consola** |

**Y la palabra que decide la respuesta es «intensidad».** **La opción a habla de temperatura de
color, la c de programación del encendido y la d de cambio de color**: **las tres son funciones
reales de una instalación de iluminación**, pero **ninguna es la del atenuador.**

**Por qué la respuesta oficial dice «o mecánico», que es la parte que puede extrañar**: **el primer
atenuador de la historia del espectáculo fue una resistencia variable movida a mano**, y **antes que
él el regulador de gas.** **La definición mantiene la puerta abierta a lo mecánico porque el aparato
es más viejo que la electrónica que hoy lo resuelve.**

**Y el aviso que separa dos mundos**: **una lámpara incandescente se atenúa recortando la onda de red,
y el proyector de diodos no.** **Un diodo se atenúa modulando la anchura de los impulsos con que se le
alimenta o variando su corriente**, y por eso **un proyector de diodos no se cuelga de un atenuador de
sala: se cuelga de una toma de corriente sin regular y se le manda el nivel por el cable de datos.**
**Enchufar un proyector de diodos a un canal de atenuador es la avería más frecuente del punto.**

## 2. La consola y la señal DMX

**La consola es el instrumento del iluminador**, y **lo que sale de ella no es corriente: son datos.**

**Cómo está montada la cadena, de la consola al foco:**

| Eslabón | Qué lleva |
|---|---|
| **Consola** | **Genera la señal de control: qué nivel quiere cada canal** |
| **Cable de datos** | **Transporta esa señal, en serie, a todos los aparatos de la línea** |
| **Bloque de atenuadores** | **Recibe el nivel y entrega la potencia correspondiente a cada circuito** |
| **Proyector convencional** | **Se limita a lucir lo que le llega por el circuito de potencia** |
| **Proyector inteligente o de diodos** | **Recibe los datos directamente y él mismo regula, mueve y colorea** |

**Las cifras de la señal DMX512, que son las que hay que llevar aprendidas:**

- **Quinientos doce canales por universo.** **Ese número está en el propio nombre de la norma.**
- **Un byte por canal**, de modo que **cada canal admite doscientos cincuenta y seis valores**, de 0
  a 255.
- **Un solo sentido**: **la consola habla y los aparatos escuchan.** **El DMX no devuelve nada**, y
  ésa es su limitación de fondo: **la consola no sabe si el foco recibió la orden.**
- **Cableado en cadena**, de aparato a aparato, **con un terminador al final de la línea.**
- **Conector de cinco contactos** en la norma, **aunque el sector use masivamente el de tres.**

**Qué es un universo, porque el término aparece siempre**: **es una línea completa de quinientos doce
canales.** **Una instalación que necesite más canales necesita más universos**, y **de ahí que las
instalaciones grandes hayan pasado a llevar el DMX encapsulado dentro de una red**, con protocolos
como Art-Net, **que meten muchos universos en un solo cable de red.**

**Y la cuenta que el iluminador hace todos los días**: **un aparato ocupa tantos canales como
funciones tenga.** **Un atenuador de sala ocupa un canal por circuito.** **Un proyector de diodos de
cuatro colores ocupa cuatro.** **Una luminaria robotizada puede ocupar veinte o más** —posición,
color, haz, efectos—, **de manera que un universo se llena con veinticinco aparatos de esos.**

## 3. Los proyectores de diodos y la iluminación robotizada

**El proyector de diodos ha sustituido al incandescente en televisión por tres motivos, y los tres
tienen consecuencia técnica:**

| Ventaja | Consecuencia en la instalación |
|---|---|
| **Consume mucho menos para la misma luz** | **Menos potencia contratada y menos sección de cable** |
| **Calienta mucho menos el plató** | **Menos carga de climatización y más confort del presentador** |
| **Cambia de color sin filtros** | **Se acabaron las gelatinas y su recambio** |

**Y sus tres inconvenientes, que el mantenimiento conoce bien:**

- **El parpadeo con la cámara.** **Un proyector de diodos mal ajustado produce bandas en la imagen
  cuando la frecuencia de su modulación bate con la del obturador.** **Se corrige subiendo la
  frecuencia de modulación del proyector o ajustando el obturador de la cámara.**
- **El espectro incompleto.** **Un diodo blanco barato no emite en todas las longitudes de onda**, y
  **la piel sale mal.** **Es el mismo problema que el epígrafe 1 del tema 10 llamaba «valores
  espectrales no captados»**, sólo que aquí el que falla es el emisor y no el sensor.
- **La atenuación**, ya dicha: **no se regula con el atenuador de sala.**

**La iluminación robotizada** añade movimiento a lo anterior. **Un aparato robotizado tiene motores de
horizontal y de vertical, y en muchos casos rueda de color, rueda de figuras, iris, enfoque y
zoom**, y **cada uno de esos ejes es un canal de la consola.** **Su virtud no es sólo moverse durante
el programa**: **es que un plató entero se reenfoca desde la consola sin subir nadie a la parrilla**,
lo que **convierte una tarea de altura en una tarea de sala.**

**Y ese último detalle enlaza este tema con el 17**: **la iluminación robotizada reduce trabajos en
altura**, que son uno de los riesgos que el punto de prevención de esta ocupación nombra
expresamente.

## 4. Lo que el mantenimiento de este punto revisa

**El punto es de control de iluminación, y el control falla por sitios muy concretos:**

| Síntoma | Causa habitual |
|---|---|
| **Un aparato de la cadena no responde y los demás sí** | **Dirección de inicio mal puesta en ese aparato** |
| **Los aparatos parpadean o responden a destiempo** | **Falta el terminador al final de la línea, o el cable de datos no es de la impedancia debida** |
| **Un aparato responde a las órdenes de otro** | **Dos aparatos con la misma dirección de inicio y distinto número de canales** |
| **El proyector de diodos parpadea sólo en cámara** | **Batido entre la modulación del proyector y el obturador** |
| **El canal sube pero el foco no luce** | **Avería en el bloque de atenuadores o lámpara fundida: el fallo está en la potencia, no en los datos** |

**La regla de diagnóstico del punto**: **separar siempre los datos de la potencia.** **Si el aparato
recibe pero no luce, el problema está aguas abajo del atenuador; si no recibe, está en el cable de
datos o en el direccionamiento.** **Es la misma disciplina que el tema 14 aplica a la señal de vídeo:
antes de cambiar una pieza, hay que saber en qué mitad de la cadena está el fallo.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 79 | Qué es un dimmer | b) Dispositivo que controla la intensidad de una o varias fuentes de luz ✔ |

**La respuesta oficial es correcta**, y **no descansa en la plantilla**: la definición del atenuador es
inequívoca y las otras tres opciones nombran funciones de otros aparatos.

**El aviso de estudio**: **con una sola pregunta caída, el rendimiento de este punto está en lo que
puede caer, no en lo que cayó.** **Lo más preguntable son las cifras de la señal DMX** —quinientos
doce canales, un byte por canal, un solo sentido, terminador— **y la incompatibilidad entre el
proyector de diodos y el atenuador de sala.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La norma DMX512 está publicada por la Asociación de Tecnología y Producción de Espectáculos y
   no se ha consultado.** **Las cifras del epígrafe 2 —quinientos doce canales, un byte por canal,
   transmisión en un solo sentido, terminación de la línea y conector de cinco contactos— son de uso
   universal en el sector**, y **el temario no las atribuye a ningún apartado de esa norma.**
2. **Ninguna pregunta del examen depende de esas cifras.** **La única pregunta del punto es la
   definición del atenuador**, que se contesta sin ellas.
3. **Los cuadros de ventajas, inconvenientes y averías de los epígrafes 3 y 4 son oficio de
   mantenimiento**, redactados como orientación de estudio. **No se atribuyen a ninguna norma ni a
   ninguna documentación de fabricante.**
4. **La relación entre la iluminación robotizada y los trabajos en altura del epígrafe 3 es una
   observación del temario**, no una cita: **lo que sí está en el anexo de la convocatoria es que el
   punto 21 de esta ocupación nombra la seguridad en trabajos en altura**, y así consta en el tema
   de prevención.

**El resto del tema va como oficio y así se declara**: la tabla de qué aparato cambia qué, el
argumento de por qué la definición oficial dice «o mecánico», la incompatibilidad del diodo con el
atenuador de sala, las ventajas e inconvenientes del proyector de diodos, el reparto de canales de una
luminaria robotizada y la regla de separar datos de potencia. **Nada de eso está en un boletín oficial
ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
