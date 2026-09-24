# Puesto 34 · Tema 4 · Fase 5 · Remate

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/04-fuentes-informativas-verificacion.md`.
Entrada: `34-T04-refutacion.md` (0 graves, 6 menores, 1 observación, 2 lagunas) y `34-T04-preguntas.md` (11 / 1 / 3).

**Resultado: SÍ se amplió contenido nuevo** (lagunas L1 y L2): dos subepígrafes nuevos en el epígrafe 1 y
dos fuentes nuevas. Hace falta la fase 5 bis sobre los pasajes marcados como AMPLIACIÓN.

## Fuentes leídas en esta fase (todas el 24-09-2026)

- Libro de Estilo de Canal Sur, `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 4.3, 4.3.1,
  4.3.2, 4.3.2.1 (ll. 2338-2422), 4.3.6 y 4.3.7 (ll. 2517-2570), 7.3.2 a 7.3.4 (ll. 3580-3670), 9.4.2.1,
  9.5, 9.5.1, 9.5.1.1, 9.5.4 (ll. 5486-5705).
- Orden PCM/1030/2020, `fuentes/canal-sur/BOE-A-2020-13663.md`, l. 35 («entre otros»).
- Resolución PE 25-XI-2020, `fuentes/informacion/PE_resolucion-25-11-2020.txt`, ap. 35 (l. 518).
- **Nueva**: Protocolo de Comunicación de la Justicia 2020 (CGPJ), descargado de poderjudicial.es
  (`fuentes/informacion/CGPJ_protocolo-comunicacion-2020.pdf` y `.txt`, pasado con `documento.py texto`):
  aps. 4, 5.a, 5.f y 7. La página «Sala de Prensa · Protocolo de Comunicación de la Justicia» del CGPJ
  sigue publicando la versión 2020 como la única (comprobado hoy); no se ha localizado una posterior.
- **Nueva**: Science Media Centre España, «¿Qué son los embargos? El mecanismo de las revistas y la
  revisión por pares», 23-III-2022, guardada como `fuentes/informacion/SMC_embargos-revision-por-pares.txt`.

## Correcciones de exactitud (todas comprobadas en la fuente; ninguna rechazada)

| # | Pasaje | Antes | Ahora |
|---|---|---|---|
| M1 | Ficha, «Fuente» | Carta FIP «arts. 3, 5 y 14» | «arts. 3, 5, 6 y 14» |
| M2 | 6, «La definición oficial» | «…o la seguridad**»» | «…o la seguridad, entre otros**»» (literal, l. 35 de la Orden) |
| M3 | 2, «Una sola fuente no basta» | «honorabilidad o la intimidad de alguien»; versiones contradictorias sin «opinión delicada» | cita literal «la honorabilidad, la intimidad y el prestigio de personas, instituciones o entidades», con los casos de controversia; añadido «una de estas informaciones contradictorias o una opinión delicada» |
| M4 | 3, «Anonimato y confidencialidad» | sin el último párrafo de 4.3.1 ni la regla de 4.3.6 | añadidos, literales: fuente de garantía que pide anonimato («debemos precisar cuando sea posible las razones…») y confidencialidad invocada previamente («no puede emitirse, ni hacer referencia directa o indirecta…») |
| M5 | 2, «Cifras propias» | sin «generalmente en miles…» ni el inciso de las manifestaciones reducidas | añadidos ambos, literales |
| M6 | 6, «El remedio» | ap. 35 cortado en «órganos de censura privados» | se completa con la sujeción a garantías y el control de las autoridades jurisdiccionales de los Estados miembros |
| Obs. | 2, «Fuentes dudosas» | «exdirector de *The Washington Post*» | «director de *The Washington Post*», como en 4.3.6 (l. 2564) |

## Ampliaciones (lagunas; pasan a la fase 5 bis)

- **AMPLIACIÓN L1** · nuevo `### Las fuentes judiciales` (epígrafe 1, tras «Los tipos del enunciado»):
  Protocolo CGPJ 2020 (Oficinas de Comunicación como «cauce institucional y fuente oficial»; información
  a todos a la vez, por nota de prensa escrita; sentencias públicas una vez dictadas y firmadas;
  notificación simultánea; «La primera noticia que llega…») y Libro de Estilo 9.5, 9.5.1, 9.5.1.1, 9.5.4
  y 9.4.2.1. Remite al tema 11 las pautas de redacción de tribunales. Responde la pregunta 13 (clave b).
- **AMPLIACIÓN L2** · nuevo `### Las fuentes científicas`: Libro de Estilo 7.3.2 (identificar la fuente,
  no inflar el hallazgo, embargar para no alarmar), 7.3.3 (expertos que explican), 7.3.4 (estudios de
  parte); SMC España (revisión por pares, *preprints*, límite de la revisión, embargos). Responde la
  pregunta 14 (clave a).
- Ajustes derivados: bullet «Judiciales y científicas» (remite a los subepígrafes); «De dónde sale este
  tema»; «Qué se puede preguntar»; índice; sigla CGPJ presentada en la entrada; ficha (Fuente,
  Extensión 5.700); tabla de normativa (Libro de Estilo ampliado y fila del protocolo, marcado como no
  normativo); «Lo que este tema no da» (se quita «no se dan» y queda sólo lo que no consta); Trazabilidad.

## Preguntas tras el remate

6 (a medias → entera, M5), 13 (no → entera), 14 (no → entera), 15 (no → entera, M4). Resultado: 15 enteras.
No se recortó ninguna pregunta.

## Lentes

- `indice.py`: 5.646 palabras, 33 epígrafes, índice regenerado sin avisos.
- `negritas.py` (Libro de Estilo, Orden, carta FIP, Resolución PE, protocolo CGPJ, SMC, LGCA, CE): 110
  cotejadas, 29 «no están»; todas son falsos positivos por ligaduras «ﬁ» del PDF, saltos de página,
  líneas de cita «>» o fuentes no pasadas (STC, Barot). Las 8 negritas nuevas que salieron se
  comprobaron normalizando ligaduras y cabeceras: las 8 literales.
- `refutar_exactitud.py`: 28 «no literales», todas por leer «(4.3.1)» del Libro de Estilo como «art. 4» de
  la LGCA; falso positivo ya conocido. `refutar_modo.py`: 0. `refutar_prosa.py`: 0.
- Relectura de antecedentes: «El mismo apartado» (5.a, citado justo antes), «Tres cautelas» (tres
  viñetas), «el protocolo» (presentado en el párrafo anterior): correctos.

## Otros ficheros tocados

Creados: `fuentes/informacion/CGPJ_protocolo-comunicacion-2020.pdf`, `…/CGPJ_protocolo-comunicacion-2020.txt`,
`fuentes/informacion/SMC_embargos-revision-por-pares.txt` y este informe. Ningún otro tema.
