# T01 · Segunda refutación (fase 5 bis, modo ahorro) · Constitución Española de 1978

Fase 5 bis acotada (CICLO): se releyeron sólo los cinco pasajes que lista `T01-remate.md` más la
ficha de extensión. Cada cita se comprobó contra la fuente con `grep -n -A40`; el precepto que la
antecede también.

## Pasajes comprobados

| Pasaje | Fuente | Resultado |
| --- | --- | --- |
| Sección 2.ª Cap. II, antes del art. 30 (~680) | CE 53.2 y 30 | Literal; antecedente («esas dos garantías») presente en la frase anterior |
| CE 150.3, cierre (~2554) | `BOE-A-1978-31229` art. 150.3: «aun en el caso de materias atribuidas a la competencia de éstas» | Literal |
| EAA 42.2.3.º (~2575) | `BOE-A-2007-5825` art. 42.2.3.º | Literal, inciso en su sitio |
| EAA 60.1.c) y d) (~2651) | `BOE-A-2007-5825` art. 60.1.c) y d) | Literal; «estos órganos» remite a los órganos de gobierno de la letra d), como en la fuente |
| LAULA 11.1 (~3173) | `BOE-A-2010-11491` art. 11.1: «podrán consistir en» | Literal, con sujeto («las competencias de asistencia que la provincia preste») |
| Ficha, Extensión: 34.987 palabras | — | Confirmado (sin fila en `portadas.tsv`, cifra puesta a mano por no reescribirla `indice.py`) |

No se encontró ningún defecto en estos seis puntos.

## Las quince preguntas de `T01-preguntas.md`

Repetidas con sólo el cuerpo del tema delante: **15 enteras, 0 a medias, 0 no.** Coinciden las
respuestas ya fijadas (1c, 2b, 3b, 4c, 5c, 6b, 7b, 8c, 9c, 10b, 11b, 12b, 13a, 14c, 15a); se
verificaron además contra el propio texto del tema los pasajes de los artículos 64, 90.3
(«veinte días naturales»), 113, 143.2, 149.1.27.ª y los tramos de población del art. 26.1 LBRL.

## Lentes

| Herramienta | Tramos comprobados | Resultado |
| --- | --- | --- |
| `refutar_prosa.py` (tema entero) | relleno, repeticiones, siglas, negritas | 0 hallazgos |
| `refutar_modo.py` (tema + las tres fuentes) | 31 coincidencias de número de artículo entre las fuentes concatenadas | 31 "hallazgos", los 31 falsos positivos por colisión de numeración entre CE/EAA/LBRL/LAULA (aviso propio de la herramienta): comprobados art. 155 y 169 CE contra la fuente — el tema dice «podrá»/no dice «obligatorio» donde corresponde (el «debe»/«obligatorio» detectado pertenece a frases vecinas sobre el art. 161.2 y el 168.3, no al 155/169); el resto son artículos de LBRL/LAULA que el tema no cita con ese detalle |

Cero correcciones aplicadas: el tema, en los puntos comprobados, está bien.
