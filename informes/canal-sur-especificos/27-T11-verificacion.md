# Verificación · Oficial Técnico Electricista (27) · Tema 11 · Protección contra incendios y seguridad en instalaciones

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/11-proteccion-contra-incendios-y-seguridad-en-instalaciones.md`
(12.893 palabras tras la verificación, 43 epígrafes). Copia previa: `scratchpad/27t11v/antes-verif.md`.
Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»; ninguna fuente citada cambia entre esas fechas según sus cadenas de redacciones).

Ficheros tocados: el tema y este informe. Nada más.

## Lo que no se re-verifica (comprobado sólo que es literal)

- «Copiado del común» (7.1, art. 20 Ley 31/1995): `diff` contra `temas/canal-sur-comun/09-ley-31-1995.md`
  líneas 810-826 → **idéntico**. No se toca. (Sigue en pie el aviso 9 del redactor sobre la salvedad
  «en función de las circunstancias antes señaladas» que omite el común; es del común, no de este tema.)
- «Copiado de RTVE sin cambios»: el redactor declara **nada**; todo lo de RTVE está adaptado o cita
  norma, así que se ha verificado entero.

## Fuentes releídas (05-10-2026)

- RIPCI (BOE-A-2017-6606) con `boe.py`: arts. 1, 2, 9, 19, 20, 21, 22 (cadenas: 9, 20, 22 con
  redacción 2025; 1, 2, 19, 21 única), dd, anexo I secc. 1.ª y 2.ª, anexo II; apartado 5.4 en la
  redacción anterior (`--fecha 20250101`). Tablas I, II y III del anexo II y títulos del apéndice
  leídos celda a celda en el HTML consolidado del BOE (`scratchpad/ripci.html`).
- RD 164/2025 (BOE-A-2025-7190): dd, DT 1.ª, DT 6.ª, DF 1.ª (arts. 9.2, 20, 22), DF 12.ª, arts. 1-2
  del Reglamento; título por el XML del BOE.
- CTE art. 11 (`boe.py`, redacción única). DB SI consolidado 4-III-2025 (PDF de codigotecnico.org):
  SI 1 apdos. 1-4 y tablas 1.1, 1.2, 2.1, 2.2; SI 4 apdos. 1-2 y tabla 1.1 con notas. **Columnas de la
  tabla 2.1 re-comprobadas por coordenadas** (pymupdf): «En todo caso» de cuadros, grupo, ascensores,
  climatización y CT seco en la columna de riesgo bajo; decorados 100-200 m³ medio, >200 m³ alto.
- Ley 31/1995 arts. 18.1.c) y 33.1.c); RD 486/1997 anexo I 10.7.º, 11, 12.2.º; RD 485/1997 anexos II y
  III; RD 393/2007 (volcado) arts. 2, apdos. 3.3, 3.6, 3.7, anexos I-III y nota de vigencia; RD
  524/2023 dd; ITC-BT-28 apdo. 4 b) y f).
- NTP 536 (`fuentes/prl-especifico/ntp-536.*`): tabla 1 **re-comprobada por coordenadas en el PDF**,
  notas, etiquetas, halón. Búsqueda BOE «autoprotección» (`boe_buscar.py`): ninguna norma nueva.

## Hallazgos y correcciones (con el número de error)

| # | Epígrafe | Error | Qué había | Corrección |
|---|---|---|---|---|
| 1 | 4.2, tabla NTP | 9 | Agua pulverizada: «Muy adecuado / Aceptable (2)» | En el PDF la nota (2) está en la columna A (x≈234), no en la B: «Muy adecuado (2) / Aceptable» |
| 2 | 7.2, aviso NBA | 1/6 | «El apartado 3 ... mantiene en aplicación los instrumentos derogados» | El dd.3 del RD 524/2023 sólo nombra «Las Directrices Básicas de Planificación y los Planes Estatales de protección civil»; la extensión a la Norma Básica es la nota del consolidado. Reescrito y añadidos los efectos (11-07-2023) |
| 3 | 1.5, tabla | 6 | Ap. 3 y 4 del anexo II sin la condición | Añadido «si cumplen con los requisitos establecidos en el artículo 16 del presente Reglamento» |
| 4 | 1.5 | 6 | Actas del titular: «basta con el contenido mínimo del apartado 5» | Añadida la sustitución de a.6-a.8 por los datos del último mantenimiento y de quien lo hizo |
| 5 | 1.1 aviso | 6 | DT 1.ª RSCIEI sin plazo ni excepción del ap. 4 | Añadidos los seis meses y la aplicación a ampliaciones, reformas o cambios de actividad (parte afectada) |
| 6 | 1.7 | 6 | «Lo ya instalado» | DT 6.ª b) incluye lo que tenía licencia de obra solicitada y lo instalado en el plazo transitorio; añadido el plazo de cinco años de cocinas comerciales |
| 7 | 1.7 | 9 | «en los edificios de la RTVA conviven hoy BIE...» (dato de la RTVA sin documento) | «en un mismo edificio pueden convivir» |
| 8 | 2.5 | 6 | Vida útil de detectores sin la regla de los anteriores al RD 513/2017 | Añadida (verificación a partir de diez años en funcionamiento) |
| 9 | 1.2 | 3 | «Las seis rúbricas del enunciado caen en dos de esas exigencias» | Son cinco; la coordinación con planes de emergencia no es del CTE |
| 10 | 6.2 | 9 | Retenedores de puertas presentados como la maniobra «compuertas cortafuego» de la tabla II | La tabla II nombra las compuertas; los retenedores sólo caben en «otras partes del sistema de protección contra incendios». Reescrito y marcado como oficio |
| 11 | 1.3 | 9 | Mantas «siguen la misma regla que los extintores»; anexo II «reserva» al titular | Mantas: regla análoga (instaladoras o mantenedoras de PCI, no «mantenedoras de extintores»). El anexo II «permite», no reserva |
| 12 | 4.3 | literal | «según la norma UNE23110» | La NTP pone «UNE-23110» (guion partido por el salto de línea del PDF) |
| 13 | 4.4 | 9 | «El DB SI dice lo mismo» | El DB SI repite los 15 m, no la altura: «repite los 15 m» |
| 14 | Lo que no da | 9 | Proyecto de decreto andaluz de 2020 «sometido a audiencia» (tomado de la investigación, sin releer) | No confirmado: quitado; queda el hueco |
| 15 | Siglas | 5 | BOE y BOJA usados sin presentar; HVAC, BMS, kW, MJ, l/min presentados sin uso | Presentados BOE y BOJA; quitadas las no usadas. En trazabilidad, «HTML» y «PDF» sustituidos por «página web» y «documento publicado» |
| 16 | Portada y trazabilidad | 9 | Portada omitía DT 1.ª y DF 12.ª del RD 164/2025; la fila de la Ley 31/1995 no fechaba el 18.1.c) | Igualadas |

Confirmado sin cambios (muestra de lo más preguntable): arts. 1, 2, 9, 19.2, 20, 21, 22 RIPCI y la
redacción anterior del 22.2 (sin «zonas de uso almacén» ni el párrafo de 20.2/alumbrado: la
afirmación «la redacción de 2025 endureció» es correcta); pulsadores 25 m y 80-120 cm; extintores
15 m y 80-120 cm; clases A-F y la errata «combinación»; BIE (25/45 mm, K 42/85, 85 l/min a 4 bar,
160 l/min a 3,5 bar, máx. 9 bar, 1,50 m, 5 m de la salida, radio manguera + 5 m, 50 m, 20/30 m,
prueba 980 kPa dos horas) y la presión derogada 300-600 kPa; gases (cinco elementos, retardo y
prealarma, UNE-EN 15004-1 / UNE ISO 6183 «dióxido de carbono para uso en edificios», UNE-EN 12094);
tablas I, II, III celda a celda; títulos UNE-EN 54-5/7/10/12/17/18/20, 14604; señalización
(UNE 23033-1, 23032, ISO 7010, 23035-4 categoría A, 3 %, 20 años/80 %/10 años); DB SI tablas 1.1,
1.2, 2.1, 2.2, SI 4 tabla 1.1 y notas (1), (2), (6), (7), (8); art. 11 CTE; RD 485/1997 y 486/1997;
ITC-BT-28 4 b) y f); NBA (definiciones, anexo I, 3.3.1, 3.3.3, 3.3.5-6, 3.3.8, 3.6.4, 3.7, capítulo 5
del anexo II); RD 1942/1993 derogado por la dd del RD 513/2017; títulos y fechas de la normativa.

## Lentes (cita normas: todas)

- `negritas.py` contra 13 fuentes (RIPCI HTML, RD 164/2025, CTE 11, RIPCI 5.4 anterior, DB SI, Ley
  31/1995, RD 486 y 485/1997, RD 393/2007, RD 524/2023, REBT, NTP 536): 259 negritas; 9 «no están»,
  todas explicadas: dos rótulos de forma; seis cifras con «m2» que el HTML del BOE escribe con
  superíndice (leídas en `boe.py`); «UNE-23110», partido en el PDF de la NTP (leído). 1 «¿art. 20?»:
  falso positivo (el tema la atribuye al 33.1.c), donde está).
- `refutar_exactitud.py`: 32 «no literales», todos falsos positivos: lee «apartado 4.4», «3.3.8»,
  «10.7.º» como artículos 4, 3, 10 de la norma equivocada; las 32 están confirmadas por `negritas.py`.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 12.893 palabras, 43 epígrafes, índice
  sin cambios.

## Para la refutación

- La tabla de agentes es doctrina de la NTP (tomada del RD 1942/1993 derogado), no norma vigente: el
  tema ya lo dice; vigilar que las preguntas no la presenten como del RIPCI.
- La vigencia de la Norma Básica de Autoprotección descansa en la nota del consolidado del BOE, no
  en la letra del dd.3: está dicho así.
