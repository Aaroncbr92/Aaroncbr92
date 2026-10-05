# Redacción · Oficial Técnico Electricista (27) · Tema 11 · Sistemas de protección contra incendios y seguridad en instalaciones

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/11-proteccion-contra-incendios-y-seguridad-en-instalaciones.md`
(12.688 palabras según `indice.py`, 43 epígrafes). Material: `27-investigacion-B-alimentacion-instalaciones.md`
(§11). Reuso RTVE: `ing-tec-industrial/06`, `prl/prl-especifico` §9, `ing-tec-industrial/03` §4
(65 %, actualizar: **sí**). Fecha declarada: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»). Lentes corridas: `indice.py` (índice generado), `refutar_prosa.py` (0 hallazgos tras
presentar EI), `negritas.py` contra 13 fuentes (259 negritas; las que no casan se explican abajo).

Ficheros tocados: el tema (nuevo) y este informe.

## Estructura

1 Marco (reparto de normas, activa/pasiva, exigencias SI, quién instala, puesta en servicio,
mantenimiento, inspecciones, transitorio 2025); 2 Detección; 3 Alarmas; 4 Extinción; 5
Señalización; 6 Sectorización (con la seguridad contra incendios en la instalación eléctrica);
7 Coordinación con planes de emergencia; normativa; lo que no da; trazabilidad. «Seguridad en
instalaciones» se ha leído como seguridad contra incendios en las instalaciones (locales de riesgo
especial, pasos de cables, cables del REBT); la seguridad eléctrica de las personas es de los temas
5, 15 y 19.

## Fuentes leídas por el redactor (05-10-2026)

- RIPCI (`boe.py precepto BOE-A-2017-6606`): arts. 1, 2, 9, 19, 20, 21, 22; anexo I secc. 1.ª
  (apdos. 1, 4, 5, 11, 15) y 2.ª; apéndice; anexo II (apdos. 1-11) y tablas I-III. **Columnas de
  periodicidad de las tablas I y II leídas en el HTML del BOE** (confirma la investigación: detección,
  requisitos generales y fuentes de alimentación, tres meses). Títulos de las normas UNE-EN 54
  leídos en la tabla HTML del apéndice (el volcado plano no los trae: por eso `negritas.py` no los
  encuentra). Apdo. 5.4 en la redacción anterior (`--fecha 20250101`).
- RD 164/2025 (`BOE-A-2025-7190`): dd, DT 1.ª, DT 6.ª, DF 12.ª, arts. 1 y 2 del Reglamento.
- CTE art. 11 (redacción única). DB SI consolidado 4-III-2025 (PDF de codigotecnico.org, pasado a
  texto con `documento.py`): SI 1 apdos. 1-4 y tablas 1.1, 1.2, 2.1, 2.2; SI 4 apdos. 1-2 y tabla
  1.1. **Columnas de la tabla 2.1 comprobadas por coordenadas** (pymupdf): «En todo caso» de cuadros,
  grupo, ascensores, climatización y CT seco cae en «riesgo bajo»; taller de decorados: 100-200 m³
  medio, >200 m³ alto.
- RD 486/1997 anexo I apdos. 10-12; RD 485/1997 anexos II y III; Ley 31/1995 arts. 18, 20, 33;
  RD 393/2007 (volcado local) arts. 2, apdos. 3.1-3.7, anexos I-III; RD 524/2023 dd; ITC-BT-28 apdo. 4.
- NTP 536 (INSST, PDF descargado de insst.es): tabla 1 y notas, etiquetas.

## Avisos para el verificador

1. **RD 2267/2004 derogado** (investigación 11.0.1, confirmado): no se copia nada de prl §9.7 ni de
   ing-tec-industrial/06 §5-7. El tema sólo da ámbito y transitorio del RSCIEI 2025.
2. **Presión de las BIE de prl §9.6, derogada** (confirmado): se da la vigente y, como aviso, la
   antigua en literal de la redacción anterior.
3. **Recuento «cinco» exenciones de ing-tec-industrial/06 §4, erróneo** (confirmado): son seis; se
   añade la condición «o zonas de uso almacén» y el párrafo nuevo.
4. **Hallazgo nuevo: la tabla de agentes extintores de prl §9.4 se atribuye allí al «reglamento de
   instalaciones de protección contra incendios»**; la NTP 536 dice que es la del **RD 1942/1993**,
   derogado. El RIPCI 2017 no trae tabla. El tema la da como doctrina del INSST con esa salvedad.
5. **Hallazgo nuevo: el RD 393/2007 (Norma Básica de Autoprotección) figura derogado** por el RD
   524/2023, dd 2.d), con efectos 11-07-2023; el texto consolidado del BOE anota que «continuará
   aplicándose hasta tanto sea aprobado el nuevo instrumento». El dd.3 habla literalmente de
   «Directrices Básicas de Planificación y los Planes Estatales»; la extensión a la Norma Básica es
   la nota del BOE. Comprobar. Búsqueda por título en el BOE (05-10-2026): ninguna nueva norma
   básica de autoprotección. prl §9.9 la da como vigente sin salvedad.
6. Errata del BOE en la clase A («combinación» por «combustión»): citada literal y anotada.
7. Columna «Fuentes de alimentación» (tres meses) y demás periodicidades: tomadas del HTML.
8. Norma andaluza de autoprotección: sólo lo que dice la investigación (proyecto de 2020, no
   confirmado); no se ha releído. Se dice como hueco.
9. Observación sobre el común (no tocado): el tema 9 del común pone en negrita «El citado personal
   deberá poseer la formación necesaria, ser suficiente en número y disponer del material
   adecuado.» y omite el final del precepto «, en función de las circunstancias antes señaladas»
   (salvedad omitida, error 6). Lo copio tal cual por la regla del encargo; lo señalo al coordinador.
10. Negritas que `negritas.py` no encuentra: «Enunciado del programa» y «Qué se puede preguntar»
    (rótulos de forma, como en T07); los títulos del apéndice y «Prueba de funcionamiento de todos
    los pulsadores.» (sólo en el HTML del BOE, leídos); el pasaje con «[...]» del RD 524/2023 se
    partió en dos negritas.

## Copiado del común

- 7.1, desde «El empresario, **teniendo en cuenta…**» hasta «…sectorización no están en la Ley
  31/1995.»: literal del tema 9 del común de Canal Sur, epígrafe «Artículo 20. Medidas de
  emergencia» (se quitó su rótulo `###` para no duplicar el del epígrafe 7.1). No se re-verifica.

## Copiado de RTVE sin cambios

Nada. Los tres temas de RTVE de este reuso están marcados «actualizar: sí» (no «sin actualizar»), y
además todo lo que se ha tomado de ellos cita norma. Lo reutilizado está adaptado y se verifica:

- ing-tec-industrial/06: tabla de reparto (§1, sin la fila del RD 2267/2004 y con el RSCIEI 2025),
  cita de los arts. 1.1, 1.2 y 19.2 (releídos), tabla activa/pasiva (§2, sin negritas de énfasis),
  tabla del art. 2 (§2, reescrita con literal), art. 20 (§3, reescrito con la redacción de 2025),
  art. 21 (§3), art. 22 (§4, corregido a seis exenciones y redacción de 2025). Quitado lo propio de
  RTVE (puertas de automantenimiento de otros temas, «sedes por toda España», remisiones a temas 1,
  3, 4, 5 de RTVE).
- ing-tec-industrial/03 §4: art. 11 del CTE (releído), tabla de las seis exigencias (rehecha con el
  literal de 11.1-11.6).
- prl-especifico §9: plano RD 486/1997 (apdos. 10-12, releídos), clases de fuego (§9.3, sustituida
  por el literal del RIPCI), tabla de agentes y lectura CO₂/polvo (§9.4, reatribuida a la NTP 536 y
  al RD 1942/1993), extintores (§9.5, rehecha con literal del RIPCI y de la NTP), BIE (§9.6, rehecha
  con la redacción de 2025), plan de autoprotección (§9.9, con la salvedad de derogación y ampliada).

## Lo nuevo (pasa entero por el ciclo)

1.1 aviso RSCIEI; 1.3 art. 9; 1.4 párrafos de 2025; 1.5 entero; 1.6 condición y párrafo nuevos,
UNE 192005-2, apdos. 3-4; 1.7 entero; 2 entero; 3 entero; 4.4 DB SI; 4.5 caudal/presión, K, aviso,
dotación; 4.6 y 4.7 enteros; 5 entero; 6 entero; 7.2 aviso, definiciones, anexo I, tabla de reglas,
capítulo 5; 7.3 entero; normativa, lo que no da, trazabilidad.

## Comprobación con 10 preguntas tipo test

Contestadas sólo con el tema. Las diez, enteras; no ha hecho falta ampliar.

1. (Marco, práctica) La prueba individual anual de funcionamiento de todos los detectores la puede
   hacer: a) el personal del titular; b) sólo personal del fabricante o de la empresa mantenedora;
   c) cualquier electricista con carné del REBT; d) el organismo de control. → **b**. Tema 1.5
   (tabla II, apdo. 4) y 2.5. Entera.
2. (Marco) Un edificio administrativo de 1.500 m² con un local de riesgo especial alto, respecto a la
   inspección decenal del RIPCI: a) exento por superficie; b) no exento; c) exento si sólo tiene
   alumbrado de emergencia; d) inspección cada cinco años. → **b**. Tema 1.6. Entera.
3. (Detección) Recorrido máximo desde cualquier origen de evacuación hasta un pulsador y altura de
   su parte superior: a) 15 m, 80-120 cm; b) 25 m, 80-120 cm; c) 25 m, 1,50 m; d) 50 m, 1,20 m. →
   **b**. Tema 2.3. Entera.
4. (Detección) Si el fabricante no fija la vida útil de un detector, se considera: a) 5 años; b) 10
   años desde su puesta en servicio; c) 20 años; d) indefinida. → **b**. Tema 2.5. Entera.
5. (Alarmas) En uso pública concurrencia el DB SI exige sistema de alarma: a) si la superficie
   excede de 1.000 m²; b) si la ocupación excede de 500 personas, apto para megafonía; c) siempre;
   d) si excede de 2.000 m². → **b**. Tema 3.3. Entera.
6. (Extinción, práctica) Para un conato en un cuadro eléctrico en tensión de una sala de control, el
   agente más indicado es: a) agua a chorro; b) espuma física; c) CO₂; d) agua de BIE. → **c**.
   Tema 4.2. Entera.
7. (Extinción) Según el RIPCI vigente, una BIE de 25 mm debe dar un caudal mínimo de: a) 85 l/min con
   4 bar mínimos y 9 bar máximos a la entrada; b) 160 l/min con 3,5 bar; c) presión dinámica entre 3
   y 6 bar; d) 100 l/min con 2 bar. → **a**. Tema 4.5 (y la c como redacción derogada). Entera.
8. (Señalización) Las señales fotoluminiscentes se sustituyen: a) cada 10 años; b) a los 20 años
   desde su fabricación, salvo que una medición de muestra dé al menos el 80 % de sus valores; c) cada
   5 años; d) nunca. → **b**. Tema 5.3. Entera.
9. (Sectorización, práctica) Una sala de grupo electrógeno integrada en el edificio es, según el DB
   SI: a) local de riesgo especial bajo, con paredes EI 90 y puerta EI2 45-C5; b) riesgo medio, con
   vestíbulo de independencia; c) riesgo alto; d) no es local de riesgo especial. → **a**. Tema 6.3.
   Entera. (Variante sobre pasos de cables: la exclusión de penetraciones ≤ 50 cm², tema 6.4.)
10. (Coordinación) El plan de autoprotección: a) caduca a los tres años; b) tiene vigencia
    indeterminada, se revisa al menos cada tres años y se hace al menos un simulacro al año; c) se
    revisa cada cinco años; d) sólo exige simulacro cada dos años. → **b**. Tema 7.2 (con la
    salvedad de vigencia de la Norma Básica). Entera.
