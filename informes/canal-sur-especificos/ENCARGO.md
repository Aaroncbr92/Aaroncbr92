# Encargo · Temarios específicos de Canal Sur

**Es lo único que lees del método.** Sustituye a `metodo/MANUAL.md`, `metodo/ENCARGOS.md` y a los
ficheros del común: no los abras. Lees además el enunciado de tu puesto
(`convocatoria/canal-sur/especificos/NN-*.md`) y las filas de tu tema en `AGRUPACION.tsv` y en
`informes/canal-sur-reuso/*.tsv`.

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (**RTVA**); Canal Sur
Radio y Televisión, S.A. (**CSRTV**); Corporación de Radio y Televisión Española (**RTVE**).

## La oposición

Concurso-oposición RTVA/CSRTV, BOJA núm. 186, de 24-IX-2026. Test con preguntas del común, de
teoría específica y de aplicación práctica, y después una prueba práctica del puesto. **No hay
exámenes anteriores**, ni fecha de corte: se estudia lo vigente el día en que se escribe.

## La regla que manda

**Nada de memoria. Cada dato se lee en su fuente antes de afirmarlo, y lo que no se puede
confirmar se quita.** Un hueco declarado vale más que un dato inventado.

- **Fuente de una norma**: el BOE/BOJA vigente (`herramientas/boe.py precepto <id> <bloque>`,
  volcados en `fuentes/canal-sur/`). No leas volcados enteros: saca el precepto o usa `grep -n -A40`.
- **PDF y documentos sin articulado del BOE** (BOJA, convenio, Carta, informes): nunca los leas
  enteros ni escribas tu propio extractor. `herramientas/documento.py texto <pdf>` lo pasa a `.txt`
  limpio; `documento.py indice <fichero>` da sus rótulos; `documento.py seccion <fichero> 33` (o
  «Disposición transitoria tercera», «Anexo II») imprime sólo ese trozo.
- **Fuente técnica** (oficio, equipos, formatos): normas y recomendaciones publicadas (UIT, EBU,
  SMPTE, AES, UNE, ISO), documentación del fabricante, manuales universitarios y organismos
  oficiales. Cita cada una en «Trazabilidad». Lo que sólo es costumbre de oficio se dice como tal,
  sin disfrazarlo de norma.
- **Lo propio de la RTVA** (organización, Libro de estilo, Estatuto profesional): sólo lo que conste
  en un documento publicado. Si no consta, se dice en «Lo que este tema no da».

## Reutilizar antes de escribir

1. **Temas repetidos entre puestos** (`AGRUPACION.tsv`): «idéntico», se copia el tema ya cerrado y
   sólo se reescribe la ficha; «parecido», se copia y se amplía lo que el enunciado nuevo pida de
   más (eso sí pasa por el ciclo, limitado a lo nuevo).
2. **Temario común de Canal Sur** (`temas/canal-sur-comun/`): si el tema pide una norma que el
   común ya desarrolla, se toma su texto literal y el tema se centra en **la aplicación al puesto**.
   No se reescribe el común.
3. **RTVE** (`informes/canal-sur-reuso/`): se reutiliza el texto literal, releyendo cada precepto
   en su redacción vigente y quitando lo que es propio de RTVE.

## Forma del tema

`# Tema N del específico de <Puesto> · <título>`; ficha entre `<!-- portada -->` y
`<!-- /portada -->` (Bloque «Temario específico de <Puesto> · punto N», Sirve para, Fuente,
Redacción que se estudia, Extensión); siglas de entrada; enunciado literal en cita; qué se puede
preguntar; `<!-- indice -->` `<!-- /indice -->`; epígrafes que reproducen el enunciado en su orden
(`##` rúbrica, `###` dentro); «Normativa que el tema invoca» (si la hay); «Lo que este tema no da,
y dónde está»; «Trazabilidad». **Negrita = literal de la fuente**; lo demás, en redonda. Nada de
rutas, herramientas ni informes dentro del tema. **La extensión la manda el enunciado**: se recorta
prosa (repeticiones, «como hemos visto», doctrina sin apoyo), nunca un dato.

## Cláusulas

- «Si algo de este encargo no cuadra con la fuente, manda la fuente y dímelo.»
- «Lo que no puedas confirmar, quítalo. No lo sustituyas por lo que recuerdes.»
- «Limítate a tu tema y declara qué otros ficheros has tocado.»
- «Escribe tu informe en `informes/canal-sur-especificos/PP-TNN-<fase>.md` según lo vayas produciendo.»
- «Declara la fecha en la que leíste cada fuente.»
- Refutar: «Cero hallazgos es un buen resultado si el tema está bien.»
- Rematar: «Comprueba cada corrección en la fuente antes de aplicarla; si el informe se equivocó,
  no la apliques y dilo.» «Relee cada pasaje cambiado y comprueba que cada "ese artículo", "dicha
  ley" o "el apartado X" tiene delante su antecedente.»

## Los nueve errores

1 cita cruzada · 2 ley por reglamento · 3 recuentos que no cuadran · 4 «podrá» por «deberá» ·
5 siglas sin presentar · 6 salvedad omitida · 7 redacción derogada como vigente · 8 artículo mal ·
9 afirmación sin fuente. En técnico, el 9 es el que más pasa: cifras, valores de norma y nombres
de estándar que suenan bien.

## El ciclo, con sus ahorros

| Fase | Quién | Qué |
|---|---|---|
| 1 Investigar | Opus, **uno por puesto o por bloque de 4-6 temas** que comparten fuentes | Material denso con la fuente pegada a cada dato; dice lo que no pudo confirmar. `PP-investigacion-<bloque>.md` |
| 2 Redactar | Opus, uno por tema | Por partes, guardando cada epígrafe |
| 3 Verificar | Opus | Relee cada dato en su fuente, quita lo que no confirma, corrige |
| 4 Refutar | Opus, un agente, dos lentes | Exactitud + cobertura; **15 preguntas tipo test** en `PP-TNN-preguntas.md`, contestadas sólo con el tema: entera, a medias, no. Laguna = se amplía el tema |
| 5 Rematar | Sonnet si corrige pasajes; Opus si amplía | Aplica y lista los pasajes cambiados |
| 5 bis | Opus distinto, **sólo si el remate amplió** | Revisa sólo los pasajes cambiados |
| Esquema | Sonnet | Esqueleto telegráfico, ~2.000 palabras / ~130 líneas, no crece con el tema |

**Lentes automáticas, sólo si el tema cita normas**: `negritas.py`, `refutar_exactitud.py`,
`refutar_modo.py` con las fuentes que cite. En un tema técnico sin norma, sólo `refutar_prosa.py`
e `indice.py`. **Respuesta final al coordinador: 120 palabras como máximo**; el detalle, en el informe.

**Lo copiado del común no se vuelve a verificar**: el redactor lo lista bajo «Copiado del común» en
su informe y verificación y refutación lo saltan (ya pasó el ciclo con redacción vigente). Lo
copiado de RTVE sí se verifica, porque está escrito a otra fecha.

**Lo copiado de RTVE sin tocar, en temas técnicos sin actualizar, tampoco se re-verifica** (desde
Operador/a de Sonido): el redactor lo lista bajo «Copiado de RTVE sin cambios»; el verificador
comprueba sólo que es literal. Lo adaptado o lo que cite normas sí se verifica. Medido en
Redactor/a: la verificación era el 27 % del gasto.
