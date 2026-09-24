# 34 · T05 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/05-generos-periodisticos.md`
(3.404 → 3.580 palabras). Entrada: `34-T05-refutacion.md` (3 menores, 2 lagunas) y `34-T05-preguntas.md`.

## Fuentes releídas (24-09-2026)

- Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004), `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`:
  3.5 (líneas 1528-1572), 3.17.2.2 (2171-2175), 7.1 (3315-3321), 8.1 punto 2 (4011-4016), 8.3 y 8.3.2 (4124-4197).
- Manual de estilo de RTVE, RNE: índice 3.3 y 3.4, `fuentes/informacion/RTVE_manual-de-estilo_rne.txt` (líneas 27-37, 78, 101).

## Correcciones: todas comprobadas en la fuente; ninguna rechazada

| # | Pasaje | Antes | Después | Comprobación |
|---|---|---|---|---|
| H1 | §5, entrevista en plató | «Tratamiento de usted (3.17.2.2).» | Cita literal: **«Como norma general que sólo se podrá obviar en casos y formatos muy concretos, en plató siempre nos dirigiremos al entrevistado con tratamiento de usted»** | LE 3.17.2.2, literal |
| H2 | §7, primer bullet y «Conexión» | Todo atribuido a 8.3; cita «(8.1.2, 8.3.2)» | 8.3: interrogantes y seis preguntas; «Y en 8.3.2»: mirar a cámara, saludo/despedida, «sólo habla el presentador». Cita: «(8.1, punto 2; 8.3 y 8.3.2)» | 8.1 no tiene subapartados; «conexión en directo» en el punto 2 de 8.1, en el párrafo inicial de 8.3 y en 8.3.2. Mirada a cámara y despedida, en 8.3.2 |
| H3 | §6, quién opina | «Y en general: … vedada … (7.1)» | «Y en el apartado de Política: … vedada … La subjetividad pertenece en exclusiva a las declaraciones» (7.1) | LE 7.1, rúbrica «Política», literal |

## Lagunas: se amplía el tema

| # | Pasaje | Qué se añade | Fuente |
|---|---|---|---|
| L1 (preg. 8) | §3, Crónica, Canal Sur | Se completa la cita («y permite al autor una interpretación propia, aunque no radical, de lo que ve.») y se añade el límite: **«La opinión personal no tiene cabida […] a partir de datos fehacientes y nunca como hipótesis arriesgadas.»** Enlace con 3.11 dicho como lectura del tema, no como texto de la fuente | LE 3.5 (el párrafo está en 3.5, antes de 3.5.1) |
| L2 (preg. 9) | §8, primer bullet nuevo | RNE agrupa en «Géneros de opinión» (3.4) debate, tertulia, comentario y encuesta a pie de calle; en «Géneros informativos radiofónicos» (3.3) noticia, crónica, reportaje, informe y entrevista | Manual RTVE, RNE, rótulos 3.3 y 3.4 |

Con esto, preguntas 8, 9 y 13 quedan contestables con el tema: **15 de 15 enteras**.

## Relectura de antecedentes

«El mismo apartado» (§3) → 3.5, nombrado justo antes. «Ese margen» → la interpretación propia de 3.5.
«§ 6» → epígrafe 6 del tema. «Y en 8.3.2» → sigue a 8.3 en la misma frase. «el apartado de Política» →
7.1, citado al final. Sin antecedentes huérfanos.

## Lentes

- `indice.py`: 3.580 palabras, 17 epígrafes; índice sin cambios de estructura. Portada no en
  `portadas.tsv`: «Extensión» actualizada a mano (3.404 → 3.580).
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (LE, Manual RTVE, Carta, Contrato-programa): las negritas nuevas o cambiadas aparecen
  todas. Las 14 «no están» son anteriores y no cambiadas: cortes con «[...]», saltos de página del volcado
  o fuente no pasada (Estatuto Profesional); la refutación ya las dio por literales con normalización.
- No proceden `refutar_exactitud.py` ni `refutar_modo.py`: el tema no cita normas con articulado.

## Ficheros tocados

El tema y este informe. **Se amplió contenido nuevo** (L1, L2): procede la fase 5 bis sobre los pasajes
de §3 y §8 (y, si se quiere, los de §5-§7).
