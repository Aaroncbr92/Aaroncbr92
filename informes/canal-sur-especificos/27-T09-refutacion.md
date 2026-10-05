# Refutación · Oficial Técnico Electricista (27) · Tema 9 · Climatización y frío industrial

Fase 4 (refutar, no corregir). Tema:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/09-climatizacion-y-frio-industrial-en-edificios-y-salas-tecnicas.md`.
Leído entero (≈1.330 líneas, 16.267 palabras con `wc`). Fuentes leídas el **05-10-2026** (reloj del
sistema; el encargo dice «hoy es 24-09-2026»; ninguna redacción citada cambia entre las dos fechas:
la IF-14 rige desde el 10-05-2025 y la IF-02, no reproducida, desde el 19-08-2026).

Ficheros tocados: este informe y `27-T09-preguntas.md`. El tema no se ha tocado.

## Fuera de la lente de exactitud

- «Copiado del común»: nada.
- «Copiado de RTVE sin cambios»: nada (`27-T09-redaccion.md`: todo lo de RTVE está adaptado y cita
  normas). Se mira, pues, el tema entero.

## Fuentes releídas

| Fuente | Qué se ha cotejado | Resultado |
|---|---|---|
| RSIF, BOE-A-2019-15228 (arts. en redacción única; art. 9 de 01-07-2021) | arts. 2, 8, 9, 18 (a-q), 20.2, 21, 22, 26-29 | Literal y bien atribuido. Diecisiete letras en el art. 18: cuadra |
| IF-14 (vig. 10-05-2025) | 1.1.1, 2.1, 2.2.8, 2.6, 3.1, 3.3 | Literal. Hallazgo M1 y laguna de la pregunta 15 |
| IF-17 (redacción única) | 1.6, 2.3.u, 2.4.c, 2.5.1, 2.5.2, 2.5.3.2-2.5.3.5 | Literal. Hallazgo M3 y laguna de la pregunta 14 |
| RITE, BOE-A-2007-15820 (vig. 01-07-2021) | IT 1.1.4.1.2 (tabla 1.4.1.1), 1.1.4.2.2-2.5 (IDA, caudales, tabla 1.4.2.5, AE), 1.2.4.3.2 (THM-C y equipamiento), 1.2.4.5.1-2, IT 3.3 (tabla 3.1), 3.4.2, IT 3.8 entera | Literal; cifras correctas (23…25/45…60; 21…23/40…50; 20/12,5/8/5; 0,83/0,55/0,28; filtros; 70 kW; 0,28 m³/s; 21/26 °C; 30-70 %; 1.000 m²; 100 m², 1,7 m, ± 1 °C) |
| Reglamento (UE) 2024/573, texto DOUE | arts. 4.1, 4.5, 5.1-5.3, 5.6, 6.1-6.4, 7.1-7.2, 8.6, 13.3-13.5, 13.7 | Literal. Hallazgos M2 y M4 |
| Guía IDAE (2007) | familia 6 (resistencias de aceite m, cuadros A, relés m, interruptores de flujo 2.A, serie de seguridades M), familia 12 (avisador de filtros 2.A) | Coincide |

Lentes automáticas: no se han vuelto a pasar; el verificador corrió `negritas.py`,
`refutar_exactitud.py`, `refutar_modo.py`, `refutar_prosa.py` e `indice.py` sobre esta misma
versión (el tema no ha cambiado desde la fase 3).

## Hallazgos de exactitud

Graves: **ninguno**. Ningún dato falso, ningún artículo mal, ninguna redacción derogada, ningún
«podrá» por «deberá». Los límites de 19/27 °C se dan correctamente como no vigentes.

Menores (todos error 6, salvedad omitida):

- **M1 · 7.6 · IF-14, 3.1.** Se da «**Se inspeccionarán cada diez años las instalaciones frigoríficas
  de nivel 2.**» sin los dos párrafos que la matizan: **Las instalaciones de nivel 2, que de acuerdo
  con el artículo 11 del presente Reglamento puedan ser realizadas por empresas de nivel 1 se
  consideran, a efectos de inspecciones, como si fueran de nivel 1.** y la inspección de equipos a
  presión del punto 6, que **se realizará cada diez años independientemente del nivel de la
  instalación y del refrigerante empleado.** Afecta a los A2L, que el tema trata en 2.3 y 7.1.
  Propuesta: añadir los dos literales tras la cita, y ajustar la fila «Inspección, nivel 2» de 7.7.
- **M2 · 3.3, tabla del art. 13.** La fila de 2025 omite que el 13.3 ya prohibía antes el mismo uso
  en aparatos de refrigeración **con un tamaño de carga de al menos 40 toneladas equivalentes de
  CO2**, y que **no se aplicarán a equipos militares ni a aparatos destinados a aplicaciones
  diseñadas para enfriar productos a temperaturas por debajo de -50 °C.** No altera lo afirmado para
  2025; basta una línea en la columna «Salvedad».
- **M3 · 6.3 · IF-17, 2.5.3.5.** Tras el informe de fuga significativa, la norma añade: **se
  realizará una nueva revisión, en todo caso antes de un mes de la fecha en la que se identificaron
  las fugas, informándose a la autoridad competente de los resultados de la misma.** El tema sólo da
  el control «antes de un mes a partir del momento en que se haya subsanado» (2.5.1). Son dos plazos
  con distinto punto de partida; conviene darlos juntos.
- **M4 · 7.5 · art. 6.** «el de la aparamenta eléctrica, al menos cada seis años (6.4)»: el 6.4 se
  refiere a la aparamenta sujeta al 6.2, que sólo obliga al sistema de detección si el aparato tiene
  ≥ 500 t CO2-eq **y hayan sido instalados a partir del 1 de enero de 2017**. Falta esa condición.

Comprobado sin tacha (además de lo que ya listó la verificación): art. 2.2 (2,5/0,5/0,5 kg y fórmula
A2L), art. 20.2 (excepción A2L), art. 21 («podrá sustituir»; certificado eléctrico), arts. 26-29;
IF-17 2.4.c (0,6/0,3 bar, 200 dm³), 2.5.3.3 (5 g/año, anual); art. 4.5 UE (24 horas/un mes); 5.1
(10 t, 3 kg residencial, 0,1 %, 6 kg); 5.6 (tabla de frecuencias); 13.4 (2026 y 2032); 13.5; 13.7.

## Cobertura del enunciado

| Punto del enunciado | Dónde | Juicio |
|---|---|---|
| Principios básicos | 1.1-1.4 | Cubierto (ciclo y aire húmedo declarados como oficio) |
| Equipos | 2.1-2.4 | Cubierto |
| Refrigerantes | 3.1-3.4 | Cubierto; grupo de cada refrigerante concreto (IF-02) declarado como hueco |
| Ventilación | 4.1-4.8 | Cubierto |
| Control de temperatura y humedad | 5.1-5.5 | Cubierto; humedad de salas de equipos declarada como hueco |
| Averías frecuentes | 6.1-6.6 | Cubierto (tabla de oficio, declarada) |
| Mantenimiento preventivo | 7.1-7.7 | Cubierto, con las dos lagunas de abajo |

Preguntas (`27-T09-preguntas.md`): **13 enteras, 0 a medias, 2 no.**

Lagunas (se amplía el tema):

- **L1 (pregunta 14) · 7.5.** IF-17, 2.5.2: si los sistemas de detección de fugas no funcionan correctamente, **se duplicará
  la frecuencia de las revisiones de fugas anteriormente mencionadas.**
  Una línea tras el control anual del sistema de detección; también en 7.7.
- **L2 (pregunta 15) · 7.6.** La equiparación a nivel 1, a efectos de inspección, de las
  instalaciones de nivel 2 que puede realizar una empresa de nivel 1 (M1).

Observación sin hallazgo: la extensión (≈15.700 palabras) es alta para un punto de siete rúbricas,
pero no hay repeticiones que recortar sin perder datos; no se propone recorte.

## Para el remate

Aplicar M1-M4 y L1-L2 (todo literal, con la cita ya dada aquí). Sonnet basta: son añadidos de una o
dos frases, sin ampliación de epígrafe.
