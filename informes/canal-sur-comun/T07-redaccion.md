# T07 · Redacción · X Convenio Colectivo de la RTVA y cuadro de licencias y permisos

Tema: `temas/canal-sur-comun/07-x-convenio-colectivo.md` (22.681 palabras de cuerpo, contadas con
`herramientas/tema.py:cuerpo`). Fase 2 (redactar, un solo agente). Fecha de trabajo y de lectura de
todas las fuentes: **24-09-2026**. Escrito por partes, guardando cada bloque.

## Fuentes leídas (todas el 24-09-2026)

- **Convenio**, BOJA núm. 240/2014 (`fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt`):
  leído entero el articulado, las 10 DA, las 10 DT y los Anexos I y II; el Anexo III, por estructura y
  recuento (114 «CÓDIGO PUESTO»). Cada cifra, plazo y porcentaje del tema se ha comprobado en él.
- **Transcripción literal** del art. 33 y de la DT 3.ª: se tomó la del informe de investigación
  después de compararla palabra por palabra (script) con el texto del BOJA: 3.154 y 79 palabras, sin
  diferencias salvo espacios no separables.
- **ET** (`fuentes/canal-sur/BOE-A-2015-11430.md`): arts. 3, 14, 34, 35, 37 (15 redacciones; vigente
  desde 3-3-2025, Ley 6/2024), 38, 46 (3; RDL 5/2023), 48 (8; RDL 9/2025, título y convalidación
  comprobados en el BOE: BOE-A-2025-15741 y BOE-A-2025-17999), 60, 63, 86 (2; RDL 32/2021).
- **Ley 3/2012** (`BOE-A-2012-13126.md`): arts. 3, 4, 5, 14, 19, 22, 23, 24, 25, 26, 28, 32. La
  redacción original del art. 26 (derogado) se leyó con la API del BOE, porque el tema la describe.
- **Ley 7/2024** (texto del diario): derogatoria única e) y DA 4.ª y 5.ª. **Ley 8/2025**
  (`BOE-A-2026-945.md`): arts. 12.2, 18.1, DA 4.ª y 5.ª.
- Reglamento de la Mesa de Contratación (puntos 1, 2.1, 23, DA 1.ª, DT 4.ª); informe de la Cámara de
  Cuentas (BOJA 36/2021, puntos 8, 78, 234); Acuerdo de fusión de 3-XI-2015 (BOJA 219/2015); consulta
  REGCON; bases de la convocatoria (2.1, 5.1, 6.3) y programa común.
- El cuadro sindical de CCOO de 2017 y la noticia de CCOO de 2025 **no se usan como fuente**: solo se
  menciona la existencia del cuadro de 2017 en «Lo que este tema no da».

## Estructura del tema

Ficha, siglas, enunciado, párrafo inicial; `## Identificación y vigencia` (publicación, ámbitos,
vigencia y prórroga con art. 5 y ET 86.2-86.3, fusión en CSRTV, estructura real, diferencias
índice/cuerpo, erratas, Reglamento de la Mesa); `## Articulado` con `###` por capítulo y `####` por
artículo (número y rúbrica del cuerpo); `## Cuadro de licencias y permisos` (no hay cuadro con ese
nombre; art. 33 y DT 3.ª literales; cuadro-resumen marcado como elaboración del tema, con artículo
por fila; `###` de contraste con el ET, sin decidir cuál prevalece); `## Disposiciones adicionales,
transitorias y anexos` (con tabla del estado de cada base de la Ley 3/2012 y la norma y año de cada
cambio); normativa, lo que no da, trazabilidad. Índice vacío, para `indice.py`.

## Decisiones de redacción

1. **Negrita solo para citas literales.** Se comprobó con un script que todo texto en negrita está
   literalmente en alguna fuente. Excepciones por forma (como en T06): etiquetas de las tablas de ficha
   y trazabilidad, siglas y la etiqueta «Enunciado del programa». Los rótulos van en cursiva.
   Incidencia: una primera conversión por líneas emparejó mal negritas que cruzaban salto de línea en
   ~30 líneas; se restauraron a mano y se rehízo la conversión sobre el texto entero. Balance de `**`
   comprobado.
2. **Artículos 1 a 5**: se desarrollan en «Identificación» (lo pedía el encargo) y en el articulado
   van con una remisión de dos líneas, para no repetir.
3. **Transitorias**: el tema da texto, base legal que cita cada una y estado de esa base el
   24-09-2026 (derogación por Ley 7/2024 desde 1-1-2025; lista de medidas mantenidas en 2026 por la DA
   4.ª de la Ley 8/2025). Dice expresamente que no se ha podido confirmar la aplicación práctica.
4. **DT 3.ª B**: se expone la ambigüedad (rótulo «asuntos propios» frente a texto «las licencias y
   permisos del art. 33») sin resolverla.

## Premisas del encargo contrastadas con la fuente

Todas cuadran. Matices que el tema recoge y que el informe de investigación no traía o traía de otro
modo:

- **Remisión rota nueva**: art. 32.II.2 remite al «párrafo a) del apartado 2 del punto III», que no
  tiene letras.
- **Anexo I**: la tabla da 66,07 € por trienio; el 0,0024 del salario base anual de B03 da 52,85 €
  (cálculo propio; el texto no lo explica).
- **Art. 33.A.1.h** habla de «las veinte semanas previstas anteriormente» (16 + 4).
- **Anexo II**: los totales de los centros territoriales suman 428, no 452, porque Jerez y Madrid no
  tienen total propio; el tema no da la suma parcial y marca 1.529 como suma propia.
- **Ley 7/2024, DA 4.ª** añade que el art. 28 se aplica según su DA 5.ª (acción social); la Ley
  8/2025 tiene DA 5.ª análoga para 2026. El tema lo menciona sin estudiar su alcance para la RTVA.
- **Convocatoria**: el requisito que cita el Anexo III es la base **6.3** (no 3.3).
- **Índice del convenio**: las DA y DT sí tienen rúbrica en el índice (salvo DA 7.ª, DA 9.ª y DT
  10.ª), y la de DT 3.ª es «Permisos y reducciones de jornada».

## Lo que no se ha podido confirmar (fuera del tema como dato)

- Aplicación práctica actual de jornada, vacaciones, permisos, IT y acción social en RTVA-CSRTV.
- Denuncia no inscrita del X Convenio o negociación de un XI.
- Tablas salariales posteriores a 2013; qué queda de la DT 4.ª; ley de presupuestos (año) del «art.
  11.5» que cita.
- Fecha del Reglamento de la Mesa en su propio texto (la convocatoria dice 12-3-2026).
- Plan de Igualdad inscrito: la consulta REGCON guardada no lo muestra; no se ha incluido su código.

## Prueba de terminado (manual, apartado 7)

| # | Pregunta (estilo test) | ¿Se contesta con el tema? |
|---|---|---|
| 1 | ¿Hasta cuándo duraba el X Convenio según su art. 4? | Entera (31-12-2015) |
| 2 | Antelación de la denuncia para evitar la prórroga | Entera (tres meses, art. 5) |
| 3 | Jornada anual pactada en el art. 10 | Entera (1.540 h, 35 semanales) |
| 4 | Composición de la COMVI | Entera (5 + 5, dos asesores) |
| 5 | Días por matrimonio del trabajador y plazo de solicitud | Entera (20 naturales; 15 días) |
| 6 | Permiso por traslado de domicilio tras la DT 3.ª | Entera (1 día) |
| 7 | Máximo de días de asuntos propios con más de 15 años de antigüedad | Entera (8; DT 3.ª: 4) |
| 8 | Límite de la licencia no retribuida | Entera (6 meses en el año natural) |
| 9 | Duración máxima de la excedencia voluntaria y reserva | Entera (6 meses-10 años; reserva ≤3 años, ≤5 %) |
| 10 | Sanción máxima por falta grave | Entera (2 a 20 días de suspensión) |
| 11 | Máximo de miembros del Comité Intercentros | Entera (13; 5 Sevilla, 2 Málaga, 6 resto) |
| 12 | Plus de nocturnidad y franja nocturna | Entera (35 %; 22.00-7.00) |
| 13 | Excepciones al traslado forzoso | Entera (48 años, disciplinario, representantes 2 años) |
| 14 | Lactancia en el convenio y en el ET vigente | Entera (12 meses; 9, ampliable a 12) |
| 15 | ¿Qué artículo de la Ley 3/2012 invoca la DT 2.ª y está vigente? | Entera (art. 26, derogado desde 1-1-2025) |

Quince de quince enteras.

## Ficheros tocados

- `temas/canal-sur-comun/07-x-convenio-colectivo.md` (nuevo) y este informe.
- Ningún otro fichero del proyecto. Temporales solo en el scratchpad de la sesión. No se ha corrido
  `indice.py` ni tocado `portadas.tsv` (los temas de Canal Sur no están en él).
- Nota: durante el trabajo, el coordinador hizo un commit intermedio (7a8cd71) con el tema a medio
  convertir; el estado en disco actual es el final.
