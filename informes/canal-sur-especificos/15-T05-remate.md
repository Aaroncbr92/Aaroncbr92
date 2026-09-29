# Grafista (15) · Tema 5 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/05-animacion-motion-graphics-composicion-rotoscopia-tracking-efectos.md`
(10.970 → 11.360 palabras). Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026
(fecha de sistema). Base: `15-T05-refutacion.md` y `15-T05-preguntas.md`.

Ficheros tocados: el tema y este informe. Copia previa del tema y descarga de la especificación PNG en el
scratchpad (`t05-antes.md`, `png3.html`, `png3.txt`).

**Amplía: sí** (dos epígrafes o párrafos nuevos y una nota con fuente nueva). Pide fase 5 bis.

## Fuentes releídas (29-09-2026)

| Fuente | Qué se comprobó |
|---|---|
| RD 1583/2011 (BOE-A-2011-19532), texto del diario | Módulo 1086, RA 5, 5.a y 5.c; módulo 1087, 4.d, 6.a, 6.b, 6.f |
| RD 500/2024 (BOE-A-2024-10685), art. séptimo | Suprime FOL, EIE y FCT e incluye módulos nuevos; no toca el 1086 |
| RD 1085/2020, disp. derogatoria única, ap. 2 | Según `15-T05-verificacion.md` (no releído aquí): deroga el anexo de convalidaciones, con el RD 1583/2011 en la lista |
| Apple ProRes white paper (abril de 2022) | «Apple ProRes 4444 is a high-quality solution for storing and exchanging motion graphics and composites…» |
| DaVinci Resolve 21 Reference Manual, cap. 94 «Composite Nodes», nodo Merge, *Apply Modes*, pp. 2266-2267 (número de página por el pie que cierra cada página) | Normal, Screen, Darken, Multiply, Linear Dodge (Add), Lighten, Overlay, Difference |
| Blender 5.2 LTS Manual, Glossary | «NURBS», «Subdivision Surface» |
| W3C, PNG Specification (Third Edition), recomendación de 24-VI-2025, 11.2.1 IHDR y tabla 12 | Profundidad por muestra, no por píxel; tipo de color 6 (*truecolor with alpha*): 8 y 16 bits |

## Hallazgos de exactitud: los tres, aplicados tras comprobarlos

1. «Normativa que el tema invoca»: «su anexo de convalidaciones lo derogó» → «**el anexo de
   convalidaciones del RD 1583/2011** lo derogó el Real Decreto 1085/2020». Antecedente releído: correcto.
2. §2 «Qué es»: «Apple llama a su códec con alfa» → «Apple dice de ProRes 4444 que es». Confirmado en el
   white paper: la frase es de ProRes 4444.
3. Glosas sin fuente:
   - §6 «Los efectos 3D», cuerpos blandos: quitada la glosa «como una tela o una gelatina»; en su lugar,
     el criterio 4.d entero y literal («…(soft bodies) necesarias para cada plano, pintando las
     influencias y generando los tensores que definirán el movimiento.»).
   - §1 «La cámara virtual»: «como en una cámara real» → «en cada plano» (6.b dice «Se han colocado las
     focales fijas en cada plano»).

## Lagunas

1. **Modos de fusión (pregunta 10)**: nuevo epígrafe `### Los modos de fusión` al final del §3, con la
   definición del *Apply Mode* y una tabla de siete filas (normal, multiplicar, trama, suma, superponer,
   diferencia, oscurecer/aclarar), citas literales del manual de Resolve. Los nombres en castellano y
   el uso (multiplicar para sombras; trama y suma para brillos sobre negro) van como oficio.
2. **Métodos de modelado (pregunta 11)**: nuevo párrafo tras la tabla de fases 3D (RA 5, 5.c y 5.a del
   módulo 1086, literales) con las definiciones de NURBS y superficie de subdivisión del glosario de
   Blender; remisión en la fila «Diseño y modelado». Módulo 1086 añadido a la ficha y a la normativa.
3. **Principios clásicos de la animación (pregunta 12)**: sin fuente citable a mano; siguen declarados en
   «Lo que este tema no da», con la razón ampliada. No se dan de memoria.
4. **PNG de 16 bits (pregunta 9)**: nota tras la cuenta del TGA (la tabla, copiada del común, no se toca)
   con tres citas de la especificación W3C y la cuenta 16 × 4 = 64 bits.

Con el tema rematado, las preguntas 9, 10 y 11 pasan a enteras; la 12 sigue en «no» declarada.

## Otros pasajes cambiados

- Siglas: se presenta W3C (World Wide Web Consortium, nombre leído en la propia especificación).
- Ficha: «Fuente» (módulo 1086; especificación PNG) y «Redacción que se estudia» (PNG 3.ª ed., 24-VI-2025).
- «Qué se puede preguntar»: métodos de modelado, bits por píxel con alfa, modos de fusión.
- «Trazabilidad»: cuatro filas nuevas (RD 1583/2011 módulo 1086; Resolve cap. 94; Blender glosario NURBS
  y Subdivision Surface; W3C PNG) y lista de oficio ampliada (nombres en castellano y uso de los modos;
  cuenta del PNG).
- Índice regenerado.

Antecedentes releídos en cada pasaje cambiado: «Sus criterios» (del módulo 1086), «los dos que no son la
malla» (tras «nurbs, polígonos…»), «la tabla» del PNG (tabla inmediatamente anterior): todos tienen
delante lo que nombran.

## Lentes

- `indice.py`: regenerado; 11.360 palabras, 49 epígrafes.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` contra RD 1583/2011, glosario y páginas de Blender, Resolve 21, ProRes y PNG: 132
  cotejadas; las 6 que no aparecen son del Libro de estilo (copiadas del tema de Montador/a, ya
  verificadas; el volcado no se pasó a la lente). Todas las negritas nuevas están literales.
- `refutar_exactitud.py` y `refutar_modo.py`: no aplican; el tema no cita normas con volcado del BOE en
  `fuentes/` (la única norma es de enseñanza y no tiene «podrá/deberá» en juego).
