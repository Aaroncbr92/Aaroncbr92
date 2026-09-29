# Grafista (15) · Tema 6 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/06-escenarios-virtuales-realidad-aumentada-pantallas-videowalls-tiempo-real.md`.
Fecha de trabajo del encargo: 24-09-2026. Fuentes releídas el 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe. Nada más. Descargas de trabajo en el scratchpad, fuera del repositorio.

## Pasajes copiados: sólo comprobación literal

Cotejo por script (sin negritas ni cursivas, espacios normalizados; en RTVE, sin distinguir mayúsculas)
de cada párrafo, fila y viñeta contra los originales, y *word diff* de los que no casaban:

- **Copiado del común** (`33-realizador-a/12-…`): los 18 bloques de la lista del redactor son literales;
  las únicas diferencias son exactamente los ajustes declarados (remisiones «epígrafe 2/4», «tema 9/11/14»,
  frase del mezclador, filtro de moiré, parpadeo, «Otro banco M/E», párrafo del RD 1680/2011 sustituido).
  **Un resto no declarado**: en «Lo que se comprueba en el ensayo» quedaba la frase truncada «La
  integración de lo real y lo virtual se revisa con los movimientos de cámara y del personal» (sin punto;
  en el común sigue «artístico previstos (IMS077_3, CR4.2, arriba)…»). Era el primer renglón del párrafo
  que el redactor dice haber suprimido: **quitada**.
- **Copiado de RTVE sin cambios** (`ing-sup-teleco/16`, `diseno-grafico/10` § 6): literales (sólo
  minúsculas donde RTVE usaba mayúsculas de énfasis, como declara el redactor).
- **Adaptado de RTVE**: las dos frases de entrada recortadas, literales en lo demás; la tabla «Con quién
  habla» (MOS/Viz Multiplay, pantallas, tema 5) coincide con lo que dicen las fuentes; correcta.

## Fuentes releídas

| Fuente | Qué se cotejó |
|---|---|
| Epic, *In-Camera VFX Overview* (UE 5.8; volcado local de Realizador) | armarios, procesador, paso de píxel y coste, frustum interior/exterior, genlock, tonemapper/sRGB lineal, OCIO, efectos en espacio de pantalla, Composure (y el croma en el frustum interior, «Live Compositing») |
| Epic, *Recommended Hardware for In-Camera VFX* (UE 5.8) | sync de procesadores, Quadro Sync por nodo, tarjeta SDI para croma en directo |
| Epic, *nDisplay Overview* (UE 5.8) | nodos, instancias, viewports, «ensures…», Output Mapping, Mosaic/Eyefinity, *failover* |
| Epic, *Motion Design* y *Quickstart* (UE 5.8) | las cinco citas; etiqueta «experimental» en ambas páginas |
| Epic, *Professional Video IO* (UE 5.8) | las cinco citas |
| Vizrt, *Viz Multiplay User Guide* 3.3, «Introduction» (© 2025) | las nueve citas |
| Vizrt, *Viz Engine Administrator Guide* 5.4 «Video Output»; 5.2 «Dual Channel Mode» (publicada 20-III-2024) | Video Wall/Multi-Display; doble canal y control externo |
| Vizrt, *Introduction to Viz Artist* 5.3 | modos y licencia |
| Chyron, *PRIME CG™ - 3D Real-Time Graphics* (chyron.com/products/all-in-one-production-systems/3d-real-time-graphics/), *About Chyron*, nota PRIME 5.3 (12-II-2026) | todas las citas |
| Libro de Estilo (citas nuevas en §§ 3 y 4) | son reproducciones de las citas 6.5.2 y 3.10 ya presentes en el común; coinciden |

Todas las negritas nuevas están en su fuente, literales. Cuentas (40/80/160 ms, 2 fr a 50 fps = 40 ms,
9 entradas, 4 motores, 3.200 × 1.350) rehechas: correctas. Remisiones a otros temas (1, 3, 5, 8, 9, 17,
18) cotejadas con el enunciado y con los temas 1 y 3 ya redactados: correctas.

## Correcciones aplicadas (16)

1. Frase truncada del común (arriba). (literal)
2. nDisplay, *failover*: se daba como automático («si una máquina cae, el resto sigue»). La fuente dice que
   sólo cubre fallos detectables por la red y que hay que activarlo (política «Drop S-node on fail»).
   Añadida la salvedad. (6)
3. nDisplay: «una sola máquina no basta para todos los píxeles» no está en la fuente → «el trabajo puede
   repartirse entre varias máquinas». (9)
4. «El sistema tiene dos obligaciones»: la fuente enumera garantías «and more» → «entre lo que garantiza
   hay dos cosas». (3)
5. Efectos en espacio de pantalla: «Epic los excluye» → «Epic pide evitarlos» («should be avoided»); la
   explicación previa, marcada oficio. (4)
6. Dual Channel: faltaba «typically» → «normalmente»; «el motor se gobierna desde fuera» → «puede
   gobernarse desde sus consolas o desde fuera» (la fuente da las dos vías). (6, 4)
7. Dual Channel: «Vizrt lo describe» atribuía a Vizrt la explicación general del relleno y la llave →
   «en la documentación de Vizrt, relleno y llave aparecen en su modo de doble canal». (9)
8. Viz Artist: «dos modos principales» → «varios modos, entre ellos el de diseño y el de emisión» (la
   fuente da tres: Artist, Engine, Configuration). La lectura «Viz Engine las emite» se apoya además en
   Multiplay («Uses Viz Engine for playout»). (3)
9. Motion Design: añadida la etiqueta «experimental» que llevan las dos páginas de Epic. (6)
10. Viz Multiplay: «el motor … de la casa» (ambiguo: podía leerse CSRTV) → «de Vizrt». (9)
11. Salida de las pantallas: «no va al mezclador…, sino a los paneles» omitía que la misma guía admite SDI
    → añadido. (6)
12. «La salida a la pared no es la de los rótulos» → «En un videowall, …» (el ajuste de Viz Engine es
    para configuraciones de videowall). (6)
13. Paso de píxel: «(epígrafe 3, con la fuente)» atribuía a Epic el acercamiento de cámara, que en el
    epígrafe 3 es deducción de oficio; separado lo de la fuente (densidad, coste) de lo deducido. (9)
14. Frustum: la definición de «pirámide truncada» no está en la fuente → marcada oficio. Espacio de color
    de cada pared «lo fija su fabricante» → marcado oficio. (9)
15. Siglas: quitada «CSTV» (no se usa en el tema); quitados AJA y Blackmagic Design de la presentación y
    de «Lo que este tema no da» (el tema no los nombra en el cuerpo: la cita de Epic se corta antes). (5)
16. Trazabilidad: añadidos el *failover*, la etiqueta «experimental» y la fecha de publicación de la
    guía 5.2 de Viz Engine.

Relectura de los pasajes cambiados: cada «la misma guía», «la fuente», «Epic pide evitarlos» tiene su
antecedente en el mismo párrafo o subepígrafe.

## Lentes

Tema técnico sin normas: `refutar_prosa.py` (4 hallazgos, falsos positivos: AMD, NVIDIA, PRIME, CAMIO,
nombres de fabricante o producto presentados como tales) e `indice.py` (índice sin cambios; 11.996
palabras, 47 epígrafes). No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## No confirmado / discrepancias

- La página de producto de Chyron ya no está en la URL corta; se leyó en
  `/products/all-in-one-production-systems/3d-real-time-graphics/` (mismo título que cita el tema).
- Ninguna discrepancia con el encargo.
