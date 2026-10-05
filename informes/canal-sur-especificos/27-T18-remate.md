# Remate · Oficial Técnico Electricista (27) · Tema 18 · Innovación aplicada al mantenimiento

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/18-innovacion-aplicada-al-mantenimiento.md`.
Entrada: `27-T18-refutacion.md` (0 graves, 6 menores, 4 lagunas) y `27-T18-preguntas.md` (11 / 2 / 2).

**Resultado: 6 menores aplicados (los 6 confirmados en la fuente) y 4 lagunas cerradas ampliando el tema.**
**Hay contenido nuevo: procede la fase 5 bis sobre los pasajes 2.1, 2.6, 3.5, 4.2, 6.1 y las adiciones de portada,
siglas, «Lo que no da» y «Trazabilidad».** Extensión: de unas 13.100 a unas 14.970 palabras (`indice.py`).

Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo fija «hoy» en 24-09-2026; ninguna
de las fuentes normativas cambió entre las dos fechas; la ISO 29821:2026 es de abril de 2026, antes de las dos).

Ficheros tocados: el tema y este informe. Copia previa del tema en el scratchpad (`t18r/18-antes.md`), fuera del repo.

## 1. Menores (todos comprobados en la fuente antes de aplicarlos)

| N.º | Pasaje | Comprobación | Cambio |
|---|---|---|---|
| 1 | 2.1 (ISO/IEC 30141, comité) | Vista previa oficial de la ISO/IEC 30141 ed. 2.0 (2024-08), prólogo: «ISO/IEC 30141 has been prepared by subcommittee 41: Internet of Things and Digital Twin, of ISO/IEC joint technical committee 1: Information technology». El dato era cierto, pero sin fuente leída y con «JTC» sin presentar | El paréntesis «(comité conjunto JTC 1/SC 41)» se sustituye por la cita literal del prólogo y la remisión a 4.1. Sin sigla JTC |
| 2 | 7.1 (art. 2.2 RD 244/2019) | `boe.py precepto BOE-A-2019-5089 a2` (redacción única): «… de acuerdo con las definiciones del artículo 100 del Real Decreto 1955/2000, de 1 de diciembre, por el que se regulan …» | Literal completado en la tabla; párrafo nuevo con la remisión y el título literal del RD 1955/2000; la lectura de oficio queda acotada («los matices los darían esas definiciones, no leídas»); entrada nueva en «Lo que no da» |
| 3 | 6.6 (art. 61.1 Reg. 2023/1542) | Volcado `DOUE-L-2023-81096`, art. 61.1: «o, de haber sido designadas con arreglo al artículo 57, apartado 1, las organizaciones competentes en materia de responsabilidad del productor» | Primera frase reescrita con la condición y el nombre literales |
| 4 | 5.4 (art. 3.1 RD 56/2016) | `boe.py precepto BOE-A-2016-1460 a3`: «Las grandes empresas o grupos de sociedades incluidos en el ámbito de aplicación del artículo 2 … que cubra, al menos, el 85 por ciento del consumo total de energía final …» | Sujeto y alcance literales. «Normativa»: art. 3, apartados **1**, 3.a) y 5 |
| 5 | Portada, «Fuente» | Cotejo interno con 6.2 (art. 95), 5.3 (nota IT 3.3), 1.2 y 2.4 (apéndice 1) y la tabla «Normativa» | Añadidos el art. 95, el apéndice 1 y la nota a la tabla de la IT 3.3; y las fuentes técnicas nuevas. «Extensión»: unas 15.000 palabras |
| 6 | 7.11, fila «Más de 100 kW» | `boe.py precepto BOE-A-2019-5089 a4` (redacción RDL 7/2026): 4.1.a) sin excedentes no tiene límite de potencia; el de 100 kW es sólo condición ii del 4.2.a) | «Fuera de la compensación: si se quiere verter, con excedentes no acogida; si no, sin excedentes, con antivertido» |

## 2. Lagunas (se amplía el tema; las preguntas no se tocan)

| Pregunta | Laguna | Pasaje nuevo | Fuente leída |
|---|---|---|---|
| 2 (no) | Comunicaciones de los sensores IoT | **2.6 Cómo se comunican los sensores**: tabla LoRaWAN / NB-IoT / MQTT con literales; clases A y C de LoRaWAN; tres calidades de servicio de MQTT; la pasarela como equipo que mantener | LoRa Alliance, «What is LoRaWAN® Specification»; 3GPP, «Standardization of NB-IOT completed» (21-06-2016) y «The Cellular Internet of Things» (09-10-2017); OASIS, *MQTT Version 5.0* (07-03-2019), apartado 1 |
| 5 (a medias) | Ultrasonidos y descargas | **3.5 Una técnica más: los ultrasonidos**: definición 3.1 (>20 kHz), aplicaciones eléctricas de la tabla 1, riesgo de arco antes de abrir para termografía, descarga frente a vibración de 50/60 Hz, falsa descarga parcial con sensor de contacto, equipos portátiles y en línea | Vista previa oficial de la ISO 29821:2018 (prólogo, introducción, apartados 3-5, tabla 1); ficha de DIN Media de esa edición: **anulada, sustituida por ISO 29821:2026-04** (no leída; el tema lo declara) |
| 6 (a medias) | BIM y gemelo digital | **4.2**: fila nueva en la tabla y tres párrafos: definición 3.3.14 de BIM y 3.3.9 de AIM, traducción propia, y por qué un BIM sin conexión de datos no es gemelo | Vista previa oficial de la ISO 19650-1:2018 (prólogo y apartado 3); ficha AENOR de la UNE-EN ISO 19650-1:2019 (2019-07-03, En Vigor, corregida 2020-06-24, idéntica a EN ISO e ISO 19650-1:2018) |
| 11 (no) | LFP frente a NMC | **6.1**: párrafo y tabla LFP/NMC (estructura, peligrosidad comparada, propagación, manifestación) y dos lecturas de oficio para la sala de baterías | Yang y otros, *Advanced Science* 13 (2026), doi 10.1002/advs.76228; Su y otros, *Advanced Science* 13 (2026) e76502, doi 10.1002/advs.76502 (texto completo de Europe PMC, PMC13336748 y PMC13359442) |

Con estas ampliaciones las cuatro preguntas pasan a **enteras** con el tema: 2 (2.6, tabla), 5 (3.5, tabla), 6
(4.2, fila BIM y párrafos) y 11 (6.1, tabla LFP/NMC). Resultado esperado: 15 de 15.

Lo que **no** se ha escrito por no poderse confirmar: bandas de frecuencia, alcances y duración de pila de LoRaWAN
o NB-IoT (sólo en fuentes secundarias); temperaturas de inicio del embalamiento por química (varían entre
estudios); la densidad de energía comparada de LFP y NMC (no está en las revisiones leídas); el texto de la ISO
29821:2026. Todo ello consta en «Lo que este tema no da».

## 3. Pasajes cambiados (para la 5 bis)

1. Portada, celdas «Fuente» y «Extensión».
2. Siglas: BIM, LPWA, NB-IoT, 3GPP, LFP, NMC/NCM, kHz.
3. «Qué se puede preguntar»: redes y protocolos de los sensores, BIM, ultrasonidos, química de litio.
4. 2.1, última frase (comité de la ISO/IEC 30141).
5. **2.6, epígrafe nuevo** (nuevo).
6. **3.5, epígrafe nuevo** (nuevo).
7. **4.2**: fila BIM y tres párrafos antes de «La "tasa de sincronización adecuada"» (nuevo).
8. 5.4, primera frase.
9. **6.1**: párrafo, tabla LFP/NMC y dos viñetas tras la tabla de químicas (nuevo).
10. 6.6, primera frase.
11. 7.1: fila de la tabla de exclusiones y párrafo «La segunda exclusión».
12. 7.11, fila «Más de 100 kW de inversores».
13. «Normativa que el tema invoca», fila del RD 56/2016.
14. «Lo que este tema no da»: art. 100 del RD 1955/2000; vistas previas y ISO 29821:2026; especificaciones de
    LoRaWAN, NB-IoT y MQTT; descargas parciales y cifras de embalamiento.
15. «Trazabilidad»: ocho filas nuevas y ampliación de la lista de oficio.

Relectura de antecedentes: «el artículo 2.2» (7.1) tiene delante la tabla del art. 2; «Su artículo 61.1» (6.6)
sigue a «El capítulo VIII»; «Una de ellas» (6.1) sigue a «dos revisiones científicas»; «esa edición» (3.5) sigue a la
de 2018; «Las dos primeras» (2.6) remite a la tabla inmediatamente anterior; «la misma norma» (4.2) a la ISO
19650-1. Las remisiones internas nuevas (2.2, 2.5, 3.2, 4.1, 6.4, 6.5, tema 9) existen.

## 4. Lentes

- `indice.py`: índice regenerado, 58 epígrafes (antes 56), 14.966 palabras. Sigue sin portada automática (el tema no
  tiene fila en `portadas.tsv`; no la he añadido: fuera de mi encargo).
- `refutar_prosa.py`: 0 hallazgos (tras presentar DIN, LCO, LMO y NCA).
- `negritas.py` con las 5 fuentes normativas y los textos técnicos guardados (30141, 19650-1, 29821, LoRaWAN,
  MQTT, AENOR 19650-1, las dos revisiones): 207 negritas; 21 «NO ESTÁ» (15 heredadas, ya cotejadas) y 6 nuevas, todas
  comprobadas a mano: 3 del 3GPP (leídas con WebFetch, sin fichero local: el servidor bloquea la descarga),
  2 de la ISO 29821 y 1 de la ISO 19650-1 (cortes de línea y de página del PDF). «Otro artículo»: 6, falsos
  positivos (art. 2 citado dentro del 3.1 del RD 56/2016; art. 57 dentro del 61.1; anexo V tras el art. 96; título
  del RD 1955/2000 dentro del art. 2 del RD 244/2019; los dos heredados).
- `refutar_exactitud.py`: 59 citas, 11 «no literales» (7 heredadas; 4 nuevas, falsos positivos: toma por artículo
  los números de epígrafe 4.1, 5, 6.4 y la remisión al art. 57). `refutar_modo.py`: 0 hallazgos.

## 5. Pendiente (no es de este remate)

- La fecha efectiva de la etiqueta del art. 13.1 del Reglamento (UE) 2023/1542 (acto de ejecución del 13.10).
- La fila del tema en `herramientas/portadas.tsv`.
