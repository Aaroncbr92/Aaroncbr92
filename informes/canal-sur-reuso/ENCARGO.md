# Encargo · cruce Canal Sur ↔ temas escritos para RTVE

Para cada tema del programa de Canal Sur que te toque, decide cuánto de él **ya está
desarrollado** en algún tema escrito para RTVE (`temas/**`), leyendo los temas de RTVE,
no sólo su título. El catálogo con rutas y epígrafes está en
`informes/canal-sur-reuso/catalogo-rtve.md`; úsalo para localizar y **abre el tema
para confirmar**.

Programa de Canal Sur, literal: `convocatoria/canal-sur/PROGRAMA-COMUN.md` y
`convocatoria/canal-sur/especificos/NN-*.md`.

## Qué escribes

Un TSV en `informes/canal-sur-reuso/<grupo>.tsv`, con cabecera, UNA fila por tema de
Canal Sur (sin saltarte ninguno) y estas columnas separadas por tabulador:

`puesto` (número 0 para el común, 1–40 para los específicos) · `tema` (su número) ·
`rtve` (rutas de los temas de RTVE que lo cubren, separadas por `;`, o `-`) ·
`pct` (0–100) · `actualizar` (`sí`/`no`) · `nota` (una línea: qué cubre y qué falta)

## Cómo se puntúa `pct`

Porcentaje del enunciado de Canal Sur (cada materia que nombra cuenta) que un tema de
RTVE **ya desarrolla con el contenido que pide**. Criterios:

- Misma materia desarrollada con la profundidad pedida → 80–100.
- Se cubre una parte de las materias del enunciado → proporcional.
- Sólo la misma área, sin el contenido → 0–15.
- **Norma distinta cuenta 0**: el convenio de RTVE no es el de la RTVA; la Ley 17/2006
  de RTVE no es la Ley 18/2007 de la RTVA; lo andaluz (Estatuto, Ley 10/2018, Ley
  12/2007, instituciones y administración de la Junta) no está en RTVE salvo que lo
  encuentres escrito.
- **No inflar.** Si dudas entre dos cifras, la menor. Cero es un buen resultado cuando
  no hay nada.

`actualizar = sí` cuando el tema de RTVE estudia una redacción congelada (por ejemplo,
la vigente el 21-12-2022) o habla de RTVE donde Canal Sur pide la RTVA: se puede
aprovechar, pero hay que revisarlo contra la redacción vigente o reescribir la parte
de empresa.

## Reglas

- Lo que no puedas confirmar leyendo el tema de RTVE, no lo cuentes.
- No modifiques ningún fichero salvo tu TSV. Escríbelo según avanzas.
- Al terminar, contesta con: número de filas, media de `pct` por puesto y los tres
  hallazgos más útiles (temas de RTVE que casan casi enteros).
