# T05 · Remate (fase 5, modo ahorro) · Ley 18/2007 (RTVA)

Aplicados los hallazgos de `T05-refutacion.md` sobre
`temas/canal-sur-comun/05-ley-18-2007-rtva.md`. El informe traía **un solo hallazgo**
(prosa, gravedad menor); los demás apartados («Exactitud», «Cobertura») no listaban
correcciones. Comprobado en la fuente antes de aplicar. No amplía el tema (no hay
laguna de preguntas: las quince se contestan enteras según `T05-refutacion.md`).

## Corrección aplicada

| # | Dónde | Decía | Pasa a decir | Comprobación |
| --- | --- | --- | --- | --- |
| 1 | «Funcionamiento, mandato y condición (artículo 20.2 a 20.5)», línea tras la cita del 20.2 | «Lo convoca el Consejo de Administración, y su opinión es obligada en lo relativo a las programaciones.» | «Su opinión es obligada en lo relativo a las programaciones.» | `fuentes/canal-sur/BOE-A-2008-1185.md`, art. 20.2: «El Consejo Asesor será convocado por el Consejo de Administración y emitirá opinión o dictamen...». La convocatoria ya está en la cita literal que precede (dentro de las comillas en negrita); la paráfrasis la repetía. El sujeto de la frase que queda («Su opinión») tiene delante el antecedente correcto, «El Consejo Asesor», en la cita literal inmediatamente anterior. |

Extensión de portada corregida de 15.087 a **15.080 palabras** (cifra que da `indice.py`
tras el recorte).

## Antecedentes releídos

Releído el epígrafe entero «Funcionamiento, mandato y condición (artículo 20.2 a
20.5)» (20.2 a 20.5) y el que le precede inmediatamente: el sujeto elíptico «Su
opinión» sigue remitiendo, sin ambigüedad, al Consejo Asesor nombrado en la cita
literal del 20.2 que abre el punto.

## Lentes automáticas (sobre el tema ya rematado)

| Lente | Tramos mirados | Resultado |
| --- | --- | --- |
| `refutar_prosa.py` | tema entero | 2, ambos falsos positivos ya explicados en `T05-verificacion.md`/`T05-refutacion.md`: rótulo «redacción anterior…» ×3 (frase repetida por diseño, en tres epígrafes de redacciones históricas distintas) y «LGBTI» sin presentar (es parte del nombre oficial «Consejo Andaluz LGBTI», no una sigla del tema) |
| `refutar_modo.py` (con las 6 normas del BOE del encargo) | tema entero contra las 6 fuentes | 0 |
| `indice.py` | tema entero | 15.080 palabras, 42 epígrafes |
| `negritas.py` (con las 8 fuentes del encargo + `BOE-A-2010-5303` + Contrato-Programa 2024-2026 `.txt`, igual que en la refutación) | 220 negritas | 2 «NO ESTÁ» y 10 «¿ART. N?», ambos idénticos a los ya explicados como falsos positivos en `T05-refutacion.md` (nada nuevo tras el recorte) |

No se corre fase 5 bis con agente aparte: el remate sólo corrige un pasaje puntual
(uno, no de tres a cuatro) y no amplía el tema, según la cláusula del titular del
24-09-2026 en `CICLO.md` («Fase 5 bis recortada»). Basta con lo anterior.

## Pasajes cambiados (lista para la fase siguiente)

1. Línea 1263 (numeración tras la corrección) del epígrafe «Funcionamiento, mandato y
   condición (artículo 20.2 a 20.5)»: se quita «Lo convoca el Consejo de
   Administración, y» de la paráfrasis que sigue a la cita del art. 20.2.
2. Portada: campo «Extensión», de 15.087 a 15.080 palabras.

## Ficheros tocados

`temas/canal-sur-comun/05-ley-18-2007-rtva.md` (las dos correcciones de arriba). Este
informe. Ningún otro.
