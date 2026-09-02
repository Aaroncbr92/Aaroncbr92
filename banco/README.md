# Banco de preguntas del bloque común

**505 preguntas reales** —476 del temario general y 29 del tema de prevención del
específico— sacadas de los cuadernillos de la convocatoria 1/2022 (pruebas de
octubre y noviembre de 2024), **todas con la respuesta de la plantilla oficial**.

Se puede hacer porque el temario general es el mismo para las más de cincuenta
ocupaciones tipo convocadas, y porque las preguntas del bloque común se comparten
entre ocupaciones: está comprobado en `informes/preguntas-repetidas.md`.

| Fichero | Materia | Preguntas |
|---|---|---|
| `g1.md` | Constitución | 117 |
| `g2-g3.md` | Ley 17/2006 y Ley 5/2017 | 53 |
| `g4.md` | Ley 8/2009, financiación | 35 |
| `g5.md` | III Convenio Colectivo | 114 |
| `g6.md` | II Plan y Guía de Igualdad | 48 |
| `g7.md` | Ley 13/2022, General de Comunicación Audiovisual | 47 |
| `g8.md` | Ley 31/1995, prevención de riesgos | 61 |
| `prl-especifico.md` | Prevención en el temario **específico** (P18 · D7 · IyC11) | 29 |

Se regenera con `herramientas/banco.py`. **Las correcciones no se hacen sobre
estos ficheros**, que se sobrescriben enteros: van en `reclasificadas.tsv`.

## Y el banco del bloque **específico**

| Fichero | Materia | Preguntas |
|---|---|---|
| `produccion-02.md` | Producción (Asistencia) · tema 2 · propiedad intelectual | 9 |

Se regenera con `herramientas/banco_especifico.py`, y **el reparto se escribe a
mano** en `especifico-produccion.tsv`, una fila por pregunta y con el motivo al
lado. No se clasifica por palabras clave, y no por comodidad: las preguntas del
específico hablan de *beauty shot*, del cuaderno ATA o de SMPTE 2110, y muchas
podrían caer en dos temas a la vez. Una regla automática sobre eso no da un
reparto discutible, da **uno falso que nadie va a revisar**.

El script avisa de las **filas que ya no casan con ninguna pregunta** y cuenta
**cuántas preguntas específicas quedan sin repartir**: de las **129** de los dos
cuadernillos de Producción (Asistencia), **9 repartidas y 120 pendientes**. Esa
cifra es la que mide lo que falta de la Fase B, y es la que no aparece sola.

**Para qué sirve.** El apartado 7 del manual manda cerrar cada tema comprobando
que entre diez y quince preguntas del estilo real se contestan con el cuerpo del
tema delante. Aquí no hace falta inventarlas: hay 505 reales, todas con su respuesta
oficial. Un tema del bloque común no está terminado hasta que contesta las suyas.

## Cómo se arma

1. **`calibrar.py` trocea cada cuadernillo por su numeración.** Solo acepta la
   marca que continúa la serie, porque los números que aparecen dentro de las
   respuestas también parecen marcas.
2. **`banco.py` empareja cuadernillo y plantilla por el nombre de la ocupación**
   —no por el orden, que no siempre coincide— y saca la letra correcta.
3. **`calibrar.py` clasifica por palabras clave**, con la primera regla que casa.
4. **`reclasificadas.tsv` corrige a mano lo que la palabra clave no puede ver.**

## Los ficheros `.ocr.txt`

**Cinco cuadernillos llevan la fuente incrustada sin tabla de caracteres**, así
que extraerles el texto devuelve `(cid:12)(cid:13)…` y no una sola letra. No
daban error: sencillamente no aportaban ninguna pregunta, que es la manera
silenciosa de perder cinco exámenes enteros. Se han releído **rasterizando la
página y pasándole Tesseract en español** (`--tesseract-pagesegmode 6`), y la
lectura buena se guarda al lado como `<cuadernillo>.ocr.txt`. `banco.py` la
prefiere cuando existe, y el identificador de la pregunta sigue nombrando al
cuadernillo, no a la transcripción.

| Cuadernillo | Preguntas leídas | Plantilla |
|---|---|---|
| `15_preguntas_gestion` | 108 de 108 | recuperada celda a celda |
| `17_preguntas_gestion_abogado_a` | 96 de 96 | recuperada celda a celda |
| `25_preguntas_iluminacion` | 96 de 96 | recuperada celda a celda |
| `44_preguntas_ing_sup_teleco` | 96 de 96 | legible |
| `50_preguntas_tec_teleco` | 96 de 96 | legible |

**Comprobación de que la lectura está completa**: en los cinco la numeración va
de 1 a N sin huecos, el número de bloques de opciones `a)` coincide con el de
preguntas, y en los dos que tienen plantilla legible N coincide con el número de
respuestas de la plantilla.

## Las tres plantillas que hubo que leer celda a celda

**Tres plantillas de respuestas llevan la fuente incrustada sin tabla de
caracteres**, igual que sus cuadernillos: Gestión, Gestión-Abogado/A e
Iluminación. Sus **65 preguntas** entraban como «sin plantilla».

Pasarles OCR a la hoja entera no funciona —son tablas de dos columnas y el
lector pierde la de letras a partir de la segunda página—, así que
`herramientas/plantilla_ocr.py` **no lee la hoja: lee la celda**. La geometría
sale de los bordes de la tabla, que en el PDF son dibujos vectoriales; los
códigos de la fuente distinguen las cuatro letras aunque no sepamos nombrarlas;
y el OCR solo tiene que decir **cuál es cuál**, sobre la celda recortada y por
mayoría de varias.

**Comprobado por dos caminos independientes**: la lectura coincide **50 de 50**
con las dos primeras páginas de la plantilla de Iluminación leídas a ojo, y las
**dos preguntas que se repiten** en cuadernillos de plantilla legible dan la
misma respuesta, aunque las opciones estén en distinto orden.

## Lo que este banco no tiene

**Un cuadernillo no tiene preguntas que sacar**, y `banco.py` lo avisa en cada
regeneración: `35_preguntas_iyc_prueba_invalidada_por_filtracion`. RTVE publicó
el cuadernillo de la prueba anulada por la filtración como un PDF con el sello
«PRUEBA INVALIDADA» repetido veinte veces y nada más.

**Y un aviso que sigue en pie.** Las preguntas del cuadernillo de Documentación
—y las de los cinco `.ocr.txt`— vienen de un OCR, así que para citarlas
literalmente hay que mirar el PDF.
