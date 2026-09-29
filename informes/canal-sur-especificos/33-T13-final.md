# Realizador/a (puesto 33) · Tema 13 · Fase 5 bis, revisión de lo rematado

Tema: `temas/canal-sur-especificos/33-realizador-a/13-postproduccion-montaje-edicion-efectos-grafismo-mezcla-calidad.md`.
Fecha del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha del sistema).
Alcance: sólo los pasajes que lista `33-T13-remate.md`, localizados por diff contra la copia previa al
remate (`33t13-antes-remate.md`, directorio de trabajo). Copia previa a esta fase: `33t13-antes-5bis.md`.

Resultado: **3 correcciones** (una afirmación con un «por eso» sin apoyo, un recuento incompleto de la
R 123 con su arrastre en las siglas, una afirmación sin fuente) y una sigla desarrollada dos veces.
Todo lo demás, confirmado.

## Comprobado en la fuente (sin cambios)

| Pasaje | Fuente releída | Veredicto |
|---|---|---|
| § 1, EDL: definición y «events» | Avid, *Media Composer User's Guide* R8 (1999), p. 710 (volcado, líneas 18531-18535) | Literal y página correctos |
| § 2, tres puntos; *splice-in*, *overwrite*, *replace* | Avid, pp. 447 (líneas 11616-11624), 448 (11653-11656), 449 (11689) | Literales y páginas correctos; bien la corrección del remate (p. 447, no 450) |
| § 2, corte partido y vista de cabezas | Avid, p. 502 (13027-13029) | Correcto |
| § 2, edición solapada, *trim* de dos rodillos, *linger*, *extend edit* | Avid, pp. 537 (13968) y 538 (14000-14016); índice, «L-cut edit (Overlap edit) 537» (23478) | Correcto. «Lo construye como una edición solapada» es lectura razonable del índice y de p. 538 |
| § 2, multicámara: clip de grupo y agrupar | Avid, glosario p. 268 (7224-7227), p. 662 (17280-17281) | Correcto; antecedente «La aritmética del código de tiempo» existe y lleva la cita del Libro de Estilo (3.17.1.5, p. 61) |
| § 6, destellos: diferencia de luminancia y exención | UIT-R BT.1702-3, texto inglés, líneas 326-330 | Literales correctos |
| § 6, «El máster», Libro de Estilo, falso directo | Libro de Estilo, líneas 2075-2082 (pp. 61-62) | Literal correcto; «pide tender» traduce «tenderemos» |
| § 6, «La banda internacional.» | RD 1680/2011, módulo 0907, contenidos (BOE-A-2011-19599, línea 960) | Correcto; antecedente «Qué es y quién la hace» existe y la cita |
| § 6, definiciones SMPTE, 2.3, 2.3.1, 2.3.2 | EBU R 123 (julio de 2009), anexo, líneas 884-907 | Literales correctos |
| Remisiones | Tema 14, «Los formatos de proyecto» (existe, línea 1176); § 5, «El fundido cruzado de audio» (existe) | Antecedentes presentes |

## Corregido (comprobado en la fuente antes de aplicar)

| # | Error | Pasaje | Antes | Ahora |
|---|---|---|---|---|
| 1 | 9 (y cita cruzada, 1) | § 1, «Offline y online» | «Por eso la EDL depende de que el código de tiempo y los nombres… sean únicos (epígrafe «El código de tiempo»)»: la p. 710 no lo dice y ese epígrafe del tema no trata la unicidad | «Como cada evento se localiza por su código de tiempo, la lista sólo funciona si el código y el nombre… identifican el material sin ambigüedad (oficio)» |
| 2 | 3 y 6 | § 6, «El máster», y siglas de entrada | «Las dos variantes que distingue»; la R 123 distingue cuatro (2.3.1 a 2.3.4: *Documentary M&E*, *Fiction or Drama M&E*, *Clean FX*, *World Feed*) | «Distingue cuatro versiones (2.3.1 a 2.3.4); dos llevan la sigla… M&E, y las otras dos, *Clean FX* y *World Feed*, son las de las retransmisiones en exteriores». En las siglas: «para dos de las variantes» |
| 3 | 9 | § 6, «El máster», primera frase | «permite cambiar el idioma de un programa sin rehacer su sonido», sin fuente | «permite ponerle… otra locución, por ejemplo en otro idioma, sin rehacer su sonido (oficio)»; la SMPTE citada a continuación habla de «local commentary» |
| 4 | forma | § 6, «El máster» | M&E desarrollada otra vez tras presentarla en las siglas | Sólo «(M&E)» |

## Lentes

- `indice.py`: 17.899 palabras, 63 epígrafes; índice sin cambios de estructura.
- `refutar_prosa.py`: el mismo único aviso de antes (UX, parte de un nombre comercial).
- Sin preceptos nuevos: `refutar_exactitud.py` y `refutar_modo.py` no aplican.

## Pendiente fuera de este tema

Lo que ya anotó el remate: el tema 14 dice de la EDL «ni efectos»; la p. 710 de Avid dice que lleva
**«supported effects information»**.

Ficheros tocados: el tema 13 y este informe.
