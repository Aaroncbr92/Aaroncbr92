# Esquema · Realización (Asistencia) 10: el mezclador de vídeo

Esqueleto para repasar. Todo desarrollado y verificado en el tema.

*Aviso de vocabulario: el manual de Blackmagic dice «composición» donde el examen dice «llave», y
«nivel» donde dice «clip».*

<!-- indice -->

## Índice

- [Qué hace y con qué](#qué-hace-y-con-qué)
- [Bancos y buses](#bancos-y-buses)
- [Transiciones](#transiciones)
- [Las tres señales de una llave](#las-tres-señales-de-una-llave)
- [Tipos de llave](#tipos-de-llave)
- [Aditivo frente a lineal](#aditivo-frente-a-lineal)
- [Clip, ganancia y premultiplicado](#clip-ganancia-y-premultiplicado)
- [DVE](#dve)
- [Memorias](#memorias)
- [Sincronización y GPI](#sincronización-y-gpi)
- [Los avisos](#los-avisos)

<!-- /indice -->

## Qué hace y con qué

**Conmutar · mezclar · combinar.** Todo lo demás sirve a esas tres.
**Panel de control** = **conjunto de botones y controles**, con arquitectura modular: buses de
programa y previo, transición, llaves, DSK, menús, memorias y auxiliares.
***Source*** = **fuente de vídeo con sus atributos asociados**: nombre, llave asociada, retardo,
corrección de entrada, piloto, botón.

## Bancos y buses

**M/E** = un mezclador dentro del mezclador; **se usa para transiciones y combinaciones complejas**.
Cadena: **M/E → programa → DSK → fundido a negro**. *La salida limpia se toma antes del DSK.*
**Bus auxiliar** = salida reasignable, como una matriz: **pantallas de plató, retornos, grabadores**.
*Con él se manda una corrección de color específica a las pantallas.* En mezcladores de gama alta
**se puede mezclar y hacer cortinillas en un auxiliar; depende del modelo.*

## Transiciones

**Corte · MIX · WIPE** (borde con forma que recorre la pantalla) **· fundido a color / SÚPER MIX ·
NAM** (se ve la más brillante de las dos) **· FAM** (las luminancias **se suman**: 100 % en el punto
medio) **· transición con DVE**.

## Las tres señales de una llave

**Fondo · relleno (*fill*) · llave (*key*)**. **Un *self key* implica tres señales**, aunque dos
salgan de la misma fuente.
**salida = relleno × llave + fondo × (1 − llave)**

## Tipos de llave

**Luminancia · lineal · crominancia (*chroma*) · figura (*preset pattern*) · con DVE.**
***Coring* no es un tipo de llave**: es reducción de ruido.
**Ultimatte** se asocia al **mezclador de vídeo**.

## Aditivo frente a lineal

| | **Lineal / no aditiva** | **Aditiva** |
|---|---|---|
| Fórmula | relleno **×** llave + fondo × (1 − llave) | relleno **+** fondo × (1 − llave) |
| Donde la llave vale 0 | **No aparece nada del relleno** | **Aparece el relleno sumado al fondo** |

*Levantar los negros del relleno al 7 % sólo se nota con llave **aditiva**.*
*Para que no se incruste el relleno sin llave: **llave de luminancia no aditiva**.*
*Con canal alfa acoplado en **autoselect**, la luminancia del relleno **es indiferente**: la
transparencia la decide la llave.*

## Clip, ganancia y premultiplicado

**Clip** = dónde se recorta la señal de llave. **Ganancia** = la pendiente, es decir, el borde.
**Premultiplicado** = **el relleno ya se ha multiplicado por la llave**. Hay que declararlo para que
el mezclador no multiplique dos veces.
***Show key*** = **previsualización de la señal de llave**, no del resultado compuesto.

## DVE

Traslación (X, Y, **Z**) · tamaño · rotación · **aspecto** · recorte · perspectiva · bordes ·
**corner pinning** (cambia la perspectiva **moviendo las esquinas**).
**Ampliar conservando proporciones → traslación en el eje Z.** *El aspecto es lo que deforma.*
**PinP** superpone ventanas.

## Memorias

**Snapshot** = un estado, instantáneo. **Macro** = **secuencia de instrucciones con sus tiempos**.
**Timeline** = estados sobre una línea de tiempo. **Shotbox** = teclado de disparo.
*Una secuencia con «pausa de 15 fr» dentro es una **macro**.*
**Clip store** = memoria interna de clips y grafismos, con su canal alfa.

## Sincronización y GPI

**Black burst** (referencia clásica) y **tri-level sync** (alta definición). Engancharse = *genlock*.
Lo que viene de fuera pasa por un **sincronizador de cuadro**, que añade **retardo**.
**GPI** = contacto seco que dispara: **es lo que hace falta para controlar un EVS desde el mezclador**.

## Los avisos

**Seis preguntas dependen de una figura** que el texto del cuadernillo no conserva. Una de ellas
tiene por respuesta oficial «**no se sabe, los datos son insuficientes**».
**La salida CLEAN** se deriva del **programa**, no del previo, aunque el enunciado la llame «de previo».
