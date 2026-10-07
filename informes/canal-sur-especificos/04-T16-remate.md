# 04 · Ayudante de Producción · Tema 16 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/16-igualdad-diversidad-accesibilidad-y-sostenibilidad.md`.
Entrada: `04-T16-refutacion.md` (3 hallazgos menores, 1 laguna) y `04-T16-preguntas.md` (14 enteras,
1 a medias: la 15). Fecha de corte 24-09-2026; fuentes releídas el 06-10-2026 (fecha del sistema).
Ficheros tocados: el tema y este informe. **Amplía: sí** (requiere fase 5 bis).

## 1. Correcciones (cada una comprobada en la fuente)

| # | Hallazgo | Fuente releída | Resultado |
| --- | --- | --- | --- |
| 1 | Ep. 8, «Qué debe saber antes de venir»: falta el inciso «—la fórmula es inhabitual—» del punto 4 del decálogo (3.17.2.1) | Libro de estilo, txt l. 2112-2117 | Confirmado. Se cita el punto 4 entero hasta «tres minutos», con nota «(así, "una informativo", en el original)» y una frase que dice que es la excepción |
| 2 | «Doble objetivo» y «En nuestros informativos…» atribuidos a 9.7.3; están en 9.7.3.1 | Libro de estilo, l. 6144-6187 | Confirmado. Ep. 2: «Y en su subapartado 9.7.3.1 («Precisión donde sea necesaria») fija un…»; ep. 8: «Libro de estilo 9.7.3.1». Trazabilidad: añadido 9.7.3.1 |
| 3 | Ep. 1, «Para el productor, el punto 57…» (pasaje copiado de Productor) | — (adaptación, no dato) | Aplicado: «Para la producción, el punto 57…». **Cambio en texto copiado del común/Productor**, declarado aquí |

## 2. Ampliación (laguna de la pregunta 15)

Nuevo `###` al final del ep. 2, **«La diversidad sexual y de origen en la producción»**, con:

- Ley 4/2023 (BOE-A-2023-5366, redacción única desde 02-03-2023): arts. 3.a (discriminación directa),
  3.i (identidad sexual), 3.j (expresión de género), 3.k (persona trans), 27.1 entero y 28
  (autorregulación), literales del volcado l. 113-135 y 428-435.
- LGCA 4.2 (redacción única): motivos orientación sexual, identidad y expresión de género (sin negrita).
- Carta 8.1.m (remite al literal del ep. 1).
- Constatación: el Libro de estilo 2004 no trata la identidad sexual; su diccionario sólo da *gay*,
  *lesbiana*, *homosexual*, *travesti* (l. 12266-12271, 12470-12472, 12775, 14044).
- LGCA 15.4.h (remite a la subsección anterior) y Libro de estilo 9.3: 9.3.1 recomendación 1 (del
  Colegio de Periodistas de Cataluña), 9.3.3.1, 9.3.4 («moro»), 9.3.4.1 (gitano), 9.3.5.3 (Debates),
  literales de l. 4929-5126.
- Párrafo «Aplicación, no texto de norma»: ninguna fuente fija cómo rotular a una persona trans; de
  3.i y 27.1 se sigue confirmar con ella nombre y cargo y no pedir más justificación que a otra;
  origen, etnia u orientación no figuran salvo que sean el motivo de la intervención.

Pasajes tocados para enlazar lo nuevo:

- Ep. 2, entradilla: «…; al final, la diversidad sexual y de origen llevada a la producción.»
- Ep. 8, «A quién se invita»: viñeta **Minorías étnicas** (9.3.5.3).
- Ep. 8, «Cómo se le atiende»: «(epígrafes 2, 5 y 6). Si la persona es trans, … sigue lo dicho en el
  epígrafe 2 («La diversidad sexual y de origen en la producción»).»
- Ep. 9, tabla, fila «Documentos y rótulos»: nombre con que quiere ser rotulada; sin origen, etnia ni
  orientación si no vienen al caso; base Ley 4/2023 3.i y 27.1, Libro de estilo 9.3.1 y 9.3.4.
- Ep. 9, caso 8 nuevo: colaboradora trans que pide cambiar el nombre del rótulo.
- «Qué se puede preguntar»: identidad sexual, art. 27 Ley 4/2023, Libro de estilo sobre origen
  étnico y debates; rótulo de persona trans.
- «Normativa»: Ley 4/2023, artículos 3, 14, 15.1, 27 y 28.
- «Lo que este tema no da»: viñeta nueva (pauta RTVA sobre personas trans/LGTBI no publicada; códigos
  del art. 28 suscritos por Canal Sur, no consta).
- «Trazabilidad»: filas Ley 4/2023 (3, 27, 28) y LGCA 4.2; fila del Libro de estilo ampliada
  (9.3.1, 9.3.3.1, 9.3.4, 9.3.4.1, 9.3.5.3, 9.7.3.1, diccionario).
- Ficha: Extensión 18.500 → 19.800 palabras.

Relectura de antecedentes: «(más arriba)» de 15.4.h remite a la subsección inmediatamente anterior;
«por esa razón» a la identidad sexual de la frase; «epígrafe 8» y «epígrafe 2» existen. Correcto.

## 3. Lentes

- `indice.py`: 19.802 palabras, 47 epígrafes; índice regenerado con la subsección nueva. (Una
  primera llamada sin argumentos recorrió todos los temas del `.tsv`; `git status` confirma que no
  cambió ningún fichero rastreado.)
- `negritas.py` (Ley 4/2023, LGCA, Libro de estilo): todas las negritas nuevas halladas salvo
  «La palabra moro…» (ligadura «ﬁ» del PDF; cotejada a mano, l. 5026-5027) y «respeto a la
  diversidad de las orientaciones sexuales» (Carta, no pasada como fuente; ya en el ep. 1).
  «siente y autodefine» sale atribuida a «art. 27»: falso positivo, el tema la da como 3.i.
- `refutar_prosa.py`: 1 hallazgo, la frase repetida del texto copiado ya conocida.
- `refutar_exactitud.py` / `refutar_modo.py`: sin avisos sobre los pasajes nuevos (los que salen son
  del texto copiado, ya revisados en verificación).

## 4. Pregunta 15

Con la ampliación, la 15 pasa a **entera** (ep. 2 nueva subsección, ep. 8 y caso 8).
