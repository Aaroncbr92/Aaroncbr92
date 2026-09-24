# T02 · Refutación (fase 4, modo ahorro: una lectura, dos lentes)

Tema: `temas/canal-sur-comun/02-estatuto-autonomia-andalucia.md` (24.652 palabras, verificado).
Leídos antes: `ENCARGO.md`, `CICLO.md` (avisos y dos modos ahorro) y `T02-verificacion.md`.
**Fecha de lectura de todos los preceptos: 24-09-2026**, redacción vigente, extraídos uno a uno de
los volcados de `fuentes/canal-sur/` y del Reglamento del Parlamento en `documentos/`. No he
corregido el tema. Ficheros tocados: este informe y `T02-preguntas.md`.

## 1. Exactitud normativa

Cotejado, con el foco en lo que la verificación no listó o parafraseó: Estatuto 2, 89, 100 a 111,
113, 114, 116, 117, 120, 123, 125 a 127, 142 y rúbricas de 15 a 34; Ley 6/2006, 9, 11, 13, 27,
30 a 32, 37, 43, 46 y 10.1.f-h; Ley 9/2007, 12, 17, 19, 58, 60, 65, 67, 70, 72, 76 y 77; Ley
2/2024, 5 a 10, 17 a 19, 21 a 26, 28 y 29; Ley 1/1986, 14 y 23; Reglamento del Parlamento 22, 33,
52, 69, 70 y 145. Mayorías, plazos, composición, mandatos, clases de competencia y modo verbal
cuadran. Tres omisiones de salvedad, todas menores:

| # | Dónde | Qué dice el tema | Qué debería decir | Fuente literal | Gravedad |
| --- | --- | --- | --- | --- | --- |
| 1 | Consejo de Gobierno, párrafo tras las atribuciones (artículo 43 de la Ley 6/2006) | «el anteproyecto se informa por la Secretaría General Técnica y el Gabinete Jurídico y, finalmente, se pide dictamen del Consejo Consultivo» | Añadir «y demás órganos cuyo informe o dictamen sea preceptivo, salvo lo previsto en el artículo 45 bis» | Ley 6/2006, 43.5: «En todo caso, los anteproyectos de ley deberán ser informados por la Secretaría General Técnica respectiva, el Gabinete Jurídico de la Junta de Andalucía y demás órganos cuyo informe o dictamen tenga carácter preceptivo conforme a las normas vigentes, a excepción de lo previsto en el artículo 45 bis. Finalmente, se solicitará dictamen del Consejo Consultivo de Andalucía.» | Menor (error 6) |
| 2 | Consejo Consultivo, *Composición* (artículo 5 de la Ley 2/2024) | «excluidos los que lo son por su cargo» | «excluidos los designados en función del cargo específico que desempeñen o hubieren desempeñado» (alcanza a los permanentes, antiguos Presidentes de la Junta) | Ley 2/2024, 5: «De esta regla se excluirán aquellos que fueren designados en función del cargo específico que desempeñen o hubieren desempeñado.» | Induce a error (error 6): deja la pregunta 12 a medias |
| 3 | Consejo Consultivo, consultas preceptivas, número 9 | «Revocación de actos tributarios con deuda superior a 30.000 euros.» | Añadir «y conflictos en la aplicación de la norma tributaria» | Ley 2/2024, 17.9: «Revocación de actos de naturaleza tributaria cuando la deuda supere los 30.000 euros y conflictos en la aplicación de la norma tributaria.» | Menor (error 6) |

## 2. Cobertura

- La cabecera y las rúbricas a) y b) se cubren enteras, cada institución del enunciado con su
  epígrafe y en su orden.
- Quince preguntas en `T02-preguntas.md` (cabecera 5, a) 7, b) 3): **14 enteras, 1 a medias**
  (la 12, por el hallazgo 2), 0 sin contestar.

## 3. Prosa

| # | Dónde | Qué pasa | Qué debería ser | Gravedad |
| --- | --- | --- | --- | --- |
| 4 | Agencias públicas empresariales, fin del párrafo del artículo 70 | La nota sobre la sentencia del Tribunal Constitucional 230/2015 (del art. 69) va pegada a la frase del personal (art. 70), en la misma línea: «…(artículo 70). El artículo 69 lleva…» | Separarla en párrafo propio o subirla tras el párrafo del 69.2 | Menor |
| 5 | «Lo que este tema no da, y dónde está», entre el guion del Decreto 155/1988 y el del tipo de agencia | Línea en blanco dentro de la lista, que la parte en dos | Quitar la línea en blanco | Menor |

Sin antecedentes rotos, siglas sin presentar ni referencias a ficheros del proyecto.

## 4. Lentes automáticas

| Lente | Fuentes | Resultado |
| --- | --- | --- |
| `refutar_prosa.py` | tema entero | 0 hallazgos |
| `refutar_modo.py` | las nueve normas del BOE | 0 hallazgos |

`refutar_exactitud.py`, `refutar_citas.py` y `refutar_documento.py` no se han vuelto a correr: el
tema no ha cambiado desde la verificación, que da su cuadro.
