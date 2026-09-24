# 34 · T12 · Refutación (fase 4)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/12-informacion-politica-institucional-electoral.md`.
No corrijo: el remate aplica. Saltado por «Copiado del común» (34-T12-redaccion.md): epígrafe 1 salvo el
art. 66 LOREG (Ley 18/2007 arts. 4.1, 4.3.b, 32, 33; Carta 13.3, 13.10, 13.11; Ley 13/2022 arts. 51 y 56.2);
viñetas del art. 31 Ley 18/2007 y de la Carta 13.5/13.6 (epígrafe 3); cita del art. 30 Ley 18/2007 (epígrafe 4).

## Fuentes releídas (todas el 24-09-2026)

- LOREG, `fuentes/canal-sur/BOE-A-1985-11672.md`: arts. 50-53, 60-69 y disposición adicional primera
  (redacción aplicable desde 30-01-2011). (`boe.py precepto` devolvió 404 del BOE; se leyó el volcado del día.)
- LEA, `BOE-A-1986-2788.md`: título V, capítulos I a IV (arts. 20-30).
- Instrucción JEC 1/2015 con el texto consolidado de la 4/2011, `documentos/jec-instruccion-1-2015-BOE-A-2015-4280.txt`: apartados primero a noveno.
- Libro de estilo, `documentos/libro-de-estilo-333233b.txt`: 7.1 a 7.1.5.
- Ley 18/2007 (`BOE-A-2008-1185.md`): art. 4.3.n y búsqueda de «electoral».
- Ley 13/2022 (`BOE-A-2022-11311.md`): arts. 5, 9, 125; Ley 10/2018 (`BOE-A-2018-15240.md`): arts. 2, 7, 37; Ley 1/2004 del Consejo Audiovisual (`BOE-A-2005-655.md`): art. 4 (sin nada electoral).
- Carta 2024-2029 y Contrato-programa 2024-2026 (`documentos/*boja-247-2023.txt`, `*boja-245-2023.txt`): búsqueda de «electoral».

## Lentes

`refutar_prosa.py`: 0. `refutar_modo.py` (LOREG, LEA): 0. `negritas.py` y `refutar_exactitud.py` ya corridas en verificación, sin cambios desde entonces.

## Hallazgos graves (1)

**G1 · Art. 51 LOREG dado sin la salvedad de las autonómicas (err. 6).** El epígrafe 4 («Período electoral y
campaña») dice que la campaña «comienza el día trigésimo octavo posterior a la convocatoria» (51.1) como regla
general, y la «Qué se puede preguntar» incluye «cuándo empieza y acaba la campaña». Pero la disposición adicional
primera.2 LOREG sólo aplica a las elecciones autonómicas los apartados **2 y 3** del art. 51 (y 50.1-3, no 50.4-5;
no el 64 ni el 67); el resto es supletorio (DA 1.ª.3). Para el Parlamento de Andalucía, **«El Decreto de
convocatoria fijará la fecha de iniciación de la campaña electoral y el día de la votación»** (art. 27.1 LEA).
Para el redactor de Canal Sur las autonómicas son el caso principal. Propuesta: añadir la salvedad con la DA 1.ª.2
y el art. 27.1 LEA; decir también que en autonómicas el baremo del 64 cede ante el art. 29 LEA (el tema ya los
separa, pero sin explicar por qué). Pregunta 10.

## Hallazgos menores (2)

- **M1 · Instrucción 4/2011, quinto.1 (err. 9, leve).** El tema dice que la Junta pone el plan «a disposición de
  los representantes de las candidaturas»; la fuente: «representantes generales o de las candidaturas
  acreditados». Igual legitimación en sexto.2.
- **M2 · Art. 64 LOREG incompleto frente a la LEA.** Se da el 29.3 LEA (agrupaciones federadas, cinco minutos),
  pero no su paralelo 64.4 LOREG (agrupaciones federadas, diez minutos, si cumplen el 64.2) ni el 64.3 (quince
  minutos en la programación general de medios nacionales con el 20 % en una Comunidad). Menor: el 64 no rige en
  autonómicas.

## Lagunas de cobertura (4)

- **L1 · Régimen aplicable a las autonómicas y campaña institucional andaluza.** Falta la DA 1.ª.2-3 LOREG (qué
  artículos de campaña rigen en las autonómicas) y el art. 27.2 LEA: **«Durante la campaña electoral el Consejo de
  Gobierno podrá realizar campaña institucional orientada exclusivamente a fomentar la participación de los
  electores en la votación.»** Tampoco el art. 26 LEA (definición de campaña, paralela al 50.4). Pregunta 15.
- **L2 · «Normativa audiovisual» escasa.** El enunciado pide las obligaciones derivadas de ella, y el tema sólo
  da los arts. 51 y 56.2 de la Ley 13/2022 (copiados del común). Falta el art. 9.1 Ley 13/2022 (informativos:
  veracidad, objetividad, imparcialidad, **«diferenciando de forma clara y comprensible entre información y
  opinión, respetando el pluralismo político, social y cultural»**), que es la obligación de todo el año para la
  información política; el art. 125.f (la propaganda electoral se rige por su normativa específica); y la Ley
  10/2018, arts. 2.1.c (pluralismo político como principio) y 7 (derecho a una comunicación audiovisual plural).
  Basta con una viñeta y la fila en la tabla del epígrafe 7; el art. 9 se desarrolla en el tema 2 y en el
  tema 4 del común, pero «Lo que este tema no da» no lo nombra. Pregunta 13.
- **L3 · Criterios de servicio público: Contrato-programa 2024-2026 (BOJA 245/2023), cláusula tercera, 3.1.**
  Punto 6: la oferta generalista incluirá espacios informativos **«electorales cuando concurran comicios de
  cualquier ámbito territorial»**; punto 8: coberturas informativas especiales de **«las sesiones más
  significativas de la actividad del Parlamento de Andalucía, así como de otras instituciones democráticas»**.
  Es el mandato concreto para «cobertura de instituciones» y «campañas electorales»; el tema no cita el
  Contrato-programa.
- **L4 · Alzada ante la JEC e inadmisión.** Instrucción 4/2011, quinto.3 y sexto.11: las resoluciones de las
  Juntas Provinciales y de Comunidad Autónoma son recurribles ante la JEC (art. 21 LOREG e Instrucción 11/2007),
  salvo que en autonómicas los recursos contra las Provinciales los conoce la Junta de Comunidad Autónoma.
  Sexto.9: inadmisión de oficio del recurso que no guarde relación con los principios del 66. Pregunta 14.

## Confirmado sin hallazgo

LOREG 50.1-5, 51, 53, 60, 61, 62, 63.3, 64.1-2, 65.6 (con «solamente»), 66.1-2, 68, 69 (1, 2, 4, 7, 8), con sus
redacciones. LEA 28, 29.1-3, 30 y rúbrica del capítulo IV. Instrucción 4/2011: primero, segundo, tercero, cuarto.1,
2.1-2.4, cuarto.3, quinto.2 y 4, sexto.1-6. Libro de estilo 7.1-7.1.5: todas las citas literales. Ley 18/2007,
art. 4.3.n; ni ella ni la LEA ni la Carta contienen obligación de programar debates.

## Preguntas

`34-T12-preguntas.md`: de 15, 11 enteras, 1 a medias (15) y 3 no (10 por G1; 13 por L2; 14 por L4).

## Discrepancias con el encargo

Ninguna. `boe.py precepto` falló (404 del BOE); se usó el volcado local del mismo día.

Ficheros tocados: este informe y `34-T12-preguntas.md`.
