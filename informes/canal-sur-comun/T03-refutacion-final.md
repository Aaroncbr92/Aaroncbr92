# T03 · Refutación final (fase 5 bis, modo ahorro acotado)

Tema: `temas/canal-sur-comun/03-union-europea.md`. Leídos: `ENCARGO.md`, `CICLO.md` (avisos y
modos ahorro), `T03-remate.md`, `T03-preguntas.md`.

## 1. Pasajes que cambió el remate

Los tres releídos con su antecedente: 48.7 (Título VI), Protocolo n.º 2 art. 7 (control de
subsidiariedad) y las cinco «en la rúbrica "La Unión Europea"». Comprobados letra por letra contra
`tue-version-consolidada-doue-c202-2016.txt` (art. 48.7) y `tue-tfue-protocolos-doue-c202-2016.txt`
(Protocolo n.º 2, art. 7.2): los tres coinciden con la fuente y los antecedentes de «esta
exclusión», «el segundo párrafo» y «la rúbrica…» quedan claros. Sin correcciones.

## 2. `negritas.py`, todas las fuentes del tema

TUE, TFUE, Carta y protocolos; Decisiones 2023/2061, 2013/272 y 2013/336; decretos 164/1995,
230/1995, 189/2026 (y su corrección) y del Presidente 9/2026; BOE-A-1996-21096, -2005-4388 y
-2011-13747; página institucional del euro; EAA, Ley 2/1997, Ley 8/1994, Ley 2/2014 y Constitución.
389 negritas cotejadas; 11 «NO ESTÁ» y 15 «¿ART. N?», revisadas una a una:

- **Citas de fuentes no pasadas** (4): el Instrumento de Ratificación de 1985/86 (BOE-A-1986-1, dos
  negritas), la Ley Orgánica 10/1985 («de acuerdo con lo previsto en el artículo 93...») y el
  Acuerdo de la Mesa del Parlamento de Andalucía de 5-V-2010; ninguna está entre las fuentes que
  cita el enunciado de este cotejo.
- **Acuerdo de la CARUE de 2010** (2): «por la de "Conferencia..."» y «acorde con el Tratado de
  Lisboa» son de la reunión de la Conferencia, no de la Ley 2/1997; fuente no pasada.
- **Rótulo** (1): «Cómo se leyeron los textos de la Unión», cabecera de tabla.
- **Elisión «[...]» correcta** (2): el art. 6.1 del TUE y el art. 2 de la Ley 2/1997 llevan un
  «[...]» donde el tema omite un inciso; comprobado en la fuente, el resto es literal.
- **Título de la Ley 2/1997** (1): «por la que se regula la Conferencia...» es el nombre oficial de
  la norma; el volcado de `boe.py` no incluye el título, solo el articulado.
- **Salto de página no depurado** (1): «así como la coordinación de las competencias...» (Decreto
  189/2026, art. 17) está partida por una cabecera de BOJA «Extraordinario núm. 15» que el patrón de
  `negritas.py` no reconoce (solo «Número N»); comprobado en el `.txt`, el texto es literal.
- **¿ART. N? por coincidencia** (13): once son las rúbricas de artículos de la Carta («Derecho a la
  vida», «Libertad de empresa»...), comprobadas una a una contra `carta-derechos-fundamentales-ue...`
  y correctas en el artículo que dice el tema; la coincidencia es con frases idénticas en otras
  normas. Las otras dos («procedimientos de revisión simplificados», del art. 48.1 del TUE, y «La
  Comisión de Coordinadores...», del art. 1.3 de la Ley 2/1997) están bien atribuidas en el tema; el
  script ancla mal el paréntesis del artículo siguiente o coincide con una frase igual en otra norma.

Ninguna de las 26 marcas exige corrección en el tema.

## 3. Quince preguntas (`T03-preguntas.md`)

Repasadas contra el tema ya rematado: las 15 se contestan enteras, incluida la 8 (exclusión
militar/defensa del art. 48.7), que el remate dejó resuelta.

## 4. `refutar_prosa.py`

0 hallazgos (tejido conectivo, repeticiones, siglas y negritas rotas, sobre el tema entero).

## Cuadro de lentes

| Lente | Tramos comprobados | Hallazgos |
| --- | --- | --- |
| Relectura de pasajes del remate | 3 pasajes, 2 fuentes | 0 |
| `negritas.py` | 389 negritas, 20 fuentes | 26 marcas, las 26 explicadas, 0 correcciones |
| 15 preguntas | 15 | 0 (todas enteras) |
| `refutar_prosa.py` | tema entero | 0 |

Cero hallazgos que corregir: el tema, tal como lo dejó el remate, está bien.
