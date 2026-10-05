# Remate · Oficial Técnico Electricista (27) · Tema 9 · Climatización y frío industrial

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/09-climatizacion-y-frio-industrial-en-edificios-y-salas-tecnicas.md`.
Entradas: `27-T09-refutacion.md` (graves 0 · menores 4 · lagunas 2) y `27-T09-preguntas.md` (13 enteras, 0 a medias, 2 no).
Ficheros tocados: el tema y este informe. Nada más.
Fecha de lectura de las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; ninguna fuente usada cambia entre las dos fechas).

**Amplió contenido nuevo: sí** (L1, duplicación de la frecuencia si falla la detección de fugas, IF-17, 2.5.2; L2, equiparación a nivel 1 a efectos de inspección, IF-14, 3.1; y las salvedades M1-M4). Procede la fase 5 bis sobre los pasajes de abajo.

## Comprobación en la fuente

| Corrección | Fuente releída (05-10-2026) | Resultado |
|---|---|---|
| M1 / L2 · IF-14, 3.1 | `BOE-A-2019-15228.md`, l. 3035-3046: párrafo «Las instalaciones de nivel 2, que de acuerdo con el artículo 11…» y punto 6 «…se realizará cada diez años independientemente del nivel de la instalación y del refrigerante empleado.» | Confirmada. Aplicada. La referencia a los A2L se ciñe al art. 11.2 (l. 335: excepción A2L «siempre que se cumplan las siguientes condiciones») |
| M2 · art. 13.3 R. (UE) 2024/573 | `documentos/reglamento-ue-2024-573.txt`, l. 1066-1067: «…con un tamaño de carga de al menos 40 toneladas equivalentes de CO2» y exclusión de equipos militares y de aplicaciones por debajo de -50 °C | Confirmada. Aplicada en la columna «Salvedad» |
| M3 · IF-17, 2.5.3.5 | `BOE-A-2019-15228.md`, l. 3594: «…se realizará una nueva revisión, en todo caso antes de un mes de la fecha en la que se identificaron las fugas…» | Confirmada. Aplicada, con la distinción de los dos plazos frente a 2.5.1 (l. 3543) |
| M4 · art. 6.2 y 6.4 | Reglamento, l. 723-726: 6.2 sólo para art. 5.2 e) y f) **y hayan sido instalados a partir del 1 de enero de 2017**; 6.4 sólo letra f) (aparamenta) | Confirmada. Aplicada; además se precisa que el 6.1 cubre las letras a) a d) |
| L1 · IF-17, 2.5.2 | `BOE-A-2019-15228.md`, l. 3546-3547 | Literal confirmado. Ampliado en 7.5 y en 7.7 |

Ninguna corrección del informe de refutación resultó equivocada.

## Pasajes cambiados

1. **Portada, Extensión**: 15.700 → 16.100 palabras (`indice.py`: 16.096 después).
2. **3.3, tabla del art. 13, fila 1-1-2025, columna «Salvedad»** (M2): añade la prohibición previa para cargas de al menos 40 t CO2-eq y la exclusión literal de equipos militares y aplicaciones por debajo de -50 °C.
3. **6.3, final del último párrafo** (M3): literal de la nueva revisión «antes de un mes de la fecha en la que se identificaron las fugas» y frase que separa los dos plazos de un mes (2.5.1, desde la subsanación; 2.5.3.5, desde la identificación).
4. **7.5, párrafo del sistema de detección** (M4): reescrito; obligación para refrigeración, aire acondicionado, bombas de calor y protección contra incendios (6.1, 6.3); para aparamenta eléctrica, sólo si instalada a partir del 1-1-2017 (6.2), control cada seis años (6.4).
5. **7.5, párrafo nuevo** (L1): el RSIF recoge la obligación (IF-17, 2.5.2) y literal «**En los casos en que no funcionen correctamente se duplicará la frecuencia de las revisiones de fugas anteriormente mencionadas.**», con la aclaración de que se refiere a las revisiones del programa del propio RSIF.
6. **7.6, tras la cita de 3.1** (M1, L2): literal de la equiparación a nivel 1; aplicación a los A2L del art. 11.2 (remite a 2.3); literal del punto 6 (equipos a presión, cada diez años sea cual sea el nivel).
7. **7.7, tabla**: fila «Sistema de detección de fugas» con la duplicación y la cita IF-17, 2.5.2; fila «Inspección, nivel 2» con la salvedad; fila nueva «Inspección de equipos a presión».

Antecedentes releídos: «esta nueva revisión», «ese sistema», «su propio programa», «(2.3)» y «punto 6 de la lista de la IF-14, 3.1» tienen delante su referente.

## Lentes

- `indice.py`: 48 epígrafes, índice sin cambios de rúbrica.
- `refutar_prosa.py`: 1 hallazgo previo, no tocado por el remate (sigla «GF» en la tabla de filtros del RITE, que es la notación de la propia norma).
- `negritas.py` (RSIF, RITE, R. (UE) 2024/573, guía IDAE): todas las negritas nuevas, literales. Los 8 «no está» y 5 «otro artículo» son previos (ASHRAE, rótulos propios, anclaje de la herramienta).
- `refutar_exactitud.py`: los avisos sobre «(IF-14, 3.1)» son falsos positivos por leer el número de apartado de la ITC como artículo; el literal se ha comprobado a mano (l. 3036).
- `refutar_modo.py`: 0 hallazgos.
