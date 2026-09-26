# Productor/a (puesto 32) · Tema 12 · Fase 5 bis, revisión de los pasajes rematados

Tema: `temas/canal-sur-especificos/32-productor-a/12-gestion-documental-y-trazabilidad.md`.
Entrada: la lista de 11 pasajes cambiados de `32-T12-remate.md`. «Hoy» del encargo: 24-09-2026.
Fuentes leídas el 26-09-2026 (fecha del sistema); ningún precepto revisado tiene redacción posterior
al 24-09-2026.

## Fuentes leídas

| Fuente | Preceptos | Cómo | Resultado |
|---|---|---|---|
| Ley 7/2011 (BOE-A-2011-18654) | 11, 18, 31 (dos redacciones), 38, 43, 71 | `boe.py precepto` | Todo literal; el 31 vigente es el de la DF 3.1 de la Ley 1/2014, vigencia 30-06-2015, y se llama «Comisión Andaluza de Valoración de Documentos»; 38.2 y 43.5 conservan «de Valoración y Acceso a los Documentos». Confirmado |
| LCSP (BOE-A-2017-12902) | 37, 120.1, 335 | volcado local (el BOE en línea respondió 404 a `boe.py precepto`) | Una redacción, desde 09-03-2018; literal |
| Libro de estilo Canal Sur TV (2004) | 4.4 y 4.4.4 (pasos 1-10) | `libro-de-estilo-333233b.txt`, l. 2610-2745 | Punto 6 literal (ligaduras aparte); son diez pasos, así que «decálogo» y «diez pasos» cuadran; «tareas administrativas…» es del 4.4, antes del decálogo |

## Revisión pasaje por pasaje

| Nº | Pasaje | Dato y fuente | Antecedentes | Resultado |
|---|---|---|---|---|
| 1 | Libro de estilo 4.4.4.6 | Literal, con la salvedad «En la medida de lo posible» | «ese decálogo» → «los diez pasos» | Bien |
| 2 | «Hay cuatro sitios» | Cuatro puntos numerados | — | Bien |
| 3 | 335.2 | Enumeración literal (omite «de los contratos indicados», no en negrita) | — | Bien |
| 4 | Ficha | 13.700; `indice.py` mide 13.695. LCSP 36, 37, 63, 116, 118, 120, 153, 317, 318, 335, 346 = tabla de normativa | — | Bien |
| 5 | Eliminación (31.3.a y c, 71.b) | Literales; nombre vigente y anterior y fecha 30-06-2015 correctos; el 18 remite a procedimientos reglamentarios | «ese procedimiento» → procedimiento del 18 | **Corregido**: faltaban los dos puntos entre el paréntesis y la cita de 31.3.a (la frase no se leía); ahora «…Documentos»): **«Dictaminar…** |
| 6 | 38.2, 38.4, 43.3, 43.5 y nota del nombre | Literales; nota del nombre cierta; el paso oficina→central lo respalda además la definición 2.h | «véase…» apunta a epígrafe anterior existente | Bien |
| 7 | 11.1 | Literal | «las exige» → las cinco cualidades | Bien |
| 8 | 37.1 y 120.1 | Literales | «esa base» → la forma escrita; «dos preceptos» = arts. 36 y 153 (153.1 y 153.6 son del mismo) | Bien |
| 9 | Normativa | Preceptos coinciden con el cuerpo | — | Bien |
| 10 | «Lo que no da» | 31.3.c y 38.2 correctos | «esos plazos» → los de la Comisión | Bien |
| 11 | Trazabilidad | Filas coinciden | — | Bien |

Hallazgos: 1 (formal, corregido). Ningún dato erróneo. Los nueve errores: ninguno en los pasajes.

## Ficheros tocados

El tema 12 (una edición, pasaje 5) y este informe. `indice.py` se corrió una vez sin argumentos por
error (reescribe temas de `portadas.tsv` y `esquemas/`): `git status` no muestra cambios en ficheros
seguidos fuera del puesto 32; los esquemas no seguidos pudieron regenerarse (operación idempotente).
Después, sobre el tema 12: 13.695 palabras, 50 epígrafes.
