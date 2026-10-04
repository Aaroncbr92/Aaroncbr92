# 31-T16 · Remate · Análisis de audiencia radiofónica y digital, indicadores y mejora de contenidos

Fase 5. Rematado el 04-10-2026 (fecha de referencia del encargo: 24-IX-2026), sobre
`31-T16-refutacion.md` y `31-T16-preguntas.md`. **Amplía contenido**: pasa a la fase 5 bis.

## Correcciones comprobadas en la fuente (04-10-2026)

1. **Carta 6.7 (§5, «Lo que manda la Carta»)** — confirmado en
   `documentos/carta-servicio-publico-2024-2029-boja-247-2023.txt`, líneas 454-455: el apartado sigue
   «y a la dinámica del mercado audiovisual digital caracterizado por la evolución permanente.» Se
   completa la cita (se mantiene «completo», que ahora es cierto) y la tercera idea para el examen
   recoge el añadido.
2. **Autoría del comunicado de 8-X-2025** — confirmado en
   `radio/aimc-comunicado-2025-10-comision-seguimiento-digital.txt`: «COMUNICADO DE LA COMISIÓN DE
   SEGUIMIENTO…», firma «La Comisión de Seguimiento». Corregidos la ficha («Fuente»), la frase de
   entrada del §2 («en los comunicados de AIMC y de la Comisión de Seguimiento») y la fila de
   Trazabilidad.
3. **Observación del ap. 126** — confirmado en `documentos/contrato-programa-2024-2026-boja-245-2023.txt`,
   líneas 2346-2351. Se completa la cita con «en general y para el sector productivo de las
   industrias audiovisuales, artísticas y culturales».

## Laguna (pregunta 13): ampliación

Nuevo epígrafe en §2: **«Impresiones, alcance, interacción y retención en las plataformas»**
(tabla de 12 métricas + lectura de la curva de retención + nota sobre la tasa de interacción).
Fuentes descargadas el 04-10-2026 y guardadas en `fuentes/canal-sur/radio/`:

- `meta-ig-media-insights-2026-10-04.txt` (Meta for Developers, «Instagram Media Insights»,
  actualizada el 11-09-2026): *impressions* (y su retirada para lo publicado desde el 2-VII-2024),
  *reach* («Metric is estimated»), *views*, *total_interactions*, *ig_reels_avg_watch_time*,
  *reels_skip_rate*.
- `youtube-analytics-metricas-2026-10-04.txt` (Google for Developers, métricas de YouTube Analytics,
  actualizada el 10-09-2026): vistas, *engagedViews*, *estimatedMinutesWatched*,
  *averageViewDuration*, *averageViewPercentage*, *audienceWatchRatio*.
- `youtube-ayuda-retencion-2026-10-04.txt` (Ayuda de YouTube, 9314415): descenso gradual, picos,
  caídas, introducción de 30 segundos y su recomendación.

No confirmado y declarado en «Lo que este tema no da»: definiciones de X y TikTok (los volcados de
TikTok y Meta ya presentes, `tiktok-dev-media-transfer-guide` y `meta-ig-user-media`, no definen
métricas; las páginas de ayuda de TikTok, Meta Business e IAB Spain se cargan por JavaScript y no
dieron texto) y una definición oficial de la tasa de interacción, que se trata como costumbre de
oficio (decir sobre qué base se divide).

La pregunta 13 se contesta ahora entera con el tema. La 14 (metodología de GfK DAM) sigue como
hueco declarado: no se ha encontrado fuente publicada.

## Pasajes cambiados

- Ficha: «Fuente» (comunicado de la Comisión de Seguimiento; documentación de Meta y Google),
  «Redacción que se estudia» (Meta y Google leídas el 04-10-2026), «Extensión» (9.700 → 10.800).
- Índice: nueva entrada (regenerado por `indice.py`).
- §2 «El medidor digital recomendado…»: frase de entrada de la cronología.
- §2 nuevo epígrafe «Impresiones, alcance, interacción y retención en las plataformas».
- §3 «Los indicadores digitales»: tabla con impresiones, alcance, duración media, retención,
  fidelidad, me gusta y guardados.
- §5 «Lo que manda la Carta»: final de la cita del 6.7 y tercera idea.
- §5 «Más allá de la audiencia»: cita del ap. 126 completa.
- «Lo que este tema no da»: nueva viñeta (X, TikTok, tasa de interacción).
- Trazabilidad: fila del comunicado de 8-X-2025 reatribuida; dos filas nuevas (Meta; Google/YouTube);
  fechas de relectura del 6.7 y del 126.

Releídos los pasajes cambiados: «epígrafe 4» (curva por medias horas, «Leer un programa por
dentro») y «epígrafe 1» tienen su antecedente; las siglas IAB, aea y AIMC están presentadas.

## Lentes

- `negritas.py` (tema contra los `.txt` de `radio/`, Carta y Contrato-programa): 180 negritas, 31 no
  encontradas (antes 32); las 31 son rótulos, fechas y las dos citas del Manual de RTVE, como en la
  verificación. Todas las negritas nuevas están en la fuente. Se quitaron tres negritas de énfasis
  propias (veces, cuentas distintas, tasa de interacción).
- `refutar_prosa.py`: 1 hallazgo (ODEC, ya justificado en la redacción). Se quitó «API» sin
  presentar de la Trazabilidad.
- `indice.py`: 10.782 palabras, 40 epígrafes.
- `refutar_exactitud.py` y `refutar_modo.py`: no se pasan; el tema no desarrolla preceptos del BOE.

## Ficheros tocados

- Modificado: el tema 16.
- Creados: este informe y los tres volcados de `fuentes/canal-sur/radio/` citados arriba.
