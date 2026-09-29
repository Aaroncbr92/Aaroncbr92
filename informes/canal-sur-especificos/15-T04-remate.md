# Grafista (15) · Tema 4 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/04-infografia-y-visualizacion-de-datos.md`. Fecha de trabajo
del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema). Entrada: `15-T04-refutacion.md`
y `15-T04-preguntas.md`. Ficheros tocados: el tema y este informe.

## Correcciones, comprobadas en la fuente antes de aplicarlas

| Hallazgo | Comprobación | Aplicado |
|---|---|---|
| G1 · §4 «Qué obliga a la casa»: «la única mención expresa» | Contrato-programa, cláusula tercera, punto 28 (txt, l. 990-999): «…argumentales, textuales, infográficos, o narrativos de tratamiento de redacción periodística, estando siempre conformes con la deontología profesional…». El informe acierta | Sí: la frase pasa a «Son las dos menciones expresas…», con el literal del punto 28 |
| M1 · §4 «Reconstruir no es informar»: «En los sucesos (9.2.12.3…)» | LE, índice y cuerpo: 9.2 «Malos Tratos» (l. 4500) > 9.2.12 «Los modelos informativos» > 9.2.12.3 «Reconstrucciones» (l. 4686). El informe acierta | Sí: «En la información sobre malos tratos (…dentro del apartado 9.2, «Malos tratos», aunque formulada en términos generales)» |
| M2 · misma viñeta: salvedad omitida | LE 9.2.12.3 (l. 4686-4700): literales de «También es arriesgado…» e «En caso necesario, podemos usar una imagen subjetiva de cámara…» confirmados | Sí: añadidos, con la conexión a la infografía de proceso declarada como lectura del tema |
| M3 · sigla LRISP sin uso | El cuerpo dice siempre «Ley 37/2007» | Sí: quitada la entrada de las siglas (el título completo sigue en la ficha y en «Normativa») |

## Laguna L1 · ampliación (contenido nuevo)

Nuevo epígrafe `### Los colores que codifican datos` en §6, antes de «Color, contraste y formato» (unas
400 palabras). Todo cotejado en *Data visualisation: colours* (copia leída el 29-09-2026): «Limit the number
of colours you use» (l. 224) y su desarrollo; «When you have categorical data that cannot be grouped, use a
single colour.» (l. 236); «Use colour consistently» (l. 240); «Consider colour associations» (l. 248-256:
azul/agua, verde/hierba, culturales, tonos similares); paleta categórica, definición (l. 391-393), «Ideally,
use just the first four» (l. 445) y «We recommend a limit of four categories…» (l. 447); paleta secuencial,
definición y «when absolutely necessary» / «do not meet accessibility standards on their own» (l. 711),
«it is best to use a single hue…» (l. 715); ejemplo de quintiles (l. 721). Remite al mapa de coropletas
del epígrafe 3. Fila de Trazabilidad de la guía de colores ampliada con lo que sostiene ahora.

Las preguntas 2, 12, 13 y 14 se contestan ya enteras con el tema. No se ha recortado ninguna pregunta.

## Pasajes cambiados (para la fase 5 bis)

1. Siglas de entrada: fuera «Ley 37/2007 … (LRISP)».
2. §4 «Qué obliga a la casa», primera viñeta (G1).
3. §4 «Reconstruir no es informar», segunda viñeta (M1, M2).
4. §6, nuevo `### Los colores que codifican datos` (L1).
5. Trazabilidad, fila de *Data visualisation: colours*.
6. Ficha: Extensión 9.200 → 9.900 palabras (9.839 medidas por `indice.py`); índice regenerado.

Relectura de antecedentes: «El apartado da una alternativa» remite al 9.2.12.3 de la misma viñeta; «el
epígrafe 3» es «3. Rigor» del tema; «repite la cláusula» tiene delante la Carta 10.1.

## Lentes

- `indice.py`: índice regenerado con el epígrafe nuevo (36 epígrafes).
- `refutar_prosa.py`: 0 hallazgos (la repetición del título de la Ley 37/2007 que aparecía se debía a la
  entrada de siglas quitada).
- `negritas.py` + cotejo normalizado (ligaduras ﬁ, comillas, guiones): todas las negritas nuevas o
  cambiadas están literales en LE, Contrato-programa y guía de colores. Las «no encontradas» restantes
  son previas y ya explicadas en verificación y refutación (saltos de página del LE y fuentes no pasadas
  al script).
- `refutar_exactitud.py` / `refutar_modo.py`: no se corren; los pasajes cambiados no citan preceptos del BOE.

Ampliación: sí (L1). Requiere fase 5 bis.
