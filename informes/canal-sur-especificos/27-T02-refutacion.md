# Refutación · Oficial Técnico Electricista (27) · Tema 2 · REBT e ITC: documentación, puesta en servicio, verificaciones, inspecciones y mantenimiento

Fase 4 (refutar, no corregir). Tema:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/02-reglamento-electrotecnico-para-baja-tension-documentacion-puesta-en-servicio-inspecciones-y-mantenimiento.md`.
Leído entero (1.529 líneas). Fecha de lectura de las fuentes: 05-10-2026 (reloj del sistema; el
encargo dice «hoy es 24-09-2026»; el consolidado del REBT no tiene redacciones con vigencia entre
ambas fechas: última actualización, 18-12-2025).

Ficheros tocados: este informe y `27-T02-preguntas.md`. El tema no se ha tocado.

## Fuera de la lente de exactitud

`27-T02-redaccion.md` lista «Nada» en «Copiado del común» y en «Copiado de RTVE sin cambios». Todo
el tema entra en la lente de exactitud.

## Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| REBT, arts. 2, 4, 6, 18 a 26, 29 | `boe.py precepto BOE-A-2002-18099` y volcado `fuentes/canal-sur/BOE-A-2002-18099.md` | Literales; redacciones bien atribuidas (art. 2, RD 298/2021, con su redacción anterior; art. 25, RD 145/2023) |
| Cadena de redacciones | `BOE-A-2002-18099.redacciones.tsv` y `boe.py` (ib-2, ib-3, ib-52, da a da-4) | La tabla de reformas de 1.1 cuadra (RD 560/2010: arts. 18, 20, 22, ITC-BT-03, 04, 18 y DA 1.ª-4.ª; RD 1053/2014: au, ITC-BT-02, 04, 05, 10, 16, 25, 52; etc.) |
| ITC-BT-02, notas (*) y (**) | grep en el volcado | Hallazgo M1 |
| ITC-BT-03 (vigente, RD 770/2025) y a 01-05-2004 | `boe.py`; `--fecha 20040501` | 2, 3.1, 3.2 (nueve modalidades, cuatro primeras únicas), 4 a)-e), 5.4, 5.5, 5.7, 5.8, 5.9, 7, apéndice I literales. Hallazgo M3 (STS 2004) |
| ITC-BT-04 entera | volcado | Tabla 3.1 (16 grupos y límites), 3.2, 3.3, 4, 5.1-5.6, 6: literal |
| ITC-BT-05 entera | volcado | Objeto, 2, 3, 4.1 a)-h), 4.2, 5, 6 y los 16 defectos graves: literal |
| ITC-BT-18, 9 y 12 | volcado | Literal; hallazgo M2 |
| ITC-BT-19, 2.9 | volcado | Tabla 3 y condiciones literales; laguna L1 |
| ITC-BT-24, 4.1.2; ITC-BT-28, 1 y 2.1; ITC-BT-38, 2.4.2 | volcado | Literal |
| Títulos de ITC-BT-09, 10, 29, 30, 34, 38, 40, 44, 51, 52 (muestra) | volcado | Coinciden con el mapa |
| Decreto 59/2005, arts. 3 y 5 y notas | `fuentes/canal-sur/tecnica/boja-decreto-59-2005-consolidado.txt` | Literal; la cautela del Decreto 9/2011 está bien recogida |

## Hallazgos de exactitud

Graves: ninguno. Ninguna cifra, plazo, umbral o artículo mal; ninguna redacción derogada como
vigente; los modos («deberá», «podrá») bien.

Menores:

- **M1 · 1.5 · error 6 (salvedad imprecisa).** La exención de la nota (*) de la ITC-BT-02 se resume
  como «si el proyecto (firmado o visado) o la memoria se firmaron, o la licencia de obras se
  solicitó». El BOE: **siempre que el correspondiente proyecto de instalación haya sido firmado
  electrónicamente o visado antes de la fecha de aplicabilidad, o, en el caso de instalaciones que
  no requieren proyecto, si la licencia de obras fue solicitada antes de la fecha de aplicabilidad
  o la memoria técnica ha sido firmada electrónicamente**. Faltan «electrónicamente» y que la
  licencia sólo vale para las que no requieren proyecto. Propuesta: citar la nota literal en
  negrita (pregunta 14).
- **M2 · 4.4 · error 6 (salvedad omitida).** Del apartado 9 de la ITC-BT-18 se cita el 24/50 V pero
  no la frase que lo sigue: **Si las condiciones de la instalación son tales que pueden dar lugar a
  tensiones de contacto superiores a los valores señalados anteriormente, se asegurará la rápida
  eliminación de la falta mediante dispositivos de corte adecuados a la corriente de servicio.**
  Propuesta: añadirla tras la cita.
- **M3 · 1.1 · error 6 (alcance de la anulación).** «La Sentencia del Tribunal Supremo de 17 de
  febrero de 2004 declaró nulo un inciso de la ITC-BT-03 (el 4.2.c.2…)». La nota del BOE: se anula
  **el inciso 4.2.c.2, en tanto que incluye a los Ingenieros industriales**. Anulación parcial.
  Propuesta: añadir «en tanto que incluía a los ingenieros industriales».
- **M4 · 2.4 · error 9 (sin fuente).** «La c) es la más preguntable y la más incumplida»: no hay
  exámenes anteriores ni fuente sobre incumplimientos. Propuesta: quitar «y la más incumplida» (y,
  si se quiere, «la más preguntable»).

Sin hallazgo, comprobado (muestra de lo preguntable): art. 2.1 (1.000/1.500 V), 2.2 vigente y
anterior, 2.3, 2.4, 2.5, 2.6 (50/75 V); art. 4 (tabla, 230/400 V, 50 Hz); art. 23.2-3; art. 24
(previo al art. 18, silencio desestimatorio); art. 25 (Turquía, AELC, Reglamento 2019/515); art. 26;
art. 27 (quince primeros días de cada trimestre); art. 29; ITC-BT-03 (600.000/900.000 €, un mes,
24 h, 5 años, apéndice I.1 vigente, equipos 2.1.2 y 2.2); ITC-BT-04 (quintuplicado, cuatro copias,
una electrónica, un año, «18.3» literal con su nota); ITC-BT-05 (ocho letras, 100/25/25/10/5 kW,
5 y 10 años, 6 meses, calificaciones); ITC-BT-19 (250/500/1000 V; 0,25/0,5/1 MΩ; 100 m; 1 mA;
2U + 1000, mínimo 1.500 V; exclusión de locales con riesgo); ITC-BT-18 12 (anual, época seca,
cinco años); ITC-BT-24 (RA × Ia ≤ U); ITC-BT-28 (0,8 m², más de 100 personas, más de 50 con
oficinas con presencia de público); aritmética (1.800 V, 1.667 Ω, 167 Ω).

## Cobertura del enunciado

Las cinco materias del enunciado (documentación, puesta en servicio, verificaciones, inspecciones,
mantenimiento) tienen bloque propio y en su orden, precedidas del marco del REBT y las ITC.
Preguntas (`27-T02-preguntas.md`): 13 enteras, 1 a medias (14, por M1), 1 no (12).

- **L1 · Laguna · 4.3 (pregunta 12).** En las condiciones de la medida de aislamiento falta el
  párrafo que sigue a «aislados de tierra, así como de la fuente de alimentación…»: **Si las masas
  de los aparatos receptores están unidas al conductor neutro, se suprimirán estas conexiones
  durante la medida, restableciéndose una vez terminada ésta.** Es aplicación práctica directa del
  puesto. Ampliar: un guion más en la lista de condiciones de 4.3, literal.
- Hueco declarado, no laguna: la secuencia de ensayos de la UNE 20.460-6-61 / UNE-HD 60364-6 (no
  leída; el tema lo dice en 4.2 y en «Lo que este tema no da»).

## Recuento

Graves: 0. Menores: 4 (M1-M4). Lagunas: 1 (L1).
