# T08 · Remate (fase 5) · Normativa sobre igualdad

Aplica `informes/canal-sur-comun/T08-refutacion.md` (modo ahorro) sobre
`temas/canal-sur-comun/08-igualdad.md`. Único hallazgo comprobado en la fuente el
24-09-2026 antes de aplicarlo: `fuentes/canal-sur/BOE-A-2024-20402.md`, artículo 5.
Ficheros tocados: el tema y este informe.

## Corrección aplicada

**Hallazgo 1 (exactitud, menor) — confirmado y aplicado.**

- Dónde: bloque de la Ley 4/2023, «Medidas por ámbitos», desarrollo reglamentario del
  Real Decreto 1026/2024, viñeta del artículo 5.
- Decía: «si en tres meses desde el inicio no hay acuerdo, se aplican las medidas del
  real decreto (artículo 5)», sin más.
- Comprobado en `fuentes/canal-sur/BOE-A-2024-20402.md` (`grep -n -A40 "^Artículo 5"`):
  el artículo 5.1, párrafo segundo, dice **«Para aquellas empresas que, al momento de
  la entrada en vigor de este real decreto, no estuviesen incluidas en su ámbito de
  aplicación, el plazo anterior empezará a contarse desde el momento en que alcancen
  el número de personas trabajadoras indicado en el artículo 2»**; el 5.3 añade un
  segundo supuesto de aplicación supletoria, **«o en el supuesto de que el convenio
  colectivo de aplicación no incluya las medidas planificadas»**, y que esas medidas
  **«se continuarán aplicando hasta que entren en vigor las que posteriormente se
  puedan acordar»**.
- Dice ahora: el tema amplía la viñeta con las tres piezas comprobadas (el cómputo
  diferido del 5.1 para empresas que se incorporan después, el segundo supuesto del
  5.3 y la vigencia de las medidas supletorias hasta el nuevo acuerdo), cada una en
  cita literal con su apartado.
- Precepto: RD 1026/2024, artículo 5 (`BOE-A-2024-20402`), redacción única, vigente
  desde el 10/10/2024, leída el 24-09-2026.

No hay más hallazgos que aplicar: cobertura y prosa dieron 0 en la refutación.

## Pasajes cambiados

Un único pasaje, hacia el final del tema (bloque «Ley 4/2023 · Medidas por ámbitos»,
viñeta del artículo 5 del RD 1026/2024): la viñeta que empieza «La comisión
negociadora se constituye…» pasó de una frase a un párrafo con tres citas literales
más (5.1 párrafo segundo, 5.3 primer supuesto ampliado y la vigencia supletoria de
las medidas). Antecedentes de alrededor releídos: siguen apuntando bien («este real
decreto» = RD 1026/2024, citado dos frases antes; «el número de personas trabajadoras
indicado en el artículo 2» remite al artículo 2 del mismo real decreto, citado en la
viñeta anterior). No se ha tocado ninguna otra parte del tema.

Es corrección puntual de un pasaje (no amplía contenido nuevo del enunciado, sólo
completa una remisión reglamentaria ya citada), así que, según el modo ahorro
(`CICLO.md`, «Fase 5 bis recortada»), no hace falta un agente nuevo de comprobación
final: basta con que el coordinador revise lo que marquen las lentes automáticas
sobre el tema rematado.

## Lentes automáticas

```
python3 herramientas/indice.py temas/canal-sur-comun/08-igualdad.md
→ 21.325 palabras · 31 epígrafes (antes: 21.254). Extensión de la ficha actualizada.

python3 herramientas/refutar_prosa.py temas/canal-sur-comun/08-igualdad.md
→ 2 hallazgos, los mismos de la verificación/refutación: la fórmula «la Ley 9/2018…
  dio la redacción actual» repetida ×5 (distintos artículos, no relleno) y «LGBTI»
  dentro de una cita literal del Consejo Andaluz LGBTI (sigla de la fuente, no del
  tema). No afectan al pasaje tocado.

python3 herramientas/negritas.py temas/canal-sur-comun/08-igualdad.md \
  fuentes/canal-sur/BOE-A-2008-2492.md fuentes/canal-sur/BOE-A-2022-11589.md \
  fuentes/canal-sur/BOE-A-2023-5366.md fuentes/canal-sur/BOE-A-2026-16172.md \
  fuentes/canal-sur/BOE-A-2024-20402.md fuentes/canal-sur/BOE-A-2008-1185.md \
  fuentes/canal-sur/BOE-A-2005-655.md
→ 426 negritas cotejadas (antes 423; +3 por las citas nuevas del artículo 5, las tres
  literales y sin marcar). 7 «no están» y 38 «¿art.?», los mismos falsos positivos ya
  explicados en la verificación y en T08-refutacion.md (anclas en números de otras
  leyes cercanos al marcador). Entre ellos sigue el de la viñeta del artículo 5 («¿ART.
  3? … → está en art. 5»), preexistente al remate: la cita «dentro del plazo máximo de
  los tres meses…» ancla en el «3» de «tres meses» en vez del artículo 5 nombrado al
  final de la viñeta; revisada, está en el artículo 5 que dice el tema.
```

## Extensión

21.325 palabras (cifra de `indice.py`), frente a las 21.254 de la ficha anterior.
