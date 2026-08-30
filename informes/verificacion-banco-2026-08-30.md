# Pasada de verificación sobre el banco de preguntas

**2026-08-30.** Leer una a una las preguntas del bloque común, separar las que la
transcripción había fundido y recolocar las mal clasificadas. Lo que empezó como
una revisión de clasificación acabó destapando **dos formas distintas de perder
preguntas sin que nada diera error**.

| | Antes | Después |
|---|---|---|
| Preguntas en el banco | 465 | **504** |
| De ellas, del temario general | 425 | **475** |
| Del tema de PRL del específico | 40 (mezcladas en `g8.md`) | **29 (en su propio fichero)** |
| Con respuesta de plantilla oficial | 447 | 437 |
| Entradas con dos preguntas fundidas | 33 | **0** |
| Cuadernillos que no aportaban nada | 6 | **1** |

Bajan las respuestas oficiales porque suben las preguntas: los tres cuadernillos
recuperados de Gestión, Gestión-Abogado/A e Iluminación tienen la **plantilla
ilegible**, y sus preguntas entran marcadas como «sin plantilla» en vez de con
una respuesta inventada.

## 1. El salto de página fundía una pregunta por página

`calibrar.py` trocea el cuadernillo por su numeración, exigiendo que la marca
esté **a principio de línea**. El PDF pone el salto de página (`\x0c`) **sin
salto de línea detrás**, así que el pie y la cabecera de la página siguiente
quedan pegados al número de la pregunta que la abre:

```
2º Llamamiento\x0c2º Llamamiento\x0c1.-
```

Esa marca deja de estar a principio de línea, la pregunta no se reconoce, y su
texto **se acumula dentro de la anterior**. En los cuadernillos maquetados así
pasaba **una vez por página**: 83 preguntas de cuatro exámenes, cada una fundida
con su vecina y **ninguna de las dos contestable**.

Convertir el salto de página en salto de línea las recupera todas. La
comprobación es dura: después del arreglo, **todos los cuadernillos legibles
numeran de 1 a N sin un solo hueco**.

Dos arreglos menores del mismo sitio:

- **La coma por punto.** El OCR del cuadernillo de Documentación lee `19,` donde
  el papel pone `19.`. Aceptar la coma como separador recupera esa pregunta.
- **La primera, cuando el OCR le lee mal el número.** En ese mismo cuadernillo la
  pregunta 1 sale como `4.`, no continúa la serie y **se descartaba entera**. Si
  la serie arranca en la 2 y justo antes hay una marca con su juego de opciones,
  esa marca es la 1. Lo confirma la plantilla: da **d**, y la opción d de ese
  bloque es la definición de perspectiva de género del II Plan de Igualdad.

**Y el pie de página, que ya no hace falta llevar arrastrando.** Al deshacer el
pegado, `Página: 13 de 24` y `2º Llamamiento` dejan de caer dentro de la pregunta
siguiente y caen al final de la anterior. Se quitan en el generador, no al
maquetar: la cita queda limpia en el banco y no hay que limpiarla dos veces.

## 2. Cinco cuadernillos que no aportaban nada, y no lo decían

Cinco PDF llevan la fuente incrustada **sin tabla de caracteres**: extraerles el
texto devuelve `(cid:12)(cid:13)…` y no una sola letra. **No daban error.**
Simplemente no aportaban preguntas, y nadie las echaba de menos —que es
exactamente lo que avisa el apartado 10 del manual: *un hueco de cobertura no
levanta ningún error*.

Se han releído **rasterizando la página y pasándole Tesseract en español**, con
`--tesseract-pagesegmode 6`, que respeta el renglón y deja el número de la
pregunta donde estaba. La transcripción se guarda al lado como `.ocr.txt` y
`banco.py` la prefiere cuando existe. Son **93 preguntas más** del bloque común.

| Cuadernillo | Preguntas | Comprobación |
|---|---|---|
| `15_preguntas_gestion` | 100 | 1..100 sin huecos, 100 bloques `a)` |
| `17_preguntas_gestion_abogado_a` | 96 | 1..96 sin huecos, y la plantilla numera 96 |
| `25_preguntas_iluminacion` | 96 | 1..96 sin huecos |
| `44_preguntas_ing_sup_teleco` | 96 | 1..96, y la plantilla numera 96 |
| `50_preguntas_tec_teleco` | 96 | 1..96, y la plantilla numera 96 |

**Lo que no se ha podido recuperar, y por qué no se ha forzado.** Tres de esas
plantillas están rotas igual, y son **tablas de dos columnas**: Tesseract lee
bien la primera página —`1 C`, `2 a`, `3 b`…— pero **a partir de la segunda
devuelve solo la columna de números y pierde la de letras**. Se probaron cuatro
modos de segmentación; ninguno la recupera. Y el poco que sí lee trae números mal
leídos: el 5 sale como `9`.

**Una plantilla leída a medias es peor que ninguna**, porque desplaza las
respuestas sin avisar —es el mismo fallo que ya obligó a reescribir el lector de
plantillas—. Así que **el OCR de esas tres no se guarda** y sus 67 preguntas
entran como «sin plantilla». El volumen imprimible lo dice en el apéndice de
respuestas.

**Y un sexto cuadernillo que no es un fallo**: `35_preguntas_iyc_prueba_invalidada_por_filtracion`
no tiene preguntas que sacar. RTVE publicó el cuadernillo de la prueba anulada
por la filtración como un PDF con el sello «PRUEBA INVALIDADA» repetido veinte
veces y nada más.

**Ahora el hueco se oye.** `banco.py` avisa por pantalla de todo cuadernillo del
que no salga ninguna pregunta, y de todo aquel del que salgan menos de las que
numera su plantilla.

## 3. La clasificación por palabras clave, corregida a mano

`calibrar.py` reparte por palabras clave con la primera regla que casa, y una
palabra clave no lee. «Constitución de capitales» mandaba al tema de la
Constitución una pregunta de **matemática financiera**; «Corona», una de
**mecanismos** (el piñón) y otra de **quién compuso la «Misa de la Coronación»**.

De las **565 entradas** que la clasificación por palabras clave llegó a producir,
leídas una a una, **113 estaban en el cajón equivocado**. El reparto vive
en `banco/reclasificadas.tsv`, con el motivo de cada una, y lo aplica `banco.py`
**después** de clasificar. Eso es lo que corregir los `banco/g*.md` a mano no
conseguía: sobrevive a regenerar el banco. Y las filas que dejan de casar con
una pregunta **se avisan**, para que una corrección no desaparezca en silencio.

Los cuatro grupos:

- **Fuera del temario general (61).** El programa del anexo 2 son ocho normas y
  ninguna de ellas es el **Estatuto de los Trabajadores**, la **LO 3/2018 de
  protección de datos** ni la **Ley 3/2013 de la CNMC**; tampoco es materia
  general la **actualidad** —quién preside hoy el Tribunal Constitucional, cómo
  votó el Congreso la ley de amnistía, si Evo Morales puede presentarse en
  2025—, ni la nómina, ni el IRPF, ni Mintzberg, ni los sectores de incendio del
  RD 2267/2004.
- **A otro tema del general (23).** Preguntas de convenio en el cajón de
  igualdad, de Ley 8/2009 en el de la Ley 17/2006, de Ley 13/2022 en el de la
  Constitución. Cada una comprobada contra su precepto: el vínculo del Presidente
  con la Corporación es el **art. 38.1 de la Ley 17/2006**, «una relación
  mercantil»; los límites del endeudamiento, los fijan los **contratos-programa**
  (art. 31); la Comisión de producción interna la componen **siete y siete,
  catorce** (art. 8 del convenio).
- **Al tema de PRL del específico (29).** Dos temas distintos caían en el mismo
  cajón, porque hablan de la misma materia y ninguna palabra clave los separa: la
  **Ley 31/1995** (tema 8 del general) y el tema de **prevención del específico**
  —pantallas de visualización, trastornos musculoesqueléticos, incendios,
  accidente in itinere o in misión, riesgo eléctrico—. Ahora tiene su propio
  fichero, `banco/prl-especifico.md`, y no entra en el volumen del general.
- **Se quedan donde estaban.** Las de la **Orquesta y Coro** siguen en el
  convenio, porque el **anexo 4** es el Reglamento de la Orquesta y Coro y forma
  parte del III Convenio; comprobado que el tema 5 lo cubre.

## Lo que queda

- **67 preguntas sin respuesta oficial**, por las tres plantillas ilegibles.
  Recuperarlas exige leer la columna de letras de una tabla que el OCR pierde:
  habría que probar recorte por columnas antes de pasarle Tesseract.
- **El identificador de cada pregunta es el cuadernillo y su número.** Si mañana
  se relee mejor un cuadernillo y cambia la numeración, las filas de
  `reclasificadas.tsv` que dejen de casar **saldrán avisadas**, no se perderán.
