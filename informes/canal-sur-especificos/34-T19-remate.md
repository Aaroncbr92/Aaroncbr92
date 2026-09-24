# 34 · T19 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/19-inteligencia-artificial-periodismo.md`.
Entrada: `34-T19-refutacion.md` (M1, M2, M3, L1, L2 y el opcional 50.3) y `34-T19-preguntas.md` (10 y 15 «a medias», 14 «no»).
Otros ficheros tocados: sólo este informe.

## Fuentes releídas antes de aplicar (24-09-2026)

- RIA, `fuentes/canal-sur/DOUE-L-2024-81079.md`, art. 50.1-50.5: confirmadas literales la cláusula «teniendo en cuenta las circunstancias y el contexto de utilización», la salvedad de los sistemas autorizados por ley (50.1, con «salvo que estos sistemas estén a disposición del público para denunciar un delito penal») y la de 50.2 in fine; 50.3 (reconocimiento de emociones y categorización biométrica).
- Ómnibus, `DOUE-L-2026-81147.md`: el art. 50 del RIA sólo cambia en el apartado 7 (el «6) En el artículo 50» de la línea 394 modifica el Reglamento (UE) 2018/1139, no el RIA). Art. 5.1 ter confirmado.
- Corrección `DOUE-L-2025-81474.md`: sólo sustituye «puede» por «pueda»; no explica el alcance (confirma M2).
- Carta de París (copia de trabajo de rsf.org en el scratchpad, descargada el 24-09-2026 en la refutación): principios 1, 2, 3 y 4, literales confirmados.

Ninguna corrección del informe resultó errónea; se aplicaron todas.

## Pasajes cambiados

1. **Portada, «Extensión»**: 6.311 → 6.909 palabras.
2. **Qué se puede preguntar**: añadidos la evaluación previa (Carta de París) y los riesgos del análisis con IA.
3. **§1, «Qué es un sistema de IA»** (M2): suprimido «la capacidad de adaptación es posible, no necesaria»; ahora «el texto de la corrección no explica el alcance del cambio».
4. **§1, «Apoyo a la redacción», 2.º punto** (M1): añadida la exclusión de los sistemas autorizados por ley para perseguir delitos (50.2).
5. **§1, «Verificación y análisis»** (L2, pregunta 15): nuevo párrafo sobre el análisis con IA, marcado como oficio, con cuatro riesgos enlazados: confidencialidad (principio 1), datos personales (art. 2.7 y tema 16), comprobación con el original y sesgo de automatización (art. 14.4.b).
6. **§2, «Riesgos»** (L1, pregunta 14): nuevo párrafo sobre el principio 3 de la Carta de París, con sus literales.
7. **§2, «Supervisión humana»** (L1): principio 2 («Editorial teams must clearly define…») y principio 4 («to humans»).
8. **§3, art. 5** (M3): una frase sobre el 5.1 ter.
9. **§3, art. 50** (M1 y opcional): 50.1 con «teniendo en cuenta…» y la salvedad penal literal; 50.2 con su salvedad penal literal; nuevo punto 50.3, en resumen.
10. **Lo que este tema no da**: añadido el análisis de documentos con IA a lo que no tiene fuente técnica localizada.
11. **Trazabilidad**: Carta de París «preámbulo y principios 1 a 8»; en la fila de oficio, «qué es el análisis con IA».

Releídos los pasajes: cada remisión («epígrafe 2», «epígrafe 3», «más abajo», «la letra b bis)», «el artículo») tiene su antecedente.

## Lentes

- `indice.py`: índice regenerado, 24 epígrafes, 6.909 palabras (el tema no está en `portadas.tsv`; la extensión de la portada se puso a mano).
- `negritas.py` (RIA, corrección 2025, Ómnibus, EMFA, Carta de París, `fuentes/ia/`): 78 cotejadas; 3 «no están» (Carta del Servicio Público y Ley 15/2022, copiadas del común, cuyas fuentes no se pasaron); 7 atribuidas a otro artículo, falsos positivos por la estructura del Ómnibus (todo va en su art. 1) y de la corrección. Todas las negritas nuevas, encontradas.
- `refutar_exactitud.py` (RIA, Ómnibus, EMFA): 10 «no literales», todos preexistentes y ya explicados (redacción corregida o del Ómnibus cotejada contra el original; común). Ninguno en los pasajes nuevos.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 1, «PRIOR» como sigla, falso positivo (rótulo en mayúsculas del principio 3, cita literal).

## Resultado

Amplió contenido nuevo: **sí** (párrafo de análisis con IA en §1, principio 3 en §2, 50.3 en §3). Procede la fase 5 bis sobre los pasajes 5-9.
Preguntas que pasan a «entera»: 10, 14 y 15.
