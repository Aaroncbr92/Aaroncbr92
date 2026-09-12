# Cultura y actualidad

Las fuentes del **tema 6 del específico de Documentación**, que es el punto más
preguntado del cuadernillo —**40 de 96 preguntas**— y el que menos parecía tener
fuente.

**Resultado de la búsqueda: 15 de las 40 respuestas quedan atadas a un
documento**; nueve al BOE y seis a páginas de organismos oficiales.

## Norma y documento del BOE — primer nivel

| Fichero | Qué contiene |
|---|---|
| `BOE_preceptos.txt` | Preceptos de legislación consolidada, volcados con la herramienta del proyecto a la fecha de corte: **artículo 3 del Estatuto de Roma** —sede de la Corte Penal Internacional—, **artículos 23 y 24 de la Ley 46/1998** —unidad de cuenta y canje de billetes— y **artículo 57 de la Constitución** —orden de sucesión— |
| `BOE_documentos.txt` | Documentos no consolidados, en su texto original publicado: **RD 1673/2010** y **RD 1717/2010** —estado de alarma y prórroga—, la **Resolución del Congreso** que la autorizó, **RD 359/2022** y **RD 351/2022** —nombramiento y cese en el Centro Nacional de Inteligencia—, **Ley 40/1975** —descolonización del Sahara—, **Ley Orgánica 3/2014** —abdicación— y dos **órdenes de febrero de 1976** que liquidan la administración española del Sahara. Al final, los **títulos tal como los da el sumario del BOE** |

A ellos se suma el **Real Decreto 2032/2009** de unidades legales de medida,
volcado en `../corte-20221221/BOE-A-2010-927.md`, del que este tema usa las
definiciones del **amperio** y el **kelvin**, el ejemplo del **newton** y la regla
del **becquerel**.

## Documentación institucional — tercer nivel

`instituciones.txt` reúne, con su dirección y la fecha de lectura, las páginas
de: el **comité ejecutivo del Banco Central Europeo**; «About the Fed», de la
**Reserva Federal**; los contactos del **Banco Europeo de Inversiones**, con su
dirección postal en Luxemburgo; «Tasks & Mission», de la **agencia europea de
fronteras**; «Who we are», de la **Unión por el Mediterráneo**; las entradas
**«Chromosome»** y **«CRISPR»** del glosario del instituto estadounidense de
investigación del genoma; la portada del **festival Sónar**; y las portadas del
**Neues Museum** y del **Museo Egipcio y Colección de Papiros** de los museos
estatales de Berlín.

## Cómo se buscó en el BOE

Los nombramientos y los decretos **no están en la legislación consolidada**: son
documentos sueltos. Se localizaron consultando **el sumario del día** por la API
de datos abiertos del BOE —`https://boe.es/datosabiertos/api/boe/sumario/AAAAMMDD`—
y buscando la palabra clave en los títulos. Es una ruta barata y exacta **cuando
se sabe la fecha aproximada**, y no sirve cuando no se sabe: por eso quedaron sin
localizar dos nombramientos.

## Lo que no se ha podido traer

- **Cinco páginas oficiales no responden** a la consulta automática, con agente
  de usuario de navegador: la de la **Corte Penal Internacional** —cuya sede se
  resolvió por el BOE—, la de la **presidencia de la República italiana**, la de
  la **empresa del cohete Miura 1**, la de la **Semana de Música Religiosa** y la
  del **comité olímpico español**.
- **Tres rutas devuelven «no encontrado»**: la del **gobernador del Banco de
  España**, la del **palmarés de la academia de cine** y la del **premio de las
  artes de 1994**.
- **Dos búsquedas en el sumario del BOE no dieron resultado** en las fechas
  probadas: el nombramiento del **ministro de la Gobernación de 1975** y el del
  **gobernador del Banco de España**.
- **La página del Banco Central Europeo confirma quién preside, no desde cuándo.**
