# 34 · T18 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/18-etica-profesional-responsabilidad.md`.
Entrada: `34-T18-refutacion.md` (G1, M1, M2, L1-L3) y `34-T18-preguntas.md` (11 y 12 «no», 15 «no», 2 «a medias»).
Otros ficheros tocados: sólo este informe.

## Fuentes releídas antes de aplicar (24-09-2026)

- `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 1.5, 1.7, 1.8 (pp. 31-32), 2.3.2.8, 2.3.2.13, 2.5.3; anexo FAPE («Documento aprobado en la asamblea ordinaria de la FAPE. Sevilla 27 noviembre 1993»). Todo confirmado literal.
- `fuentes/canal-sur/documentos/norma-reguladora-defensor-audiencia-rtva.txt`: arts. 4.2 y 7.4. Confirmados.
- Portada (M1): cotejada con la tabla de normativa del propio tema.

Ninguna corrección del informe resultó errónea; se aplicaron todas.

## Pasajes cambiados

1. **Portada, «Fuente»** (M1): añadidos Constitución (art. 20.1.d) y LO 2/1997 (arts. 1 a 3); Ley 18/2007 con «17.1.m, 17.2» en vez de «17»; Carta con «10.1». Extensión: 7.392 → 8.137 palabras.
2. **Qué se puede preguntar**: añadidas las normas básicas 1.5, 1.7 y 1.8 y el secreto con sus dos salvedades.
3. **§1, art. 7 FIP**: remisión a las salvedades del Libro (epígrafe 3).
4. **§3, inventario** (G1): capítulo 1 con 1.5, 1.7, 1.8 y 1.9; mención del anexo FAPE (M2).
5. **§3, nuevo ### «La responsabilidad del redactor (1.8)»** (L1, pregunta 12): literal de 1.8 y comentario.
6. **§3, nuevo ### «El secreto profesional (2.3.2.13)»** (L3, pregunta 15): literal y contraste con art. 7 FIP y 6.9 de 2006 (antecedentes nombrados).
7. **§6**: nuevo primer punto, Libro 1.5 Imparcialidad, literal (L1).
8. **§7**: nuevo punto, Libro 2.3.2.8 Relaciones sociales (L3, opcional).
9. **§9, arranque** (G1, pregunta 11): suprimido «Ninguna de las fuentes del tema tiene un apartado con este nombre»; en su lugar, literal de 1.7 Transparencia y nuevo punto 2.5.3 Equidad (L2).
10. **§9, punto del Defensor** (L2, pregunta 2): añadidos art. 4.2 in fine y art. 7.4.
11. **§10, funciones (art. 4)**: la segunda función completa (4.2 in fine). **§10, arts. 6 y 7**: frase sobre 7.4 con remisión al epígrafe 9.
12. **Normativa que el tema invoca**: fila de la norma del Defensor, «(4.2 y 7.4 en el epígrafe 9)».
13. **Lo que este tema no da** (M2): FAPE, «el tema no los desarrolla, aunque… figura como anexo del Libro de estilo».
14. **Trazabilidad**: apartados del Libro 1.5, 1.7, 1.8, 2.3.2.13, 2.5.3 y anexo FAPE.

Releídos los pasajes: cada remisión («epígrafe 3», «epígrafe 9», «Frente al art. 7 de la Carta de la FIP») tiene su antecedente.

## Lentes

- `indice.py`: índice regenerado, 38 epígrafes, 8.137 palabras (el tema no está en `portadas.tsv`; la extensión de la portada se puso a mano con esa cifra).
- `negritas.py` (Libro con ligaduras normalizadas en el scratchpad, norma del Defensor, FIP, Estatuto 2006, Ley 18/2007, Carta, X Convenio, CE, LO 2/1997): 121 cotejadas, 2 «no están», ambas falsos positivos por salto de página en el Libro (1.5 entre pp. 31-32; 2.5.5 entre pp. 41-42, preexistente).
- `refutar_exactitud.py` (Ley 18/2007, CE, LO 2/1997): los 20 «no literales» son citas de la norma del Defensor cotejadas contra el BOE, no contra su fuente; falsos positivos ya confirmados en la refutación.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0 hallazgos.

## Resultado

Amplió contenido nuevo: **sí** (dos ### nuevos en §3 y puntos nuevos en §6, §7, §9 y §10). Procede la fase 5 bis sobre los pasajes 4-11.
Preguntas que pasan a «entera»: 2, 11, 12 y 15.
