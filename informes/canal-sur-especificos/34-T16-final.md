# 34 · T16 · Revisión final de los pasajes del remate (fase 5 bis)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/16-proteccion-de-datos-privacidad-imagenes.md`.
Alcance: solo los 10 pasajes listados en `34-T16-remate.md`.

## Fuente releída

Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004), `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`,
leído el 24-09-2026 con `grep -n` + `sed` por tramo: 9.1.4 y 9.1.8 (l. 4463-4482), 9.4.2.1 (l. 5487-5501),
9.5.2 entero (l. 5648-5676), 9.7 párrafos 1-2 (l. 6022-6032), 9.9, 9.9.1 y 9.9.2 enteros (l. 6203-6282).

## Cotejo por pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1 | Portada, extensión | Actualizada a 9.760 tras esta fase (`indice.py`) |
| 2 | «Qué se puede preguntar» | Cada asunto nuevo tiene respuesta en el tema. Correcto |
| 3 | Índice | Entrada presente y ancla correcta |
| 4 | §3, 9.7 párrafo 2 | Negrita literal. **Corregido**: la paráfrasis omitía «en situación de aflicción»; ahora «enferma o en situación de aflicción, convalecencia, …» (error 6, salvedad omitida, menor) |
| 5 | §4, pauta sobre imágenes (9.9, 9.9.2) | Negritas literales; ardid/cámara oculta, planos cortos, factor de riesgo y 9.9.2 fieles. «Planos cortos» bien situados en 9.9. Remisión «se cita literal en el epígrafe 6» con antecedente. Correcto |
| 6 | §5, 9.4.2.1 | Negritas literales («se estima» en redonda por «se estimase»: paráfrasis admisible). La regla de entrevistas está, en efecto, bajo el rótulo «Confidencialidad» del 9.4.2.1. Correcto |
| 7 | §6, 9.9 literal y 9.5.2 párrafo 2 | Literal y fiel. El «asediarán con una cercanía desmesurada» es del 9.9.1 (confirmado). Correcto |
| 8 | §7, 9.1.8, 9.1.4, 9.7, 9.9.2 | Fieles; la errata «si así o solicita» va en redonda. Remisión «9.7, en el epígrafe 3» con antecedente. Correcto |
| 9 | §8, 9.5.2 detenidos y personas públicas | Negritas literales; paráfrasis fiel. **Corregido** el encabezado de la lista: decía «Es también el único criterio escrito de la RTVA sobre el interés público informativo que se ha localizado». Es falso dentro del propio tema: el 9.9 (añadido en el §4 por el mismo remate) exige «auténtico interés público» para la cámara oculta. Además «Es también» no tenía sujeto claro. Ahora: «El mismo 9.5.2 da además criterios para pesar el interés público de la identidad de detenidos y personas públicas (el 9.9, en el epígrafe 4, exige «**auténtico interés público**» para la cámara oculta):» (error 9 / 3) |
| 10 | §8, remisión a LO 2/1984 en el tema 1 | Coherente con «Lo que este tema no da». Correcto |

## Lentes tras corregir

- `indice.py`: 9.760 palabras, 27 epígrafes.
- `refutar_prosa.py`: 0 hallazgos.
- `refutar_documento.py` contra el Libro de estilo (copia con «ﬁ/ﬂ» normalizadas en el scratchpad): ninguna negrita de los pasajes revisados sale como no literal (las 90 «no literales» del recuento son citas de leyes, ajenas a esta fuente).

## Resultado

2 correcciones (1 afirmación sin fuente contradicha por el propio tema, 1 salvedad omitida en paráfrasis); 8 pasajes correctos. El informe del remate no se equivocó en lo que listó; sus remisiones tienen antecedente.

## Ficheros tocados

- El tema 16 (dos frases y la extensión de la portada).
- Este informe.
- Copia normalizada del Libro de estilo en el scratchpad, fuera del repositorio.
