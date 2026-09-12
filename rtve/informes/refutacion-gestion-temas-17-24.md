# Refutación · Gestión, temas 17 a 24

**Siglas de este informe**: beneficio antes de impuestos (**BAI**); beneficio antes de intereses e
impuestos (**BAII**); el beneficio antes de intereses e impuestos (**EBIT**); el beneficio antes de intereses,
impuestos, depreciaciones y amortizaciones (**EBITDA**); impuesto sobre el valor añadido (**IVA**).

## 1 · La octava errata del proyecto, y la primera que no se refuta con un artículo

**Pregunta 32.** El enunciado pide **«el indicador del resultado de explotación de una empresa, sin
tener en cuenta justamente los intereses y los costes financieros»**. Las opciones: *BAI*, *EBITDA*,
*Resultado Viable* y *Margen Bruto*. **La plantilla da la a), BAI.**

**El BAI es el único de los cuatro que sí tiene en cuenta los costes financieros**, y la refutación
no necesita doctrina: está en el propio **modelo de cuenta de pérdidas y ganancias del Plan General
de Contabilidad**, que lo construye como

> **A.3) RESULTADO ANTES DE IMPUESTOS (A.1+A.2)**

donde **A.1)** es el resultado de explotación y **A.2)** el resultado financiero, cuya partida
**13** es, literalmente, **«Gastos financieros»**. El BAI es, por definición del modelo, el escalón
inmediatamente **posterior** a restar los intereses.

De las otras tres: el **margen bruto** se queda por encima del resultado de explotación —ni siquiera
ha restado los gastos de estructura—; **«Resultado Viable» no existe** como indicador de análisis
contable; y el **EBITDA** es el único que se sitúa por encima de los intereses en la escalera y por
tanto **no los computa**.

**El nombre exacto de lo que el enunciado describe es BAII, o EBIT, y no estaba entre las
opciones.** Ésa es la raíz del problema: la pregunta describe un indicador y luego no lo ofrece.
Pero entre un indicador que ignora los intereses **y algo más** y otro que **sí los computa**, la
única respuesta compatible con el enunciado es la **b), EBITDA**.

**Es la primera errata del proyecto refutada con un modelo normalizado de cuentas anuales en lugar
de con un artículo.**

## 2 · Dos herramientas aprendieron algo escribiendo estos ocho temas

**`despintar.py` gana el modo `--cursiva`.** Antes borraba la marca de las negritas no literales;
ahora puede **rebajarlas a cursiva**, que es lo que la convención del proyecto reserva para los
rótulos propios del tema. En un punto como el 17 —tres cuartas partes de doctrina— eso son sesenta y
tres marcas que pasan de ser una promesa incumplida a ser lo que siempre fueron: énfasis del autor.

**`refutar_exactitud.py` aprende la forma «Art. 34».** El Código de Comercio y las normas
decimonónicas titulan así sus preceptos. Con el patrón anterior la lente **no reconocía ni uno** y
devolvía «0 comprobadas», que se lee como impecable y es un tema sin revisar.

## 3 · Exactitud

**Cero no literales en los ocho temas**, tras corregir dos clases de problema:

- **Atribución por estructura.** Varias veces un bloque se comía las citas del siguiente porque el
  ancla del artículo iba **en mitad de una frase** —«Y sus topes, del **artículo 19** de la misma
  ley»— y la lente entonces sólo le da su frase. Reescritos con el ancla **abriendo párrafo**, cada
  cita queda en su artículo.
- **Anclas que el filtro descartaba.** «**Artículo 147 de la Ley General de la Seguridad Social**»
  no abre bloque, porque la lente descarta las remisiones a otra norma —«artículo 5 **de la Ley**
  X»— para no comprobar contra el precepto equivocado. Se nombra la norma en la frase anterior y el
  ancla queda limpio: «**Artículo 147.**».

Y una cita mal transcrita, cazada por la lente en el tema 20: el artículo 4 de la Ley del IVA dice
**«incluso si se efectúan en favor de los propios socios»** y el tema escribía *efectúen*. Una letra.

## 4 · Modo verbal y salvedades

**Cero hallazgos**, tras incorporar a los temas las salvedades que la lente reclamó, que en estos
ocho puntos fueron **quince** y varias con contenido de examen:

- Que el inmueble exento de IVA **sí tributa por transmisiones patrimoniales, salvo renuncia a la
  exención** (art. 4.Cuatro).
- Que la exención de operaciones con divisas **no alcanza a las monedas y billetes de colección**
  (art. 20).
- Que la obligación de cotizar **se suspende durante la huelga y el cierre patronal**, y que hay
  **reducción del 75 %** de cuotas empresariales por incapacidad temporal de mayores de 62 años
  (art. 144 LGSS).
- Que la incapacidad permanente **ha de derivarse de la incapacidad temporal, salvo quien careciera
  de esa protección** (art. 193 LGSS).
- Que la jubilación **puede causarse desde no alta** si se reúnen edad y cotización (art. 205 LGSS).

Ninguna de las cinco estaba en el tema antes de que la lente la reclamara, y las cinco son materia.

## 5 · Un error propio, corregido antes de publicarlo

El tema 20 anotaba una **errata en el Anexo 2**: citar la Ley del IVA como publicada en el «BOE núm.
312, de **29/12/2022**», cuando la ley es de 1992. **Comprobadas las bases de la convocatoria, el
anexo dice 29/12/1992**: el error era de la transcripción del propio tema.

Es el apartado 5 del manual funcionando: **el que detecta se equivoca**. Se corrigió la cita y se
retiró la errata inventada.

## 6 · Prosa

**Cero hallazgos** en los ocho temas. Dos ajustes de forma:

- Los rótulos del modelo de cuentas anuales, que el BOE escribe en mayúsculas —«A.1) RESULTADO DE
  EXPLOTACIÓN»—, disparaban el aviso de sigla sin presentar por cada palabra. Se pasan a caja normal
  conservando el código, que es lo que identifica el escalón.
- Un párrafo duplicado en el tema 24, detectado por el aviso de frases repetidas entre epígrafes.
