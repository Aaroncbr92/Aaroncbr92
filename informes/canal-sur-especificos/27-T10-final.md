# Fase 5 bis · Oficial Técnico Electricista (27) · Tema 10 · Reglamento de instalaciones térmicas en los edificios

Revisión, por otro Opus, sólo de los ocho pasajes que lista `27-T10-remate.md`.
Fuente releída el **05-10-2026** (reloj del sistema; el encargo dice «hoy es 24-09-2026»; el RITE no
tiene redacción posterior al 01-07-2021): `fuentes/canal-sur/BOE-A-2007-15820.md`, líneas 536-544
(art. 31), 1661-1666 (IT 1.2.4.8), 1767-1786 (IT 1.3.4.1.2.7), 2366-2385 (IT 3.8.2 a 3.8.5) y las
cabeceras de redacción de los arts. 1 a 47.

Ficheros tocados: el tema y este informe.

## Pasaje por pasaje

| Pasaje | Dato contra la fuente | Antecedentes | Resultado |
|---|---|---|---|
| 1 Portada | Cabeceras: arts. 1, 8, 13, 14, 27 y 43 «aplicable desde 20080229, 1 redacción(es)»; cuadra con la lista de artículos citados (el 3, también original, no se cita). 2010: 19, 21, 22, 26, 35, 36, 41; 2013: 25, 28: correctos. Extensión 17.100: `indice.py` da 17.129 | — | Correcto |
| 2 IT 1.2.4.8 (2.4) | Las cinco negritas, literales; «deberá» y «podrá» respetados | «dicha evaluación» y «Todas estas medidas», con antecedente | Correcto |
| 3 Ventilación (3.3) | 5 cm²/kW, 50/30 cm, 10·A, menos de 10 m, 7,5 y 10 cm²/kW, dos aberturas, 1,8·PN + 10·A, 30 cm, 20 Pa, 10·A con mínimo 250 cm²: literales | «apartado 2.1… 4.2» cuelgan de la IT 1.3.4.1.2.7 | **Corregido**: la lista daba la regla de gases para orificios (2.3) pero no su paralela para conductos (3.3). Añadido literal el apartado 3.3 (error 6, salvedad omitida) |
| 4 IT 3.8.2.2 (4.8) | Literal | Remisión a 2.5, correcta | **Corregido** el párrafo siguiente: «Se aplican exclusivamente durante el uso…» quedó, tras insertar la IT 3.8.2.2, con ésta como antecedente aparente (los valores de confort), cuando la fuente lo dice de los límites del apartado 1. Ahora: «Los límites de 21 y 26 ºC se aplican…» (error 1) |
| 5 Visualizador (4.8) | Ubicación, DIN A3, ± 0,5 ºC, uno cada 1.000 m², salvedad del uso cultural: literales | «apartado c)» tiene delante la lista de usos de la IT 3.8.1.2 en el mismo epígrafe | Correcto |
| 6 Art. 31.6 (5.3) | Literal, con su segundo párrafo; «podrán acordar» respetado | «El mismo apartado añade» sigue a la cita | Correcto |
| 7 «Lo que este tema no da» | Ya no figura la ventilación por conducto | — | Correcto |
| 8 Trazabilidad | IT 1.2.4.8 en la lista; aviso de oficio sobre la sustitución de un generador, declarado | — | Correcto |

La línea de oficio de 2.4 («la sustitución de una enfriadora o de una caldera no se cierra con el
equipo montado…») se apoya en la IT 1.2.4.8 («parte sustituida o modificada», «proyecto o memoria
técnica») y va declarada como lectura de oficio: se mantiene.

## Lentes tras las correcciones

- `negritas.py` (contra el RITE): 312 negritas (una más, la del apartado 3.3, que está en la
  fuente); 8 fuera del RITE y 2 atribuidas a otro artículo, las mismas previas del remate.
- `refutar_prosa.py`: 0. `indice.py`: 17.129 palabras, 42 epígrafes; la portada (17.100) sigue valiendo.

## Resultado

Dos correcciones (antecedente en 4.8; apartado 3.3 en 3.3), ambas comprobadas en la fuente. El tema
queda cerrado.
