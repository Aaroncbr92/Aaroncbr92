# Grafista (15) · Tema 6 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/06-escenarios-virtuales-realidad-aumentada-pantallas-videowalls-tiempo-real.md`.
Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema). No se corrige:
sólo se informa. Ficheros tocados: este informe y `15-T06-preguntas.md` (descargas de trabajo en el
scratchpad, fuera del repositorio).

Saltado en exactitud (según `15-T06-redaccion.md`): los 18 bloques «Copiado del común» (Realizador/a,
T12: definiciones, seguimiento y Mo-Sys, croma/LED, iluminación y Libro de Estilo, RV/RA/RM, *foreground*,
retardos, pantallas, motores) y lo «Copiado de RTVE sin cambios». La cobertura mira el tema entero.

## Método

Tema técnico sin normas: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`. Cada
negrita nueva y cada paráfrasis cotejadas a mano (grep con contexto) contra:

| Fuente | Cómo | Leída |
|---|---|---|
| Epic, *In-Camera VFX Overview* (UE 5.8) | volcado local de Realizador | 29-09-2026 |
| Epic, *nDisplay Overview*, *Recommended Hardware for In-Camera VFX*, *Professional Video IO*, *Motion Design* y *Quickstart* (UE 5.8) | descargadas | 29-09-2026 |
| Epic, *In-Camera VFX Best Practices* (UE 5.8) | descargada (para la laguna) | 29-09-2026 |
| Vizrt, *Viz Multiplay User Guide* 3.3 «Introduction»; *Viz Engine Administrator Guide* 5.4 «Video Output» y 5.2 «Dual Channel Mode» | descargadas | 29-09-2026 |
| Chyron, *PRIME CG* (URL larga) y *About Chyron* | descargadas | 29-09-2026 |

*Introduction to Viz Artist* 5.3 no respondió (redirección vacía); sus dos citas se dan por buenas con la
verificación. La nota de prensa de PRIME 5.3 no se volvió a descargar.

## Hallazgos de exactitud

### Graves (0)

Ninguno.

### Menores (4)

- **M1 · Siglas** (error 5, inverso). Se presentan y no se usan en el cuerpo: CGI, PGM, PVW y «fr». Quitarlas
  de la presentación (o usarlas).
- **M2 · §5 «Qué hace un sistema de grafismo», párrafo tras la tabla** (error 6, salvedad omitida / encuadre).
  El tema explica la reproducción «con su alfa» por relleno y llave y la apoya sólo en el modo *Dual
  Channel*, que **«requires two graphics cards»**. Quien lo estudie deduce que entregar relleno y llave exige
  ese modo y dos tarjetas. Pero el *Dual Channel* sirve para tener dos salidas de programa; que una salida
  entregue la llave es una propiedad de la salida: *Viz Engine Administrator Guide* 5.4, «Video Output»,
  «Key Properties»: **«Contains Alpha: Defines if this output channel provides key information on the
  associated key output connector.»** (la misma guía que el tema ya cita en §4). Propuesta: citar
  «Contains Alpha» como apoyo del relleno y la llave y dejar el doble canal como lo que es (dos salidas de
  programa, dos tarjetas, control externo). Pregunta 15 (no).
- **M3 · §1 «La pared de LED: frustum interior y exterior»** (error 6, salvedad omitida). La fuente dice a
  continuación: **«The outer frustum remains static when the camera moves. This mimics how lights and
  reflections do not move with the camera in the real world.»** Es el contraste que da sentido a la
  pareja interior/exterior. Y para «Y dentro del frustum interior puede seguir habiendo croma», la misma
  página da la razón: **«Using a green screen only in the camera's FOV minimizes the amount of green screen
  required for a given shot. Less green screen means less green spilling onto the actors and set.»**
  Añadir las dos (unas 60 palabras). Pregunta 2 (a medias).
- **M4 · Portada, «Fuente»** (trivial). Para Chyron nombra la página de *PRIME CG* y la nota de 5.3, pero el
  cuerpo cita también *About Chyron* (la frase de la plataforma), que sí está en «Trazabilidad». Añadirla.

### Comprobado sin hallazgo

Epic: armarios (92 × 92 a 400 × 450), procesador («ten or more»), paso de píxel y coste, frustum interior y
exterior, Composure, tarjeta SDI, genlock y reloj interno, Quadro Sync, sincronía de procesadores,
tonemapper/sRGB lineal, OCIO, efectos en espacio de pantalla; nDisplay (nodos, instancias, viewports,
«ensures…», Output Mapping, Mosaic/Eyefinity, *failover* con su salvedad y «Drop S-node on fail»);
*Professional Video IO* (cinco citas); Motion Design (dos citas, *Quickstart*, visor de alfa y zona segura;
la etiqueta «experimental» es la de la página, `"tags":["experimental"]`). Vizrt: Multiplay (nueve citas);
Viz Engine 5.4 «Video Wall/Multi-Display… FULLSCREEN»; 5.2 *Dual Channel* («typically», dos tarjetas, control
externo desde consolas o Viz Trio/Pilot; publicada el 20-III-2024). Chyron: PRIME CG (seis citas), *About
Chyron*. Cuentas del lienzo (3.200 × 1.350) y de retardos: correctas. Lo marcado como oficio se dice como tal.

## Cobertura del enunciado

«Escenarios virtuales, realidad aumentada, pantallas, videowalls y grafismo en tiempo real»: cinco
rúbricas, cinco epígrafes en el orden del enunciado, con aplicación práctica. Test (15 preguntas, en
`15-T06-preguntas.md`): **12 enteras, 1 a medias, 2 no**. La a medias es M3; los dos «no», M2 y una laguna.

### Laguna (1)

- **L1 · Cómo se prepara una escena para que el motor la dibuje en tiempo real** (escenarios virtuales y
  grafismo en tiempo real; es el trabajo propio del grafista en un plató virtual). El tema dice que «la
  escena se construye para que quepa en ese tiempo» y que lo que no llega «se ve como un tirón», pero no
  cómo. Fuente de fabricante leída: Epic, *In-Camera VFX Best Practices in Unreal Engine* (UE 5.8,
  dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-best-practices-in-unreal-engine,
  29-09-2026). Lo aprovechable: las dos preocupaciones, **«Building assets that appear realistic on an LED
  wall. Optimizing the environment for performance so it runs in real time.»**; el objetivo que se fijaron,
  **«we targeted a frame rate between 48-72 frames-per-second (FPS) on Artist workstations when viewed in
  4K full screen»**, con la salvedad **«While a 2-3x target frame rate approach can provide a rough
  guideline for Artists, do not assume it will be sufficient in all cases»**; niveles de detalle, **«Level
  of Detail: Use different levels of polygon counts for when a Mesh is rendered larger or smaller on the
  screen.»**, y **«We recommend you budget resources for some hand-crafted LODs.»**; llamadas de dibujo
  (**«Each material ID adds draw calls»**); texturas en potencias de 2 (**«textures need to be a power of 2
  in both dimensions, however, they don't have to be perfect squares»**); iluminación precalculada frente a
  trazado de rayos (**«Because ray tracing is expensive in terms of performance, you can achieve
  better-looking and more stable image quality using baked lighting with volumetric light maps and
  reflection probes.»**); y la aprobación de lo optimizado por dirección de arte. Encaja al final de §1 «Lo
  que hace el grafista en un escenario virtual» o en §5 «Las dos exigencias del tiempo real». Unas 250-300
  palabras. Pregunta 14.

## Resumen

Graves 0 · menores 4 · lagunas 1. Las citas nuevas de Epic, Vizrt y Chyron son literales y están bien
leídas; la verificación ya dejó el *failover*, el doble canal y el paso de píxel en su sitio. El remate:
quitar siglas sin uso (M1), reencuadrar relleno y llave con «Contains Alpha» (M2), completar el frustum
(M3), la portada (M4) y ampliar L1 (la ampliación exige fase 5 bis).
