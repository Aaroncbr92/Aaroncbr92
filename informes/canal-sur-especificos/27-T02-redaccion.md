# Redacción · Oficial Técnico Electricista (27) · Tema 2 · REBT e ITC: documentación, puesta en servicio, verificaciones, inspecciones y mantenimiento

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/02-reglamento-electrotecnico-para-baja-tension-documentacion-puesta-en-servicio-inspecciones-y-mantenimiento.md`
(unas 15.700 palabras con índice según `indice.py`, 43 epígrafes). Material: `27-investigacion-A-electrico.md`
(§1, §3 y, de §6 y §7, la ITC-BT-18 apdo. 12, la ITC-BT-19 apdo. 2.9 y el apéndice I de la
ITC-BT-03). Reuso RTVE: `teitse/15`, `teitse/09`, `teitse/13` (actualizar: sí; redacción a
21-12-2022). Fecha de lectura declarada: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»; la investigación no halló redacciones con vigencia entre ambas fechas).

Lentes ejecutadas: `indice.py` (índice generado); `refutar_prosa.py` (0 hallazgos, tras presentar
ISO, SAI, TT y RA/Ia/U en las siglas y quitar «(*)» y «(**)» de la trazabilidad, que rompían la
paridad de negritas); `negritas.py` contra `fuentes/canal-sur/BOE-A-2002-18099.md` y
`fuentes/canal-sur/tecnica/boja-decreto-59-2005-consolidado.txt`: 264 negritas cotejadas, 2 no
encontradas (rótulos: «Enunciado del programa», «Qué se puede preguntar.») y 11 «atribuidas a otro
artículo» que son falsos positivos (las citas de los artículos 18, 21, 23 y 24 contienen «artículo
12.3 / 12.5 de la Ley 21/1992» o «artículo 18» dentro del propio texto).

Ficheros tocados: el tema (nuevo) y este informe. Nada más.

## Fuentes leídas por el redactor (05-10-2026)

Todas con `boe.py precepto BOE-A-2002-18099 <bloque>` (redacción vigente hoy):

- Artículo único (`au`) y `.redacciones.tsv` (cadena de reformas).
- Reglamento: `a1`, `a2`, `a4`, `a1-10` (art. 18), `a1-11` (19), `a2-2` (20), `a2-3` (21), `a2-4`
  (22), `a2-5` (23), `a2-6` (24), `a2-7` (25), `a2-8` (26), `a2-9` (27), `a2-10` (28), `a2-11`
  (29).
- ITC-BT-02 (`ib-2`): encabezamiento, notas (*), (**) y de correspondencia; entrada UNE-HD 60364-6.
- ITC-BT-03 (`ib-3`): 2, 3, 4, 5, 7, apéndice I.
- ITC-BT-04 (`ib-4`) y ITC-BT-05 (`ib-5`) enteras; ITC-BT-05 además con `--fecha 20150101`.
- ITC-BT-18 (`ib-18`) apdos. 9 y 12; ITC-BT-19 (`ib-19`) apdo. 2.9; ITC-BT-24 apdo. 4.1 (TT);
  ITC-BT-28 (`ib-28`) apdos. 1 y 2.1.
- Primera línea de las 52 ITC (títulos del mapa): coinciden con los de teitse/15.
- Decreto 59/2005 consolidado (txt de la investigación): arts. 3, 5, 7 y anexo (sólo se usan 3 y 5).

## Correcciones a RTVE y a la investigación (manda la fuente)

- **Art. 25**: RTVE lo resumía en su redacción de 2002 («aceptar certificados y marcas de
  conformidad… del Espacio Económico Europeo»). Hoy es «Reconocimiento mutuo» (RD 145/2023). Se cita
  la vigente.
- **ITC-BT-05, letra h) del 4.1**: con `--fecha 20150101` la lista anterior tenía siete letras
  (a-e, g, h, sin f) y la h) era el alumbrado exterior; la letra de recarga del vehículo eléctrico
  llega con la redacción del RD 1053/2014. El tema lo dice así, sin afirmar más.
- **teitse/09 §3**: decía que la ITC-BT-05 «califica como no evidentes» dos entradas de la lista de
  defectos graves; la ITC no dice eso. Se ha quitado y se da la lista completa (16 guiones).
- **teitse/09 §3**: «es la misma regla que el reglamento de instalaciones térmicas aplica»: no
  verificado; quitado.
- **teitse/13 §3**: no daba los umbrales de la tabla 3.1 («no se ha leído»); ahora se dan todos,
  leídos.
- **teitse/15 §7**: «la ITC-BT-52 es la que más se pregunta ahora»: sin fuente; quitado. Su
  incorporación por el RD 1053/2014 se confirma en la nota del artículo único.
- **teitse/15 §8 y ficha**: lo de la convocatoria RTVE (actualización de 28/04/2021) quitado.
- **teitse/15 §6 «Ministerio de Ciencia y Tecnología»**: literal del art. 29 vigente; se mantiene.
- **Investigación §3.5**: «las instalaciones de baja tensión no necesitan autorización» no se
  afirma (el anexo del Decreto 59/2005 tiene una historia de supresión y redacción por órdenes que
  no he resuelto); se dice sólo que el REBT no exige autorización sino registro (art. 18) y se cita
  el art. 5.1.
- **Mapa de ITC**: la columna «dónde» de RTVE remitía a temas de RTVE. Ahora remite sólo a temas de
  este puesto ya escritos que la usan (grep en 01, 06, 07, 08, 11) o a los temas cuyo enunciado es
  esa materia (3, 4, 5).

## Avisos para el verificador

- ITC-BT-05 apdos. 1 y 2.2 remiten al «artículo 20» para inspecciones (hoy el 21): citado literal
  con salvedad (4.1 y 5.1).
- ITC-BT-04 5.5 remite al «Artículo 18.3» como salvedad del suministro; el suministro provisional
  está en el 18.4. Citado literal con nota.
- Tablas recompuestas (1.4 art. 4.1; 2.4 ITC-BT-04 3.1; 4.3 ITC-BT-19 tabla 3): contenido de la
  norma en redonda. La de 5.4 lleva negritas literales dentro de celdas.
- Aritmética: 2·400+1000 = 1.800 V; 50/0,03 ≈ 1.667 Ω; 50/0,3 ≈ 167 Ω.
- Aplicaciones a Canal Sur (2.4 pública concurrencia; 5.2 punto 3; 6.4 ejemplo): declaradas como
  oficio; la ITC-BT-28 no nombra estudios de televisión.
- 6.1: el tema no afirma si el mantenimiento ordinario puede hacerlo personal propio del titular;
  lo declara no resuelto por el art. 20.

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur, no hay temas cerrados del
puesto 27 y `AGRUPACION.tsv` marca el tema 27/2 como «nuevo» (sin repetición).

## Copiado de RTVE sin cambios

Nada. Los tres temas de RTVE de este tema están marcados «actualizar: sí» y citan norma, de modo que
nada de ellos entra en esta excepción. Además, todo lo tomado de ellos se ha adaptado: quitadas las
negritas de énfasis (en RTVE no son literal), las remisiones a sus temas, las referencias a su
convocatoria y a «este temario», y releído cada precepto en su redacción vigente. Pasajes de oficio
procedentes de RTVE, adaptados (se verifican): la lectura de las tres finalidades (1.2), los tres
verbos del art. 2.5 (1.3), el orden de consulta (1.8, de teitse/15 §8), las tres observaciones del
mapa (1.7), la tabla de documentos gráficos y las reglas de documentación (2.5, de teitse/13 §5 y
§6, reducidas), la tabla de los tres regímenes (4.1, de teitse/09 §1), el método de medida de
tierras y la pinza (4.4, de teitse/09 §5), los tipos de mantenimiento, el plan y la tabla de estados
de medida (6.3, de teitse/09 §4 y §6).

## Lo nuevo (pasa entero por el ciclo)

1.1 entero (reformas, aviso de «nuevo REBT»); 1.3 apdo. 2 literal y su lectura de 2021; 1.5 art. 25,
art. 26 y ITC-BT-02 con la cautela UNE-HD; 1.6 entero (ITC-BT-03); 2.1 a 2.4 en letra (tabla 3.1
completa, 3.2, 3.3, excepción de recarga, campo de la ITC-BT-28); 3.1 a 3.6 en letra; 3.7 (Decreto
59/2005); 4.2 y 4.3 enteros (ITC-BT-05 3; ITC-BT-19 2.9); 4.4 (ITC-BT-18 9, ITC-BT-24 TT); 4.5
(apéndice I); 5.1 a 5.5 en letra; 6.1, 6.2 y 6.4.

## Comprobación con 10 preguntas tipo test

Contestadas sólo con el tema. Las diez, enteras; no ha hecho falta ampliar.

1. (REBT, campo) El REBT se aplica en corriente continua a tensiones nominales iguales o inferiores
   a: a) 75 V; b) 750 V; c) 1.000 V; d) 1.500 V. → **d**. Tema 1.3. Entera.
2. (REBT, mantenimiento) Según el artículo 20 del REBT, si una instalación necesita modificaciones,
   deben efectuarlas: a) el titular, con personal propio; b) una empresa instaladora; c) un
   organismo de control; d) la empresa suministradora. → **b**. Tema 6.1. Entera.
3. (Documentación) Las instalaciones de locales de pública concurrencia precisan proyecto:
   a) si P > 10 kW; b) si P > 20 kW; c) si P > 50 kW; d) sin límite. → **d**. Tema 2.4. Entera.
4. (Documentación, aplicación) Una instalación que se ejecutó con proyecto recibe varias
   ampliaciones pequeñas. Necesita proyecto nuevo cuando, sumadas, superan: a) el 25 %; b) el 50 %
   de la potencia prevista en el proyecto anterior; c) el 50 % de la potencia contratada; d) 100 kW.
   → **b**. Tema 2.4 (ITC-BT-04 3.2.c). Entera.
5. (Puesta en servicio) Presentado en papel, el certificado de instalación se entrega ante la
   comunidad autónoma: a) por duplicado; b) por triplicado; c) por cuadruplicado; d) por
   quintuplicado. → **d**. Tema 3.4 (y devuelve cuatro; por vía electrónica, una sola). Entera.
6. (Puesta en servicio, aplicación) Para un montaje repetido idéntico registrado la primera vez, se
   puede prescindir de la documentación de diseño durante: a) seis meses; b) un año; c) dos años;
   d) cinco años, salvo modificaciones significativas. → **b**. Tema 3.5. Entera.
7. (Verificaciones) La resistencia de aislamiento mínima de una instalación de 230/400 V, medida
   con 500 V en continua, es: a) ≥ 0,25 MΩ; b) ≥ 0,5 MΩ; c) ≥ 1 MΩ; d) ≥ 2 MΩ. → **b**. Tema 4.3.
   Entera.
8. (Verificaciones, aplicación) Al medir el aislamiento de un circuito que alimenta equipos
   electrónicos de una sala técnica, la ITC-BT-19 manda: a) desconectar sólo el neutro; b) unir entre
   sí fases y neutro durante la medida; c) medir a 1.000 V; d) no medir. → **b**. Tema 4.3. Entera.
9. (Inspecciones) Un organismo de control encuentra un defecto grave en una instalación en servicio.
   La calificación y el plazo son: a) negativa, remisión inmediata; b) condicionada, plazo no
   superior a 6 meses; c) condicionada, 1 año; d) favorable con anotación. → **b**. Tema 5.4.
   Entera. (Variante: periodicidad de las inspecciones periódicas de lo que tuvo inspección inicial:
   5 años, tema 5.3.)
10. (Mantenimiento) Según la ITC-BT-18, la comprobación de la instalación de puesta a tierra se hace
    al menos: a) cada mes; b) cada año, en la época en que el terreno esté más seco; c) cada cinco
    años; d) sólo al dar de alta la instalación. → **b**. Tema 6.2 (y cada cinco años, electrodos al
    descubierto donde el terreno no favorezca su conservación). Entera.
