# Realizador/a (puesto 33) · Tema 13 · Fase 5, remate

Tema: `temas/canal-sur-especificos/33-realizador-a/13-postproduccion-montaje-edicion-efectos-grafismo-mezcla-calidad.md`.
Fecha de trabajo: 24-09-2026 (encargo); fuentes releídas el 29-09-2026 (fecha del sistema).
Entrada: `33-T13-refutacion.md` (2 hallazgos menores, 4 lagunas) y `33-T13-preguntas.md` (11 enteras,
1 a medias, 3 no). Copia previa al remate: `33t13-antes-remate.md` en el directorio de trabajo.

Resultado: **2 hallazgos aplicados, 4 lagunas cubiertas ampliando el tema, 1 observación cubierta**.
Ninguna pregunta recortada. **Se amplió contenido nuevo** (≈1.900 palabras: de 15.900 a 17.900); toca
fase 5 bis.

## Hallazgos (comprobados en la fuente antes de aplicar)

| # | Fuente releída | Veredicto | Pasaje cambiado |
|---|---|---|---|
| 1 | Libro de Estilo, 3.17.1.5, pp. 61-62 (volcado, líneas 2071-2080): «En caso de que la entrevista en exteriores sea grabada en una unidad móvil, tenderemos a la fórmula de falso directo (sin interrupciones) y sólo se manipulará el ‘master’…» | Correcto el informe | § 6, «El máster», segunda viñeta: ahora «en la entrevista en exteriores grabada con unidad móvil, para la que el Libro de Estilo pide tender **«a la fórmula de falso directo (sin interrupciones)»**, dice también que…» |
| 2 | UIT-R BT.1702-3, orientación de patrones (texto inglés, líneas 326-330) | Correcto el informe | § 6, «Destellos y patrones»: tras los umbrales del 40 % y 25 %, las dos condiciones con su cita (diferencia de luminancia de la directriz 1; exención de los patrones que fluyen en un sentido) y una línea de oficio para la sala |

## Lagunas (el tema se amplía; las preguntas quedan como están)

| # | Pregunta | Qué se añadió | Fuente, leída el 29-09-2026 |
|---|---|---|---|
| L1 | 4 | § 1, «Offline y online»: párrafo «Con qué se reconforma», definición de EDL y eventos con cita, dependencia del código de tiempo y remisión al tema 14 («Los formatos de proyecto») para AAF y XML | Avid, *Media Composer User's Guide* R8 (1999), p. 710 |
| L2 | 5 | § 2, epígrafe nuevo «Llevar un plano a la secuencia: tres puntos, insertar y sobrescribir»: regla de las tres marcas, tabla *splice-in* / *overwrite* / *replace* con citas, un ejemplo (cálculo propio) y regla de uso (oficio) | Avid, pp. 447, 448 y 449. **Corrección al informe**: la refutación daba p. 450 (la del índice, «with phantom marks»); el texto de las tres marcas está en la p. 447 |
| L3 | 6 | § 2, epígrafe nuevo «El corte desfasado: imagen y sonido por separado»: *split edit* y *overlap edit* con citas, procedimiento (trim de dos rodillos en una sola pista; *extend edit*), tabla L / J (oficio), advertencia de la vista de cabezas. § 5, «El fundido cruzado de audio»: una frase que sitúa el *crossfade* en el corte del sonido (oficio) | Avid, pp. 502, 537, 538 e índice («L-cut edit (Overlap edit)»). El nombre «corte en J» no está en la guía: declarado como oficio y en «Lo que este tema no da» |
| L4 | 14 | § 6, «El máster»: párrafo y tabla de la pista internacional (definición SMPTE que recoge la UER; variantes M&E de documental y de ficción, con citas); consecuencia para la mezcla (oficio) | EBU R 123 (julio de 2009), anexo 2.2, 2.3, 2.3.1 y 2.3.2 (`fuentes/normas-tecnicas/EBU_R123.txt`) |
| Obs. | — | § 2, epígrafe nuevo «Montar un programa grabado con varias cámaras»: clip de grupo y sincronía por código de tiempo, con remisión a la cita del Libro de Estilo ya presente | Avid, glosario p. 268 y p. 662 |

## Otros pasajes cambiados por arrastre

- Portada: Fuente (+ EBU R 123), Redacción que se estudia (+ R 123, «la versión leída»), Extensión
  (17.900 palabras).
- Siglas de entrada: EDL, AAF, XML y M&E; en el texto se quitó el desarrollo repetido.
- «Qué se puede preguntar»: EDL, tres puntos e insertar/sobrescribir, corte en L o en J, multicámara,
  pista internacional.
- «Normativa y recomendaciones técnicas que el tema cita»: fila de la EBU R 123.
- «Lo que este tema no da»: el corte en J como oficio; la vigencia de la R 123 no comprobada en la web
  de la UER (Cloudflare bloqueó la ficha el 29-09-2026) y la ocupación de pistas de CSRTV. Por eso no
  se copió la frase del tema 6 de Operador/a de Sonido sobre que la UER la mantiene «as-is».
- «Trazabilidad»: páginas nuevas de Avid (268, 447-449, 502, 537-538, índice, 662, 710), fila de la
  R 123 y ampliación de la fila «Oficio».

Antecedentes releídos: cada «la misma guía», «la guía de Avid», «la UER», «la R 123», «el módulo
0907», «epígrafe…» tiene su referente delante o remite a un epígrafe que existe («Los formatos de
proyecto» en el tema 14, «La aritmética del código de tiempo», «Qué es y quién la hace», «El corte
desfasado»).

## Lentes

- `indice.py` sobre el tema: 17.867 palabras, 63 epígrafes; índice regenerado con los tres epígrafes
  nuevos. (Se lanzó también sin argumentos por error: sólo reescribe los temas de `portadas.tsv` y los
  esquemas, y `git status` no muestra cambios en ellos.)
- `negritas.py` con Avid 1999, EBU R 123, BT.1702-3, Libro de Estilo y RD 1680/2011, antes y después:
  29 negritas nuevas, 28 halladas; la que no, «must be accompanied by a qualifying explanation, often
  genre-dependent», es literal (el volcado parte «genre-/dependent» en fin de línea).
- `refutar_prosa.py`: el mismo único aviso que antes del remate (UX, parte de un nombre comercial).
- `refutar_exactitud.py` y `refutar_modo.py`: no aplican a lo cambiado (ningún precepto nuevo; la única
  cita nueva del RD, «La banda internacional.», está en los contenidos del módulo 0907 y ya estaba en
  el tema); sin hallazgos.

## Para otro tema (no tocado)

El tema 14 del puesto dice de la EDL «ni efectos» (oficio); la guía de Avid, p. 710, dice que la EDL
lleva **«supported effects information»**. Conviene matizarlo en su remate.

Ficheros tocados: el tema 13 y este informe.
