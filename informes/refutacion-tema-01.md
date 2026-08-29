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

## Esquema

Hecho, en `esquemas/general/01-constitucion-espanola.md`: **128 líneas de artículo
y unas 4.900 palabras**.

La horquilla del método —unas 130 líneas y unas 2.000 palabras— se cumple en
líneas y **se dobla en palabras**. El motivo, medido y no opinado: el enunciado de
este tema es la Constitución entera, así que las 128 líneas cubren **169
artículos**, a 35 palabras por línea, y **el 51 % de las palabras van dentro de
negrita porque son dato normativo**. Bajar a 2.000 obligaría a quitar preceptos,
recuentos o cifras. Explicación ya no queda ninguna que quitar.

Un aviso, porque casi cuela. El primer intento de comprimir se hizo con
sustituciones automáticas y estaba cambiando el modo verbal de la norma: «podrán»
por «puede», «en todo caso» por «siempre», «corresponde a» por una flecha. Es el
error 4 del catálogo, metido por la propia ronda de arreglar, que es contra lo que
avisa el apartado 5 del manual. Se tiró y se rehízo a mano.

## Antes de dar el tema por terminado (apartado 13 del manual)

- [x] **Los epígrafes reproducen el enunciado de la convocatoria.** El enunciado es
      una sola línea —«Constitución Española de 27 de diciembre de 1978»—, así que
      va literal en cabecera y el tema se ordena por la sistemática de la propia
      norma, que es la que sigue el examen.
- [x] **Cada dato tiene su precepto detrás**, leído en la redacción vigente a la
      fecha de corte.
- [x] **Los preceptos con varias redacciones, releídos enteros**: 13, 49, 69 y 135.
      A 21/12/2022 se aplican la de 1992 del 13, las de 1978 del 49 y del 69 y la
      de 2011 del 135.
- [x] **Ciclo completo**: investigar, redactar, verificar, refutar, rematar y
      refutar otra vez.
- [x] **La última refutación vuelve sin hallazgos reales.** Los cuatro que quedan
      están analizados uno a uno y son falsos positivos.
- [~] **Las preguntas se contestan con el cuerpo delante.** 87 de las 89 que son de
      esta materia, enteras. Las dos restantes se contestan a medias y por qué está
      dicho en `cobertura-tema-01.md`: una fecha y una cifra de actualidad que no
      se han podido confirmar en fuente oficial.
- [x] **Lo que no se pudo confirmar está fuera y anotado** en `PENDIENTES.md`: la
      fecha de cese del artículo 155 en Cataluña y el número total de Senadores.
- [x] **Ficheros tocados fuera del tema**, que el método obliga a declarar:
      `esquemas/general/01-constitucion-espanola.md` y los informes de este tema;
      `PENDIENTES.md` y `ESTADO.md`; las herramientas `refutar_exactitud.py`,
      `refutar_modo.py` y `refutar_prosa.py`, nuevas; y `herramientas/banco.py`
      con el arreglo del lector de plantillas, que obligó a **regenerar `banco/`
      entero**. Ningún otro tema se ha tocado, porque todavía no hay otro.
