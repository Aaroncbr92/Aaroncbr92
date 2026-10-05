# Remate · Oficial Técnico Electricista (27) · Tema 13 · Mantenimiento preventivo, correctivo y predictivo

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/13-mantenimiento-preventivo-correctivo-y-predictivo.md`.
Entrada: `27-T13-refutacion.md` (graves 0, menores 3, lagunas 3) y `27-T13-preguntas.md`.
Fuentes leídas el 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; ninguna
redacción usada es posterior al 24-09-2026). **Se ha ampliado contenido nuevo** (L1, L2, L3): toca 5 bis.

Ficheros tocados: el tema y este informe. Copia previa del tema en el scratchpad
(`27t13-antes-remate.md`), no en el repositorio.

## Correcciones (comprobadas en la fuente antes de aplicarlas)

| # | Comprobación | Aplicada | Pasaje cambiado |
|---|---|---|---|
| M1 | Investigación D §1.1: la ficha AENOR dice «Anula a UNE-EN 13306:2011»; el pliego dice «edición 2010». No consta que sea la EN 13306:2010 publicada como UNE en 2011 | Sí, en la forma de reserva que propone el informe: sin año | 1.2: «reproducción secundaria de una edición anterior a la vigente»; Trazabilidad, fila de la reproducción secundaria: «en una edición anterior a la vigente» |
| M2 | RITE, apéndice 3 (redacción RD 178/2021): A3.1 punto 2 es calefacción y ACS; la GMAO y la gestión de almacén están en A3.2 punto 2 | Sí | 3.4: «(apéndice 3, A3.2, punto 2)»; 7.2: «(apéndice 3, A3.2, punto 2)» |
| M3 | X Convenio, BOJA 240/2014, ficha 9310000 (J. Sec. Mantenimiento): primera tarea **Desarrollo e implantación del Plan de Mantenimiento y Explotación.** | Sí | 1.1: se añade «y como primera de sus tareas **Desarrollo e implantación del Plan de Mantenimiento y Explotación.**» tras la función básica del jefe de sección |

## Lagunas (ampliación; ninguna pregunta recortada)

| # | Fuente leída | Pasaje nuevo |
|---|---|---|
| L1 (preg. 13) | IEC 60050-192 (Electropedia): 403, no leída. Leído: Universidad de Cantabria, OCW «Técnicas de mantenimiento en instalaciones mineras», cap. 2 (2.3, 2.5, 2.14: MTBF, MTTR con su fórmula, disponibilidad = MTBF/(MTBF+MTTR)); UC3M, «Mantenimiento Industrial» (2003), MTTR como medida de la mantenibilidad | 3.4: párrafo «Los tres indicadores básicos…», lista MTBF/MTTR/disponibilidad (negritas literales del manual), ejemplo de oficio del SAI (4.380/4.400 ≈ 99,5 %) y aviso de que no es la UNE-EN 15341. Se reescribe la frase previa («lo que sigue no se toma de ellas») |
| L2 (preg. 14) | RD 401/2023, módulo 0968, criterio 7 d); UC3M, diapositiva 10; Universidad de Cantabria, cap. 5, 5.2.2 | 1.2: párrafo nuevo sobre el TPM tras el del mantenimiento legal (el «total», tareas del operario, tres ceros, mantenimiento autónomo como uno de ocho pilares, traducción de oficio a la instalación eléctrica). La sigla deja de estar sin uso |
| L3 (preg. 15) | UOC, «Gestión de stocks. Órdenes de compra», PID_00253874, 1.3, 1.4 y 1.6.2 | 7.2: definiciones literales de punto de pedido, stock de seguridad y stock mínimo; fórmula del punto de pedido; ejemplo de oficio de los fusibles; el repuesto crítico no va por punto de pedido |

Arrastre: siglas MTBF, MTTF y MTTR añadidas a la lista de entrada; «Qué se puede preguntar»
(TPM, indicadores, punto de pedido); ficha «Fuente» (manuales universitarios) y «Extensión» (unas
9.850 palabras, recuento de `indice.py`; antes 8.877); «Lo que este tema no da» (indicadores:
sólo los normalizados quedan fuera); Trazabilidad (cuatro filas nuevas; RD 401/2023 con el
criterio 7 d)); lista de oficio (ejemplos del SAI y de los fusibles, TPM aplicado).

Relectura de antecedentes: «El real decreto no lo define» (antes «La norma»), con el RD 401/2023
inmediatamente delante; «ellas» en 3.4 remite a las UNE-EN 15341 y 17007 de la frase anterior;
«El mismo manual» en 7.2, al de la UOC; «epígrafe 7.1» y «epígrafe 1.1» existen. Corregido
«Su primer pilar» por «Uno de sus ocho pilares»: la fuente dice que el orden no es preferencia.

## Lentes

- `indice.py`: índice regenerado, 44 epígrafes, 9.853 palabras (sin fila en `portadas.tsv`: ficha a mano).
- `refutar_prosa.py`: 0 (tras añadir MTBF/MTTR a las siglas; antes 2).
- `negritas.py` (BOE + convenio + RD 401/2023 + los cuatro manuales): 88 cotejadas; 7 no
  encontradas, todas previas (rótulos y títulos de catálogo AENOR sin copia local); las 5
  «otro artículo» son las mismas que antes del remate. Todas las negritas nuevas, encontradas.
- `refutar_exactitud.py` y `refutar_modo.py` (RITE, RD 1215/1997, REBT, RIPCI): idénticos antes y
  después; `refutar_modo` 0 hallazgos.

## Preguntas tras el remate

12, 13 y 14 pasan de «no» a «entera»; 15 de «a medias» a «entera». Recuento: 15 enteras.
