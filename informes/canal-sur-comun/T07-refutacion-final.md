# T07 · Refutación final (fase 5 bis acotada) · X Convenio Colectivo de la RTVA

Modo ahorro: releídos sólo los pasajes que lista `T07-remate.md` (no el tema entero).

## Pasajes releídos y comprobados

1. **Portada, campo «Extensión»**: «23.002 palabras» — comprobado con `herramientas/indice.py`,
   que da 23002 palabras, 35 epígrafes. Coincide.
2. **«Disposiciones transitorias» → Quinta. Retribuciones → apartado C**: «…y medio punto menos
   para los temporales de los tramos T5 y T6 (de 30.001 a 40.000 € y de 22.001 a 30.000 €).» —
   comprobado contra `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` (`grep -n
   -A40` sobre el cuadro de tramos, líneas ~2458-2484): «T6 / 22.001 hasta 30.000»; «T5 / 30.001
   hasta 40.000». Coincide con el paréntesis añadido. Antecedente: el apartado C ya presenta el
   sistema de tramos dos frases antes («tipo medio de descuento» por tramos, de 0 % hasta 22.000 €
   a 8,30 % en el tramo de más de 60.000 €); la aclaración no rompe nada alrededor.

Ningún error. Nada que corregir.

## Quince preguntas (`T07-preguntas.md`)

Recontestadas buscando sólo en `temas/canal-sur-comun/07-x-convenio-colectivo.md`: las quince
siguen enteras (el pasaje tocado por el remate — el paréntesis de tramos — no es objeto de ninguna
pregunta ni de su antecedente). **15 enteras, 0 a medias, 0 no.**

## Cuadro de lentes

| Lente | Tramos mirados | Resultado |
| --- | --- | --- |
| `refutar_prosa.py` | tema entero | 7 avisos, los mismos que ya explicó `T07-refutacion.md`: cinco siglas (CEMAC, CSR, CSTV, RTVA, SERCLA) presentadas en el párrafo de siglas o en su propio paréntesis, y dos frases repetidas que cierran reservas distintas en epígrafes distintos (vigencia; transitorias). Ningún aviso nuevo. |
| `refutar_modo.py` (4 fuentes del encargo: `x-convenio-rtva-boja-240-2014.txt`, `BOE-A-2015-11430.md`, `BOE-A-2012-13126.md`, `BOE-A-2026-945.md`) | tema entero contra las 4 fuentes | 44 avisos, mismo número y mismo cruce de numeración que ya explicó `T07-verificacion.md`: tres son de modo verbal (arts. 7, 10 y 32), literales en el convenio («habrá de», «podrán», «será obligatoria»); las 41 restantes son salvedades de preceptos del ET o de la Ley 8/2025 que el tema no cita con ese número (numeración cruzada, no hallazgo). Nada nuevo tras el remate. |
| `negritas.py` (4 fuentes del encargo + 10 documentos citados por el tema: Ley 7/2024, Reglamento de la Mesa de Contratación, fusión CSRTV, Cámara de Cuentas, REGCON, bases y programa de la convocatoria de 2026) | 383 negritas | 1 «NO ESTÁ» («Enunciado del programa», etiqueta de forma ya declarada, no una cita) y 4 «¿ART. N?», falsos positivos por cruce de numeración con el ET y la Ley 8/2025 (la misma clase de aviso, mismo recuento total, que ya explicaron `T07-refutacion.md` y `T07-remate.md`; comprobado uno al detalle: «en el plazo de quince días» está literal en el convenio, art. 67.18, y el aviso lo cruza con el «artículo 73.3 y 4» nombrado dos líneas antes en el mismo punto de la lista). |
| `indice.py` | tema entero | 23.002 palabras, 35 epígrafes (coincide con la portada) |
| Preguntas (`T07-preguntas.md`) | 15 | 15 enteras, 0 a medias, 0 no |

**Cero hallazgos.** El remate estaba bien aplicado y comprobado en la fuente; no hace falta ninguna
corrección adicional.

## Ficheros tocados

Este informe. Ningún otro (no hubo nada que corregir en el tema).
