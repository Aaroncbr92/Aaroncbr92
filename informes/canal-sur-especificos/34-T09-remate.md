# 34 · T09 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/09-presentacion-locucion-comunicacion-oral.md`.
Entradas: `34-T09-refutacion.md` (3 menores, 3 lagunas, 1 menor sin pregunta) y `34-T09-preguntas.md` (15; no 3, a medias 2).
**Amplía contenido nuevo: sí** (L1, L2, L3 y la advertencia de ME-RTVE 6.3.1). Hace falta la fase 5 bis sobre los pasajes 4 a 8.

## Fuentes releídas antes de aplicar (24-09-2026)

- LE-CS `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 3.14 (l. 1816-1848), 8.3 y 8.3.1-8.3.2 (l. 4124-4200), 8.6 (l. 4340-4345).
- ME-RTVE `_el-lenguaje.txt` 6.3.1 (l. 111-115).
- `fuentes/fabricantes/Autocue_portada.txt` l. 5 y 106 (captura del 02-09-2026).

Todas las correcciones y lagunas del informe de refutación se comprobaron en la fuente y eran correctas. No se descartó ninguna.

## Pasajes cambiados

| # | Hallazgo | Dónde | Cambio |
|---|---|---|---|
| 1 | M1 | §4, 2.º guion | «debe prever, **«hasta donde sea posible»**, **«todo lo que pueda planificarse»**» (8.3) |
| 2 | M2 | §6 Qué es | Cita de Autocue completa hasta «...and more connected audiences.», con traducción |
| 3 | M3 | §6 Qué es | Quitado: «el nombre que se oye en muchas redacciones», «el propio fabricante llama teleprompters a sus autocues» y «marca convertida en nombre común». Ahora dice: el fabricante llama a sus aparatos prompters y teleprompters. Decir «autocue» por el aparato queda como costumbre de oficio |
| 4 | L3 | §6 Cómo se usa | Nuevo: el paso no puede ser imprescindible; si lo es, **«el redactor está obligado a comunicárselo al editor y el presentador, y pactar sus términos con quien se encargue de leerlo en cámara»** (3.14) |
| 5 | L2 (3.14) | §6 Cómo se usa | Nuevo párrafo: formalidad atenuable con pronunciación más relajada o giros coloquiales moderados; **«debe administrarse con prudencia»** |
| 6 | L2 (8.6) | §8 El presentador | Nuevo: **«Por encima de las normas, cada uno puede usar fórmulas particulares [...] sin perder rigor»** |
| 7 | L1 | §8, nuevo `### La conexión en directo` | Mirada, micrófono vertical sobre el esternón y de corbata en interiores habilitados; protocolo al mínimo; no dirigirse al presentador; segunda persona / plural; **«en la despedida sólo habla el presentador»** (8.3.2) |
| 8 | Menor sin pregunta | §2 Ritmo | Nuevo: advertencia de ME-RTVE 6.3.1 sobre las pausas innecesarias de presentadores e informadores |
| 9 | Cambios derivados | Portada, «Qué se puede preguntar», índice, Trazabilidad | Extensión de 2.691 a 3.088 palabras; dos preguntas posibles nuevas; epígrafe en el índice; fila de Autocue (fecha de captura, nueva formulación) y fila de costumbre de oficio («autocue» como nombre del aparato) |

Se releyó cada pasaje cambiado para comprobar que tiene antecedente: «El mismo apartado» → 3.14, que se acaba de citar; «Y advierte» → el Manual de RTVE, que es el sujeto de la frase anterior; «Y añade» → la cita de 8.6 del mismo párrafo; «El fabricante, por tanto» → Autocue.

## Lentes

- `indice.py`: 3.088 palabras, 21 epígrafes; índice regenerado. El tema no está en `portadas.tsv`, así que la cifra de la ficha se puso a mano.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (LE-CS, ME-RTVE ×3, Autocue): 85 cotejadas, 14 «no están». Todas son negritas que ya estaban antes de este remate y que la refutación dio por literales: el volcado del PDF parte las palabras con la ligadura «ﬁ» y en los saltos de página. Entre ellas, «todo lo que pueda planificarse» (en la fuente, «planiﬁcarse»). Todas las negritas nuevas se encuentran en la fuente.
- No se corren `refutar_exactitud.py` ni `refutar_modo.py`, porque el tema no cita normas.

## Preguntas tras el remate

Con el tema ampliado, las 15 se contestan enteras (6, 12, 13, 14 y 15 ya tienen respuesta en el tema). No se recortó ninguna pregunta.

Ficheros tocados: el tema y este informe.
