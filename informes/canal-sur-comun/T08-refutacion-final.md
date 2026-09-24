# T08 · Refutación final (fase 5 bis acotada, modo ahorro) · Normativa sobre igualdad

Relectura acotada según `CICLO.md` («Fase 5 bis acotada»): sólo el pasaje que lista
`T08-remate.md` (bloque RD 1026/2024, viñeta del artículo 5, líneas 1565-1573 del
tema). Fichero tocado: sólo este informe; el tema no requirió corrección.

## Comprobación del pasaje

- Fuente: `fuentes/canal-sur/BOE-A-2024-20402.md`, `grep -n -A40 "^Artículo 5"`,
  leída el 24-09-2026.
- Las cuatro citas literales del pasaje (**«dentro del plazo máximo de los tres
  meses siguientes a la entrada en vigor de este real decreto»**; **«el plazo
  anterior empezará a contarse desde el momento en que alcancen el número de
  personas trabajadoras indicado en el artículo 2»**; **«o en el supuesto de que
  el convenio colectivo de aplicación no incluya las medidas planificadas»**;
  **«se continuarán aplicando hasta que entren en vigor las que posteriormente se
  puedan acordar»**) coinciden palabra por palabra con el artículo 5.1 (párrafos
  primero y segundo) y 5.3 del volcado. Sin hallazgo.
- Antecedentes: «este real decreto» remite al RD 1026/2024 nombrado dos frases
  antes (línea 1555); «el artículo 2» remite al artículo 2 del mismo real decreto,
  citado en la viñeta inmediatamente anterior (línea 1561). Ambos antecedentes
  están delante y son correctos.

## Lentes automáticas

```
python3 herramientas/refutar_prosa.py temas/canal-sur-comun/08-igualdad.md
→ 2 hallazgos, los mismos ya explicados en verificación/refutación (fórmula «la
  Ley 9/2018… dio la redacción actual» ×5, no relleno; «LGBTI» dentro de cita
  literal del Consejo Andaluz LGBTI). No tocan el pasaje relevante.

python3 herramientas/negritas.py temas/canal-sur-comun/08-igualdad.md \
  fuentes/canal-sur/BOE-A-2008-2492.md fuentes/canal-sur/BOE-A-2022-11589.md \
  fuentes/canal-sur/BOE-A-2023-5366.md fuentes/canal-sur/BOE-A-2026-16172.md \
  fuentes/canal-sur/BOE-A-2024-20402.md fuentes/canal-sur/BOE-A-2008-1185.md \
  fuentes/canal-sur/BOE-A-2005-655.md
→ 426 negritas cotejadas ; 7 «no están» ; 38 «¿art.?» — mismas cifras que
  T08-remate.md, mismos falsos positivos ya explicados (anclas en números de
  otras leyes o de plazos cercanos al marcador, incluida la viñeta del artículo 5
  del RD 1026/2024, que ancla en el «3» de «tres meses» y está, comprobado, en el
  artículo 5). Ningún hallazgo nuevo.
```

`refutar_exactitud.py`, `refutar_citas.py`, `refutar_modo.py` y `refutar_documento.py`
no aplican: fase 5 bis acotada sólo pide prosa y negritas más la comprobación
manual del pasaje (`CICLO.md`).

## Quince preguntas (`T08-preguntas.md`), contestadas sólo con el tema delante

1. b — líneas 671-672, 856-857 (art. 4.16 remitido). Entera.
2. c — líneas 671-672 y cuadro de multas del bloque de sanciones (arts. 77.c/80.3). Entera.
3. b — líneas 1851-1853 (58.1, párrafo primero). Entera.
4. b — línea 1859 (58.2). Entera.
5. b — líneas 39 (umbral 40-60 %) y 1844-1847 (DA 3.ª Ley 18/2007, remite al 3.3 Ley 12/2007). Entera.
6. b — línea 990 (art. 6.2.b, «por error»). Entera.
7. b — línea 1103 (art. 22.3). Entera.
8. c — línea 1278 (art. 41.4, «cinco años sin posibilidad de renovación»). Entera.
9. b — línea 1692 y bloque de la Autoridad (art. 40.e, interesa la actuación de la AGE). Entera.
10. c — línea 1793 (art. 51, «tres años» para graves; el enunciado de la pregunta habla de graves, no de muy graves). Entera.
11. b — línea 1070 (art. 9.5). Entera.
12. b — líneas 1545 y 1890 (art. 15.1). Entera.
13. c — línea 1631 (art. 43.2, «asistidas en el procedimiento por sus representantes legales»). Entera.
14. b — línea 1651 (art. 44.8, «en el plazo máximo de tres meses desde la comparecencia inicial»). Entera.
15. a — líneas 1741-1742 (art. 77.2, «exceda los 100.000 euros»). Entera.

Resultado: 15 enteras, 0 a medias, 0 sin respuesta. Coincide con `T08-preguntas.md`.

## Cuadro de lentes

| Lente | Tramos comprobados | Hallazgos | Estado |
|---|---|---|---|
| Comprobación manual del pasaje (art. 5 RD 1026/2024) | 1 pasaje, 4 citas literales | 0 | limpio |
| Antecedentes del pasaje | 2 («este real decreto», «el artículo 2») | 0 | limpio |
| `refutar_prosa.py` | tema completo | 2 (ya explicados, no defecto) | limpio |
| `negritas.py` (7 fuentes) | 426 negritas | 0 nuevos (7 no están / 38 ¿art.? ya explicados) | limpio |
| Quince preguntas de `T08-preguntas.md` | 15 | 15 enteras | limpio |

Cero hallazgos nuevos: la corrección del remate está bien aplicada y el tema no
necesita más cambios.
