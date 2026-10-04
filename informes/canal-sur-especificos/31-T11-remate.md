# 31-T11 · Fase 5 · Remate · Producción multiplataforma

Fecha: 4-X-2026 (referencia del encargo: 24-IX-2026). Tema:
`temas/canal-sur-especificos/31-presentador-productor-de-radio/11-produccion-multiplataforma-podcast-redes-videorradio-clips-directos-participacion.md`.
Entrada: `31-T11-refutacion.md` (M1-M4, L1) y `31-T11-preguntas.md` (9 a medias, 13 no).

## Correcciones, comprobadas en la fuente

| Hallazgo | Comprobación | Aplicado |
| --- | --- | --- |
| M1 | AIMC, *Normas de radio en EGM*, «Aclaración de la asignación horaria de audiencia» (AIMC 24/07/2019), releída el 4-X-2026: confirma la asignación a la cadena en el momento de escucha y al programa que se emite entonces. El informe recortaba la segunda cita («...que se esté emitiendo»); se pone entera («...en el día y cadena en el que se está escuchando el podcast») | Sí. Quitada la frase sin fuente «se mide por otra vía» |
| M2 | El 99 es punto de la cláusula tercera | Sí: «el punto no se la exige» |
| M3 | Definición literal en la misma página de AIMC | Sí, como definición del medidor, no normativa; «Lo que este tema no da» ajustado |
| M4 | — | Sí, sin sigla: «el híbrido y el retorno al oyente» |

## Laguna L1 (ampliación)

Las páginas de ayuda de usuario de TikTok e Instagram no se pudieron leer (se cargan por JavaScript;
la de TikTok devuelve sólo el menú). Se leyó, el 4-X-2026, la documentación oficial para
desarrolladores de cada plataforma, guardada en `fuentes/canal-sur/radio/`:

- `meta-ig-user-media-2026-10-04.txt` (Meta for Developers, «Contenido multimedia de usuario de
  Instagram»): reels 15 min máx./3 s mín., 9:16 recomendado; portada 9:16 recortada al centro, 1:1 en
  noticias; JPEG ≤ 8 MB; historias 60 s.
- `tiktok-dev-media-transfer-guide-2026-10-04.txt` («Media Transfer Guide», actualizada 4-8-2026):
  3 min para todos los creadores, 5 o 10 para algunos; 360-4096 px; no da relación de aspecto.

Se avisa en el tema de que son límites de la vía de programación y que los de la aplicación pueden
ser otros. Facebook y la relación de aspecto de TikTok quedan como hueco declarado. La pregunta 13
pasa a contestarse para Instagram y, a medias, para TikTok (duración sí, relación de aspecto no).

## Pasajes cambiados

1. Portada: «Fuente» (+ documentación para desarrolladores de Instagram y TikTok, AIMC),
   «Redacción que se estudia» (fecha de lectura 4-10-2026), «Extensión» 13.700 → 14.200.
2. Siglas: + AIMC, EGM; «JPG (o JPEG)».
3. §2 «El pódcast en la ley y en Canal Sur»: párrafo nuevo con la definición de AIMC.
4. §2 «Producir un pódcast», viñeta «Medición»: reescrita con las dos citas literales.
5. §5: subepígrafe nuevo «Reels de Instagram y vídeos de TikTok» (índice regenerado).
6. §7 «Lo que obliga...: el punto 99»: «la cláusula» → «el punto».
7. §7 remisiones finales: «N-1» quitado.
8. «Lo que este tema no da»: viñetas de la definición de pódcast y de las especificaciones de plataformas.
9. Trazabilidad: fila de AIMC ampliada; filas nuevas de Meta y TikTok.

Releídos los pasajes: «el punto» tiene delante el punto 99; «esa definición»/«ella» remiten a la de AIMC.

## Lentes

`indice.py` (13.892 palabras, 44 epígrafes); `refutar_prosa.py`: 0 hallazgos tras quitar una frase
repetida («tema 16») y presentar JPEG; `negritas.py` con AIMC, Meta y TikTok: las 11 citas nuevas,
literales. Las demás lentes no se repiten: lo de norma no ha cambiado.

## Ficheros tocados

El tema; este informe; las dos fuentes nuevas de `fuentes/canal-sur/radio/`.

Amplió: sí (pasa a la fase 5 bis).
