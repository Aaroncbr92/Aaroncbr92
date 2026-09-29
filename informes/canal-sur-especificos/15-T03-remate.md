# Grafista (15) · Tema 3 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/03-grafismo-informativos-programas-deportes-promociones-continuidad-eventos.md`.
Fecha de trabajo del encargo: 24-09-2026; fuentes releídas en esta fase: 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe. Copia previa del tema en el scratchpad de la sesión.

Resultado: 3 menores aplicados, 1 laguna cubierta **ampliando** (sección nueva). Observación de
«Trazabilidad» (fechas de lo copiado del común) no aplicada: no es hallazgo y exigiría releer los temas
de origen.

## Comprobación en la fuente (29-09-2026)

- *Fonseca* 25 (2022), texto del PDF: el resumen da tres funciones (comprensión, identidad,
  espectacularización); Marín añade la pedagógica; Blanco se introduce con «No obstante, los grafismos
  son igualmente relevantes a la hora de otorgar "Espectacularidad Visual"» (desarrolla la tercera).
  Hallazgo 1, confirmado.
- Mismo texto: «los departamentos implicados […] son Mediacoach, Audiovisual, Realización y Grafismo»;
  «El director de Mediacoach […] el grupo humano bajo sus órdenes»; «sistema de análisis de datos de
  juego Mediacoach»; tabla 1: «Suite de análisis de datos y estadísticas para clubes». Hallazgo 2,
  confirmado.
- DSK y LED: una aparición cada una (grep). Hallazgo 3, confirmado.
- LGCA (BOE-A-2022-11311, volcado): arts. 97, 98.1, 98.2, 98.4, 98.7, 99.1 y 99.2.c; una sola redacción,
  aplicable desde el 9-7-2022. Laguna, confirmada; literales cotejados con `negritas.py` (todos «ok»).

## Pasajes cambiados

1. **Términos técnicos** (entrada). Antes: «la composición posterior del mezclador (DSK, del inglés
   *downstream keyer*); la realidad aumentada y la realidad virtual; el diodo emisor de luz (LED, del
   inglés *light-emitting diode*); el videowall». Ahora: «la composición posterior del mezclador (la
   capa que se superpone a todo lo demás); la realidad aumentada y la realidad virtual; el videowall».
   La glosa sale de la cita ATEM del epígrafe 5.
2. **Siglas** (entrada). Antes: «Mediacoach, la herramienta de datos de la liga…». Ahora: «Mediacoach,
   el sistema y el departamento de análisis de datos de juego de la liga profesional de fútbol española
   (LaLiga)».
3. **3 · Qué aporta el grafismo a una retransmisión**. Antes: «añade, de otros autores, dos funciones
   más. Una pedagógica […] Y otra de espectáculo, que el estudio expone a partir de Blanco». Ahora:
   «añade, de otros autores, una función más, la pedagógica (Marín, 2011) […] Y desarrolla la del
   espectáculo a partir de Blanco (2001, sobre el baloncesto)».
4. **3 · Los datos y quién decide qué se grafía**. Antes: «la herramienta de datos (Mediacoach)
   **«Lidera la estrategia…»**». Ahora: «entre cuatro departamentos: el de Mediacoach (el sistema de
   análisis de datos de juego de la liga, con director y equipo propios) **«Lidera la estrategia…»**».
5. **5 · Qué es la continuidad**, lista: «Los avisos: la señalización de contenido (la calificación por
   edades, abajo), los rótulos de servicio.»
6. **Nuevo `### Lo que la ley exige a la continuidad: la calificación por edades`** (tras «Las piezas
   de continuidad», antes de «Coherencia visual»; ~550 palabras): 98.1 literal y sus dos condiciones de
   diseño; remisión al acuerdo de corregulación (98.2, 98.7 literales en lo citado), descriptores (97 y
   98.4); 99.1 literal; 99.2.c literal (franja 22:00-6:00 de los no recomendados para menores de 18);
   aplicación al grafista (oficio) y salvedad de que los símbolos, colores y tiempos los fija el acuerdo,
   no leído.
7. **Ficha**: Fuente con arts. 97, 98 y 99; Extensión 8.800 → 9.400 palabras aproximadamente.
8. **Qué se puede preguntar**: añade el indicativo de edad y la franja de los no recomendados para
   menores de dieciocho años.
9. **Índice**: entrada nueva (regenerado con `indice.py`).
10. **Normativa**: LGCA con arts. 97, 98 y 99.
11. **Lo que este tema no da**: la línea «no se ha leído su norma» se sustituye por los símbolos,
    colores y tiempos del indicativo (acuerdo de corregulación, 98.2 y 98.7, no leído; tampoco consta
    cuál aplica CSRTV).
12. **Trazabilidad**: fila nueva LGCA arts. 97-99 (leída 29-09-2026); «el indicativo de edad como
    pieza de continuidad» añadido al párrafo de oficio.

Antecedentes releídos: «ese artículo», «este artículo», «el apartado anterior» sólo aparecen dentro
de citas literales, con su artículo delante; «abajo» (lista de continuidad) apunta a la sección nueva,
que va después.

## Lentes

- `indice.py`: 10.695 palabras, 46 epígrafes; índice regenerado.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (LGCA, LOREG, *Fonseca*): todas las negritas nuevas, «ok»; las «no está» son del
  Libro de Estilo, Carta, Contrato-programa, Mateu, ATEM y RD, fuentes no pasadas (sin cambios).
- `refutar_exactitud.py`: 2 «no literales», arts. 13.6 y 13.7 de la Carta, falsos positivos (se cotejan
  contra la LGCA, no contra la Carta; la refutación las leyó literales).
- `refutar_modo.py`: 0 hallazgos.

## Preguntas

Con el tema rematado, la 14 pasa a entera (98.1 literal) y la 15 a entera (Mediacoach como
departamento y sistema). Quedan 15 enteras.

Amplió contenido nuevo: sí (sección de calificación por edades). Procede la fase 5 bis sobre los
pasajes 3, 4 y 6.
