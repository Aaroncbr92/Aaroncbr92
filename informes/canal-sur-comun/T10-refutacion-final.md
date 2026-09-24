# T10 · Refutación final (fase 5 bis, acotada) · Protección de datos de carácter personal

Un agente nuevo. Modo ahorro 2: releídos solo los diez pasajes que lista `T10-remate.md`, no el
tema entero. Leídos `ENCARGO.md` y `CICLO.md` antes de empezar. Fecha de lectura de todos los
preceptos: **24-09-2026**, sacando solo el precepto con `grep -n -A40` sobre los volcados de
`fuentes/canal-sur/`.

## 1. Cotejo de cada pasaje nuevo contra la fuente

| Pasaje (línea) | Qué dice el tema | Fuente | Resultado |
|---|---|---|---|
| 449-453, consentimiento (art. 7 RGPD) | «el responsable deberá ser capaz de demostrar que aquel consintió el tratamiento de sus datos personales» (7.1); «será tan fácil retirar el consentimiento como darlo» (7.3) | DOUE-L-2016-80807, art. 7.1 y 7.3 | Literal |
| 660-668, recursos (arts. 77.1, 79.1, 82.1 RGPD) | reclamación ante autoridad de control «en particular en el Estado miembro en el que tenga su residencia habitual, lugar de trabajo o lugar de la supuesta infracción» (77.1); tutela judicial ante el responsable o encargado (79.1); «toda persona que haya sufrido daños y perjuicios materiales o inmateriales como consecuencia de una infracción del presente Reglamento tendrá derecho a recibir del responsable o el encargado del tratamiento una indemnización» (82.1) | DOUE-L-2016-80807, arts. 77.1, 79.1 y 82.1 | Literal |
| 1354-1356, regla nemotécnica (art. 83.4.a RGPD) | ya no dice «consentimiento» sin matiz; añade la salvedad del art. 8 | DOUE-L-2016-80807, art. 83.4.a) («…los artículos 8, 11 y 25 a 39, 42 y 43») | Correcto: el art. 8 está en el escalón del 2 %, como dice ahora la regla |
| 1295, art. 72.1.d) LOPDGDD | «…sin contar con el consentimiento del afectado o con una base legal para ello» | BOE-A-2018-16673, art. 72.1.d) | Literal |
| 891, art. 35.3.a) RGPD | «decisiones que produzcan efectos jurídicos para las personas físicas o que les afecten significativamente de modo similar» | DOUE-L-2016-80807, art. 35.3.a) | Literal |
| 2037, tabla «Mensajes de la empresa fuera de la jornada» | remite a negociación colectiva o, en su defecto, a lo acordado con los representantes; política interna del empleador | BOE-A-2018-16673, art. 88.2 y 88.3 | Correcto, sin la afirmación sin apoyo que tenía antes |
| 1021, la AEPD (art. 44 LOPDGDD) | ya no dice que la relación con el Gobierno sea «el cauce ordinario de toda autoridad independiente» | BOE-A-2018-16673, art. 44 | Correcto: la frase quitada no estaba en el precepto y no se ha sustituido |
| 2059, fila Ley 1/2014 | «Artículos 43, 45 y 48» | Cuerpo del tema, líneas 1120 y 1133 (arts. 43 y 45) y 2039 (Ley 1/2026 modifica el 48) | Cuadra: son los mismos que cita el cuerpo |
| 283-284 y 2105, «y ninguna reforma cruzada» | quitado en las dos apariciones | — | El resto de la frase («diecisiete bloques…») sigue siendo cierto y no depende de la jerga quitada |
| 1405-1411, art. 77.3 LOPDGDD | cita el apartado 3 seguido, y en frase aparte explica que no se tocó en la reforma de 2023 | BOE-A-2018-16673, art. 77.3 (redacción de BOE-A-2023-11022, que solo tocó el apartado 2) | Literal, y la explicación es exacta: el apartado 3 es idéntico en las dos redacciones del bloque |

Diez de diez pasajes comprobados; ninguno queda sin cotejar.

## 2. Antecedentes

En el pasaje de recursos (línea 660), «Todo interesado» tiene delante, en el mismo apartado
(«Los derechos de las personas»), el sujeto que usa el resto del epígrafe («el afectado»). En el
de consentimiento (línea 449), el rótulo distingue «artículo 7 del Reglamento» del «artículo 7 de
la LOPDGDD» que viene justo después, así que ningún «dicho artículo 7» posterior queda ambiguo:
cada mención sigue llevando su etiqueta. En la fila de la desconexión digital (línea 2037), «este
derecho» no aparece: la fila remite directamente a «art. 88», sin pronombre suelto. Sin hallazgos.

## 3. Las quince preguntas (`T10-preguntas.md`), contestadas solo con el cuerpo del tema

1 (b), 2 (b), 3 (c), 4 (b), 5 (b), 6 (c), 7 (a), 8 (b): sin cambios, **enteras**.

**9.** El tema ahora responde **b** sin trampa: la regla nemotécnica corregida ya no sugiere el 4 %
para el consentimiento del niño. **Entera**.

**10.** «Debe ser tan fácil retirar el consentimiento como darlo, y no afecta a la licitud del
tratamiento previo» está ahora en el cuerpo (línea 452, cita literal del 7.3). **Entera**.

**11.** El derecho a indemnización del art. 82.1 está ahora en el cuerpo (línea 665, cita literal).
**Entera**.

12 a 15: sin cambios, **enteras**.

Resultado: **quince de quince enteras**. Las dos lagunas de la fase 4 (preguntas 10 y 11) quedan
cerradas por la ampliación del remate, no por recorte de la pregunta.

## 4. Lentes automáticas (tema entero, no solo los pasajes)

| Lente | Tramos | Resultado |
|---|---|---|
| `herramientas/refutar_prosa.py` | tema entero | 1: «LORTAD» (se presenta en la misma cita del preámbulo). Falso positivo, el mismo de las fases anteriores |
| `herramientas/refutar_modo.py` (RGPD, LOPDGDD, Ley 13/2022, Ley 10/2018, LO 1/1982, EAAnd, Estatuto CSRTV, Ley 18/2007) | tema entero | 2: arts. 8 y 16, con aviso de que otra norma numera igual esos artículos. Falsos positivos, los mismos de las fases anteriores |
| `herramientas/negritas.py` (22 volcados de `fuentes/canal-sur/` + `fusion-csrtv-boja-219-2015.txt`) | 216 negritas | 12 NO ESTÁ y 19 ¿ART.?: los mismos que ya explicó la refutación de fase 4 (rótulos, considerandos y el Reglamento 2025/2518 sin volcar, y anclajes en otro número de la misma frase). Ninguna de las negritas nuevas de este remate figura en la lista. Falsos positivos |

## 5. Resultado

**Cero hallazgos.** Los diez pasajes del remate se comprobaron literales contra la fuente citada,
sus antecedentes están bien puestos, las quince preguntas de `T10-preguntas.md` se contestan
enteras con el cuerpo del tema, y las tres lentes automáticas no marcan nada nuevo respecto a lo ya
explicado en las fases anteriores. No se ha tocado el tema en esta fase: no hacía falta.
