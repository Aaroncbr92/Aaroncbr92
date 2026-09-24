# T05 · Refutación final (fase 5 bis acotada) · Ley 18/2007 (RTVA)

Modo ahorro: releídos sólo los pasajes que lista `T05-remate.md` (no el tema entero).

## Pasajes releídos y comprobados

1. **Epígrafe «Funcionamiento, mandato y condición (artículo 20.2 a 20.5)»**, línea
   1263: «Su opinión es obligada en lo relativo a las programaciones.» — comprobado
   contra `fuentes/canal-sur/BOE-A-2008-1185.md`, art. 20.2 (`grep -n -A20 "^Artículo
   20\."`): «El Consejo Asesor será convocado por el Consejo de Administración y
   emitirá opinión o dictamen cuando sea requerido expresamente por este y, en todo
   caso, cuando se trate de las competencias referentes a las programaciones…».
   Correcto: la convocatoria queda sólo en la cita literal precedente, sin
   duplicarla en la paráfrasis. Antecedente del sujeto elíptico «Su opinión»: «El
   Consejo Asesor», nombrado en la cita literal inmediatamente anterior, dentro del
   mismo epígrafe — sin ambigüedad.
2. **Portada, campo «Extensión»**: «15.080 palabras» — comprobado con
   `herramientas/indice.py`, que da 15080 palabras, 42 epígrafes. Coincide.

Ningún error. Nada que corregir.

## Quince preguntas (`T05-preguntas.md`)

Recontestadas buscando sólo en `temas/canal-sur-comun/05-ley-18-2007-rtva.md`:
las quince siguen enteras (el pasaje tocado por el remate no es objeto de
ninguna pregunta ni de su antecedente). **15 enteras, 0 a medias, 0 no.**

## Cuadro de lentes

| Lente | Tramos mirados | Resultado |
| --- | --- | --- |
| `refutar_prosa.py` | tema entero | 2 hallazgos, ambos falsos positivos ya explicados en `T05-verificacion.md`/`T05-refutacion.md`: rótulo «redacción anterior…» ×3 (repetido por diseño en tres epígrafes de redacciones históricas distintas) y «LGBTI» sin presentar (parte del nombre oficial «Consejo Andaluz LGBTI», no sigla del tema) |
| `refutar_modo.py` (6 normas del BOE del encargo: `BOE-A-2008-1185`, `BOE-A-2007-5825`, `BOE-A-2007-19819`, `BOE-A-2005-655`, `BOE-A-1988-8592`, `BOE-A-2026-944`) | tema entero contra las 6 fuentes | 0 |
| `negritas.py` (8 fuentes del encargo + `BOE-A-2010-5303` + Contrato-Programa 2024-2026 `.txt`) | 220 negritas | 2 «NO ESTÁ» y 10 «¿ART. N?», idénticos en número y en pasaje a los ya explicados como falsos positivos en `T05-refutacion.md` (nada nuevo tras el remate) |
| `indice.py` | tema entero | 15.080 palabras, 42 epígrafes (coincide con la portada) |
| Preguntas (`T05-preguntas.md`) | 15 | 15 enteras, 0 a medias, 0 no |

**Cero hallazgos.** El remate estaba bien aplicado y comprobado en la fuente; no
hace falta ninguna corrección adicional.

## Ficheros tocados

Este informe. Ningún otro (no hubo nada que corregir en el tema).
