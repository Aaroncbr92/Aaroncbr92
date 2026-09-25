# Puesto 08 · Tema 14 · Fase 5 · Remate

Tema: `temas/canal-sur-especificos/08-camara-operador/14-prevencion-riesgos-exteriores-conduccion-cargas-clima.md`.
Fecha de trabajo y de lectura de todas las fuentes: **24-09-2026** (sesión fechada el 25-09 en el sistema;
se trabaja con la fecha del encargo). Parte de `08-T14-refutacion.md` y `08-T14-preguntas.md`.

## Fuentes releídas antes de aplicar (24-09-2026)

- ET (BOE-A-2015-11430), `boe.py precepto a36`: redacción única, vigente desde el 13-11-2015. Confirma L1.
- RGC (BOE-A-2003-23514), `boe.py --fecha 20261001 precepto a18` y `a118`: la nota del BOE dice
  «esta actualización de los apartados 2 y 3, establecida por el art. único.2 del Real Decreto
  518/2026»; el 118, por el art. único.18. Confirma hallazgo 2.
- RD 486/1997 (BOE-A-1997-8669), `boe.py precepto aniii`, redacción de 2023: apartado 3 con letras
  c) y d) y apartado 4 con la salvedad. Confirma hallazgo 4.
- Convenio Interior-FAPE-ANIGP-TV (BOE-A-2021-962, texto en `fuentes/canal-sur/documentos/`):
  cláusula segunda, 5; tercera (Ministerio), 1 y 2; octava, 1 y 2. Confirma hallazgos 1 y 3 y la laguna L2.

Las cuatro correcciones y las dos lagunas eran ciertas: ninguna se ha dejado sin aplicar.

## Pasajes cambiados

| # | Origen | Epígrafe | Cambio |
|---|---|---|---|
| 1 | Hallazgo 1 (preg. 14) | «El chaleco de prensa», viñeta «Lo que sí permite pedir» | Se cita el apartado 1 de la cláusula tercera (departamentos institucionales de comunicación de las FCSE) y el apartado 2 con su arranque literal **«En ausencia de la representación de aquellas, …»**. «aquellas» tiene ya su antecedente en la frase anterior |
| 2 | Hallazgo 2 (preg. 7) | «Lo que exige el RGC», «Lo que cambia el 1 de octubre de 2026» | «a los artículos 18.2 y 118» → «a los apartados 2 y 3 del artículo 18 (el 3, sobre inhibidores y detectores de radares, queda fuera de este tema) y al artículo 118» |
| 3 | Hallazgo 3 | «El chaleco de prensa», viñeta «Vigencia», y «Lo que este tema no da» | Unificadas: eficacia tras inscripción en el Registro Electrónico Estatal de Órganos e Instrumentos de Cooperación y publicación (BOE 22-01-2021); cuatro años; el plazo inicial vence no antes de enero de 2025; la prórroga no se ha comprobado. No se afirma una fecha exacta de vencimiento porque la de inscripción no consta en el texto |
| 4 | Hallazgo 4 | «El anexo III: temperaturas sólo para locales cerrados» | Cita del apartado 3 cerrada con «[…]» y aviso de las letras c) y d); «obligan» → «rigen … con la salvedad del apartado 4», con el literal de ese apartado |
| 5 | Laguna L1 (preg. 12) | «Qué es trabajo nocturno» | Añadida al literal del 36.1 la frase **«El empresario que recurra regularmente a la realización de trabajo nocturno deberá informar de ello a la autoridad laboral.»** |
| 6 | Laguna L2 | «El chaleco de prensa» | Viñeta nueva «En actos imprevistos (cláusula segunda, 5)»: uso conjunto chaleco-credencial y literal de la excepción (credencial sin chaleco, colgada al cuello y visible) |
| 7 | Consecuencia | «Normativa que el tema invoca» | RD 486/1997: anexo III, apartados 2, 3, **4** y 5. Convenio: segunda (…, **5**, …), tercera (Ministerio, **1** y 2) |
| 8 | Consecuencia | Portada | Extensión 13.400 → 13.700 palabras (medida: 13.7xx) |

Relectura de antecedentes: «aquellas» (cláusula tercera) → FCSE, citadas en la frase anterior;
«el 3» → apartado 3 del artículo 18, nombrado en la misma frase; «el apartado 4» y «el apartado 3» →
anexo III, nombrado en el párrafo. Sin remisiones huérfanas.

## Preguntas tras el remate

Las 15 se contestan ya enteras con el tema (7, 12 y 14 pasan de «no» a «entera»). Ninguna pregunta
se ha recortado.

## Herramientas

- `indice.py` sobre el tema: 46 epígrafes, sin epígrafes nuevos; índice regenerado (la portada es
  manual, el script no la toca).
- `negritas.py` contra ET, RD 486, RD 487, RD 1215, RD 773, LPRL y el convenio FAPE: todas las
  negritas nuevas se encuentran literales. Las «NO ESTÁ» restantes son de fuentes no pasadas (X
  Convenio, Libro de estilo, guía MMC) y ya estaban.
- `refutar_exactitud.py` (ET, RD 486): salida idéntica a la del tema antes del remate; nada nuevo.
- `refutar_modo.py` (ET, RD 486): 0 hallazgos.
- `refutar_prosa.py`: 0 hallazgos.

## Ampliación

**Sí**: contenido nuevo (pasajes 1, 4, 5 y 6, con literales nuevos). Procede la fase 5 bis, limitada
a esos pasajes.

## Otros ficheros tocados

Ninguno fuera del tema y de este informe.
