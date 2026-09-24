# 34 · T01 · Refutación (fase 4)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/01-derecho-informacion-libertad-expresion.md`.
No corrijo: el remate aplica. Saltado por «Copiado del común» (34-T01-redaccion.md): CE arts. 18.1, 20 con glosa, 24.2, 53.2; LO 2/1997 arts. 1, 2.1, 2.2, 3.

## Fuentes releídas (todas el 24-09-2026)

- LO 1/1982, `fuentes/canal-sur/BOE-A-1982-11196.md` (+ `.redacciones.tsv`) y XML de la API de legislación consolidada del BOE, bloque `asegundo` (marcado `<strong>` del inciso anulado).
- LO 2/1984, `BOE-A-1984-7248.md`; LO 2/1997, `BOE-A-1997-13374.md` (solo estructura).
- STC 27/2020, `fuentes/internet/BOE-A-2020-4112_STC-27-2020.txt` (cabecera, antecedente 2, fallo).
- Libro de estilo, `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 2.3.2.9-2.3.2.13, 4.3.6.
- Reglamento (UE) 2024/1083, `DOUE-L-2024-80523.md`: arts. 4 y 29.
- Tema 10 del común (remisión sobre la STC 9/1990) y temas 04 y 14 de este temario (grep).

## Lentes

`negritas.py` (9 fuentes): 102 cotejadas, 0 no encontradas, 4 «mal atribuidas» falsas (ya explicadas en verificación). `refutar_modo.py`: 0. `refutar_prosa.py`: 0. Nota: `negritas.py` no detecta el hallazgo grave porque el texto anulado sigue en el volcado.

## Hallazgos graves (1)

**G1 · Art. 2.2 LO 1/1982: inciso anulado dado como vigente (err. 7 y 6).** El XML del BOE (bloque `asegundo`) marca en negrita, como «inciso destacado» anulado por la STC 9/1990, desde «o, por imperativo del artículo 71 de la Constitución, cuando se trate de opiniones manifestadas por Diputados o Senadores en el ejercicio de sus funciones. Iniciado un proceso civil… sin la previa autorización del Congreso de los Diputados o del Senado» hasta «La previa autorización será tramitada por el procedimiento previsto para los suplicatorios.» El tema:
- en §3 «Disposiciones generales», cita ese texto en negrita como parte del apartado vigente («El apartado sigue: …») y a continuación dice que «un inciso» fue anulado sin decir cuál;
- en §3 «Estructura», dice que la LO 3/1985 «le añadió la mención de los Diputados y Senadores», sin decir que está anulada;
- en «Lo que este tema no da» declara como hueco («el texto consolidado no lo marca») algo que la fuente sí marca, y que el tema 10 del común ya da;
- en la ficha y en «Trazabilidad», el art. 2 va «en la redacción de la LO 3/1985». La redacción vigente es la de 15-02-1990 (BOE-A-1990-3964), de las tres que tiene el precepto;
- en «Normativa que el tema invoca», el art. 71 CE solo se cita a través del texto anulado.
Corrección que propongo: el art. 2.2 vigente se limita a la autorización por ley y al consentimiento expreso; decir qué inciso se anuló (con la marca del BOE como fuente) y quitar el hueco. La pregunta 3 falla por esto.

## Hallazgos menores (4)

- **M1 · STC 27/2020, número del BOE (err. 9).** La ficha y la «Trazabilidad» dicen «BOE núm. 84, de 26-III-2020»; la cabecera de las 18 páginas del BOE dice «Núm. 83, Jueves 26 de marzo de 2020». (La línea que se añadió a mano al principio del `.txt` también dice 84: es de ahí de donde sale.)
- **M2 · STC 27/2020, hechos (err. 6).** Dice que el diario ilustró el reportaje «con la fotografía del herido». Según el antecedente 2.b, publicó «sendas fotografías del demandante don I.I.L. y de su hermano», las dos sacadas de Facebook. El pleito versó sobre la del demandante; basta con precisarlo.
- **M3 · Art. 4 LO 1/1982 (err. 6).** En el 4.4 (víctimas del 7.8) falta la última frase: «**En los supuestos de fallecimiento, se estará a lo dispuesto en los apartados anteriores.**» En el 4.3 falta que el plazo de ochenta años se aplica también a la persona jurídica designada en el testamento.
- **M4 · Remisión que falta.** El Libro de estilo 2.3.2.13 remite a «4.3 FUENTES Y 4.3.6 OFF THE RECORD». El tema 04 de este temario trata el *off the record*, pero «Lo que este tema no da» no remite a él.

## Lagunas de cobertura (4)

- **L1 · Secreto profesional: art. 4.3-4.5 del Reglamento (UE) 2024/1083.** Es la única norma volcada que desarrolla la protección de las fuentes, y el enunciado pide «secreto profesional». El tema da solo la primera frase del 4.3. Faltan las tres medidas prohibidas (obligar a revelar; detener, sancionar, inspeccionar o vigilar; programas espía), las condiciones de la excepción del 4.4 (previsión legal, art. 52.1 de la Carta, razón imperiosa de interés general caso por caso, autorización judicial o de autoridad independiente, previa o posterior sin demora) y el 4.8 (tutela judicial). El tema 14 da los arts. 2, 6, 18 y 29, pero no el 4. Aplicación: el 4.3 rige desde el 8-8-2025 (art. 29). Pregunta 12.
- **L2 · Independencia editorial: art. 4.2 del mismo Reglamento.** El enunciado pide «independencia editorial», y el 4.2 obliga a los Estados a respetar la «libertad e independencia editorial efectivas» de los prestadores y a no interferir en sus decisiones editoriales (aplicable desde el 8-2-2025, art. 29.b). El tema solo da el Libro de estilo 1.9.
- **L3 · LO 2/1984, arts. 5 y 6 incompletos.** Falta el art. 5, párr. 3: si el juez se declara incompetente, hay siete días hábiles para acudir al órgano competente. Falta también el art. 6: a) el juez puede reclamar de oficio la información, b) solo se admiten pruebas que puedan practicarse en el acto, la condena en costas a quien vea rechazadas del todo sus pretensiones y que la sentencia estimatoria «deberá cumplirse en sus propios términos». Pregunta 11.
- **L4 · Libro de estilo 2.3.2.11 incompleto.** Faltan «Cualquier intento de acoso posterior queda descartado» y que la restricción es «particularmente severa» con enfermos, víctimas de accidentes, pacientes de hospitales, consultas médicas y personas acogidas en instituciones sociales. Es materia de práctica. Pregunta 15.

## Confirmado sin hallazgo

Arts. 1, 3, 5, 6, 7, 8 y 9 LO 1/1982 (literales y cifras). LO 2/1984, arts. 1-4, 7 y 8, y la corrección de errores del BOE núm. 90. Estructura de la LO 2/1984 (ocho artículos y una derogatoria). Hechos, tribunales y citas de la STC 27/2020 (Sala Segunda, TS 91/2017, fallo desestimatorio). Libro de estilo 2.3.2.10, 2.3.2.13 y páginas. Art. 29 del Reglamento (UE) 2024/1083: el 4.3 es aplicable desde el 8-8-2025.

## Preguntas

`34-T01-preguntas.md`: de 15, 11 enteras, 2 a medias (12 y 15) y 2 no (la 3, por G1; la 11, por L3).

Ficheros tocados: este informe y `34-T01-preguntas.md`.
