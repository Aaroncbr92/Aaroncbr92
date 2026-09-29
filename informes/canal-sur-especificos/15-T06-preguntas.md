# Grafista (15) · Tema 6 · Preguntas tipo test (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/06-escenarios-virtuales-realidad-aumentada-pantallas-videowalls-tiempo-real.md`.
Fecha de trabajo del encargo: 24-09-2026; preguntas redactadas y contestadas el 29-09-2026 (fecha de
sistema), **sólo con el tema**. La clave se ha comprobado en la fuente (Epic Games, UE 5.8: *In-Camera VFX
Overview* —volcado local de Realizador—, *nDisplay Overview*, *Recommended Hardware for In-Camera VFX*,
*In-Camera VFX Best Practices*; Vizrt: *Viz Multiplay User Guide* 3.3, *Viz Engine Administrator Guide*
5.4 «Video Output» y 5.2 «Dual Channel Mode»; todas descargadas el 29-09-2026). No repiten las diez del
redactor.

1. (Teoría) En producción virtual con pared de LED, el frustum interior representa: a) todo lo que muestra
   la pared; b) el campo de visión de la cámara según la focal de la óptica en ese momento; c) la zona de
   la pared que ilumina el decorado; d) la zona con croma. → **b**. §1 «frustum interior y exterior».
   **Entera.**
2. (Teoría) Cuando la cámara se mueve, el contenido del frustum exterior: a) se mueve con ella; b) se
   apaga; c) permanece estático, como las luces y los reflejos reales, que no se mueven con la cámara;
   d) pasa a croma. → **c** (Epic: «The outer frustum remains static when the camera moves»). El tema dice
   que el interior se mueve con la cámara y que el exterior ilumina y se refleja, pero no que quede
   estático; se acierta por descarte. **A medias** (hallazgo M3).
3. (Teoría) Según Epic, la resolución fija de un armario de LED va de: a) 64 × 64 a 256 × 256; b) 92 × 92
   (rótulos de exterior) a 400 × 450 (interior de muy alta resolución); c) 128 × 128 a 1.920 × 1.080;
   d) es igual en todos los fabricantes. → **b**. §4 «Armarios y procesador». **Entera.**
4. (Práctica) Una pared de 10 armarios de ancho por 4 de alto, con armarios de 400 × 450 píxeles. El
   lienzo al que se diseña es: a) 1.920 × 1.080; b) 3.840 × 2.160; c) 4.000 × 1.800; d) 4.500 × 1.600.
   → **c** (10 × 400 y 4 × 450). §4 y «Cuentas que se piden». **Entera.**
5. (Teoría) El equipo y programa que combina varios armarios en una matriz que muestra una sola imagen, y
   del que en un plató grande puede haber diez o más para una sola pared: a) el nodo principal de
   nDisplay; b) el procesador de LED; c) Viz Multiplay; d) el Datapath Fx4. → **b**. §4. **Entera.**
6. (Teoría) Elegir armarios de paso de píxel menor: a) baja el coste; b) sube la densidad, la calidad y el
   coste por armario, y no garantiza por sí solo que sea el producto adecuado (ángulo de visión,
   desplazamiento y uniformidad del color, disipación de calor); c) elimina el moiré; d) obliga a
   renunciar al genlock. → **b**. §4 «El paso de píxel». **Entera.**
7. (Teoría) La tolerancia a fallos (*failover*) de nDisplay: a) funciona siempre, sin configurar;
   b) cubre cualquier fallo, también los de imagen; c) sólo cubre los fallos de nodos detectables por la
   red y hay que activarla (política «Drop S-node on fail»); el nodo que no responde sale del clúster tras
   un tiempo configurable; d) duplica cada nodo en caliente. → **c**. §4 «Muchas pantallas».
   **Entera.**
8. (Teoría) Para sincronizar las pantallas de un volumen de LED, Epic exige en cada nodo de render:
   a) una tarjeta SDI; b) NVIDIA Quadro Sync además de la tarjeta gráfica; c) un procesador de LED propio;
   d) un Datapath. → **b**. §4 «La sincronía: genlock». **Entera.**
9. (Teoría) El contenido que el motor manda a los paneles de LED debe llegar, según Epic: a) con la curva
   tonal del motor y en Rec. 709; b) con el mapeo tonal desactivado, sin curva, en sRGB lineal; c) en HDR
   PQ; d) en el espacio que marque la cámara. → **b**. §4 «El color que se manda a la pared». **Entera.**
10. (Práctica) Un grafista quiere añadir *bloom* y oclusión ambiental en espacio de pantalla a un fondo que
    se reparte en una pared entre tres nodos de nDisplay. Lo correcto: a) activarlos, dan realismo;
    b) evitarlos: al ser efectos en espacio de pantalla dan problemas en las juntas entre nodos;
    c) activarlos sólo en el nodo principal; d) activarlos con genlock. → **b**. §4 «Lo que no funciona
    en un clúster». **Entera.**
11. (Teoría) Para alimentar un videowall desde Viz Engine, el manual 5.4 pide: a) salida SDI con relleno y
    llave; b) activar «Video Wall/Multi-Display» (salida principal a DVI) con formato FULLSCREEN;
    c) modo Dual Channel; d) desactivar la salida principal. → **b**. §4. **Entera.** (Solapa con la 9 del
    redactor; se mantiene porque aquí se pregunta el ajuste de formato.)
12. (Teoría) Según Vizrt, la función de videowall de Viz Multiplay admite desde una sola GPU de un Viz
    Engine: a) dos salidas HDMI en HD; b) hasta cuatro salidas DisplayPort en UHD, ampliables con
    controladores Datapath Fx4; c) ocho salidas SDI; d) una sola salida DVI. → **b**. §4 «El videowall en
    un sistema de grafismo». **Entera.**
13. (Práctica) Decorado de pantallas de LED con un programa de gestión que retrasa 3 fotogramas (25 fps) y
    una conexión exterior abierta en ellas: a) exterior a las pantallas por un auxiliar y sonido adelantado
    120 ms; b) exterior a las pantallas por matriz, su entrada al mezclador retrasada 3 fr y su sonido
    retrasado 120 ms; c) retrasar sólo el sonido 3 fr; d) retrasar las cámaras del plató 3 fr.
    → **b**. §3 «El retardo de las pantallas» y §2 (40 ms por fotograma). **Entera** (el caso del tema es
    de 4 fr; la regla y la cuenta se aplican igual).
14. (Práctica) Un decorado virtual con geometría y texturas de alta resolución da tirones en el motor en
    tiempo real. Según la documentación de Epic sobre escenarios para pared de LED, lo indicado es:
    a) subir todas las texturas a 8K y trazado de rayos; b) niveles de detalle (LOD) por tamaño en
    pantalla, texturas en potencias de 2 y, donde convenga, iluminación precalculada (*baked*) en lugar de
    trazado de rayos; c) renderizar el decorado en diferido; d) quitar el seguimiento de cámara.
    → **b**. El tema sólo dice que «la escena se construye para que quepa en ese tiempo» (§1 «Lo que hace
    el grafista») sin decir cómo. **No** (laguna L1).
15. (Práctica) Un Viz Engine debe entregar un rótulo con transparencia al mezclador por una sola salida de
    programa. Lo que se ajusta: a) el modo Dual Channel, que exige dos tarjetas gráficas; b) en las
    propiedades de llave de esa salida, «Contains Alpha», para que el canal entregue la llave por su
    conector de llave asociado; c) «Video Wall/Multi-Display»; d) formato FULLSCREEN. → **b** (*Viz Engine
    Administrator Guide* 5.4, «Video Output»: **«Contains Alpha: Defines if this output channel provides
    key information on the associated key output connector.»**). El tema sólo asocia relleno y llave al
    modo de doble canal y a sus dos tarjetas: quien lo estudie elige **a**. **No** (hallazgo M2).

Resultado: 12 enteras, 1 a medias, 2 no.
