# T08 · Refutación (fase 4, modo ahorro) · Normativa sobre igualdad

Tema: `temas/canal-sur-comun/08-igualdad.md` (verificado). Una lectura, dos lentes. Preceptos
leídos el 24-09-2026 en los volcados de `fuentes/canal-sur/` (redacción vigente). No se ha
corregido el tema. Ficheros tocados: este informe y `T08-preguntas.md`.

## 1. Exactitud

### Hallazgo 1 · RD 1026/2024, artículo 5: salvedades omitidas (error 6)

- **Dónde**: bloque de la Ley 4/2023, «Ámbito laboral», viñeta del artículo 5 del Real Decreto
  1026/2024.
- **Qué dice**: «si en tres meses desde el inicio no hay acuerdo, se aplican las medidas del real
  decreto (artículo 5)»; el plazo de constitución se cuenta sólo desde la entrada en vigor del
  real decreto.
- **Qué debería decir**: añadir el segundo supuesto del 5.3 (cuando **el convenio colectivo
  aplicable no incluye las medidas planificadas**), que esas medidas se siguen aplicando hasta que
  entren en vigor las que se acuerden, y que para las empresas que llegan al umbral después, el
  plazo se cuenta desde que lo alcanzan (5.1, párrafo segundo).
- **Fuente literal** (RD 1026/2024, art. 5.1, párrafo segundo): «Para aquellas empresas que, al
  momento de la entrada en vigor de este real decreto, no estuviesen incluidas en su ámbito de
  aplicación, el plazo anterior empezará a contarse desde el momento en que alcancen el número de
  personas trabajadoras indicado en el artículo 2.» Art. 5.3: «Transcurridos tres meses desde el
  inicio del procedimiento de negociación […] sin que se haya alcanzado un acuerdo sobre las
  mismas o en el supuesto de que el convenio colectivo de aplicación no incluya las medidas
  planificadas, las empresas obligadas […] aplicarán el conjunto de medidas establecidas en este
  real decreto. Dichas medidas se continuarán aplicando hasta que entren en vigor las que
  posteriormente se puedan acordar […]».
- **Gravedad**: menor (es reglamento, fuera del enunciado literal; puede inducir a error en una
  pregunta práctica sobre plazos).

### Cotejado sin hallazgos

| Qué | Resultado |
| --- | --- |
| `negritas.py` (7 volcados) | 423 negritas; 7 «no está»: el rótulo del enunciado, cuatro citas de la redacción de 2007 (arts. 11.1, 11.2, 40 y 58.1; la verificación las leyó con `--fecha`), el fallo de la STC 89/2024 y el anuncio del recurso 3679-2023 (documentos no pasados). 37 «¿art.?»: anclas falsas en números de otras leyes, ya explicadas en la verificación; revisadas, cada negrita está en el artículo que dice el tema. |
| Releídos en la fuente (lo que la verificación no listó o de más riesgo) | Ley 4/2023: arts. 3.a), 9, 10, 12, 14, 43, 44, 52, 76, 77, 80; recuento de disposiciones (4 DA, 2 DT, 1 DD, 20 DF, 82 arts.) y límites de títulos. Ley 15/2022: arts. 2, 29, 34, 47, 49, 50, 51. Ley 12/2007: arts. 39, 43, 65, 80, 83, 84, 85 y citas de la LO 3/2007 (27.1, 65.2). Conformes. |
| `refutar_prosa.py` | 2, los mismos falsos positivos explicados en la verificación (fórmula de cadena ×5; «LGBTI» dentro de cita literal de la Ley 18/2007). |

## 2. Cobertura

Quince preguntas en `T08-preguntas.md` (medios, publicidad, empleo, definiciones, sanciones,
Autoridad, rectificación registral; seis de aplicación práctica en Canal Sur/CSRTV): **15 enteras,
0 a medias, 0 sin respuesta**. Cada rúbrica del enunciado (las tres leyes) tiene su bloque con
objeto, definiciones, medidas, organización, garantías y sanciones. Sin lagunas.

## 3. Prosa

Sin hallazgos: antecedentes correctos, siglas presentadas, sin referencias a ficheros del
proyecto (búsqueda de rutas, `.py` y `.md` en el tema: 0).

## Cuadro

| Lente | Hallazgos que piden corrección o ampliación |
| --- | --- |
| Exactitud | 1 (menor) |
| Cobertura | 0 |
| Prosa | 0 |
| **Total** | **1** |
