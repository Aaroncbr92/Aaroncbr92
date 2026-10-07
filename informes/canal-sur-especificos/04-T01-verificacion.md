# 04 · Ayudante de Producción · Tema 1 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/01-la-produccion-audiovisual.md`.
Verificado el 06-10-2026 (el encargo dice «hoy es 24-09-2026»; el reloj marca 06-10-2026).
Ficheros tocados: el tema (tres correcciones) y este informe. Ninguno más.

## Copiado del común y de RTVE sin cambios: sólo literalidad

Cotejo automático párrafo a párrafo (normalizando espacios y negritas) contra
`32-productor-a/01` y `02`, `31-presentador-productor-de-radio/13`, y RTVE `gestion/27`,
`produccion/04`, `produccion-asistencia/01` y `produccion/01`. Todos los pasajes listados bajo
«Copiado del común» y «Copiado de RTVE sin cambios» son literales. Los que no casan son
exactamente los cambios declarados entre corchetes (comprobados con `grep` contra el original:
«Para el área de producción», remisiones a los temas 9, 10, 11 y 14, «las «fases del proceso
productivo»», última frase de «Producción y realización», «entornos digitales»). No se
re-verificó su contenido.

## Fuentes releídas hoy (06-10-2026)

- RD 1681/2011 (`fuentes/canal-sur/radio/BOE-A-2011-19600.txt`), arts. 4, 5 (a-v), 6 y 7.
- RD 500/2024 (`fuentes/canal-sur/realizador/BOE-A-2024-10685.txt`), l. 2367 y 12416: modifica
  arts. 2, 10, 12, 15 y anexos I y III del RD 1681/2011; no los arts. 4 a 7.
- INCUAL IMS074_3 (`fuentes/canal-sur/produccion/incual-IMS074_3.txt`), págs. 1-2.
- X Convenio (`documentos/x-convenio-rtva-boja-240-2014.txt`): fichas 5212705 (pág. 110) y
  5331000 (pág. 194); niveles B03/B04 en la relación de puestos (l. 1451-1530); 114 fichas y 114
  cláusulas abiertas; una sola denominación «AYUDANTE DE PRODUCCIÓN».
- Carta 2024-2029: arts. 7.1 y 24 (l. 473-490, 1135-1186).
- Contrato-programa 2024-2026: cláusula tercera, punto 46 («en coordinación con las áreas…»).
- Ley 13/2022, art. 2: redacción única (`BOE-A-2022-11311.redacciones.tsv`).
- `temas/canal-sur-comun/06-…md`, art. 24 (para la remisión del tema).

## Comprobado sin hallazgo

Portada y «Redacción que se estudia»; siglas; párrafo nuevo de «Los entornos digitales»;
citas de la Carta 24.1 y 24.2; competencia general (art. 4 y INCUAL); las diez letras del art. 5
citadas, s) y t); i), k), l) como promoción, comercialización y explotación; art. 6.b; art. 7.1 y
7.2 c), e), f); UC0207-0209 (texto del INCUAL: «en televisión»), ámbito, sectores, ocho
ocupaciones, 510 horas; objeto, diez tareas y cláusula de la ficha del Ayudante; objeto, tarea 8 y
«tanto si se realiza con medios propios como ajenos» del Productor/a; campos de dirección y
departamento en blanco; pasajes adaptados de RTVE («Lo que no es una fase», EDL, cierre de
«Las fases en entornos digitales»), fieles a `produccion-asistencia/01` §§ 1-3 y
`produccion/04` § 5; art. 5.m en «Lo que no es una fase»; columna «Tema» de «Las funciones, fase
por fase» y remisiones de «Lo que este tema no da» contra el enunciado; casos prácticos.

## Correcciones aplicadas

1. **Error 9 / 1** («Producción propia, ajena y coproducción»): «El texto entero del artículo está
   en el tema 6 del temario común» → «El artículo, resumido, está en el tema 6 del temario común».
   El tema 6 del común lo resume, no lo transcribe.
2. **Error 9** («Las funciones del área según el título»): «las letras ñ) a v), de competencias
   personales y sociales» → «de competencias que no son propias de la producción (el artículo no
   las separa con rótulo)». El art. 5 las titula todas «profesionales, personales y sociales» sin
   distinguir.
3. **Error 9** («Las funciones en radio», párrafo final nuevo): decía que los criterios b), c), e)
   y g) son «casi palabra por palabra» tareas de la ficha, incluida la c) «condiciones de
   intervención de los invitados». La ficha no tiene esa tarea. Ahora: b), e) y g) recogen
   citaciones, aplicación del plan de trabajo y archivo; se dice expresamente que la c) no figura
   en la ficha.

Antecedentes releídos tras los cambios: «el artículo» (24.2, en el mismo párrafo), «entre estas»
(letras ñ-v), «la ficha» (sigla presentada en la entrada).

## Lentes

- `negritas.py` (RD 1681/2011, IMS074_3, convenio, Carta, Contrato-programa, RD 500/2024,
  Ley 13/2022): 150 negritas; 26 «no están», las mismas que en la redacción (Cerdà Bañón, copiado
  del común, y rótulos); 0 atribuidas a otro artículo.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_exactitud.py` con la Ley 13/2022: 15 «no literales», falsos positivos: son citas del
  RD 1681/2011, del INCUAL y del Contrato-programa que la lente ancla en artículos de la LGCA;
  cotejadas a mano arriba.
- `refutar_prosa.py`: 1, «HACIA» en la tabla copiada del común (falso positivo).
- `indice.py`: índice sin cambios; 36 epígrafes.

## Pendiente para refutación

- La fila «Diseña el plan de transmisiones (dato de la ficha del ayudante)» y la tabla del reparto
  son copia del común (no revisadas).
- La Trazabilidad fecha la Carta y el Contrato-programa el 25/09/2026; los pasajes citados se han
  vuelto a leer hoy y coinciden.
