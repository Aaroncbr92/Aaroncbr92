# 34 · T20 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/20-prevencion-riesgos-laborales.md`.
Entradas: `34-T20-refutacion.md` y `34-T20-preguntas.md`. Otros ficheros tocados: sólo este informe.
**Amplía contenido nuevo: sí** (L1, L2, L3) → procede la fase 5 bis sobre los pasajes listados abajo.

## Fuentes releídas (24-09-2026)

- `boe.py precepto`: LGSS (BOE-A-2015-11724) art. 156; RD 773/1997 art. 7 (1 redacción); RD 486/1997
  (BOE-A-1997-8669) art. 7 (1 redacción), anexo III (2 redacciones; vigente la de BOE-A-2023-11187, desde
  13-05-2023; los apartados 3.a y 3.b citados son iguales en el volcado de 2022) y anexo IV (1 redacción).
- X Convenio (`documento.py seccion … 26`): art. 26.2.
- INSST: tema 69 TME (línea de la prevalencia); Guía técnica PVD (iluminación, temperatura, humedad, relación
  estrés-TME); NTP 318 (1991), NTP 443 (1995; «Actualizada por la NTP 926», que no está en el repositorio),
  NTP 502 (1998), NTP 1149 (2020), NTP 1226 (2025), en `fuentes/salud-laboral/`.

## Correcciones: todas confirmadas en la fuente y aplicadas

| Hallazgo | Comprobación | Pasaje cambiado |
| --- | --- | --- |
| G1 cita cruzada | El §3 no trata turnos: cierto | §2, tabla de disciplinas (fila Ergonomía y psicosociología) y 1.er párrafo de «Los riesgos específicos del redactor/a»: remiten ahora a la nueva subsección del §2 |
| M1 | Tema 69: «Representan, en el ámbito laboral, el problema…» | §3, TME, «Qué son» |
| M2 | Art. 26.2: «debidamente justificadas» + acumulación trimestral y caducidad | §2, «La organización preventiva de la RTVA», viñeta Comités |
| M3 | Art. 7.2 y 7.3 RD 773/1997, literal | §5, «Utilización (artículo 7)»: añadidos 7.2 y la 2.ª frase de 7.3 |
| M4 | LGSS 156.2.g, literal | §4, tabla del art. 156.2, letra g): ahora entera en negrita literal |
| M5 | Justificación inexacta: cierto | «Lo que este tema no da», punto de voz, estrés y turnos, reescrito |

## Lagunas: se amplía el tema

- **L1 voz + L2 estrés y turnos** → nueva subsección **§2 «Otros riesgos del puesto: estrés, trabajo a turnos y voz»**
  (NTP 318: definición de McGrath, estresores, síndrome general de adaptación; NTP 443: factores psicosociales;
  Guía PVD: estrés-TME; NTP 502: tres grupos de efectos, sueño diurno; NTP 1149: perfiles, nódulos como única
  enfermedad profesional según RD 1299/2006, evaluación, medidas en tres niveles; NTP 1226: disfonía aguda/crónica,
  derivación a ORL, tres ocasiones y periodicidad). Se deja dicho que las NTP no son obligatorias.
- **L3 condiciones ambientales** → §3, «El anexo», tras la letra g): bloque de cifras (RD 486/1997 art. 8 y anexo IV:
  100/200/500/1.000 lux; Guía: 300-500 lux; anexo III 3.a: 17-27 ºC; guía técnica: 23-26 °C verano, 20-24 °C
  invierno; anexo III 3.b: humedad 30-70 %, 50 % con electricidad estática).

## Otros pasajes cambiados por arrastre

Portada (Fuente: añadido RD 486/1997; Extensión 11.298 → 13.033); «Qué se puede preguntar»; índice (regenerado,
34 epígrafes); «Las medidas preventivas del puesto, en resumen» (filas Estrés y turnos, Voz); «Normativa que el
tema invoca» (fila RD 486/1997); «Trazabilidad» (RD 486/1997 y NTP 318, 443, 502, 1149, 1226).

## Preguntas tras el remate

10, 11, 12, 13 y 14 pasan a **entera**. Entera 15 · a medias 0 · no 0.

## Lentes

- `indice.py`: 13.033 palabras, 34 epígrafes.
- `negritas.py` (NTP 318, 443, 502, 1149, 1226, Guía PVD, tema 69, RD 486, RD 773, LGSS, convenio): ninguna
  negrita de los pasajes nuevos o cambiados queda sin fuente; sólo salen los rótulos. El resto de avisos son de
  fuentes no pasadas (Ley 31/1995 del común, NTP 1090/1091, Anuario) y preexistentes.
- `refutar_exactitud.py`: sin avisos nuevos en los pasajes cambiados (los de art. 7 «e) asegurar…», art. 30 y
  Libro de estilo son preexistentes y ya explicados en verificación).
- `refutar_modo.py`: 0. `refutar_prosa.py`: 1 frase repetida introducida («la RTVA no ha publicado la evaluación…»),
  corregida; queda en 0.
- Antecedentes releídos: «los mismos» [los TME] va con aclaración entre corchetes; «ese real decreto» sigue a RD
  486/1997; «El anexo no da cifras» sigue a la exposición del anexo del RD 488/1997.
