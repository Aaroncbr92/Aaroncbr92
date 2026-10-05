# Refutación · Oficial Técnico Electricista (27) · Tema 13 · Mantenimiento preventivo, correctivo y predictivo

Fase 4. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/13-mantenimiento-preventivo-correctivo-y-predictivo.md`
(9.480 palabras según `wc -w`; ficha «unas 8.900», que es el recuento de `indice.py`). Fuentes
releídas el 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; ninguna redacción
usada tiene vigencia posterior al 24-09-2026). No corrijo: sólo informo.

Ficheros tocados: este informe y `27-T13-preguntas.md`. El tema no se ha modificado.

## Alcance

- Exactitud: todo lo normativo y lo literal, salvo los pasajes de «Copiado de RTVE sin cambios» de
  `27-T13-redaccion.md` (1.2 tabla Preventivo/Correctivo, 1.3 los dos avisos y la frase del grupo en
  vacío, 1.4 filas de máquinas y tres medidas del motor, 4.1 cinco pasos, búsqueda binaria y aviso
  del síntoma). «Copiado del común»: nada.
- Cobertura: el tema entero contra el enunciado del punto 13.
- Fichas de catálogo AENOR (UNE-EN 13306, 13460, 15341, 17007; ISO 17359): sin copia local; quedan
  como en la verificación.

## Comprobado en la fuente, sin hallazgo

- Real Decreto 1215/1997 (BOE-A-1997-17824): art. 3.5 literal (dos párrafos); art. 4.1-4.4
  (salvedad «cuya seguridad dependa de sus condiciones de instalación», «personal competente»,
  «toda la vida útil»); anexo II (redacción BOE-A-2004-19311, 03-12-2004), ap. 1, puntos 14 (con su
  segundo párrafo), 15 y 16 (primera frase).
- REBT (BOE-A-2002-18099): art. 19 (única, 18-09-2003) y art. 20 (BOE-A-2010-8190, 23-05-2010),
  literales; ITC-BT-03 ap. 7 h) y j) (BOE-A-2025-17507, 04-09-2025); ITC-BT-05 4.2 (cada 5 años,
  «que precisaron inspección inicial»; organismo de control en 5.1; redacción BOE-A-2014-13681,
  30-06-2015); ITC-BT-18 ap. 12 (anual, terreno «mas» seco, personal técnicamente competente,
  reparación urgente, cinco años; redacción BOE-A-2010-8190).
- RITE (BOE-A-2007-15820): art. 26.4, 26.5 y 26.8 (BOE-A-2010-4514); art. 27.1-3 (única); apéndice 3
  (BOE-A-2021-4572), A3.2 puntos 2 y 6, literales.
- RIPCI (BOE-A-2017-6606): art. 21.1-2; anexo II (BOE-A-2025-7190, 10-05-2025), ap. 1, 3, 4 y 6;
  reparto tabla I / tabla II en la tabla de 1.3, correcto. Real Decreto 164/2025, de 4 de marzo:
  coincide con los demás temas cerrados.
- Real Decreto 393/2007 (BOE-A-2007-6237), anexo II, cap. 5 (5.1, 5.2, cuadernillo de hojas
  numeradas). Ley 7/2025 (BOE-A-2026-944), art. 136.3.f) literal.
- Real Decreto 401/2023, de 29 de mayo (BOE-A-2023-13217): módulo 0968, criterios a), h) y b)
  literales.
- X Convenio (BOJA 240, 10-12-2014), anexo III: fichas 9311100 (literal, «optimas»), 9311200,
  9300000 y la función básica de 9310000.
- Real Decreto 614/2001, de 8 de junio: título y fecha.
- Lentes: `refutar_prosa.py` 0 hallazgos. Negritas comprobadas a mano en las citas anteriores.

## Hallazgos de exactitud

Graves: 0.

Menores: 3.

| # | Epígrafe | Error | Qué dice | Qué debería | Fuente |
|---|---|---|---|---|---|
| M1 | 1.2 y Trazabilidad | 3/9 coherencia | «anuló la edición de 2011» y, dos líneas después, «reproducción secundaria de una edición anterior (la de 2010)» | Nombrar la misma edición de dos formas sin explicarlo confunde: decir «la EN 13306:2010 (UNE-EN 13306:2011)», si la reproducción secundaria es de esa; si no consta, dejar «una edición anterior» sin año | Investigación D §1.1 (no la reabro: lo propongo para el remate) |
| M2 | 3.4 (y 7.2) | 8 cita imprecisa | «apéndice 3, punto 2» | «apéndice 3, A3.2, punto 2»: el A3.1 también tiene un punto 2 (calefacción y ACS); la Normativa ya lo dice bien | RITE, apéndice 3 |
| M3 | 1.1 | 6 salvedad omitida | «El plan de mantenimiento no lo hace el oficial: […] el jefe del departamento […] tiene la tarea de Elaborar e implantar el Plan de Mantenimiento., y el jefe de sección […] tiene como función básica Coordinar, organizar y supervisar…» | Añadir que la ficha del jefe de sección (9310000) recoge también la tarea **Desarrollo e implantación del Plan de Mantenimiento y Explotación.** Sin ella, una pregunta sobre esa tarea se contesta mal (pregunta 12) | X Convenio, anexo III, ficha 9310000 |

## Cobertura del enunciado

Los once elementos del enunciado (preventivo, correctivo, predictivo, gamas, órdenes de trabajo,
diagnóstico, priorización, trazabilidad, repuestos, inventario, documentación técnica) tienen
epígrafe propio y en el orden del enunciado. Las 15 preguntas (`27-T13-preguntas.md`): 11 enteras,
1 a medias, 3 no (una por el hallazgo M3; dos por laguna).

## Lagunas (se amplía el tema)

| # | Qué falta | Pregunta | Propuesta |
|---|---|---|---|
| L1 | Indicadores básicos: MTBF, MTTR, disponibilidad. El tema los remite a la UNE-EN 15341 no leída y no define ninguno; son pregunta de test casi segura con este enunciado (priorización, trazabilidad) | 13 (no) | Definirlos desde una fuente pública: el vocabulario IEC 60050-192 (Electropedia, consulta libre) define el tiempo medio de funcionamiento entre fallos, el tiempo medio de reparación y la disponibilidad; la fórmula elemental (disponibilidad = MTBF / (MTBF + MTTR)) sólo si se lee en fuente. Si no se confirma, dejarlo declarado como ahora |
| L2 | TPM: la sigla se presenta en las siglas y no se vuelve a usar (sigla sin uso, además de contenido ausente) | 14 (no) | O un párrafo breve con fuente (qué es y su idea de implicar al operador en el mantenimiento básico), o quitar la sigla de la lista |
| L3 | Gestión de existencias: «punto de pedido» y «existencias mínimas» aparecen sin definir; no hay existencias de seguridad ni criterio de reposición | 15 (a medias) | Una línea de definición de cada término en 7.2, declarada como oficio si no hay norma que la dé |

## Resumen

Graves 0 · menores 3 · lagunas 3. El tema está bien anclado en la fuente; las correcciones son de
precisión (M1-M3) y la ampliación, corta (L1-L3).
