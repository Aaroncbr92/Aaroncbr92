# Grafista (15) · Tema 5 · Preguntas de refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/05-animacion-motion-graphics-composicion-rotoscopia-tracking-efectos.md`.
Fecha de trabajo del encargo: 24-09-2026; preguntas redactadas y contestadas el 29-09-2026 (fecha de
sistema). Quince preguntas tipo test de cuatro opciones, de teoría y de aplicación práctica,
contestadas **sólo con el tema**. Veredicto: entera / a medias / no.

## Teoría

1. Según el RD 1583/2011 (art. 5.c), NO es una fase de la animación 2D:
   a) animática; b) intercalación; c) renderizado; d) pintura.
   → c. El renderizado es fase de la 3D (art. 5.d). §1 «La animación 2D y sus fases» y «La animación 3D
   y sus fases». **Entera.**

2. La interpolación que mantiene el valor hasta la clave siguiente y produce un efecto de escalera es la:
   a) lineal; b) constante; c) Bézier; d) Ease In Out.
   → b. §1 «La curva de animación y los tipos de interpolación». **Entera.**

3. En la terminología de Blender, *Ease Out* significa que el valor:
   a) arranca despacio y acelera; b) sale deprisa y frena al final; c) rebota con amortiguación
   exponencial; d) avanza a velocidad constante.
   → b. §1 «El suavizado: entrada y salida». **Entera.**

4. Mover la mano de un personaje y que el antebrazo y el brazo la sigan solos es:
   a) cinemática directa (FK); b) cinemática inversa (IK); c) *bind skin*; d) pintado de pesos.
   → b. §1 «El *rig*: esqueleto y cinemática». **Entera.**

5. De la familia ProRes, admiten canal alfa:
   a) todos; b) 422 HQ y 4444; c) sólo 4444 y 4444 XQ; d) ninguno.
   → c. §2 «La entrega». **Entera.**

6. Según el RD 1583/2011 (módulo 0907, RA 3.c), NO es un tipo de key:
   a) luminancia; b) crominancia; c) por diferencia; d) por profundidad.
   → d. §3 «Qué es componer». **Entera.**

7. Según el manual de Resolve, la corrección de color de un elemento con alfa se hace:
   a) sobre la imagen premultiplicada; b) sobre la imagen directa (no premultiplicada); c) después de
   premultiplicar dos veces; d) es indiferente.
   → b. §3 «Alfa directo y alfa premultiplicado». **Entera.**

8. El seguimiento de cámara de Fusion tiene dos fases:
   a) *keying* y *matting*; b) *tracking* y *solving*; c) *blocking* y *spline*; d) *rigging* y *skinning*.
   → b. §5 «El seguimiento de cámara». **Entera.**

9. Un PNG con alfa a 16 bits por canal ocupa por píxel:
   a) 24 bits; b) 32 bits; c) 48 bits; d) 64 bits.
   → d. El tema sólo da el PNG de 8 bits por canal (32 bits) y dice «32 o más» para el TIF; no dice que
   el PNG admita 16 bits por canal. Con el tema se contestaría b, que es la cifra del caso de 8 bits.
   **A medias.**

10. En composición, el modo de fusión que oscurece la imagen multiplicando los valores de los canales es:
    a) *Screen* (trama); b) *Multiply* (multiplicar); c) *Add* (suma); d) *Difference*.
    → b. El tema nombra los «modos de fusión» sólo dentro de la cita del glosario de Blender sobre la
    máscara; no dice cuáles hay ni qué hace cada uno. **No.**

11. Según el RD 1583/2011 (módulo 1086, RA 5.c), los métodos de modelado 3D que se eligen según el
    modelo son:
    a) nurbs, polígonos y *subdivision surfaces*; b) UV, bitmaps y procedurales; c) FK, IK y *bind skin*;
    d) extrusión, torno y barrido.
    → a. El tema da la fase «Diseño y modelado» y la malla de Blender, pero no los métodos de modelado.
    **No.**

12. Es uno de los principios clásicos de la animación (Disney):
    a) interpolación lineal; b) *squash and stretch* (estirar y encoger); c) extrapolación; d)
    *corner pin*.
    → b. El tema declara en «Lo que este tema no da» que no los da. **No.**

## Aplicación práctica

13. Una cortinilla de 3 segundos a 25 imágenes por segundo tiene:
    a) 50 fotogramas; b) 72; c) 75; d) 90.
    → c (3 × 25). §«Cuentas que se piden». **Entera.**

14. Hay que sustituir el contenido de un cartel que la cámara recorre y que a ratos queda tapado por un
    peatón. Lo más adecuado:
    a) seguimiento de un punto; b) seguimiento planar con *corner pin*; c) estabilización; d) *luma key*.
    → b. §5 «Los tipos de seguimiento» y «Cinco encargos corrientes», 2. **Entera.**

15. Una pieza informativa reconstruye un suceso con infografía animada. Según el Libro de estilo:
    a) basta un rótulo al principio; b) lleva el rótulo «reconstrucción» durante todo el tiempo en que
    las imágenes «falsas» estén en pantalla; c) no necesita rótulo si es infografía; d) lleva el rótulo
    «Archivo».
    → b (LE 3.2.2). §6 «Los efectos y la información». **Entera.**

## Resultado

Enteras: 11 (1-8, 13-15). A medias: 1 (9). No: 3 (10, 11, 12).
