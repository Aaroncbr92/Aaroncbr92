# Verificación · Oficial Técnico Electricista (27) · Tema 2 · REBT e ITC

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/02-reglamento-electrotecnico-para-baja-tension-documentacion-puesta-en-servicio-inspecciones-y-mantenimiento.md`
(16.082 palabras tras la verificación según `indice.py`, 43 epígrafes). Fecha de lectura de todas las
fuentes: **05-10-2026** (reloj del sistema; el encargo dice «hoy es 24-09-2026»; el BOE no muestra
redacciones con vigencia entre ambas fechas: última actualización del consolidado, 18-12-2025).

Ficheros tocados: el tema y este informe. Nada más (los otros temas del puesto que `git status` da
como modificados no los he tocado).

## Copiado del común / Copiado de RTVE sin cambios

El informe de redacción lista «Nada» en ambas secciones. No hay pasajes que saltar ni que comprobar
con diff: **todo el tema se ha verificado**, incluidos los pasajes de oficio adaptados de RTVE.

## Fuentes releídas (05-10-2026)

- `boe.py precepto BOE-A-2002-18099`: `au`, `a1`, `a2` (y `--fecha 20200101`), `a4`, `a6`, `a1-10`,
  `a1-11`, `a2-2` (y `--fecha 20040101`), `a2-3`, `a2-4`, `a2-5` a `a2-11`; `ib-2` (encabezamiento,
  notas (*), (**), (1)-(25), entrada UNE-HD 60364-6); `ib-3` entera (y `--fecha 20250901`, apéndice
  I.1); `ib-4` y `ib-5` enteras (y `ib-5 --fecha 20150101`); `ib-18` 9 y 12; `ib-19` 2.9; `ib-24`
  4.1.2; `ib-28` 1 y 2.1; `ib-38` 2.4.2; encabezamientos de las 52 ITC; cadena de redacciones de
  todos los bloques con más de una.
- API de datos abiertos del BOE: metadatos (BOE núm. 224, 18-09-2002; actualización 18-12-2025;
  «Finalizado») y análisis (referencias posteriores: las diez reformas y la STS de 17-2-2004).
- Decreto 59/2005 consolidado de la Junta (versión 17-02-2024): arts. 1, 3, 4, 5 y sus notas.
- AEMC, *Entendiendo las pruebas de resistencia de tierra* (2003): método 62 %, pinza.

## Correcciones aplicadas (cada una comprobada en la fuente)

| # | Epígrafe | Error | Qué había | Qué dice la fuente / qué queda |
|---|---|---|---|---|
| 1 | 1.1, tabla de reformas | 3 recuento | RD 560/2010: «Artículos 18, 20 y 22; ITC-BT-03; DA» | La cadena de redacciones atribuye a BOE-A-2010-8190 también **ITC-BT-04** (2.ª de 4 redacciones) e **ITC-BT-18** (la vigente); el análisis del BOE dice «SE SUSTITUYE lo indicado». Añadidas |
| 2 | 1.1, aviso «nuevo REBT» | 9 sin fuente | «se ha anunciado en foros profesionales» (fuente no citada en el tema ni releída) | Reescrito sólo con lo comprobado: ninguna reforma posterior al RD 770/2025 en el BOE; actualización 18-12-2025. Igual en «Lo que este tema no da» |
| 3 | 1.3, aplicación | 9 / exceso | rehacer un cuadro obliga a que «ese cuadro y lo que cuelga de él» cumplan | Art. 2.2.b: «**solo en lo que afecta a la parte modificada, reparada o ampliada**». Ahora «la parte rehecha» |
| 4 | 1.3, cambio de 2021 | 6 salvedad | antes sólo alcanzaba a modificaciones/reparaciones «de importancia» | La redacción anterior incluía también «**y a sus ampliaciones**». Añadido |
| 5 | 1.5, ITC-BT-02 nota (*) | 6 salvedad | exención de dos años para «proyecto o memoria firmados antes» | La nota exige «nueva norma de instalación», proyecto firmado o visado, memoria firmada o **licencia de obras** solicitada antes. Completado |
| 6 | 1.6, apéndice I anterior | 6 salvedad | «exigía un instalador contratado en plantilla a jornada completa» | La redacción a 01-09-2025 admitía tiempo parcial si el horario era menor, un socio o el autónomo habilitado. Añadido «como regla» y las salvedades |
| 7 | 2.1 | prosa | «cuyo objeto es **determinando…**» | ITC-BT-04, 1: «desarrollar las prescripciones del artículo 18…, determinando…». Antecedente añadido en redonda |
| 8 | 2.5 | 9 | art. 19 = «as built… de lo realmente ejecutado» | El art. 19 no dice «realmente ejecutado»: son instrucciones anexas al certificado. Suavizado |
| 9 | 3.1 | 3 recuento | «cinco pasos» y resumen con seis verbos | Resumen ajustado a las cinco letras a)-e) |
| 10 | 3.7 | 6 salvedad | art. 5.1 del Decreto 59/2005 sin cautela | El consolidado de la Junta anota en los arts. 1, 3, 4 y 5 que **la aplicación de la presente modificación queda supeditada a la futura aprobación de la Orden** (DF única del Decreto 9/2011). Añadido literal; la orden sigue sin leerse |
| 11 | 4.3, rigidez | 6 salvedad | sólo 2U + 1000 V y la exclusión de locales con riesgo | ITC-BT-19 2.9: se ensaya cada conductor, neutro incluido, a tierra y entre conductores, **salvo** materiales ensayados por el fabricante; interruptores cerrados. Añadido |
| 12 | 4.3, equipos electrónicos | 9 | explicación técnica sin marcar | Marcada «Lectura de oficio» (ya estaba en la trazabilidad como oficio) |
| 13 | 4.3, fugas | 4 modo / 1 | «los dos valores que la ITC-BT-04 **manda comprobar** a la suministradora» y «los dos defectos que les corresponden» (aislamiento y tierra, cuando los valores eran aislamiento y fugas) | ITC-BT-04, 6: la suministradora «**podrá realizar**» verificaciones; si aislamiento o fugas fallan, no podrá conectar. Corregido el modo y desligada la tierra de las fugas |
| 14 | 6.2 | 9 / absoluto | «la única periodicidad de mantenimiento que el REBT fija con carácter general» | Grep del consolidado: ITC-BT-38 2.4.2 fija controles semanal, mensual y revisión anual en quirófanos. Reescrito: periodicidad de alcance general, con la de quirófanos como propia de esos locales |
| 15 | 6.4, punto 1 | 6 salvedad | inspección periódica «cada cinco años» | ITC-BT-05 4.2: también cada 10 años las comunes de edificios de viviendas > 100 kW. Añadido |
| 16 | Portada, normativa, trazabilidad | 8 / 9 | art. 6 usado en 1.2 sin citarse; «ITC-BT-24 apartado 4.1»; ITC-BT-03 anterior y método de tierra sin fuente | Art. 6 añadido; ITC-BT-24 **4.1.2** (el TT está en 4.1.2); ITC-BT-38 2.4.2; redacción de ITC-BT-03 a 01-09-2025; filas nuevas: datos abiertos del BOE y manual AEMC (fuente técnica del método de caída de potencial y la pinza) |

Comprobado que cada «ese artículo», «la ITC», «esa orden» de los pasajes cambiados tiene delante su
antecedente.

## Confirmado sin cambios (muestra de lo más preguntable)

Art. 1 (tres finalidades); art. 2.1 (1.000 V CA / 1.500 V CC), 2.2 (redacción de 2021, 50 %), 2.3,
2.4, 2.5, 2.6; art. 4 (tabla, 230/400 V, 50 Hz); arts. 18 a 29 literales; ITC-BT-02: 25 notas de
correspondencia, coexistencia 1-10-2025, UNE-HD 60364-6 (2017; A11 y A12 de 2018), ninguna nota la
liga a la UNE 20.460-6-61; ITC-BT-03: 2.1, 2.2, 3.1, 3.2 (nueve modalidades, cuatro primeras
únicas), 4 (cinco situaciones), 5.4, 5.7 (un mes), 5.8 (600.000/900.000 €), 5.9, 7 a)-j) (24 h,
5 años), apéndice I.1 vigente y 2.1.2; ITC-BT-04 entera (tabla 3.1 con sus 16 grupos y límites, 3.2,
3.3, 4, 5.1 a 5.6, quintuplicado, cuatro copias, una electrónica, un año, 6); ITC-BT-05 entera (ocho
letras de 4.1, 5 y 10 años, calificaciones, 6 meses, 16 defectos graves); la h) de 4.1 no existía a
01-01-2015 (la lista era a-e, g, h); la remisión al «artículo 20» de ITC-BT-05 1 y 2.2 es literal
desde 2002 y el art. 20 ya era «Mantenimiento»; ITC-BT-18 9 (24/50 V) y 12; ITC-BT-19 2.9 (tabla 3 y
condiciones); ITC-BT-24 RA × Ia ≤ U; ITC-BT-28 1 y 2.1; los 52 títulos del mapa y los recuentos por
familia (5+6+6+1+6+3+3+12+6+4 = 52); las remisiones «Dónde» del mapa existen en los temas citados
(no son exhaustivas: otros temas del puesto escritos después también usan algunas ITC, lo que no es
error); aritmética 1.800 V, 1.667 Ω, 167 Ω; Decreto 59/2005 arts. 3 y 5.1 literales.

## Lentes

- `negritas.py` (BOE-A-2002-18099 + Decreto 59/2005): 266 negritas; 2 no están (rótulos
  «Enunciado del programa», «Qué se puede preguntar.»); 11 «atribuidas a otro artículo», falsos
  positivos (citas de los arts. 18, 21, 23 y 24 que contienen «artículo 12.3/12.5 de la Ley
  21/1992»).
- `refutar_exactitud.py`: 9 «no literales» y 8 citas entre paréntesis: falsos positivos por anclaje
  (toma «artículo 18/20» o el número de apartado de una ITC como artículo); todas esas negritas están
  literales según `negritas.py`.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0 hallazgos. `indice.py`: índice regenerado.

## Huecos que siguen declarados

UNE 20.460-6-61 y UNE-HD 60364-6 no leídas; orden andaluza del art. 5.3 del Decreto 59/2005 no
leída (y si se aprobó, condición de aplicación de la redacción de 2011, no comprobado); Ley 21/1992,
RD 2200/1995 y guía técnica del art. 29 no leídas; organización del mantenimiento de RTVA/CSRTV, sin
documento publicado.
