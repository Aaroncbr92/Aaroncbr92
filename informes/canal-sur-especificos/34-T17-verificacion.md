# 34 · T17 · Verificación (fase 3)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/17-accesibilidad-igualdad-diversidad.md`.
Fuentes leídas hoy (24-09-2026): BOE-A-2007-6115 (LO 3/2007), BOE-A-2008-2492 (Ley 12/2007, arts. 3, 58 vigente y original), BOE-A-2018-15240 (LAA), BOE-A-2022-11311 (LGCA), BOE-A-2022-11589 (Ley 15/2022), BOE-A-2023-5366 (Ley 4/2023), BOE-A-1978-31229 (CE 49); Carta 2024-2029 (BOJA 247/2023), Contrato-programa 2024-2026 (BOJA 245/2023), Libro de estilo 2004 (txt), Guía de Igualdad RTVE 2020 (txt y tabla del PDF con pymupdf).

Saltado por «Copiado del común» (según `34-T17-redaccion.md`): arts. 4, 6, 7 LGCA; §3 entero; Ley 12/2007 arts. 57-58, «Lo que se aplica», art. 9, art. 3.3; §7 arts. 95-96 y LAA 8, 31.1. Sólo se revisaron en ellos las remisiones internas.

## Confirmado sin cambios

LO 3/2007: título III, arts. 14.11, 36, 37 (dos redacciones, sólo RTVE), 39, 40; «redacción original» exacta para 14, 36 y 39. LGCA título I, 101.3, 101.1.d, 102.2. Ley 12/2007 3.8, 58.1-58.4 y la reforma de 2018. LAA 2.1.l, 9.4. Ley 15/2022 5.5. Carta 8.1 (letras citadas), 9.1, 13.9, 25.1. CP 12, 56, 57, 59, 64-66, 90-94 (RD 1112/2018, de 7 de septiembre). Libro de estilo 9.7.3, 9.7.3.1, 11.1.4-11.1.6 (1.ª ed., marzo 2004). Remisiones a los temas 11, 16 y 4/8 del común.

## Corregido

1. **Error 6 (salvedad omitida), Libro de estilo 11.1.6**: la nota 6 admite el desdoblamiento «sólo en el hipotético caso de que existiese ambigüedad». Añadida; se quita «rechazo absoluto». Se añade también la nota 4 (11.1.4).
2. **Error 6, §6**: la cifra andaluza (100 %, 15 h diarias) se daba como vigente. Ahora se dice que la DT 1.ª la refiere al art. 9 LAA, sin cifras desde 2024. La cita «y todas las informativas» no era literal y se quita.
3. **Error 1 (cita cruzada)**: «(se estudia en el punto 5)» → «tema 5 del común»; «las tres leyes del tema» → «las leyes de igualdad de este epígrafe» (en el tema hay cuatro; ninguna nombra a la RTVA, comprobado).
4. **Error 9, Guía RTVE**: quitados «no hay que forzar la lengua, porque la lengua ya da recursos» (no está en la Guía) y «en algunos casos» añadido a «es incorrecto gramaticalmente». Terminaciones -l/-z: la Guía dice que «suelen funcionar como comunes», y jueza, concejala y aprendiza son excepciones (el tema decía que admiten femenino). Los duales aparentes no «cierran el documento»: están en el 5.4. Se completa la lista con ayudanta/ayudante y bruja/brujo.
5. **Negrita no literal (Guía)**: corregidas unas 20 negritas (regla de inversión, género no marcado, economía lingüística, tabla de recursos, desdoblamientos, Nueva Gramática, profesiones, construcciones sexistas, arroba, LGTB). Pasan a redonda las que eran paráfrasis. La glosa de la sigla LGTB, que la Guía no da, sale de la negrita.
6. **Error 5**: FUNDÉU sin presentar → «Fundación del Español Urgente (FUNDÉU)».
7. **Error 8**: CE «artículo 49» → 49.1 (la cita es sólo del apartado 1).
8. **Error 3**: la «Normativa que el tema invoca» no recogía artículos citados en el cuerpo (LGCA 10.4, 15.4, 33.2, 83, 97-100, 123, 124, 129, 131, 138, DF 9.ª; LAA 19.1.b, 66.3.c, DA 3.ª; Ley 12/2007 66, 76, 77, 83, 85; normas por remisión). Completada. Extensión 10.510 → 10.690 (`indice.py`). Trazabilidad: Guía con la fecha de lectura y Libro con las notas.

Pasajes cambiados releídos: cada «son necesarios», «la Guía» o «el artículo 9» tiene delante su antecedente (en «son necesarios» se añade «los desdoblamientos»).

## Lentes

- `negritas.py`: 333 cotejadas, 38 «no están». Las que quedan son rótulos, versiones históricas de los pasajes del común o tablas de la Guía que el txt desordena; estas últimas se comprobaron en el PDF.
- `refutar_exactitud.py`: 32 citas no literales. Son falsos positivos: citas de la Carta y del Contrato-programa (no son BOE) o pasajes del común.
- `refutar_modo.py`: 3 hallazgos, falsos, porque el número de artículo coincide entre normas distintas.
- `refutar_prosa.py`: 1 hallazgo, la frase repetida dentro del común. Se deja.
- `indice.py`: índice regenerado.

## Sin resolver

- La tabla de la DT 1.ª LAA no sale en el volcado del BOE (es una imagen). Viene del común y no se ha reverificado.

Ficheros tocados: el tema y este informe.
