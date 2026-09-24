# 34 · T07 · Verificación (fase 3)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/07-redaccion-audiovisual-television.md`.

## Fuentes releídas

| Fuente | Cómo | Leída |
|---|---|---|
| Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004) | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.pdf`, texto por página con PyMuPDF (página impresa = índice + 1, comprobado en pp. 44-46) | 24-09-2026 |
| Manual de estilo de RTVE, cap. 2 TVE | Volcado `fuentes/informacion/RTVE_manual-de-estilo_tve.txt` (fechado 02-09-2026) **y** página viva https://manualdeestilo.rtve.es/tve/ (HTTP 200) | 24-09-2026 |

Copiado del común: ninguno (informe de redacción), nada que saltar. Lo copiado de RTVE sí se ha verificado contra la página viva.

## Método

Script: cada negrita del tema buscada en el texto normalizado (ligaduras, comillas, espacios) de cada página del Libro de estilo y en el Manual de RTVE; página hallada frente a página citada; luego lectura de las secciones 3.1-3.17, cap. 6 y cap. 8 enteras para salvedades y epígrafes. 130 negritas: todas localizadas salvo 2 no literales (abajo).

## Correcciones (error del catálogo entre corchetes)

| § | Qué había | Qué queda | Fuente |
|---|---|---|---|
| Siglas | «vídeo» frente a lo que «otras redacciones» llaman «pieza» (sin fuente) | frente a la «pieza» del Manual de RTVE | ME-RTVE 2.4.4 [9] |
| 1 | Máximas de Grice en una negrita corrida | cuatro negritas, porque en el original van numeradas | LE 3.1, p. 44 [negrita no literal] |
| 2 | «En otras redacciones» la entradilla es el texto del presentador (sin fuente) | quitado; se remite al «paso de locutor» | LE 3.13, p. 55 [9] |
| 2 | stand up «8.1.1» y sin «En caso de duda» | 8.1, consideración 1.ª, con la salvedad | LE p. 113 [8][6] |
| 2 | Entradilla sin «Si fuera imprescindible, se coordinarán…» | añadido | LE 8.2.2, p. 115 [6] |
| 2 | Supuestos de aparición sin la regla general | añadido «sólo… cuando sea imprescindible» (8.2) y completado el 3.er supuesto | LE pp. 115 [6] |
| 4 | Total: faltaba «sólo cuando sea preciso» | añadido | LE 3.17.1.4, p. 60 [6] |
| 4 | Canal 2 original / canal 1 doblaje atribuido a la voz superpuesta | es el caso de los subtítulos («En este caso») | LE 3.7.1, p. 52 [1] |
| 6 | Entrevista 3 min sin «la fórmula es inhabitual» | añadido | LE 3.17.2.1, p. 62 [6] |
| 6 | Titular 10 s y recurso 2 s sin «recomendable» | añadido | LE 3.6 p. 50; 6.3.2 p. 91 [4] |
| 6 | Gráfico «no más de cuatro o cinco…» en negrita | «que no incluya» fuera; negrita literal | LE 3.16, p. 57 [negrita no literal] |
| 7 | Tópicos resumidos («canciones, películas o dichos») | lista completa y «ni en el texto ni en los rótulos» | LE 3.6.1, p. 50 |
| 8 | Rótulo de archivo «cap. 2», sin supuesto | 2.1.2 y el supuesto (noticia sin imagen actual) | ME-RTVE 2.1.2 [8][6] |
| 8 | Concentración de recursos sin epígrafe; Trazabilidad decía 2.2.8 | 2.2.6 | ME-RTVE [8] |
| 9 | Escaleta «documento vivo» como costumbre de oficio (venía de RTVE, sin fuente) | sustituido por el literal de 6.1 sobre comunicar los cambios | LE 6.1, p. 88 [9] |
| 9 | Nombre en escaleta, sin la excepción | añadida la excepción del vídeo terminado antes de la escaleta | LE 6.1.1, p. 88 [6] |
| 9 | Minutaje sin «tanto como permitan las circunstancias» | añadido | LE 6.3, p. 91 [6] |
| 9 | Sistema integrado de redacción / teleprónter (de RTVE, cuya propia fuente declara no haber leído al fabricante) | **quitado**; en su lugar, el literal de 6.1.2 sobre fijar textos en escaleta | LE 6.1.2, p. 89 [9] |
| 10 | Agilidad: «recurso corto, dos» | «dos como mínimo recomendable» | LE 6.3.2 [4] |
| 11 | Reemisión citada en p. 56 | pp. 56-57 | LE 3.15 [8] |
| 11 | Pervivencia de 24 h sin a qué vídeos ni desde cuándo | «en general informes, crónicas y reportajes», «desde su primera emisión» | LE 3.15.1, p. 57 [6] |
| 11 | Cifras «(3.16)» | 3.16.1 y 3.16.2, p. 58 | LE [8] |
| Trazab. | Fila «Costumbre de oficio» | quitada: ya no queda nada sin fuente | — |

## Comprobado sin cambios

Resto de negritas (≈115): literal y página coinciden. Errata «e para» (3.2.2, p. 46): es del original. Paráfrasis señaladas por la redacción (crónica «salvo casos excepcionales», ahora literal; «cuatro supuestos»; Agilidad) cotejadas. Seis citas de RTVE (2.2.8, 2.4.4, 2.1.2, 2.2.6) idénticas en el volcado y en la página viva.

Sin norma citada: no proceden `negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`. `indice.py`: 4.396 palabras, 29 epígrafes (Extensión actualizada). `refutar_prosa.py`: 0 hallazgos. Pasajes cambiados releídos: cada «En este caso», «ésta», «(§ 5)» tiene su antecedente.

## Para la fase 4

- El Libro de estilo es de 2004; si hay versión posterior, no consta (ya en «Lo que este tema no da»).
- Guion informativo: el tema sólo da escaleta, partes de emisión y textos; no hay formato de guion de CSRTV publicado.

Ficheros tocados: el tema y este informe.
