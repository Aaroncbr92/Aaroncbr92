# Ciclo después de redactar · temario común de Canal Sur

Se aplica a cada tema una vez redactado. Cada fase la hace un agente distinto, que
lee antes `informes/canal-sur-comun/ENCARGO.md`, el informe de redacción del tema y
los de investigación.

## Las lentes automáticas

Se corren desde la raíz del repositorio y su salida se pega en el informe de la fase:

```
python3 herramientas/refutar_prosa.py      temas/canal-sur-comun/NN-*.md
python3 herramientas/refutar_exactitud.py  temas/canal-sur-comun/NN-*.md fuentes/canal-sur/BOE-A-….md [más fuentes]
python3 herramientas/refutar_citas.py      temas/canal-sur-comun/NN-*.md fuentes/canal-sur/BOE-A-….md [más fuentes]
python3 herramientas/refutar_modo.py       temas/canal-sur-comun/NN-*.md fuentes/canal-sur/BOE-A-….md [más fuentes]
python3 herramientas/refutar_documento.py  temas/canal-sur-comun/NN-*.md fuentes/canal-sur/documentos/….txt   # fuentes sin articulado del BOE
```

Cada número distinto de cero se explica en el informe: o es un defecto y se
corrige, o es un falso positivo y se dice por qué. **Un cero sólo vale si la lente
miró algo**: di cuántos tramos comprobó cada una.

## Niveles de título

`##` para cada rúbrica del enunciado y para cada sección fija (identificación,
normativa, lo que no da, trazabilidad); `###` dentro. Cuando el enunciado es una
norma entera sin rúbricas, `##` por capítulo o título y `###` por artículo, como en
RTVE, para que el índice llegue al artículo.

## Fase 3 · Verificar (corrige)

Relee **cada** precepto que cita el tema en su redacción vigente, con el catálogo de
los nueve errores delante, y **quita lo que no confirma**. Corrige en el tema.
Corre las lentes automáticas. Informe: `informes/canal-sur-comun/TNN-verificacion.md`,
con cada corrección (dónde, qué decía, qué dice, precepto).

## Fase 4 · Refutar (no corrige, informa)

Dos agentes con lentes distintas, en paralelo:

- **Exactitud normativa**: cada artículo, cifra, plazo, mayoría, enumeración,
  requisito y salvedad, contra la fuente. Informe `TNN-refutacion-exactitud.md`.
- **Cobertura y forma**: (1) ¿da el tema todo lo que anuncia cada rúbrica del
  enunciado? (2) escribe **quince preguntas tipo test** de cuatro opciones, en el
  estilo de una oposición de la Junta de Andalucía, repartidas por todo el
  enunciado, con su respuesta y el precepto; guárdalas en
  `informes/canal-sur-comun/TNN-preguntas.md`; contesta cada una **sólo con el cuerpo
  del tema delante**: entera, a medias o no; (3) prosa: antecedentes rotos,
  repeticiones, relleno, siglas sin presentar, referencias a ficheros del
  proyecto. Informe `TNN-refutacion-cobertura.md`.

Cada hallazgo, con: dónde, qué dice, qué debería decir, fuente literal, gravedad
(cambia la respuesta / induce a error / menor). **Cero hallazgos es un buen
resultado si el tema está bien.**

## Fase 5 · Rematar (corrige)

Aplica los hallazgos de la fase 4. **Comprueba cada corrección en la fuente antes de
aplicarla; si el informe se equivocó, no la apliques y dilo.** Cierra toda laguna de
las preguntas **ampliando el tema, nunca recortando la pregunta**. Relee el
resultado entero y comprueba que cada «ese artículo», «dicha ley» o «el apartado X»
tiene delante el antecedente que le corresponde. Corre `herramientas/indice.py` sobre
el tema y las lentes automáticas. Informe `TNN-remate.md`.

## Fase 5 bis · Segunda refutación (tiene que salir limpia)

Un agente nuevo, las dos lentes a la vez sobre el tema rematado, y las lentes
automáticas. Si encuentra algo, lo corrige él mismo comprobándolo en la fuente, y lo
dice. Informe `TNN-refutacion-final.md`, que termina con el cuadro de lentes.

## Aviso: incisos anulados

`boe.py norma` **pierde la negrita con que el BOE marca los incisos declarados nulos**
(ver `PENDIENTES.md`). En verificación y refutación, todo precepto cuyo bloque traiga
nota de sentencia del Tribunal Constitucional se comprueba en el XML o la página
consolidada del BOE para saber qué inciso exacto está anulado.

## Aviso: citas con el artículo entre paréntesis

Desde el 24-09-2026 `refutar_exactitud.py` tiene una **segunda pasada** para las
negritas que no van detrás de un marcador «**Artículo N**»: las ancla en el
paréntesis de detrás («(art. 7.2)», «(artículo 210.1)», «(6.3)») o en el artículo
nombrado antes en la misma frase. Da su propio recuento («citas con el artículo
entre paréntesis») y dice cuántas **no comprobó** porque remiten a otra norma o a
un artículo que no está en las fuentes pasadas. Pásale **todas** las normas que el
tema cita, o esas negritas quedan sin mirar. Una negrita que cita un documento sin
articulado del BOE (acuerdo, reglamento parlamentario, convenio) sale como no
literal aquí y se comprueba con `refutar_documento.py`.

## Modo ahorro (desde el 24-09-2026, a petición del titular: la mitad de consumo)

- **Fase 4 con un solo agente** que aplica las dos lentes (exactitud y cobertura) en una
  lectura. Informe único `TNN-refutacion.md` con dos apartados; preguntas en `TNN-preguntas.md`.
- **Fase 5 bis acotada**: no relee el tema entero. Relee **sólo los pasajes que cambió el
  remate** (el informe de remate los lista), comprueba sus antecedentes, corre las lentes
  automáticas y contesta las quince preguntas buscando en el tema. Va con modelo barato.
- **Esquemas con modelo barato**, a partir del tema cerrado.
- **Investigar, redactar y verificar no se abaratan** (manual, apartado 11).
- **Nunca más de tres agentes a la vez.**
- Un agente cortado no se reanuda si llevaba mucho contexto: se lanza uno nuevo que parte
  de lo que haya en disco (tema e informe a medias).

## Modo ahorro 2 (sin tocar la calidad)

- **No leas volcados enteros.** Saca sólo el precepto que comprueba: `python3
  herramientas/boe.py precepto <id> <bloque>` o `grep -n -A40 "Artículo N" <volcado>`.
- En fases 4 y 5 **no hace falta releer `metodo/`**: este fichero y `ENCARGO.md` llevan
  sus reglas.
- Informe **sólo con hallazgos y correcciones** (formato de CICLO), sin repetir lo que está
  bien más que en una línea de cuadro.
- **Respuesta final al coordinador: 120 palabras como máximo.** El detalle, en el informe.

## Herramienta: `herramientas/negritas.py`

Cotejo mecánico de **cada negrita contra todas las fuentes** (volcados del BOE y
documentos `.txt`), con el artículo donde aparece y aviso de **cita cruzada** cuando el
tema la atribuye a otro. Úsala **en vez de escribir un guion propio**:

```
python3 herramientas/negritas.py temas/canal-sur-comun/NN-*.md fuentes/canal-sur/BOE-A-….md fuentes/canal-sur/documentos/….txt …
```

Revisa sólo lo que lista (NO ESTÁ y ¿ART. N?); lo demás está cotejado.

## Fase 5 bis recortada (decisión del titular, 24-09-2026)

La comprobación final con agente **sólo se hace si el remate amplía el tema** (contenido
nuevo, no correcciones puntuales). Si el remate sólo corrige pasajes (hasta tres o cuatro),
basta con que el coordinador corra `refutar_prosa.py`, `refutar_modo.py`, `indice.py` y
`negritas.py` sobre el tema rematado y revise lo que marquen. Motivo, medido en los temas
1, 2, 4, 6 y 9: la refutación encontró en todos al menos un fallo grave; la comprobación
final, 0, 0, 0, 4 menores y 2 menores.

## Lección del tema 10 (24-09-2026)

Un remate hecho con modelo barato que **amplió** el tema metió dos errores (lista de
artículos del 83.4.a RGPD y la salvedad del 79.2), y sólo los cazó una comprobación
independiente con el modelo fuerte. Regla: **si el remate amplía el tema, lo revisa un
agente distinto con el modelo fuerte**, limitado a los pasajes cambiados.

## Herramienta: `herramientas/documento.py` (24-09-2026)

Para PDF y documentos que no son volcados del BOE: `texto` (PDF → `.txt` limpio), `indice`
(rótulos con su línea) y `seccion <fichero> <rótulo>` (sólo ese artículo, disposición o anexo;
si el sumario repite el rótulo, se queda con el cuerpo). Medido: el art. 33 del X Convenio son
3.217 palabras frente a 49.426 del convenio entero.
