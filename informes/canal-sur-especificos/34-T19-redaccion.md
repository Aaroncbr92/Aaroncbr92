# 34 · T19 · Redacción (fase 2)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/19-inteligencia-artificial-periodismo.md`.
Material: `34-investigacion-C-digital.md` § Tema 19 (RIA, Ómnibus, Carta de París). RTVE (reuso 34-19,
10 %): `temas/documentacion/04-inteligencia-artificial.md` (sólo transcripción, habla y PLN).
AGRUPACION: 34/19 «nuevo».

Se escribe por partes, guardando cada epígrafe.

## Avance

- [x] Cabecera, ficha, siglas, enunciado, «De dónde sale este tema»
- [x] §1 Usos (RIA art. 3.1, 3.3, 3.4 con corrección 2025; NIST y Google/arXiv copiados de RTVE y releídos; RIA 50.2 y 50.4; Carta de París preámbulo; Carta RTVA 4.3 y 7.5 copiados del común)
- [x] §2 Riesgos, sesgos, trazabilidad, supervisión humana (RIA 1.1, 3.2, 5, 10.2.f-g, 14; Ómnibus art. 4 bis; Ley 15/2022 art. 23 copiado del común; Carta de París 1-8; EMFA 18.1.e)
- [x] §3 Marco legal europeo (RIA 3.60 corregido, 4 Ómnibus, 50 con correcciones, anexo III, 99, 111.4, 113 Ómnibus)
- [x] Normativa, Lo que no da, Trazabilidad, índice, extensión

## Fuentes releídas en esta fase (24-09-2026)

- RIA, DOUE-L-2024-81079 (volcado): arts. 1.1, 3 (1-4, 60), 5.1 a)-h), 10.2 f)-g), 14.1-4, 50, 99.3, 99.4 g), 99.8, 113; anexo III (ocho ámbitos, leído entero en sus rúbricas y letras: **ninguno es la actividad periodística**; el 8.b es influir en elecciones; esto cierra el hueco que la investigación dejó abierto).
- Corrección DOUE-L-2025-81474: arts. 3.1 («pueda»), 3.60 y 50.4 («ultrafalsificación»), 111.
- Ómnibus, Reglamento (UE) 2026/1744, DOUE-L-2026-81147: art. 1, puntos 5 (art. 4), 6 (art. 4 bis), 7 (art. 5.1 b bis/b ter, 1 bis, 1 ter), 20 (art. 50.7), 38 (art. 99), 39 (art. 111.4), 40 (art. 113); art. 4 (entrada en vigor). No toca arts. 3.1, 3.60, 5.1 a)-h), 14 ni 50.1-50.6.
- EMFA, DOUE-L-2024-80523: art. 18.1.e) (la corrección DOUE-L-2024-81538 no lo toca).
- Carta de París (rsf.org/en/paris-charter-ai-and-journalism): releída entera el 24-09-2026 (descarga directa); citas en inglés.
- Google, «Understanding searches better than ever before» (25-10-2019); arXiv 1810.04805; NIST «Rich Transcription Evaluation»: releídos el 24-09-2026; las citas de RTVE coinciden. El NIST precisa que la tarea «Who Spoke When» de RT-03S se hizo sobre «broadcast news speech» y telefonía; se añade.

## Copiado del común

Literal del temario común de Canal Sur (no se vuelve a verificar):

- §1, «Lo que dice Canal Sur»: Carta del Servicio Público, art. 4.3 y art. 7.5 (tema 6 del común, «Repaso del articulado de la Carta»).
- §2, «Sesgos»: Ley 15/2022, art. 23 (tema 8 del común, «Medidas por ámbitos», párrafo «Inteligencia artificial (artículo 23)»).

## Copiado de RTVE (sí se verifica)

De `temas/documentacion/04-inteligencia-artificial.md`: §1.2 (diarización, NIST), §2.2 (BERT) y §3 (las tres tecnologías del habla), en §1 del tema. Quitado: el marco de preguntas de examen de RTVE («la respuesta oficial», distractores, tablas de opciones), el módulo prosódico y los tokens (sólo plantilla, sin fuente), la visión artificial (no la pide este enunciado) y el uso documental del archivo. Negritas de énfasis pasadas a redonda: sólo va en negrita lo literal.

## Lo que no se pudo confirmar

- Pautas publicadas de Canal Sur sobre uso de IA en la redacción: no localizadas (el Libro de estilo es de 2004).
- Fuente técnica verificable para traducción automática y resumen automático: no localizada; se dice como oficio.
- Autoridad española de supervisión del RIA: no leída; no se nombra.
- Régimen español de multas a organismos públicos (art. 99.8 RIA): no leído.

## Ficheros tocados

Nuevo: el tema. Este informe. Nada más.

## Cierre de la fase

- Extensión: 6.017 palabras, 24 epígrafes (`indice.py`). `refutar_prosa.py`: 0 hallazgos.
- Para verificar (fase 3): todo menos lo listado en «Copiado del común». Puntos delicados: redacción
  del art. 4 tras el Ómnibus; asimetría 50.4 párr. 1 / párr. 2; calendario del art. 113 reformado;
  lectura del anexo III (ningún ámbito periodístico); art. 99.4.g) (multa del art. 50).
- Incidencia heredada de la investigación: `doue.py` no detecta el Ómnibus en la cabecera del RIA;
  cualquier tema que cite el RIA debe leer DOUE-L-2026-81147 aparte.
