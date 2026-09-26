# Productor/a (puesto 32) · Tema 14 · Fase 5, rematar

Tema: `temas/canal-sur-especificos/32-productor-a/14-prevencion-de-riesgos-laborales-en-la-produccion-audiovisual.md`.
Entrada: `32-T14-refutacion.md` (3 hallazgos menores) y `32-T14-preguntas.md` (2 lagunas: preguntas 6 y 13).
«Hoy» del encargo: 24-09-2026. Fuentes releídas el 25-09-2026; ningún precepto usado tiene redacción con
vigencia entre esas dos fechas.

Ficheros tocados: el tema y este informe. (El `git diff` muestra cambios en otros temas del puesto que no
son de este remate.)

**Resultado: se amplió contenido nuevo** (dos lagunas). Procede la fase 5 bis sobre los pasajes 4, 5, 6 y 7.

## Comprobación en la fuente antes de aplicar

| # | Corrección | Fuente releída (25-09-2026) | ¿Acertaba el informe? |
|---|---|---|---|
| H1 | Art. 12 es de la Norma Básica, no del RD 524/2023 | BOE-A-2023-14679: «Artículo único» aprueba la Norma; «Artículo 12. Planes de autoprotección» bajo «NORMA», capítulo III | Sí |
| H2 | Más de cuatro trabajadores, sólo «ocurrido en un Centro de trabajo» | Orden 16-12-1987 (BOE-A-1987-28546), art. 6.º | Sí |
| H3 | Art. 1.4 Ley 13/1999 citado a medias | BOE-A-2000-1009, art. 1.4 | Sí |
| L1 | Lista del art. 22 bis.1.b RD 39/1997 | `boe.py` BOE-A-1997-1853 a22bis: redacción única, BOE-A-2006-9379, vigente desde 29-06-2006 | Sí |
| L2 | LPRL art. 21.3 | BOE-A-1995-24292, art. 21: redacción única desde 10-02-1996 | Sí; se añade además su segundo párrafo (delegados de prevención), que el informe no citaba |

## Pasajes cambiados

1. **«Presencia de público e invitados», *La autoprotección*** (H1): «y su artículo 12 define ya…» →
   «y el artículo 12 de la Norma Básica de Protección Civil que ese real decreto aprueba define ya…».
   Antecedente de «ese real decreto»: el RD 524/2023, nombrado en la misma frase («la disposición final
   primera del mismo real decreto»).
2. **«Normativa que el tema invoca», fila RD 524/2023** (H1): «Artículo 12» → «Norma Básica, artículo 12».
3. **«Comunicación de incidencias», tabla de plazos, tercera fila** (H2): → «Fallecimiento, grave o muy
   grave, o accidente en un centro de trabajo que afecte a más de cuatro trabajadores».
4. **«Presencia de público e invitados», *Los espectáculos públicos en Andalucía*** (H3): cita del 1.4
   completada (derechos fundamentales en el ámbito laboral, político, religioso, sindical o docente, y la
   salvedad de las condiciones de seguridad de los recintos) y una frase de aplicación: una manifestación
   o concentración sindical que se cubre queda fuera de esa ley.
5. **«Los recursos preventivos»** (L1, nuevo): párrafo *La lista reglamentaria* con las cinco actividades
   del 22 bis.1.b (literal la 1.ª, 2.ª, 4.ª y 5.ª; la 3.ª, de máquinas sin declaración de conformidad,
   parafraseada en redonda), la aplicación a la parrilla y al decorado, y los apartados 22 bis.2, .3, .8
   (riesgos eléctricos; explosivos y pirotecnia) y .9 (el recurso lo designa la empresa que hace la
   operación). Antecedente de «La letra b)»: la lista del 32 bis.1 inmediatamente anterior.
6. **«Montajes y desmontajes»** (L1): nueva viñeta: con riesgos especialmente graves de caída desde
   altura u operaciones concurrentes hace falta recurso preventivo (32 bis LPRL y 22 bis RD 39/1997),
   designado por la empresa que monta; remite a «Los recursos preventivos».
7. **«Emergencias», artículo 21 de la LPRL** (L2, nuevo): apartado **21.3** literal, entre el 21.2 y el
   21.4, con su segundo párrafo (delegados de prevención) y una glosa: quién paraliza, a quién alcanza, y
   las veinticuatro horas de la autoridad laboral. El 21.4 («los apartados anteriores») conserva su
   antecedente, ahora con el 21.3 incluido.
8. **«Comunicación de incidencias», tabla *La cadena*, paso 3** (L2): añade la paralización por los
   representantes; fundamento «LPRL, artículo 21.1 y 21.3».
9. **Portada**: Fuente, «RD 39/1997 (artículos 22 bis y 34)»; Extensión, 28.800 palabras.
   **Normativa**: RD 39/1997, «Artículos 22 bis y 34». **Trazabilidad**: fila nueva del RD 39/1997 art.
   22 bis y nota del 21.3 en la fila de la Ley 31/1995.

## Lentes

- `indice.py`: 28.787 palabras, 45 epígrafes (índice regenerado; sin epígrafes nuevos).
- `negritas.py` (LPRL, Ley 13/1999, RD 524/2023, RD 39/1997 art. 22 bis, Orden de 1987): todas las
  negritas nuevas localizadas; sólo «21.3. La paralización por los representantes.», rótulo en el mismo
  estilo que los ya existentes «21.2. El derecho del trabajador.» y «21.4. La garantía.», y dos
  anteriores del pasaje eléctrico (fuente no dada).
- `refutar_modo.py` (LPRL, RD 39/1997 art. 22 bis, Ley 13/1999): 0 hallazgos.
- `refutar_exactitud.py`: las no literales son citas cotejadas contra volcados que no son los suyos (como
  en la verificación); la de la viñeta de «Montajes» la ancla al 32 bis, pero está en el 22 bis.1.b
  (confirmado por `negritas.py`).
- `refutar_prosa.py`: la sigla «CE» que introducía el pasaje nuevo se quitó parafraseando; quedan «TAS»
  sin presentar y una frase repetida sobre la insolación, ambas anteriores al remate y no señaladas por la
  refutación.

## Para el coordinador

El hallazgo 1 (artículo 12 atribuido al RD 524/2023) puede repetirse en el tema 8 de Productor/a y en
RTVE `prl/prl-especifico.md` 9.9, según avisa la refutación; no los he abierto.
