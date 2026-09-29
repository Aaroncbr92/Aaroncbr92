# Grafista (15) · Tema 5 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/05-animacion-motion-graphics-composicion-rotoscopia-tracking-efectos.md`
(10.970 palabras con tablas). Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026
(fecha de sistema). No se corrige nada: el remate decide.

Ficheros tocados: este informe y `15-T05-preguntas.md`. Un script de cotejo en el scratchpad
(`chk05.py`). El tema, sin tocar.

## Alcance

- Exactitud: todo lo que no está en las listas «Copiado del común» y «Copiado de RTVE sin cambios» de
  `15-T05-redaccion.md` (esos pasajes se saltan, salvo para la cobertura).
- Cobertura: el tema entero, contra el enunciado del punto 5 («Animación 2D/3D, motion graphics,
  composición, rotoscopia, tracking y efectos visuales.») y las 15 preguntas.

## Fuentes releídas (29-09-2026)

Copias descargadas en la fase 1 (scratchpad de la sesión, `g/` y `resolve21.txt`):

| Fuente | Qué se cotejó |
|---|---|
| RD 1583/2011 (BOE-A-2011-19532), texto del diario | Art. 5.c y 5.d; módulo 1085 (RA 3, RA 4 y 4.a, 4.c; 5.c y 5.d; orientaciones); 1087 (RA 1 a 7 enteros, contenidos y orientaciones); 1088 (RA 1 a 3); 0907 (RA 3.b; contenidos de composición multicapa y de efectos) |
| RD 500/2024 (BOE-A-2024-10685) | Título y disposición final primera (modifica el RD 1085/2020) |
| Blender 5.2 LTS Manual (glosario, animación, fotogramas clave, interpolación, rigging, tracking, máscaras, alfa) | Todas las citas en negrita y su contexto |
| DaVinci Resolve 21 Reference Manual | Todas las citas; capítulo de cada una por la cabecera «Chapter N» (1, 56, 73, 77, 79, 81, 85) y páginas 1727, 1775, 1827, 1930 |
| Apple ProRes white paper (abril de 2022) | Citas de 4444/4444 XQ y del alfa de 16 bits |

Cotejo por script: 118 negritas del tema buscadas, con espacios y comillas normalizados, en las copias
de las fuentes y en los volcados del Libro de estilo. Todas aparecen literalmente salvo las cuatro
reglas de Resolve, que el tema une con « / » y que en el manual son cuatro viñetas seguidas (p. 1728):
literales. Los números de criterio y de resultado de aprendizaje citados (1085 3, 4, 4.a, 4.c, 5.c, 5.d;
1087 2.b-2.e, 3.a-3.c, 4.b-4.e, 6.a, 6.d, 6.f, 7.c, 7.d, 7.i; 1088 1.b, 2.c, 3; 0907 3.b) casan con el
texto. «La persistencia retiniana» es, en efecto, el primer contenido del 1087; 7.i es el último
criterio del RA 7; la cita «animaciones para incrustación de efectos especiales…» está en las
orientaciones del 1087 (y también del 1085). La cita «nailed to the set» está en el cap. 85 (seguimiento
de cámara), como dice la trazabilidad (aparece además en el 80, en otro contexto).

## Hallazgos de exactitud

Graves: **0**.

Menores: **3**.

1. **Antecedente ambiguo (error 1)**, línea 900, «Normativa que el tema invoca»: «Modificado por el Real
   Decreto 500/2024, de 21 de mayo, en módulos no técnicos; su anexo de convalidaciones lo derogó el Real
   Decreto 1085/2020». El «su» se lee como del RD 500/2024, que es lo último nombrado; lo derogado es el
   anexo de convalidaciones del RD 1583/2011 (disposición derogatoria única, apartado 2, del RD
   1085/2020, según verificación). Propuesta: «el anexo de convalidaciones del RD 1583/2011 lo derogó el
   Real Decreto 1085/2020».
2. **Atribución imprecisa (error 8/9)**, línea 370, §2 «Qué es»: «Apple llama a su códec con alfa «a
   high-quality solution for storing and exchanging motion graphics and composites»». Apple tiene dos
   ProRes con alfa (el propio tema lo dice en §2 «La entrega»), y la frase del white paper es de la
   descripción de **Apple ProRes 4444** («Apple ProRes 4444 is a high-quality solution…»). Propuesta:
   «Apple dice de ProRes 4444 que es…».
3. **Glosas sin fuente y sin marca de oficio (error 9)**:
   - Línea 808, §6 «Los efectos 3D»: los *soft bodies* glosados como «objetos que se deforman, como una
     tela o una gelatina». La norma dice sólo «geometrías controladas por partículas (soft bodies)» y 4.d
     sigue «pintando las influencias y generando los tensores que definirán el movimiento»; la glosa no
     figura en la lista de oficio de «Trazabilidad». Marcarla como oficio o quitar los ejemplos.
   - Línea 360, §1 «La cámara virtual»: «las focales y la profundidad de campo virtuales se eligen como
     en una cámara real (6.a y 6.f)». «Como en una cámara real» no está en 6.a ni en 6.f (sí lo sugieren
     los contenidos, «Óptica y formación de imagen», pero no lo dicen). Basta «se eligen en cada plano
     (6.a y 6.f)» o marcarlo como oficio.

Comprobado sin hallazgo: la regla del seguimiento de punto «tracking, stabilizing, matching moving, and
corner-pinning operations» es del *Tracker node*, que el mismo capítulo 81 identifica con el *point
tracking*: atribución correcta. El *Ease Out* del encargo 1 de «Aplicación práctica» casa con la
definición de Blender. Cuentas (50, 20, 19, 75 de la pregunta 13, 8.294.400, 2.073.600.000): correctas.
Lo declarado como oficio va dicho como oficio.

## Cobertura

El tema recorre los seis elementos del enunciado en su orden, con epígrafe propio cada uno, y la prueba
práctica tiene su «Aplicación práctica». Resultado de las 15 preguntas (`15-T05-preguntas.md`):
**11 enteras, 1 a medias, 3 no**.

Lagunas (**4**), por orden de peso para el test:

1. **Modos de fusión** (pregunta 10, no). Es materia de composición de las más preguntadas y el tema sólo
   los nombra dentro de la cita de Blender. El manual de Resolve 21 los define en el *Apply Mode* del
   nodo Merge (p. ej. «Multiply: Multiplies the values of a color channel. This will give the appearance
   of darkening the…», «Screen: Screen merges the images based on a multiplication of their color
   values…», hacia la línea 71214-71225 de la copia): basta una tabla corta (normal, multiplicar, trama,
   suma, diferencia) en §3.
2. **Métodos de modelado 3D** (pregunta 11, no). El RD 1583/2011, módulo 1086 «Diseño, dibujo y
   modelado para animación», RA 5.c: «Se ha elegido el método de modelado (nurbs, polígonos, subdivision
   surfaces) atendiendo a las características del modelo que hay que realizar.» Una línea en la fila
   «Diseño y modelado» de §1 «La animación 3D y sus fases»; el módulo 1086 habría que añadirlo a la
   normativa.
3. **Principios clásicos de la animación** (pregunta 12, no). Declarado en «Lo que este tema no da» por
   falta de fuente leída. Si el remate no encuentra una fuente citable (manual universitario o
   documentación técnica), que siga declarado; no se debe dar de memoria.
4. **PNG de 16 bits por canal** (pregunta 9, a medias). La tabla de formatos es copiada del común (no
   se discute su exactitud), pero deja creer que el PNG con alfa es siempre de 32 bits. Una nota tras la
   tabla, con fuente (especificación PNG del W3C, profundidades de 8 y 16 bits por muestra en RGBA),
   bastaría. No se ha leído esa fuente en esta fase: el remate debe leerla antes de escribir.

Recuento: graves 0, menores 3, lagunas 4.
