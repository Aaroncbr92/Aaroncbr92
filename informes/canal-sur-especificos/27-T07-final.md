# Fase 5 bis · Oficial Técnico Electricista (27) · Tema 7 · Grupos electrógenos, SAI y continuidad de servicio

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/07-grupos-electrogenos-sai-y-continuidad-de-servicio.md`.
Alcance: sólo los 15 pasajes que lista `27-T07-remate.md`. Ficheros tocados: el tema y este informe.
Fuentes leídas el 05-10-2026 (reloj del sistema; el encargo fecha «hoy» el 24-09-2026; ninguna
cambia entre ambas fechas): REBT, BOE-A-2002-18099, art. 10 (redacción única, vigente desde
18-09-2003), ITC-BT-28 apdos. 1, 2, 2.1-2.3 (redacción única) e ITC-BT-40 apdos. 2 y 4.2 (redacción
del RD 244/2019), con `boe.py precepto` y `grep` sobre `fuentes/canal-sur/BOE-A-2002-18099.md`.

## Cotejo pasaje por pasaje

| # | Pasaje | Fuente / antecedente | Resultado |
|---|---|---|---|
| 1 | Extensión 12.400 | `indice.py`: 12.482 tras esta fase | Correcto |
| 2 | «Qué se puede preguntar» | Remite a 3.3 y 5.1, que lo tratan | Correcto |
| 3 | Entrada epígrafe 2, «a juicio de oficio» | ITC-BT-28 apdo. 2 no asigna categorías a fuentes | Correcto |
| 4 | 2.4, sobredimensionado grupo-SAI (oficio) | Sin cifra; remisión a 3.4 válida (la cadena dice que el grupo recarga la batería) | Correcto |
| 5 | 3.1, entrada sobre el campo de la ITC-BT-28 | Apdo. 1 | **Corregido**: «fuera de ellos… sirven de referencia, no de obligación» era afirmación sin fuente (error 9) y el campo omitía los locales BD2-BD4 y los de más de 100 personas (error 6). Ahora: el campo completo, y «fuera de ellos, la ITC-BT-28 no obliga por sí misma y sus categorías y sus fuentes se usan como referencia (oficio)» |
| 6 | 3.1, «puede ser automática o no automática» | Apdo. 2, literal | Correcto; antecedente de «Y añade» presente |
| 7 | 3.3, art. 10.3 desde «Además…» | Art. 10.3, literal | Correcto; «esa lista» tiene delante la ITC-BT-28, 2.3 |
| 8 | 3.3, art. 10.2 | Art. 10.2, literal; «deberán» correcto | **Corregido** el rótulo: «la regla general de la conmutación entre los dos suministros» (el 10.2 no habla de conmutación, y «los dos» no tenía antecedente: el párrafo anterior enumera tres suministros). Ahora: «dice qué debe llevar cualquier instalación que reciba un suministro complementario además del normal» |
| 9 | 4.2, enlace con el art. 10.2 | Art. 10.2; ITC-BT-40 apdos. 2 y 4.2 | **Corregido**: omitía la salvedad del 10.2 («salvo lo prescrito en las ITC»), justo antes del epígrafe que trata la excepción (error 6). Añadida en literal y la salvedad concreta: la transferencia sin corte que la ITC-BT-40 admite en sus apartados 2 y 4.2 (comprobado: la letra b) del apdo. 2 remite al 4.2) |
| 10 | 5.1, regímenes de carga (oficio) | Sin cifras; 2.1 llama al bloque «Rectificador o cargador»; 5.2 y 7.2 tratan lo remitido | **Matizado**: «El cargador del SAI es su rectificador» pasa a «En el diagrama de bloques de 2.1, el cargador del SAI es su rectificador» (no todo SAI real lo une) |
| 11 | 5.2, ventilación «de un local de pública concurrencia» | ITC-BT-28 apdo. 2.1, literal, «con excepción de los equipos autónomos» | Correcto |
| 12 | 7.3, «de un local de pública concurrencia» | ITC-BT-28 apdo. 2.1, literal | Correcto |
| 13 | Normativa: art. 10, apdo. 1 | Coincide | Correcto |
| 14 | Lo que este tema no da | Coherente con 2.4 y 5.1 | Correcto |
| 15 | Trazabilidad | 10.2, apdo. 1 y oficio añadidos | Correcto |

El remate no se equivocó en ninguna corrección aplicada; los cuatro ajustes de arriba son del texto
nuevo que escribió.

## Lentes tras corregir

- `negritas.py` (REBT + RIPCI): 107 cotejadas; 8 «no están», las mismas ajenas al BOE (dos rótulos,
  seis citas de Sölter); 0 mal atribuidas (la primera redacción del pasaje 9 dio un falso «art. 3»
  por la remisión «(3.3)»; reescrito).
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 43 epígrafes, 12.482 palabras
  (la portada dice 12.400 aproximadamente: se mantiene).

## Veredicto

Tema cerrado. Sin pendientes.
