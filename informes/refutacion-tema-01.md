# Refutación del tema 1 del general

Fase 4 del manual, con tres lentes distintas en vez de tres escépticos iguales, y
con la cláusula delante: **cero hallazgos es un buen resultado si el tema está
bien**. Las tres lentes están automatizadas en `herramientas/refutar_*.py`, así que
se pueden volver a pasar sobre cualquier tema.

## Lente 1 · Exactitud normativa

Dos comprobaciones, las dos contra el volcado del texto consolidado a la fecha de
corte.

**Negritas contra su artículo** (`refutar_exactitud.py`). Se troceó el tema por
artículos y se buscó cada fragmento en negrita en el articulado del que dice
venir: 440 comprobaciones. Las que no salen literales son paráfrasis o
encabezados; ninguna resultó ser una invención.

Aquí apareció además un defecto de la propia herramienta: sin acotar los bloques,
el artículo 169 se tragaba todo el final del tema y devolvía 203 falsos positivos.
Corregido antes de fiarse del resultado.

**Modo verbal y salvedades** (`refutar_modo.py`), que son los errores 4 y 6 del
catálogo. Nueve hallazgos, **seis reales**:

| Artículo | Qué faltaba |
|---|---|
| **25.2** | El tema se había dejado **entero** el párrafo de los derechos del condenado: que goza de los derechos fundamentales del Capítulo **a excepción de los limitados por el fallo, el sentido de la pena y la ley penitenciaria**, y que **en todo caso** tiene derecho a **trabajo remunerado, beneficios de la Seguridad Social, acceso a la cultura y desarrollo integral de su personalidad**. |
| **136.2** | El tema decía que el Tribunal de Cuentas fiscaliza y remite un informe anual, y se había dejado el **«sin perjuicio de su propia jurisdicción»**: el **enjuiciamiento de la responsabilidad contable**. Es justo lo que pregunta el examen de Información y Contenidos de 2024. |
| **82.6** | Faltaba que **las leyes de delegación pueden establecer fórmulas adicionales de control**, sin perjuicio de la competencia de los Tribunales. |
| **150.1** | Faltaba que **cada ley marco establecerá la modalidad del control de las Cortes Generales** sobre las normas autonómicas. |
| **37.2** | Faltaba el inciso **«sin perjuicio de las limitaciones que puedan establecer»**. |
| **124.1** | Faltaba el **«sin perjuicio de las funciones encomendadas a otros órganos»** con el que abre el precepto. |

Los otros tres son falsos positivos, revisados uno a uno: el artículo 20 —«la
información **ha de** ser veraz» es comentario del tema, no cita—, el 75 —el tema
sí recoge que el Pleno puede recabar el debate, solo que sin la palabra «no
obstante»— y el 169, que es la tabla comparativa de los artículos 167 y 168
atribuida al bloque equivocado.

## Lente 2 · Cobertura de examen

**Contra el articulado.** El enunciado de la convocatoria es la Constitución
entera, así que la pregunta es qué artículos no están. De los 169, **solo faltaba
el artículo 146** —la asamblea que elabora el proyecto de Estatuto por la vía del
143—. Añadido.

**Contra las preguntas reales.** La prueba con las 103 preguntas del banco está en
`cobertura-tema-01.md`: **87 de las 89 que son de Constitución se contestan
enteras**. Ojo a una cosa: esa prueba, pasada antes de la refutación, dio por
contestada la del Tribunal de Cuentas, y no lo estaba. La destapó la lente 1. Es
la demostración de por qué el manual pide las dos cosas y no una.

## Lente 3 · Prosa y forma

`refutar_prosa.py`. **Cero** tejido conectivo: ni «como hemos visto», ni «en
síntesis», ni «cabe destacar». Antecedentes: cuatro expresiones del tipo «el
apartado 3», todas con su artículo delante o nombrado.

Tres hallazgos, los tres reales y corregidos: **CGPJ**, **TC** y **PIB** se usaban
sin presentar la primera vez.

Queda un aviso que **no** es un defecto: la frase «su estructura interna y
funcionamiento deberán ser democráticos» aparece dos veces porque la Constitución
la repite —artículos 6 y 7, y de nuevo 36 y 52—, y el tema lo señala
expresamente.

## Segunda refutación

Pasadas otra vez las tres lentes sobre el tema ya corregido:

- exactitud, negritas: sin hallazgos nuevos;
- modo verbal y salvedades: **3**, los tres falsos positivos ya analizados;
- prosa: **1**, la repetición literal de la propia Constitución.

Es decir, **ningún hallazgo real en la segunda vuelta**. El tema queda cerrado a
falta del esquema.
