# Las normas que pregunta el Administrativo C1

**Siglas de este parte**: Administración General del Estado (**AGE**); Mutualidad
General de Funcionarios Civiles del Estado (**MUFACE**); real decreto (**RD**) y
real decreto legislativo (**RDLeg**); texto refundido de la Ley del Estatuto
Básico del Empleado Público (**TREBEP**).

Volcadas con `herramientas/boe.py norma` **a redacción vigente**, que es la que
corresponde a un examen de 2026.

**Por qué en carpeta aparte y no en `fuentes/corte-20221221/`.** Tres de estas
normas ya estaban en el proyecto, pero congeladas al **21 de diciembre de 2022**,
que es el corte de la convocatoria de RTVE. La Constitución da igual —no se toca
desde 2011—, pero la **Ley 9/2017 de contratos** y la **Ley 47/2003**
presupuestaria sí se han modificado desde entonces, y entre las dos sostienen
**24 preguntas** de este banco. Se vuelven a volcar aquí **sin pisar** las de
RTVE, que tienen que seguir congeladas para aquellos volúmenes.

**Lo que no hace falta traer.** `fuentes/correos-normas/` ya tiene a redacción
vigente la Ley 39/2015, la Ley 40/2015, el TREBEP, la Ley 19/2013, la LOPDGDD y
la Ley 31/1995, y se usan desde ahí.

**Nueve de los veintisiete identificadores estaban mal la primera vez**, y por eso
se comprobó cada uno contra el título que devuelve el BOE antes de volcar nada.
El más peligroso: `BOE-A-1982-11196` **no es** la Ley Orgánica del Tribunal de
Cuentas sino la LO 1/1982 de honor e intimidad —que además ya estaba en la
bóveda—, así que darla por buena habría metido la norma equivocada en un tema.
La del Tribunal de Cuentas es `BOE-A-1982-11584`.

## Volcadas

| Identificador | Norma | Palabras |
|---|---|---|
| `BOE-A-1982-11584` | LO 2/1982 del Tribunal de Cuentas | 6.445 |
| `BOE-A-1978-31229` | Constitución Española (a redacción vigente, no al corte de RTVE) | 21.279 |
| `BOE-A-2017-12902` | Ley 9/2017 de Contratos del Sector Público | 177.542 |
| `BOE-A-2003-21614` | Ley 47/2003 General Presupuestaria | 61.603 |
| `BOE-A-2005-14836` | RD 951/2005 marco general de calidad | 8.140 |
| `BOE-A-2011-18541` | RD 1708/2011 Sistema Español de Archivos | 11.132 |
| `BOE-A-1997-25336` | Ley 50/1997 del Gobierno | 12.497 |
| `BOE-A-1985-5392` | Ley 7/1985 Bases del Régimen Local | 41.038 |
| `BOE-A-1986-18101` | RD 1405/1986 Registro Central de Personal | 2.742 |
| `BOE-A-1984-17387` | Ley 30/1984 reforma de la Función Pública | 43.546 |
| `BOE-A-2003-20977` | Ley 38/2003 General de Subvenciones | 34.423 |
| `BOE-A-2023-25758` | RD-ley 6/2023 | 105.488 |
| `BOE-A-2000-12140` | RDLeg 4/2000 MUFACE | 12.162 |
| `BOE-A-1987-12158` | RD 640/1987 pagos a justificar | 3.271 |
| `BOE-A-2002-10337` | RD 462/2002 indemnizaciones por razón del servicio | 15.151 |
| `BOE-A-2014-3248` | Ley 2/2014 Acción y Servicio Exterior | 21.442 |
| `BOE-A-2021-5032` | RD 203/2021 administración electrónica | 33.545 |
| `BOE-A-2007-6115` | LO 3/2007 igualdad efectiva | 36.811 |
| `BOE-A-1989-14441` | RD 725/1989 anticipos de caja fija | 2.860 |
| `BOE-A-1995-8729` | RD 364/1995 ingreso del personal | 16.142 |
| `BOE-A-2023-5366` | Ley 4/2023 igualdad real y efectiva | 34.271 |
| `BOE-A-1995-8730` | RD 365/1995 situaciones administrativas | 7.022 |
| `BOE-A-1985-151` | Ley 53/1984 incompatibilidades | 6.764 |
| `BOE-A-1981-10325` | LO 3/1981 Defensor del Pueblo | 5.079 |
| `BOE-A-2012-5730` | LO 2/2012 Estabilidad Presupuestaria | 17.958 |
| `BOE-A-2013-12632` | RDLeg 1/2013 discapacidad | 22.974 |
| `BOE-A-2007-6239` | RD 366/2007 accesibilidad en la AGE | 4.687 |
| `BOE-A-2015-11724` | RDLeg 8/2015 Ley General de la Seguridad Social | 189.713 |
| `BOE-A-2003-23646` | Ley 60/2003 Arbitraje | 15.068 |

## Pendiente de volcar

Sólo el **Código Civil**, que sostiene **una** pregunta del banco (el artículo 2,
sobre la entrada en vigor y la derogación de las leyes). Es la norma más larga del
lote y su volcado se interrumpió; se retoma con el mismo guion cuando haga falta
escribir el tema III.1.

| Identificador | Norma |
|---|---|
| `BOE-A-1889-4763` | Código Civil |

## Lo que no es del BOE consolidado

Tres fuentes que el examen pregunta y que no son texto consolidado, así que hay
que buscarlas aparte: el **IV Convenio Único del personal laboral de la AGE**
(3 preguntas), la **Orden de 1 de febrero de 1996** de operatoria contable
(2 preguntas) y la **Orden PRE/1576/2002** (1 pregunta).
