# Grafista (15) · Tema 5 · Revisión de lo rematado (fase 5 bis)

Tema: `temas/canal-sur-especificos/15-grafista/05-animacion-motion-graphics-composicion-rotoscopia-tracking-efectos.md`
(11.360 → 11.390 palabras, 49 epígrafes). Fecha del encargo: 24-09-2026; fuentes leídas el 29-09-2026
(fecha de sistema). Alcance: sólo los pasajes que lista `15-T05-remate.md`, localizados por diff contra
la copia previa al remate (`t05-antes.md` del scratchpad). Copia previa a esta fase: `15t05-antes-5bis.md`
(scratchpad).

Ficheros tocados: el tema y este informe.

## Fuentes releídas (29-09-2026)

| Fuente | Qué se comprobó |
|---|---|
| RD 1583/2011 (BOE-A-2011-19532), texto del diario descargado de nuevo | Título del módulo 1086; RA 5, 5.a y 5.c literales; módulo 1087, 4.d, 6.a, 6.b y 6.f |
| BOE, análisis del RD 1583/2011 (posteriores) | «SE DEROGA el anexo indicado, por Real Decreto 1085/2020» (BOE-A-2020-17274) |
| RD 1085/2020 (BOE-A-2020-17274), disp. derogatoria única, ap. 2 | Deroga «el Anexo relativo a las convalidaciones de módulos profesionales» de una lista que incluye el RD 1583/2011: correcto |
| DaVinci Resolve 21 Reference Manual, cap. 94, nodo Merge | Definición del *Apply Mode* y las seis citas de la tabla, literales; pie 2266 (Normal a Linear Burn) y 2267 (Darker Color a Hue): pp. 2266-2267 correctas. Glosas en redonda (Linear Dodge «similar but stronger results than Screen»; Overlay «preserving the highlights and shadows»; Difference «subtracts»; Darken/Lighten canal a canal) apoyadas en el mismo texto |
| Blender 5.2 LTS Manual, Glossary (página actualizada el 29-09-2026) | «NURBS ¶ Non-uniform Rational Basis Spline ¶ A computer graphics technique…»; «Subdivision Surface ¶ A method of creating smooth higher poly surfaces…»: literales |
| W3C, PNG Specification (Third Edition), Recommendation 24 June 2025, 11.2.1 IHDR y Table 12 | Tres citas literales; tipo de color 6, profundidades 8 y 16 |
| Apple ProRes White Paper, April 2022 | «Apple ProRes 4444 is a high-quality solution for storing and exchanging motion graphics and composites»: la frase es de ProRes 4444 |
| Adobe, «Descripciones de modos de fusionar en Photoshop» (ayuda en español, actualizada el 2-XII-2025) | Nombres: Normal, Multiplicar, Trama, Sobreexposición lineal (Añadir), Superponer, Diferencia, Oscurecer, Aclarar |

## Hallazgos y correcciones (comprobadas en la fuente antes de aplicarlas)

1. **Error 9 · nombre en castellano sin fuente y equivocado.** El remate daba *Linear Dodge (Add)* como
   «suma» y presentaba los nombres como «el habitual en los programas traducidos (oficio)». La ayuda de
   Photoshop en español lo llama **Sobreexposición lineal (Añadir)**; los otros seis nombres coinciden.
   Cambios: fila de la tabla → «(sobreexposición lineal o añadir)»; «Uso de oficio» → «trama y
   sobreexposición lineal»; «Qué se puede preguntar» → «multiplicar, trama, sobreexposición lineal…»;
   la frase de entrada ya no dice «oficio» sino «el de la ayuda de Photoshop en español (Adobe)»;
   Trazabilidad: fila nueva de Adobe y los nombres salen de la lista de oficio (queda «el uso de los
   modos de fusión»); ficha «Fuente»: Adobe añadido a la documentación de fabricante.
2. **Error 1 · cita cruzada.** §1 «La cámara virtual»: «se eligen en cada plano (6.a y 6.f)». «En cada
   plano» es del 6.b (**«Se han colocado las focales fijas en cada plano…»**), que el remate usó sin
   citarlo → «(6.a, 6.b y 6.f)».

## Sin hallazgo

- Normativa: «el anexo de convalidaciones del RD 1583/2011 lo derogó el Real Decreto 1085/2020, de 9 de
  diciembre»: confirmado; antecedente explícito.
- Párrafo del módulo 1086 (título, RA 5, 5.c, 5.a) y fila «Diseño y modelado»: literales; «Sus
  criterios» remite al RA 5 del 1086; «los dos que no son la malla de polígonos» tiene delante la lista.
- Cuerpos blandos (4.d del 1087, entero): literal.
- ProRes 4444: literal.
- Nota del PNG: citas literales; «la tabla» es la inmediatamente anterior (PNG, 32 bits, 8 por canal);
  cuenta 16 × 4 = 64 correcta.
- Siglas W3C, ficha (1086 y PNG), «Lo que este tema no da» (principios de animación) y las cuatro filas
  nuevas de Trazabilidad: coherentes con lo anterior.

## Lentes

- `indice.py`: 11.390 palabras, 49 epígrafes (el índice no cambia: no hay epígrafes nuevos).
- `refutar_prosa.py`: 0 hallazgos; negritas rotas o anidadas: ninguna.
- No se añadió negrita nueva; las correcciones van en redonda.
