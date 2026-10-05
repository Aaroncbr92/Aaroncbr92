# Refutación · Oficial Técnico Electricista (27) · Tema 14 · Medidas eléctricas e instrumentación

Fase 4 (sólo refuta; no corrige). Tema:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/14-medidas-electricas-e-instrumentacion.md`
(1.202 líneas, 44 epígrafes). Fuentes leídas el 05-10-2026 (reloj del sistema; el encargo dice
«hoy es 24-09-2026»; las redacciones de las ITC citadas no cambian entre ambas fechas, según
`BOE-A-2002-18099.redacciones.tsv`).

Ámbito de la exactitud: todo menos lo listado en `27-T14-redaccion.md` bajo «Copiado de RTVE sin
cambios» (28 pasajes; «Copiado del común»: nada). La cobertura mira el tema entero.

## Resultado

| | Número |
|---|---|
| Errores graves | 0 |
| Errores menores | 2 |
| Lagunas de cobertura | 2 (más un hueco ya declarado) |
| Preguntas (`27-T14-preguntas.md`) | 15: 12 entera, 1 a medias, 2 no |

## Lente 1 · Exactitud

### Qué se ha cotejado

- `negritas.py` contra REBT, Real Decreto 614/2001 y las cinco fuentes técnicas: 187 negritas,
  8 «no está». Las 8 se han comprobado a mano: 2 son rótulos de forma; las 5 del INSST y la de AEMC
  sí son literales cuando se normaliza el guion blando (U+00AD) y la ligadura «ﬁ».
- REBT, en el volcado: ITC-BT-01 (corriente de fuga); ITC-BT-03, apéndice I, 2.1.2 y 2.2 (lista
  completa y su orden, «según proceda»); ITC-BT-05, 2.1 y 3; ITC-BT-18, 3.3, 9 (con la salvedad de
  la rápida eliminación de la falta), tablas 3, 4 y 5 y 12; ITC-BT-19, 2.9 entero (tabla 3, nota,
  regla de los 100 m, generador de 1 mA, polaridad, receptores, circuitos electrónicos, aislamiento
  bajo, rigidez y su excepción, fugas); ITC-BT-24, 4.1.1 (Zs × Ia ≤ U0, tabla 1) y 4.1.2
  (RA × Ia ≤ U, selectivo de 1 s). Fechas de redacción de la ficha: coinciden con el `.tsv`.
- Real Decreto 614/2001: anexo I, 8, 10, 13 y 14; anexo II, B.3 y B.4 (rótulo de alta tensión);
  anexo IV, A.1-A.6 y B.2, 2.ª; anexo V, B.1.2.
- Fuentes técnicas, en su contexto (no sólo la literalidad): INSST (procedimiento de pruebas y su
  lista «al menos», descarga tras el ensayo de aislamiento, verificación de ausencia de tensión);
  Fluke (tabla de categorías, reglas, 0,01 Ω / 10 MΩ, tres pasos); Circutor (0,45 IΔN, 600/1000 ms,
  60 ms y 6/10/30 mA, rampa 0,30-1,40 IΔN, criterio alterna/pulsante, 25/50 V); AEMC (rotulación
  X-Y-Z / X-P-C / C1-P2-C2, área del 62 %, ±10 %, tolerancias, «no se puede dar una distancia»,
  Wenner A > 20B y ρ = 2πAR, profundidad ≈ A, electrolitos y temperatura, 2,4 kHz, 5 A, lectura que
  incluye el enlace al neutro); FLIR (fallos de baja tensión, «calentarse antes de fallar», cables no
  cargados, ventana como espejo, cinta de calibración, viento y lluvia, seis requisitos, 60 × 60,
  640 × 480, 307.200, 63,9/42,7 °C, 30 mK, ±2 %/±2 °C, cuatro pasos, puntos fríos).
- Aritmética: tabla de RA máxima, 0,5/3 ≈ 0,17 MΩ, 2·400 + 1000 = 1.800 V, ρ = 50 × 2 = 100 Ω·m y
  la pica de 4 m a 25 Ω: correctas.
- Remisiones a los temas 1, 3, 5, 6 y 8: los epígrafes citados existen y tratan lo que se dice.
- `refutar_prosa.py`: 0 hallazgos.

### Hallazgos

**M1 · Error 6 (salvedad de contexto) · epígrafe 1.3, líneas 270-274.** El tema dice que la guía del
INSST cita la UNE-EN 61243-3 para detectores bipolares de baja tensión «y recuerda que, antes de
usarlo, **es importante comprobar su tensión o gama de tensiones nominales de funcionamiento, así
como el estado de las puntas de prueba y de las pilas o baterías**». En la guía (pp. 33-34), esa
frase está en el apartado **Verificación de la ausencia de tensión en instalaciones de alta
tensión**, referida a los detectores de las UNE-EN 61243-1 y -2; el apartado de baja tensión
(p. 35) no la repite. Corrección propuesta: decir que la guía lo indica para los detectores de alta
tensión, o quitar «y recuerda que, antes de usarlo». De paso, la misma página 33 trae algo que sí es
general y que el tema no usa: comprobar el verificador antes y después es **obligatorio** en alta
tensión y **recomendable** en baja; encaja junto al método de los tres pasos de Fluke.

**M2 · Error 9 (afirmación que contradice el propio tema) · epígrafe 3.5, línea 561.** «La pinza
es, por dentro, un transformador de intensidad». El epígrafe 3.2 distingue la pinza de
transformador de corriente de la de efecto Hall, y el 3.2 y el 2.1 avisan de que la de
transformador no mide continua. Corrección propuesta: «La pinza de alterna es, por dentro, un
transformador de intensidad».

Sin errores graves: ningún precepto mal citado, ninguna redacción derogada, ningún «podrá» por
«deberá», ningún recuento que falle.

Observación, no hallazgo: «IEC 61010 (en España, UNE-EN 61010)». Las fuentes leídas dan IEC 61010
(Fluke) y EN 61010-1 (Circutor); la adopción UNE no está leída. Es una equivalencia notoria y el
tema no saca de ella ningún dato.

## Lente 2 · Cobertura del enunciado

Enunciado: multímetro, pinza amperimétrica, telurómetro, medidor de aislamiento, analizador de
redes y termografía básica. Las seis rúbricas tienen epígrafe propio y siguen el orden del
enunciado. La pinza y el telurómetro están muy bien cubiertos; el medidor de aislamiento cubre todo
el REBT. Las lagunas:

**L1 · Medidor de aislamiento: ensayos dependientes del tiempo (índice de polarización, índice de
absorción).** El tema dice que el aislamiento de un devanado vale por su evolución (5.6), pero no
explica estas dos funciones, que traen los medidores de aislamiento de mantenimiento. Es una
pregunta de teoría probable (pregunta 12: **no**). Ampliar en 5.6 con fuente de fabricante (p. ej.
la guía de pruebas de aislamiento de un fabricante de megóhmetros) o con la norma de máquinas
rotativas, y citar las cifras de la fuente. Si no se encuentra una fuente, hay que declararlo en
«Lo que este tema no da».

**L2 · Analizador de redes: magnitudes de calidad de onda (distorsión armónica total, factor de
cresta).** El 6.2 dice que el analizador mide «armónicos», pero no da la magnitud que los resume ni
cómo se lee. Es pregunta de test frecuente (pregunta 14: **no**). Ampliar en 6.2 con documentación
de un fabricante de analizadores (Circutor o Fluke). El tema ya usa los dos. Los límites
admisibles de esas magnitudes pueden seguir declarados como no dados.

**Hueco ya declarado (no cuenta como laguna):** criterios numéricos de gravedad en termografía
(pregunta 15: **a medias**). El tema lo declara en 7.5 y en «Lo que este tema no da». Si el remate
amplía, puede buscar una tabla de prioridad por ΔT publicada por una asociación o un fabricante.
Si no, queda como está.

## Recomendación para la fase 5

Corregir M1 y M2: son dos pasajes y basta con Sonnet. Para L1 y L2 hay que ampliar con fuente
nueva, y eso es trabajo de Opus. Si se amplía, toca la fase 5 bis sólo sobre 5.6 y 6.2.

## Ficheros tocados

`informes/canal-sur-especificos/27-T14-preguntas.md` y este informe, los dos nuevos. El tema no se
ha tocado.
