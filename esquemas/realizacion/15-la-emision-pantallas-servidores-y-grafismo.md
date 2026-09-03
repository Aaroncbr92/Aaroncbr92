# Esquema · Realización (Asistencia) 15: la emisión

Esqueleto para repasar. Todo desarrollado y verificado en el tema.

<!-- indice -->

## Índice

- [Gestión de pantallas](#gestión-de-pantallas)
- [Compensar el retardo](#compensar-el-retardo)
- [El programa a las pantallas, sin repeticiones](#el-programa-a-las-pantallas-sin-repeticiones)
- [El servidor de vídeo](#el-servidor-de-vídeo)
- [Grafismo en directo](#grafismo-en-directo)
- [Continuidad](#continuidad)
- [Qué hay que guardar](#qué-hay-que-guardar)
- [El aviso](#el-aviso)

<!-- /indice -->

## Gestión de pantallas

Lo que puede ir en una pantalla de plató: grafismo de fondo · el programa · una conexión exterior ·
un vídeo · datos.
Tres restricciones: **moiré**, **retardo** y **realimentación** —por eso nunca se le manda el
programa a secas—.

## Compensar el retardo

Pantallas que retrasan **4 fotogramas** y conexiones en directo por ventanas abiertas en ellas:
1. **Mandar el exterior a las pantallas por matriz**, no por auxiliar: así el único retardo es el del
   programa de pantallas.
2. **Retrasar 4 fotogramas la entrada del exterior al mezclador**, para que case con lo que las
   cámaras ven en la pantalla.
3. **Retrasar 4 fotogramas el sonido del exterior.**
***Sincronizar es siempre retrasar lo que va adelantado: nunca se adelanta nada.***
*A 25 fotogramas por segundo, **un fotograma son 40 ms**.*

## El programa a las pantallas, sin repeticiones

**Otro banco M/E distinto del programa**, **enlazado** a él con un *link*, y **con el mapeado
cambiado** para que ese banco no tenga los vídeos.
*Así la pantalla sigue al programa sola y, cuando el programa pincha la repetición, la pantalla
pincha otra cosa.*

## El servidor de vídeo

Graba varias señales a la vez · **reproduce desde cualquier punto mientras sigue grabando** · cámara
lenta · listas de reproducción · emisión · marcado y catalogación.
**Lo que NO hace: corregir el color de una señal.** *Eso es proceso de señal: CCU, mezclador o
corrector.*

## Grafismo en directo

**Vizrt · Chyron · Ventuz · Unreal Engine** trabajan en tiempo real.
**After Effects no**: compone por renderizado y entrega un fichero.
*El cuadernillo escribe «Chayron Prime» por Chyron.*

## Continuidad

**El área que emite el canal**: cortinillas, **identidad corporativa**, autopromociones, publicidad,
enlace entre programas.

## Qué hay que guardar

**Ley 13/2022, artículo 156.2**: conservar **seis meses**, desde la primera puesta a disposición del
público, **los programas y contenidos audiovisuales, incluidas las comunicaciones comerciales**, y
registrar sus datos.
*No exige copia sin rótulos ni brutos de rodaje.*
**Artículo 71**: RTVE vela por los **archivos históricos** y garantiza el acceso. **Artículo 152**:
sus archivos tienen **protección especial**. *Sólo el 156 fija plazo.*

## El aviso

**La pregunta 31 del primer llamamiento tiene un distractor humorístico**, el único del examen: en la
práctica deja la pregunta en tres opciones.
