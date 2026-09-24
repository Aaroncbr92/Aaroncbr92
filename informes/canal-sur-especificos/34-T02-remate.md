# 34 · T02 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/02-mision-informativa-radiotelevision-publica-autonomica.md`.
Base: `34-T02-refutacion.md` (0 graves, 3 menores, 4 lagunas) y `34-T02-preguntas.md` (10/2/3).
**Ha ampliado contenido nuevo**: toca la fase 5 bis sobre los pasajes 4 a 9.

## Fuentes releídas (todas el 24-09-2026)

- Ley 18/2007, `fuentes/canal-sur/BOE-A-2008-1185.md`: arts. 10, 31, 32, 33 (redacción única, en vigor desde el 15-01-2008) y rúbricas de las secciones 2.ª y 3.ª del capítulo VI.
- Ley 13/2022, `BOE-A-2022-11311.md`: arts. 5, 16 y 76 (redacción única, en vigor desde el 09-07-2022).
- Ley 10/2018, `BOE-A-2018-15240.md`: art. 2.1.c) (redacción única).
- Carta 2024-2029, `fuentes/canal-sur/documentos/carta-servicio-publico-2024-2029-boja-247-2023.txt`: art. 13 entero (`documento.py seccion`), exposición de motivos (línea 188), búsqueda de «modific».
- Tema 12 del específico (sólo para comprobar a qué remite M2).

## Correcciones: todas comprobadas y aplicadas

- **M1**: acertada. La Carta volcada no dice nada de modificaciones, así que no se puede afirmar que no se haya modificado. Cambiado por «sin que conste modificación publicada».
- **M2**: acertada. El tema 12 da los arts. 32 y 33 y la Carta 13.3 y 13.10. Ajustado el texto de la remisión.
- **M3**: acertada. Se reescribe la viñeta. De paso, la remisión interna corregida («La misión en la Carta») es donde se cita de verdad la exposición de motivos.
- **L1 a L4**: cada cita, cotejada con la fuente antes de escribirla. Ninguna corrección del informe estaba equivocada.

## Pasajes cambiados

1. Portada, «Redacción que se estudia» (M1) y «Extensión»: de 8.300 a 9.700 palabras (`indice.py`: 9.674).
2. «Qué se puede preguntar»: se añaden los arts. 16.2 y 76.2 LGCA, los arts. 32 y 33 de la Ley 18/2007 y la Carta 13.9.
3. Ley 18/2007, párrafo de entrada: «artículos 1 a 4, 10 y 31 a 33». Índice: entrada nueva.
4. **Nuevo** `### Estatuto profesional, pluralismo y acceso (artículos 10 y 31 a 33)` (L1): 10.1-10.2, 31, 32, 33.1-33.2.
5. Carta, «La información, núcleo de la misión» (L1, L2): viñetas nuevas 13.3 (entero), 13.5, 13.6, 13.9, 13.10 y 13.11, más una remisión a los apartados 8, 12 y 13.
6. Neutralidad: la viñeta de la Ley 18/2007 añade el 10.1. Se reescribe la viñeta de la Carta (M3).
7. Diversidad social (L1, L4): Ley 18/2007, arts. 32 y 33.1; Ley 13/2022, art. 5.1-5.2 (dice «se promoverá»: es un mandato de promoción, no una obligación directa); Ley 10/2018, art. 2.1.c).
8. Responsabilidad editorial (L3): párrafo nuevo sobre los arts. 16.1-16.2 y 76.1-76.2.
9. «Normativa que el tema invoca» y «Trazabilidad»: se añaden los arts. 10 y 31 a 33 (Ley 18/2007), 5, 16 y 76 (Ley 13/2022) y 2.1.c) (Ley 10/2018). «Lo que este tema no da» recoge la remisión M2.

Antecedentes releídos: «ambos en el epígrafe de la Ley 18/2007» (antes decía «de la ley», que era ambiguo); el «su Consejo Profesional» de 13.10 ya tiene delante «Canal Sur». Los demás «dicha/esa» tienen su antecedente en la misma viñeta.

## Lentes

- `indice.py`: índice regenerado, 32 epígrafes.
- `refutar_prosa.py`: 0.
- `negritas.py` (tres leyes y Carta): 288 cotejadas. Todas las negritas nuevas están en la fuente. Salen dos avisos nuevos de atribución y los dos son falsos: «la pluralidad social…» está citada como art. 32 y el aviso la ancla al 33 de la frase siguiente; en el 16.2, el aviso la ancla al 76 que viene después. Los demás avisos son los de antes, ya explicados en la verificación.
- `refutar_exactitud.py`: da esos mismos dos anclajes falsos.
- `refutar_modo.py`: 1, el falso positivo de siempre (art. 9 de la Ley 10/2018 contra el 9 de la Ley 13/2022).

## Preguntas

Con el tema rematado, las 15 se pueden contestar enteras: la 10 (L3), la 11 y la 15 (art. 32, art. 33 y Carta 13.11), la 12 (13.9) y la 14 (13.3 entero).

Ficheros tocados: el tema 02 y este informe. En el árbol hay además cambios en los temas 01 y 13 que no son de este remate.
