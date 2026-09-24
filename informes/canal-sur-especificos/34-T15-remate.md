# 34 · T15 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/15-periodismo-de-datos-informacion-publica.md`.
Entrada: `34-T15-refutacion.md` (0 graves, 7 menores, 2 lagunas) y `34-T15-preguntas.md` (12 enteras, 1 a medias, 2 no).

## Fuentes releídas (todas el 24-09-2026)

- LTAIBG (`BOE-A-2013-12887`, `boe.py precepto`): arts. 2.1.f) y 23.2.
- LTPA (`BOE-A-2014-7534`): arts. 2.b), 3.1.b), 3.2 y 33.2.
- Libro de estilo (`libro-de-estilo-333233b.txt`): 3.16.2 (l. 1923-1932), 7.1.3 (l. 3412-3418) y 7.2.2 (l. 3502-3507).

## Correcciones: todas confirmadas en la fuente y aplicadas

| Id | Comprobación | Pasaje cambiado |
|---|---|---|
| M1 | 33.2 LTPA remite al 3.1.b) (Consejo Consultivo, CES, Consejo Audiovisual) y 3.2 (Parlamento, Defensor del Pueblo Andaluz, Cámara de Cuentas); 23.2 LTAIBG remite a los órganos del 2.1.f) | § Plazos, silencio y reclamación: fila «Reclamación» con «salvo el caso del 23.2 / 33.2»; nueva lista «La reclamación no cabe en dos casos» con las dos citas literales y la enumeración del 2.1.f); viñeta del 20.5 empieza «Salvo en el caso del artículo 23.2» |
| M2 | 2.b) define «Publicidad activa» | § Publicidad activa: «La publicidad activa es lo que la Administración publica… La ley andaluza la define (artículo 2.b)» |
| M3 | 7.1.3 empieza «Como norma general,» | § Encuestas y sondeos: primera viñeta, cita desde «Como norma general» |
| M4 | 3.16.2 prefiere «25 centésimas» y admite el «cuarto de punto»; 7.2.2 prefiere el «cuarto de punto» | § Las cifras en la noticia: viñeta del 3.16.2 con la cita completa; viñeta del 7.2.2 con su ejemplo literal; párrafo nuevo que señala que las dos reglas no coinciden |
| M5 | Contradicción interna con «Variables estadísticas» | Tabla de centralización: moda «La única aplicable a variables cualitativas nominales; en las ordinales, también la mediana» |
| M6 | Varianza en unidades al cuadrado | § Varianza y cuasivarianza: quitados «es decir 2,17 %» y «es decir 3,25 %»; frase nueva que explica que sólo la desviación típica se lee en porcentaje |
| M7 | Prosa sin apoyo | «error de principiante» → frase con el ejemplo de la provincia codificada; «Es la distinción que más confusión genera» suprimida |

## Lagunas: tema ampliado (contenido nuevo, desarrollo propio sin norma)

- **L1** · nuevo `### Porcentajes, puntos y tasas` en § 5 (antes de «Las cifras en la noticia»): porcentaje y su total; variación porcentual; puntos porcentuales con el ejemplo 10 % → 12 % (pregunta 13); subidas y bajadas que no se compensan; tasa interanual y sobre el periodo anterior; crecimiento medio con media geométrica (+10 % y −10 % → −0,50 %); tasas por 100.000 habitantes con ejemplo; nominal y real, fórmulas de deflactación con el IPC y ejemplo (3 % y 4 % → −0,96 %). Aritmética comprobada.
- **L2** · § 6 «Representaciones gráficas»: párrafo nuevo con tres distorsiones (eje que no empieza en cero, con ejemplo 50/52; escalas distintas; símbolos que crecen en dos dimensiones). § 7 «Contexto»: párrafo nuevo «correlación no es causalidad», declarado como razonamiento propio, con los verbos literales del LE 7.1.3 («**sugiere**», «**indica**»).

Ninguna pregunta recortada. Con el tema rematado, las 15 se contestan enteras (8 por M1, 11 por M5, 13 por L1, 14 por M3).

## Retoques de acompañamiento

«Qué se puede preguntar» (cuándo sólo cabe el contencioso; puntos, tasas y valores reales; distorsión de gráficos); arranque del § 4 («los seis primeros del siguiente», por el apartado nuevo); «Trazabilidad» (el desarrollo propio incluye porcentajes, tasas, deflactación, distorsiones y correlación); § 7, «La última regla» → «La regla del recuento propio en las manifestaciones» (el antecedente dejó de ser el inmediato); Extensión 9.265 → 10.556 palabras; índice regenerado.

## Lentes

- `indice.py`: 10.556 palabras, 42 epígrafes, índice con el apartado nuevo. El tema no está en `portadas.tsv`; la extensión se ajustó a mano.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` y `refutar_exactitud.py` (LTAIBG, LTPA, LRISP, Ley 9/2007, LOPDGDD, LE): los «no está» y los «no literales» son citas del LE con ligaduras «ﬁ/ﬂ» o saltos de página, y citas de un artículo que remite a otro precepto, como ya había visto la refutación. Las negritas nuevas o cambiadas (23.2, 2.1.f, 33.2, 7.1.3, 3.16.2, 7.2.2, «sugiere», «indica») se han cotejado aparte, normalizando NFKC y espacios y quitando la cabecera de página del LE: todas son literales.
- `refutar_modo.py`: 0 hallazgos.
- Antecedentes releídos: «Esos órganos» (M1) tiene delante el 2.1.f); «Son las del 3.1.b)» sigue a la cita del 33.2; «Las dos reglas» sigue a las viñetas 3.16.2 y 7.2.2; «Salvo en el caso del artículo 23.2» remite a la lista de arriba.

## Nada que el informe de refutación dijera mal

Las nueve propuestas cuadran con la fuente.

Ficheros tocados: el tema 15 y este informe.
