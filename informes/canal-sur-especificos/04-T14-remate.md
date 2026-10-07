# 04 · Ayudante de Producción · Tema 14 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/14-control-administrativo-basico-de-gastos-de-produccion.md`.
Entrada: `04-T14-refutacion.md` (graves 0, menores 2, laguna 1) y `04-T14-preguntas.md` (13 enteras, 2 a medias).
Fecha de corte 24-09-2026; fuentes releídas el 06-10-2026. Ficheros tocados: el tema y este informe.
**Amplía**: sí (L1, contenido nuevo del art. 91 LIVA). Procede la fase 5 bis sobre los pasajes 3-6.

## Comprobación en la fuente (06-10-2026)

- X Convenio, art. 53.1.3 (literal ya en el tema): tres condiciones (distancia, regreso, turno) y una
  excepción; no menciona la pernocta. Hallazgo 1, correcto.
- Decreto 54/1989, art. 36, párrafo primero (texto del BOJA 31/1989): «La autoridad que ordena la
  comisión de servicio autorizará, previa solicitud del interesado, el abono de un anticipo…».
  Hallazgo 2, correcto.
- Ley 37/1992, art. 91 (`boe.py --fecha 20260924`): redacción vigente el 24-09-2026, la de
  01-01-2025 (BOE-A-2024-12944). Uno (encabezado), Uno.2 («Las prestaciones de servicios
  siguientes:»), Uno.2.1.º y 2.º, literales; idénticos en la redacción de hoy (02-10-2026,
  BOE-A-2026-20526). La de 01-12-2026 es posterior al corte. L1, correcta.

## Pasajes cambiados

1. «La dieta de rodaje», frase previa al cuadro: «cuatro condiciones y una excepción» →
   «tres condiciones y una excepción, y no exige pernocta». (H1)
2. Misma rúbrica, fila «Pernocta»: «No la exige: es una dieta de ida y vuelta en el día» → «No la
   exige: el artículo 53.1.3 no la menciona». (H1)
3. «Controlar las dietas del equipo», punto 1: añadido que el anticipo lo autoriza **«La autoridad
   que ordena la comisión de servicio»**, **«previa solicitud del interesado»** (art. 36). (H2, P15)
4. «Leer una factura: base, IVA, retención y total», párrafo del tipo: añadidos 91.Uno, 91.Uno.2,
   1.º y 2.º, literales, y la aplicación a taxi, tren, hotel y comidas, marcada como oficio. (L1, P14)
5. Ficha: «Fuente» añade el art. 91.Uno (1.º y 2.º del apartado 2); «Redacción que se estudia»
   añade el 91 (desde 01-01-2025, vigente el 24-09-2026; la de 02-10-2026 no cambia lo citado) y
   matiza que la coincidencia con el 06-10-2026 es «en los pasajes citados».
6. «Normativa que el tema invoca» y «Trazabilidad»: fila de la Ley del IVA con el art. 91; frase de
   cabecera de «Trazabilidad» matizada (pasajes, no preceptos) con el cambio de 02-10-2026.

Antecedentes releídos: «El artículo siguiente, el 91», «esas operaciones», «el artículo 53.1.3» y
«artículo 36» tienen delante su referente.

## Lentes

- `indice.py`: índice sin cambios (no hay epígrafes nuevos); 11.921 palabras, 59 epígrafes.
- `negritas.py` con arts. 90 y 91 (redacción a 24-09-2026) y el Decreto 54/1989: las 8 negritas de
  esas fuentes, incluidas las 6 nuevas, literales; las 125 restantes son de fuentes no pasadas
  (convenio, Reglamento de facturación…), ya cotejadas en fases 3 y 4.
- `refutar_modo.py`: 0 hallazgos. `refutar_exactitud.py`: no ancla artículos en el volcado de
  `precepto` (0 comprobadas); suplido por `negritas.py`. `refutar_prosa.py`: 0 hallazgos.

## Efecto en las preguntas

P14 y P15 pasan a «entera»: 15 de 15.
