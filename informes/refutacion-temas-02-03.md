# Refutación de los temas 2 y 3 del general

**Aviso sobre este informe.** Los temas 2 y 3 se escribieron y se refutaron en la primera
sesión del proyecto, pero **su informe de refutación nunca se escribió a fichero**: solo quedó
el de cobertura, `cobertura-temas-02-03.md`. El hueco se descubrió el **2026-08-30**, al
comprobar automáticamente que las rutas que citan las portadas de los temas existen de verdad.

Este informe se ha reconstruido ese día **con lo que se puede medir y verificar hoy**: las
lentes vueltas a pasar sobre los dos temas, y lo que otros informes dejaron registrado por
escrito. **No reproduce las notas de aquella sesión, que no existen**, y por eso no cuenta el
detalle de la primera pasada. Lo que afirma es comprobable volviendo a correr los comandos que
cita.

## 1 · Estado de las lentes, medido el 2026-08-30

| Tema | Exactitud | Modo verbal y salvedades | Prosa |
| --- | --- | --- | --- |
| **2 · Ley 17/2006** | **176 negritas comprobadas**, 64 no literales | **0 hallazgos** | **0 hallazgos** |
| **3 · Ley 5/2017** | **no aplicable**, ver abajo | **no aplicable** | **0 hallazgos** |

**Comandos**, para poder repetirlos:

```
python3 herramientas/refutar_exactitud.py temas/general/02-ley-17-2006.md fuentes/corte-20221221/BOE-A-2006-9958.md
python3 herramientas/refutar_modo.py      temas/general/02-ley-17-2006.md fuentes/corte-20221221/BOE-A-2006-9958.md
python3 herramientas/refutar_documento.py temas/general/03-ley-5-2017.md  fuentes/corte-20221221/BOE-A-2017-11091.md
```

## 2 · El tema 3 no se puede refutar con las lentes por artículo, y por qué

Las lentes de exactitud y de modo verbal trocean el tema por artículos y contrastan cada trozo
con su precepto. **Sobre el tema 3 devuelven «0 comprobadas, 0 no literales» y «0 hallazgos»**,
y eso **no es un aprobado: es una comprobación que no ha mirado nada**. Es la firma del
apartado 10 del manual.

La causa es de la norma, no de la herramienta: **la Ley 5/2017 tiene «Artículo único»**, sin
numeración que trocear, y **los artículos que el tema cita son de la Ley 17/2006**, que es otra
norma. No hay nada que emparejar.

**Lo que sí se hace, y es lo que vale aquí**: contrastar **cada negrita contra el texto completo
de la ley**, con `refutar_documento.py`. Medido hoy: **109 negritas de dos o más palabras
comprobadas, 66 no literales**, revisadas una a una y todas comentario propio del tema o
variantes de redacción; y **8 cifras** que no aparecen en la Ley 5/2017.

**Las ocho cifras, comprobadas una a una.** Siete son metadatos —la fecha de corte (**21 de
diciembre de 2022**), la de la consolidación (**31/07/2021**), la de publicación (**30 de
septiembre de 2017**) y la del **Real Decreto-ley 5/2024**—, ninguna de ellas afirmación sobre
el contenido de la ley.

**La octava merecía mirarse y se ha mirado**: las **«48 horas»** de la segunda vuelta por
mayoría absoluta, en la tabla del epígrafe 5. **No están en la Ley 5/2017 porque no son suyas**:
son de la redacción que el **RDL 5/2024** dio al **artículo 11.2 de la Ley 17/2006**, y allí
están, escritas con letra —«*trascurridas **cuarenta y ocho horas** se someterá a votación…*»—,
que es por lo que la lente, que busca dígitos, no las encontraba. **La tabla las atribuye
correctamente**: su columna izquierda es lo que introdujo la Ley 5/2017 y la derecha **la
situación hoy**. Comprobado contra `fuentes/corte-20221221/BOE-A-2006-9958.md` —donde el
artículo 11.3 al corte exige dos tercios **sin segunda vuelta**— y contra
`fuentes/BOE-A-2006-9958.md`, la redacción de hoy. **No se toca nada.**

## 3 · El hallazgo real del tema 2, que salió más tarde

Está registrado en `informes/refutacion-tema-05.md`, y se recoge aquí porque es del tema 2:

> El tema resumía los **artículos 35 y 36** diciendo «presentación consolidada de presupuestos y
> programas», **sin recoger que el artículo 36 empieza con «Sin perjuicio de lo establecido
> anteriormente… presentará además»**. La presentación consolidada **no sustituye a la
> individual: se suma a ella**.

Es el **error 6 del catálogo** —salvedad omitida— y **apareció al arreglar la lente**, no en la
primera pasada. Corregido entonces; el tema vuelve a **cero hallazgos** y sigue en cero hoy.

## 4 · La decisión de alcance del tema 2, que conviene tener por escrito

El tema 2 **incluye un epígrafe con redacción posterior a la fecha de corte**, el **11, «Lo que
cambia después de la fecha de corte»**, con la reforma que el **RDL 5/2024** hizo de los
artículos 10, 11 y 12 —composición y elección del Consejo de Administración—.

**Es una excepción deliberada a la regla del corte**, y la razón es que **se ha preguntado**: el
cuadernillo de Ambientación Musical, con plantilla de 21/02/2025, pregunta por los **quince
miembros y el reparto once y cuatro**, que solo se contesta con ese epígrafe. Está documentado
en `informes/cobertura-temas-02-03.md`. El cuerpo examinable sigue siendo el del corte y el
epígrafe va marcado como lo que es.

## 5 · Lo que este informe no puede decir

**Cuántos hallazgos tuvo la primera pasada de cada uno de los dos temas.** No se anotaron a
fichero y no se van a inventar. Lo que se sabe con certeza es el estado de hoy, que está medido
arriba, y el hallazgo del artículo 36, que sí quedó registrado.

## Resumen

| | |
|---|---|
| Estado de las lentes hoy | tema 2, **0 hallazgos**; tema 3, **no aplicable por artículo**, verificado por contraste de texto completo |
| Cifras comprobadas en el tema 3 | **8**, todas explicadas; **ninguna inventada** |
| Hallazgos de fondo registrados | **1** (art. 36 de la Ley 17/2006), corregido |
| Decisiones de alcance declaradas | **1** (el epígrafe 11 del tema 2, posterior al corte, porque se pregunta) |
| Lo que falta de la primera pasada | **el recuento original**, que no se escribió y no se reconstruye |
