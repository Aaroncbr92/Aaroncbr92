# T10 · Remate (fase 5) · Protección de datos de carácter personal

Aplica los ocho hallazgos de `T10-refutacion.md` (fase 4, modo ahorro) al tema
`temas/canal-sur-comun/10-proteccion-de-datos.md`. Cada corrección comprobada en la fuente antes
de aplicarla. Fecha de lectura de todos los preceptos: **24-09-2026**, en `fuentes/canal-sur/`.

## Correcciones (H1-H5, H7, H8)

1. **H1 — regla nemotécnica del régimen sancionador** (hacia la línea 1353 antes del remate).
   Comprobado art. 83.4.a) RGPD: incluye los arts. 8, 11 y 25 a 39, 42 y 43. La regla decía que el
   4 % era «para lo que afecta al ciudadano (principios, **consentimiento**, derechos,
   transferencias)», y eso mete el art. 8 (consentimiento del niño) en el escalón del 4 % cuando
   está en el del 2 %. Corregido: la regla ya no habla de «consentimiento» sin más y añade la
   salvedad expresa del art. 8.
2. **H2 — art. 72.1.d) LOPDGDD**, lista de infracciones muy graves. Comprobado literal: «…sin
   contar con el consentimiento del afectado o con una base legal para ello». Frase añadida.
3. **H3 — art. 35.3.a) RGPD**, evaluación de impacto. Comprobado literal: «decisiones que
   produzcan efectos jurídicos para las personas físicas o que les afecten significativamente de
   modo similar». Sustituido «con efectos jurídicos» por el texto completo.
4. **H4 — tabla «Qué le toca a una producción», fila del correo fuera de jornada**. Comprobado
   art. 88 LOPDGDD: el apartado 2 remite a la negociación colectiva o, en su defecto, a lo
   acordado con los representantes; el 3 impone al empleador una política interna. No hay base
   para decir que un mensaje entre compañeros «choca» con el derecho. Reescrita la fila con el
   encabezado del informe de refutación.
5. **H5 — la AEPD, art. 44 LOPDGDD**. Comprobado: el art. 44 no dice que la relación con el
   Gobierno sea «el cauce ordinario de toda autoridad independiente». Frase quitada, sin
   sustituirla por lo que el tema no puede confirmar.
6. **H7 — tabla «Normativa que el tema invoca», fila de la Ley 1/2014**. Comprobado el cuerpo: solo
   cita los arts. 43 (línea ~1120), 45 (línea ~1133) y 48 (Ley 1/2026 como modificadora). Quitados
   los arts. 3 y 44 de la fila, que no aparecen en el cuerpo.
7. **H8a — «y ninguna reforma cruzada»** (dos apariciones, hacia la Ley Orgánica 3/2018 leída hoy y
   en Trazabilidad). Jerga de trabajo sin explicar. Quitada en ambos sitios; el resto de la frase
   queda igual y sigue siendo cierto (diecisiete bloques con más de una redacción o añadidos).
8. **H8b — el paréntesis del art. 77.3 LOPDGDD** que partía la cita en dos. Comprobado el
   apartado 3 completo en la fuente. Reescrito: la cita del 77.3 sigue entera y, después, una
   frase aparte explica que el apartado no se tocó en la reforma de 2023 y por eso sigue hablando
   de «la resolución en la que se imponga la sanción» aunque el 77.2 ya no sancione.

**H6 no se aplica como corrección**, según ordena el remate: cierra laguna ampliando el tema, no
recortando las preguntas 10 y 11 de `T10-preguntas.md`.

## Ampliación (H6)

Dos pasajes nuevos, comprobados en `fuentes/canal-sur/DOUE-L-2016-80807.md`:

- En «Cuándo es lícito tratar datos», antes de «El consentimiento de los menores…»: nuevo párrafo
  «Las condiciones del consentimiento (artículo 7 del Reglamento)», con la cita literal del 7.1
  («el responsable deberá ser capaz de demostrar que aquel consintió el tratamiento de sus datos
  personales») y del 7.3 («será tan fácil retirar el consentimiento como darlo»).
- Al final de «Los derechos de las personas», antes de «Tratamientos concretos»: nuevo párrafo
  «Recursos, responsabilidad e indemnización (capítulo VIII del Reglamento)», con la reclamación
  ante la autoridad de control (77.1), la tutela judicial frente al responsable o encargado
  (79.1) y el derecho a indemnización (82.1), los tres citados literalmente.

## Antecedentes

Releído el tema entero alrededor de cada pasaje tocado: «el artículo 7 del Reglamento» y «el
artículo 7 de la LOPDGDD» quedan distinguidos por su rótulo (uno «del Reglamento», el otro «de la
LOPDGDD»), y el «Todo interesado» del nuevo párrafo de recursos tiene delante, en el mismo
apartado, el sujeto «el afectado»/«el interesado» que usa el resto de «Los derechos de las
personas». No se ha encontrado ningún «ese artículo», «dicha ley» o «el apartado X» sin
antecedente en los pasajes tocados ni en los que los rodean.

## Lentes automáticas (tema entero)

| Lente | Tramos | Resultado |
|---|---|---|
| `herramientas/indice.py` | tema entero | 24 960 palabras, 33 epígrafes; sin aviso |
| `herramientas/refutar_prosa.py` | tema entero | 1 (LORTAD, falso positivo: se presenta en la misma cita) |
| `herramientas/refutar_modo.py` (RGPD, LOPDGDD, Ley 13/2022, Ley 10/2018, LO 1/1982, EAAnd, Ley 18/2007, Estatuto CSRTV) | tema entero | 2 (arts. 8 y 16 de otra norma con la misma numeración, falsos positivos) |
| `herramientas/negritas.py` (22 volcados + Acuerdo de fusión) | 216 negritas | 12 NO ESTÁ y 19 ¿ART.?, los mismos falsos positivos ya explicados en `T10-refutacion.md` (la corrección del H1 no introduce ninguno nuevo: se comprobó sin negrita) |

Nada nuevo respecto a lo que ya cotejó la fase 4: los mismos falsos positivos, un elemento menos
en «no están en ninguna fuente» porque se quitó la única frase en negrita que no era literal (la
regla nemotécnica corregida ya no lleva negrita, por no ser cita).

## Pasajes tocados (para la fase 5 bis acotada)

Lista exhaustiva, con línea aproximada en el tema ya rematado:

1. Línea ~449-453: nuevo párrafo, condiciones del consentimiento (art. 7 RGPD).
2. Línea ~660-668: nuevo párrafo, recursos, responsabilidad e indemnización (arts. 77.1, 79.1,
   82.1 RGPD).
3. Línea ~1354-1357: regla nemotécnica del régimen sancionador (art. 83.4.a RGPD, art. 8 RGPD).
4. Línea ~1279: art. 72.1.d) LOPDGDD, lista de infracciones muy graves.
5. Línea ~875: art. 35.3.a) RGPD, evaluación de impacto.
6. Línea ~2016: tabla «Qué le toca a una producción», fila del correo fuera de jornada (art. 88
   LOPDGDD).
7. Línea ~1003-1005: la AEPD, art. 44 LOPDGDD.
8. Línea ~2038: tabla «Normativa que el tema invoca», fila de la Ley 1/2014.
9. Líneas ~283-284 y ~2105: «y ninguna reforma cruzada» (quitado, dos veces).
10. Líneas ~1391-1397: art. 77.3 LOPDGDD, el paréntesis reescrito.

Preguntas de `T10-preguntas.md` que este remate cierra: la **9** (ya no hay trampa: la regla
nemotécnica corregida no empuja a la a); la **10** y la **11**, que pasan de «no» a «entera» porque
el tema ya trae los arts. 7.3 y 82.1 del Reglamento.

## Ficheros tocados

`temas/canal-sur-comun/10-proteccion-de-datos.md` (las diez correcciones y las dos ampliaciones) y
este informe. `T10-preguntas.md` no se ha tocado: sus respuestas siguen siendo correctas: la fase
5 bis acotada debe releer el cuerpo y confirmar que ahora contestan entera.
