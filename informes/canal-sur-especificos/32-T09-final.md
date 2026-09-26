# Productor/a (puesto 32) · Tema 9 · Fase 5 bis

Tema: `temas/canal-sur-especificos/32-productor-a/09-produccion-de-contenidos-grabados-directos-y-multiplataforma.md`.
Alcance: sólo los 7 pasajes que lista `32-T09-remate.md`. Resultado: **0 hallazgos; no se toca el tema.**

Fuentes releídas el 25-09-2026 («hoy» del encargo: 24-09-2026):
- EBU R 128 s3-2023, *Loudness in Radio* (texto de `tech.ebu.ch/docs/r/r128s3.pdf`, ya extraído en el remate): historial, contexto, recomendaciones g) a s) y referencias [1], [3], [4], [5] y [8].
- EBU Tech 3401: portada e historial (título, noviembre de 2023).
- EBU R 128-2023 (texto ya extraído en fases anteriores): recomendaciones r) y s) e historial V5.
- BOE-A-2023-11022 (volcado de `fuentes/canal-sur/`), l. 2223: título oficial de la Ley 11/2023.
- Carta 2024-2029 (`fuentes/canal-sur/documentos/carta-servicio-publico-2024-2029-boja-247-2023.txt`), art. 7 (l. 473-563) y 13.9 (l. 793-795).

## Comprobación por pasaje

| Pasaje | Dato | Fuente | Resultado |
|---|---|---|---|
| 1 | R 128 s3, noviembre de 2023; remisión desde la R 128, rec. s) | R 128 s3, portada; R 128, rec. s) («guidance for Loudness in Radio is given in EBU R 128 s3 [9] and EBU Tech 3401 [10]») | Correcto |
| 1 | «The key concept…» | R 128 s3, p. 3 | Literal |
| 1 | h) e i), con elisiones de [3] y nota 1 | R 128 s3, p. 3 | Literal; [1] = EBU R 128 (referencias) |
| 1 | k) con elisión de [4]; n); p) con elisión de [5] (sin «[...]» porque cierra en «s2») | R 128 s3, p. 3-4 | Literal |
| 1 | Tech 3401, título y fecha; rec. s) | Portada de Tech 3401 (cabecera con «&»); R 128 s3, rec. s) | Correcto |
| 1 | Aplicación al puesto (−23 LUFS, −1 dBTP; distribución aparte; nivel de Canal Sur Radio no publicado) | h), i), g) y k)-n) | Se sigue de la fuente; hueco declarado |
| 2 | URL, SSL, TLS, UMH | Desarrollos usuales; se usan después (l. 944-948, 1197, 1472) | Correcto |
| 3 | «Lo que este tema no da»: sonoridad de Canal Sur y Tech 3401 no leída | — | Coherente con el pasaje 1 |
| 4 | Ley 11/2023, de 8 de mayo, título completo | BOE-A-2023-11022, l. 2223 | Literal |
| 5 | Carta 7.1, 7.2, 7.6 (HD exclusiva desde el 14/02/2024), 7.7 («podrán ser instadas»), 13.9 | Carta, l. 474-563 y 793-795 | Correcto |
| 6 | Fila R 128 s3 (1.ª ed. junio de 2021) y Tech 3401 | Historiales de ambos documentos | Correcto |
| 7 | Portada: «Fuente» con s2 y s3; extensión 16.300 | `indice.py` del remate: 16.274 | Correcto |

## Antecedentes

«la referencia [1]», «el suplemento del *streaming*» (epígrafe nombrado), «recomendación s) del
suplemento» y «(recomendaciones h e i)» tienen su antecedente delante. Siglas del pasaje 1 (UER,
LUFS, dBTP) presentadas en la entrada.

## Lentes

`refutar_prosa.py`: 0 hallazgos. Sin normas citadas en los pasajes nuevos más allá del título de la
Ley 11/2023 (literal), no se corren `refutar_exactitud.py` ni `refutar_modo.py`.

Ficheros tocados: sólo este informe.
