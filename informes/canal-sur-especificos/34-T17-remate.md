# 34 · T17 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/17-accesibilidad-igualdad-diversidad.md`.
Entrada: `34-T17-refutacion.md` (0 graves, 2 menores, 4 lagunas) y `34-T17-preguntas.md` (11/2/2).

**Resultado: el remate AMPLÍA contenido nuevo** (pasa a fase 5 bis). Extensión: 10.690 → 12.644
palabras (`indice.py`).

## Correcciones de la refutación, cada una comprobada en la fuente

| Hallazgo | Fuente leída hoy | Resultado |
|---|---|---|
| Menor 1: lista «Normativa que el tema invoca» incompleta | Ley 18/2007 art. 2.1 (BOE-A-2008-1185, `boe.py`); LAA art. 45 (BOE-A-2018-15240, `boe.py ar-45`); LGCA DA 3.ª (BOE-A-2022-11311, `boe.py da-3`); LO 1/2004 ya citada en el 57.2 copiado del común | Aplicada. LAA 45.4 y LGCA DA 3.ª no se dejan «no leídas»: se leyeron y se añaden también al cuerpo (§2) |
| Menor 2: CP punto 93 sin fundamento | Contrato-programa txt, l. 1945: «Conforme a la Ley 18/2007 en su artículo 29 y Disposición Adicional Segunda se cumplirá con el servicio de audiodescripción» | Aplicada. Leídos art. 29 y DA 2.ª de la Ley 18/2007 (una redacción, vig. 15-01-2008) |

## Lagunas: se amplía el tema

1. **Protección de menores, arts. 97-100 LGCA (P9 «no»)**. Copiado literal del tema 4 del común
   (bloque «Artículos 97 y 98» a «Artículo 100», incluida la DT 2.ª). Copiado del común: no se
   reverifica. Se añade la DT 2.ª de la LGCA y la Ley 13/2011 a la lista de normativa.
2. **Art. 49 CE (P11 «a medias»)**. Leída la redacción original con `boe.py --fecha 20240101`:
   «…integración de los disminuidos físicos, sensoriales y psíquicos…»; la vigente, de
   BOE-A-2024-3099 (17-02-2024). Se añade la cadena en §8 y un párrafo de contraste con la
   terminología del Libro de estilo (9.7.3 «Minusválidos»; 9.7.3.1 «denominaciones más dúctiles»;
   «disminuidos sensoriales»; voz «discapacitado» del vocabulario), cotejado en el txt del Libro.
3. **Lenguaje claro (P15 «a medias»)**. Fuente publicada hallada: el propio Libro de estilo de
   2004 («Lenguaje y periodismo · La sencillez es la clave», «Normas básicas»: frases cortas y
   construcción lógica; 7.2.1 «Divulgación y sencillez»). Se añade en §4 como pauta de estilo de
   la casa, no como norma. Lectura fácil sigue sin desarrollar (declarado).
4. **Normas UNE (P10 «no»)**. Leídas las fichas de catálogo de AENOR (tienda.aenor.com,
   24-09-2026): UNE 153010:2012 «Subtitulado para personas sordas y personas con discapacidad
   auditiva», edición 30-05-2012, anula la UNE 153010:2003, en vigor; UNE 153020:2005
   «Audiodescripción para personas con discapacidad visual. Requisitos para la audiodescripción y
   elaboración de audioguías», edición 26-01-2005, en vigor. La ficha de une.org devolvió 403.
   Comprobado en el BOE que el art. 101.1.d) LGCA no nombra ninguna norma concreta. El contenido
   técnico de las normas no se ha leído y así se declara. Con esto la clave de la P10 (a) queda
   confirmada.

## Pasajes cambiados

- Siglas: añadidas UNE y AENOR.
- «Qué se puede preguntar»: tres preguntas más (franja +18, reforma del art. 49 CE, norma UNE).
- §2 «La Carta del Servicio Público 2024-2029»: nuevo bloque tras el 9.1 con LAA 45.3-45.4 y LGCA
  DA 3.ª.
- §4 «Lenguaje claro»: nuevo bloque con las pautas del Libro de estilo.
- §6: introducción retocada («la ley propia de la RTVA y los compromisos de Canal Sur»); nuevo
  subepígrafe «### La Ley 18/2007» (art. 29, DA 2.ª y DT 3.ª, copiado del tema 5 del común y
  cotejado art. 29 y DA 2.ª en el BOE); punto 93 con su fundamento literal; párrafo final sobre
  normas UNE con tabla.
- §7: nuevos «Artículos 97 y 98», «Artículo 99», «Artículo 100» (copiados del común).
- §8: cadena del art. 49 CE; párrafo sobre la terminología del Libro.
- «Normativa que el tema invoca», «Lo que este tema no da» y «Trazabilidad»: actualizadas.
- Portada: extensión 12.644; índice regenerado con `indice.py`.

Releídos todos: cada «ese artículo 9.1», «el mismo epígrafe», «punto 93, abajo», «artículo 98.2»
tiene su antecedente.

## Lentes (diferencia antes/después)

- `indice.py`: 33 epígrafes, 12.644 palabras.
- `negritas.py`: nuevas «no está» = rótulos en negrita del bloque copiado del común (98.1, 99.1,
  «Las tres franjas horarias:»…; estilo del común), la redacción de 1978 del art. 49 CE (el volcado
  sólo trae la vigente; leída con `--fecha`) y «eficaz» del Libro (el txt tiene la ligadura «eﬁ»).
  Falsos positivos.
- `refutar_exactitud.py`: nuevas diferencias por atribución a artículos de otras fuentes (citas del
  Contrato-programa, del Libro y de la CE de 1978); falsos positivos por mezcla de fuentes.
- `refutar_modo.py`: 5 hallazgos; los nuevos (97-98 de otra norma, salvedad de loterías del 99.6)
  son cruces de numeración o ya están recogidos en el texto copiado.
- `refutar_prosa.py`: la sigla UNE sin presentar quedó corregida; queda 1 hallazgo anterior
  (repetición de «la Ley 9/2018… dio la redacción actual»), no tocado.

## Si el encargo no cuadra con la fuente

Nada que señalar. Nota: los rótulos en negrita del bloque copiado del común no son literales de la
norma (choca con «negrita = literal»); se dejan tal cual por la regla de copiar el común literal.

Ficheros tocados: el tema 17 y este informe.
