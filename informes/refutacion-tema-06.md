# Refutación del tema 6 del general

II Plan de Igualdad y Guía de Igualdad de RTVE. **Es el primer tema cuya fuente no está en
el BOE**, y eso rompe las tres lentes anteriores.

## 0 · Ninguna de las lentes servía

`refutar_exactitud.py` y `refutar_modo.py` **trocean el tema por artículos** y contrastan
cada trozo con su precepto. Aquí no hay artículos: hay **un plan de 118 páginas y una guía
de 26**, con epígrafes numerados pero sin articulado. Pasadas tal cual, las dos lentes
devuelven **«0 comprobadas, 0 no literales»** y **«0 hallazgos»**, que es exactamente el
resultado que el apartado 10 del manual advierte que no hay que aceptar: **un tema sin
revisar se lee igual que un tema impecable**.

Ya pasó con el tema 3 —la Ley 5/2017 tiene «Artículo único»— y allí se resolvió a mano. Como
va a volver a pasar (quedan el Manual de estilo y el Código de autorregulación del menor en
los temarios específicos), esta vez se ha escrito la herramienta:
**`herramientas/refutar_documento.py`**, que hace lo que sí se puede hacer con un documento
suelto:

- **Cada negrita del tema, contra el texto completo de las fuentes.** Lo que no aparece se
  imprime para mirarlo a mano.
- **Cada cifra en negrita, contra las fuentes.** Es la comprobación que importa: una cifra
  inventada es el error más caro al resumir un documento largo, y el más fácil de cometer.

Normaliza guiones de corte, espacios duros y comillas, que es de lo que los PDF van llenos y
lo que haría fallar la comparación por motivos tipográficos en vez de por contenido.

## 1 · Resultado

**792 negritas contrastadas**; 339 no literales, revisadas por solape de palabras: **ninguna
es una afirmación sobre las fuentes que no puedan sostener** —son rótulos, comentario propio
y paráfrasis.

**Cifras huérfanas: una**, y no es un error. Es el **«118 páginas»** con que el tema describe
la extensión del PDF: un dato sobre el fichero, no sobre su contenido, así que no puede estar
dentro. Es decir: **ninguna cifra del tema está inventada**.

## 2 · El hallazgo: había 63 medidas y son 50

El tema afirmaba que los ocho ejes despliegan **63 medidas**. Salió de contar los epígrafes
numerados del Plan, y estaba mal.

**La numeración del Plan tiene dos niveles y no significan lo mismo.** En los **ejes 1, 2, 7
y 8** el número de dos cifras **ya es una medida** (1.1, 7.3, 8.2). En los **ejes 3, 4, 5 y
6** el de dos cifras es solo el **rótulo del área de actuación** —3.1 «Conciliación y
corresponsabilidad», 4.2 «Violencia de género»— y la medida lleva **tres** (3.1.1, 4.2.2).
Contando los rótulos como medidas salen **trece de más**.

Comprobado contra el propio documento por dos vías independientes: el Plan contiene
**50 apariciones de «Ficha de Medida»** y **50 campos «Identificación»**. **Son 50 medidas**:
2 + 3 + 12 + 6 + 2 + 11 + 10 + 4.

Corregido, y añadida al tema la explicación de por qué es fácil contarlas mal, que es
justamente lo que puede preguntarse.

## 3 · Prosa

Cero relleno y cero frases repetidas. **Doce siglas sin presentar** —UGT, CCOO, SI, USO, CGT,
CRTVE, SEPI, RAE, LO, LPRL, ONU, LGTB—, todas desarrolladas en su primera aparición. Quedan
cuatro avisos que son ruido del detector: PDF, «NO», «OO» —trozo de «CCOO»— y UGT, que ya va
desarrollado entre paréntesis.

## 4 · Lo que no se puede verificar aquí, y se dice

Con una ley o un convenio se puede reconstruir la redacción vigente en una fecha y
demostrarlo. **Con estos dos documentos, no.** No hay identificador, ni texto consolidado, ni
redacciones fechadas: **hay el PDF que RTVE publica hoy en su web**, que es exactamente el
que el programa enlaza.

Para esta convocatoria el problema no se plantea —la **Guía es de 2020** y el **Plan se
suscribió el 7 de marzo de 2022**, ambos anteriores al corte—, pero **si RTVE sustituyera un
PDF no quedaría rastro de la versión anterior**. Por eso los dos PDF se versionan en el
repositorio junto con su transcripción, y no solo la transcripción.

## Resumen

| | Hallazgos | Estado |
|---|---|---|
| Negritas contra la fuente | **0** afirmaciones sin respaldo, de 792 comprobadas | — |
| Cifras | **0** inventadas | — |
| Recuento de medidas | **1** (63 → **50**) | corregido |
| Prosa | **12** siglas | corregidas |
| Huecos de cobertura | ver `informes/cobertura-tema-06.md` | corregidos |

Herramienta añadida fuera del tema: **`herramientas/refutar_documento.py`**.
