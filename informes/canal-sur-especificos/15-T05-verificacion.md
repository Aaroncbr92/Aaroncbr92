# Grafista (15) · Tema 5 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/05-animacion-motion-graphics-composicion-rotoscopia-tracking-efectos.md`.
Fecha de trabajo del encargo: 24-09-2026. Fuentes releídas el 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe. Nada más. Copia previa en el scratchpad
(`15t05-antes-verif.md`).

## Pasajes copiados: sólo comprobación literal

Cotejo por script (sin negritas ni cursivas, espacios normalizados), párrafo a párrafo y fila a fila,
contra los originales. No se re-verifican.

- **Copiado del común** (Montador/a T07 y Realizador/a T13): los ocho bloques de la lista del redactor
  son literales. Las únicas diferencias son las declaradas: «(tema 2)» → «(tema 8)» en el croma y en la
  notación 4:4:4:4 (el tema 8 de Grafista trata submuestreo y 4:4:4:4: remisión correcta); «del
  epígrafe 3» quitado en «Los ficheros gráficos»; frase de entrada de «Los efectos y la información»
  adaptada. Las citas del RD 1680/2011 (0907, RA 3.b y 3.c) están también, idénticas, en el RD 1583/2011.
- **Copiado de RTVE sin cambios** (DG 04, DG 11, EM 09): las siete piezas de la lista (frase de la
  pixilación, «Qué hace una capa…», tabla color/luminancia, «Cómo funciona, en una línea…», tabla de
  los cuatro grados, tabla del audio y aviso de la cabecera, «Para qué sirve en el trabajo…») son
  literales.
- **Adaptado de RTVE**: verificado. Se corrigió la regla del intruso (abajo, 8).

## Fuentes releídas (29-09-2026)

| Fuente | Qué se cotejó |
|---|---|
| RD 1583/2011, BOE-A-2011-19532 (texto del diario y ficha de análisis) | Art. 5.c y 5.d; módulo 1085 (RA 3 y 4 títulos, 4.a, 4.c, 5.c, 5.d); 1087 (RA 1 título, 2.b-2.e, 3.a-3.c, RA 4 título, 4.b-4.e, 6.a, 6.d, 6.f, RA 7 título, 7.c, 7.d, 7.i; contenidos; orientaciones pedagógicas); 1088 (RA 1 título, 1.b, 2.c, RA 3); 0907 (contenidos: composición multicapa, «Procedimientos de aplicación de efectos»); BOE núm. 301, 15-XII-2011 |
| RD 500/2024, BOE-A-2024-10685, art. séptimo | Sólo suprime FOL, EIE y FCT, añade módulos transversales y renombra «Proyecto»: no toca los módulos citados |
| RD 1085/2020, BOE-A-2020-17274, disp. derogatoria única, ap. 2 | Deroga el anexo de convalidaciones; el RD 1583/2011 está en la lista |
| Corrección de errores, BOE-A-2012-3441 (BOE núm. 61, 12-III-2012) | Sólo art. 10.1.b y código del FCT (1096 → 1092) y anexo IV |
| Blender 5.2 LTS Manual: Glossary; Animation › Introduction; Keyframes › Introduction; F-Curve Properties; Motion Tracking › Introduction; Masking › Introduction | Todas las citas y su glosa |
| DaVinci Resolve 21 Reference Manual (julio de 2026) | Caps. 1, 56, 73, 77 (pp. 1726-1728, página por la marca de pie), 79, 81, 85, 139 |
| Apple ProRes white paper (abril de 2022) | Citas de 4444/4444 XQ; contenedor |
| Libro de estilo, 1.ª ed., 2004 (volcado .txt) | 3.3 (cita nueva): literal (el volcado lleva ligaduras «ﬁ»); p. 47 correcta (la marca 47 abre la página; el índice pone 3.3 en la 46 y la cita cae en la siguiente) |

Lentes: `negritas.py` 118 negritas, todas en su fuente salvo LE 3.3 (sólo por la ligadura; literal a
mano); `refutar_exactitud.py` y `refutar_modo.py` con el RD 1583/2011: 0 hallazgos (las citas son de
anexo, sin artículo que anclar, salvo el art. 5, comprobado a mano); `refutar_prosa.py`: 0;
`indice.py`: 48 epígrafes. Cuentas (50, 20, 19, 8.294.400, 2.073.600.000 bytes) rehechas: correctas.

## Correcciones aplicadas (10)

1. Siglas: ECTS y fps presentadas y nunca usadas; quitadas. (5)
2. Rebote: la cita empezaba «Bounce Makes…», que es el rótulo de la tabla pegado a la definición; el
   literal es **«Makes the value bounce…»**. Ahora «el rebote (*Bounce*): «Makes…»». (literal)
3. Interpolación constante: «Blender añade que se usa «Normally only used…»» → «Blender añade: …» (la
   frase repetía el verbo). (prosa)
4. Extrapolación: faltaba la salvedad del manual, «it is also possible to configure the curve to loop»;
   añadida. (6)
5. Alfa directo/premultiplicado: «confundirlas es el error de composición más corriente con los
   grafismos que vienen de un programa 3D» no tiene fuente. Sustituido por lo que dice Blackmagic, que
   lo tiene por **«arguably one of the most confusing areas of visual effects compositing»** (p. 1726). (9)
6. Expresiones: la definición citada es la de las *Simple Expressions*, no la de las expresiones en
   general («Simple Expressions are a special type of script…», cap. 73). Atribución corregida;
   trazabilidad: «expresiones simples». (8/9)
7. Render: «El render de una pieza 3D no se hace de una vez, sino por capas» era absoluto sin fuente;
   ahora «En la norma de enseñanza, el render… se organiza por capas». (9)
8. Regla del intruso (adaptada de RTVE): «Tres de los cuatro nombres» no tenía delante los cuatro
   nombres (el cuarto, *time remapping*, sólo implícito). Reescrita nombrando los cuatro. (1, antecedente)
9. ProRes con alfa «en contenedor MOV»: Apple admite también exportar ProRes en envoltorio MXF;
   «normalmente en contenedor MOV». (6)
10. Relectura de cada pasaje cambiado: antecedentes («las define así» → las dos maneras; «la
    premultiplicación») correctos.

## Comprobado sin cambio

- Art. 5.c y 5.d son competencias del art. 5 («Competencias profesionales, personales y sociales»).
- «dibujando» en 1087 3.b es, en efecto, errata del BOE.
- RA 7.i es el último criterio del RA 7; «La persistencia retiniana» es el primer contenido del 1087.
- Las páginas de Resolve se leen por la marca de pie: 1199 (cap. 55), 1726-1728 (cap. 77), 1775
  (cap. 79), 1827 (cap. 81), 1930-1931 (cap. 85), 3338 (cap. 139). Coinciden con las del tema.
- Glosario de Blender: Matte/Mask son la misma entrada («Máscara y mate nombran lo mismo»: correcto);
  alfa directo (PNG, BMP, TARGA) y premultiplicado (motores de render, OpenEXR): correcto.
- Lo declarado como oficio va dicho como oficio.

Cero cambios en lo copiado del común o de RTVE sin cambios.
