# Refutación del tema 17 del específico de Producción (Asistencia)

Cuatro lentes sobre el tema, contra sus fuentes: la Ley Orgánica 3/2018 (`BOE-A-2018-16673`) en su
texto consolidado a **21 de diciembre de 2022**, y el Reglamento (UE) 2016/679
(`DOUE-L-2016-80807`) con sus **dos correcciones de errores**.

## Una limitación de las lentes que hay que declarar

Este tema es el primero que se apoya en **dos normas a la vez**, y las lentes por artículo
**trocean el tema por el número del artículo, no por la norma a la que pertenece**. Cuando el tema
dice «artículo 5» puede estar hablando del **artículo 5 del Reglamento** —los principios— o del
**artículo 5 de la ley orgánica** —el deber de confidencialidad—, y la lente no puede
distinguirlos: contrasta las negritas del uno contra el texto del otro y devuelve un hallazgo que
no existe.

Correrla contra la ley orgánica devuelve **230 «no literales»**; contra el Reglamento, **309**.
Ninguna de las dos cifras significa nada por sí sola. Lo que sí sirve, y es lo que se hizo, son
**tres pasadas**:

1. **La intersección de las dos.** Una negrita que no aparece literal **en ninguna de las dos
   normas** es la candidata a mirar: **193**, revisadas una a una.
2. **La lente de documento**, que contrasta contra **el texto completo de las cuatro fuentes a la
   vez** —las dos normas y las dos correcciones— y por eso **no tiene el problema de atribución**.
3. **La lectura directa** de cada artículo citado en su volcado, que es lo que decidió los casos
   dudosos.

Queda anotado como aviso de método: **con dos fuentes, la cifra de una lente por artículo no es un
resultado**.

## Lente de modo verbal y salvedades

**Doce hallazgos** en la primera pasada contra la ley orgánica. **Cinco eran reales y se
corrigieron**; el resto, cruces de numeración entre las dos normas o salvedades que el tema ya
recogía con otras palabras.

| Precepto | Lo que faltaba |
|---|---|
| Art. 20.1 de la ley orgánica | «**Salvo prueba en contrario**», que convierte la licitud en presunción |
| Art. 21 de la ley orgánica | Lo mismo, y la **inaplicación de la obligación de bloqueo** si la operación no se concluye |
| Art. 61.1 de la ley orgánica | La salvedad de que el responsable **desarrolle significativamente tratamientos de la misma naturaleza en el resto del territorio** |
| Art. 66.1 de la ley orgánica | «**Salvo en los supuestos del artículo 64.3**» |
| Arts. 38 y 39 de la ley orgánica | **No estaban en el tema**: códigos de conducta, su carácter vinculante, su aprobación y registro, y la acreditación de instituciones de certificación por la **ENAC** |

Contra el Reglamento, dos hallazgos reales más:

- **Artículo 4.9**: faltaba que **no se consideran destinatarios las autoridades públicas** que
  reciban datos **en el marco de una investigación concreta**.
- **Artículo 83.7**: faltaba la habilitación a los Estados miembros para decidir **si se pueden
  imponer multas a autoridades y organismos públicos**, que es **de donde sale el apercibimiento
  del artículo 77** de la ley orgánica. El tema lo dice ahora expresamente.

## Un fallo de la propia lente, corregido

La lente marcaba como cambio de modo verbal el **artículo 89.1** de la ley orgánica: el tema decía
«**deberán informar**» y la lente sostenía que la norma **solo dice «podrán»**. La norma dice
literalmente «Los empleadores **habrán de informar** con carácter previo, y de forma expresa, clara
y concisa». El patrón de imperativos de `refutar_modo.py` traía **«habrá de» en singular y no en
plural**, así que no reconocía la forma que usa el artículo.

Corregido el patrón —añadidos **«habrán de»**, **«hubiera de»** y los plurales de «exigirá» y
«requerirá»— y **repasados los temas ya cerrados** para ver si movía alguna cifra: no movió
ninguna. Es el corolario del apartado 10 del manual: **un falso positivo constante enseña a no
mirar la lista**, que es peor que no tener lista.

## Un bloque del tema que no se estaba comprobando

Los **artículos 80 a 86** —neutralidad, acceso universal, seguridad, educación, menores,
rectificación y actualización— iban en el tema como **una tabla**, con la primera columna en
negrita: `| **80** |`. La lente reconoce como marcador «**Artículo 80**» o «**Art. 80**», pero no
un número suelto, así que **los siete artículos se estaban contrastando contra el texto del
artículo 79**, que dice otra cosa. No daba error: daba **dieciocho «no literales»** que parecían
ruido y en realidad eran **siete artículos sin mirar**.

Arreglado en el tema, escribiendo la columna como `**Art. 80**`, que además se lee mejor. La
firma del arreglo es la correcta: **las negritas comprobadas se mantienen en 339 y los «no
literales» bajan de 248 a 230**.

## Lente de prosa

**Cero hallazgos** tras cuatro correcciones: se presentaron las siglas **DOUE** y **FEMP**, se
reformuló un rótulo que contenía un «NO» en mayúsculas que la lente leía como sigla, y se quitó
una frase repetida entre la ficha de cabecera y la trazabilidad.

## Lente de documento

**1.066 negritas** y todas las cifras en negrita contra el texto completo de las **cuatro
fuentes**. **Cuatro cifras huérfanas**, las cuatro de metadatos y ninguna del cuerpo normativo: la
fecha de entrada en vigor de los dos bloques en vacatio (**10 de mayo de 2023**), el número de
bloques del volcado (**169**) y los dos recuentos de palabras (**39.132** y **35.071**).
Comprobadas por separado contra los propios volcados y su tabla de redacciones.

## Dos afirmaciones que se verificaron aparte

No las cubre ninguna lente, porque no salen de estas dos normas:

1. **Que la Corporación RTVE no entra en el artículo 77.** Comprobado en el **artículo 5.1 de la
   Ley 17/2006** (`BOE-A-2006-9958`), que la define como «**sociedad mercantil estatal con especial
   autonomía**» con **forma de sociedad anónima**. Ninguna de las once categorías del artículo 77.1
   comprende una sociedad mercantil estatal: la letra d) habla de «organismos públicos y entidades
   de Derecho público» y la h) de «fundaciones del sector público».
2. **Que el artículo 83.4 explica por qué esta materia está en el temario.** El primer borrador
   decía que «la razón de que este tema esté en el Anexo 2 está escrita en la propia ley». Era una
   **sobreafirmación**: el artículo obliga a incorporar la materia a las pruebas de acceso **a
   cuerpos de la Administración**, y éstas son pruebas de una **sociedad mercantil estatal**. El
   tema cita ahora el precepto literal y **dice esa diferencia** en vez de dar por hecha la
   causalidad.

## Segunda pasada

Las lentes se volvieron a correr después de las nueve correcciones. Prosa, **limpia**. Modo verbal
contra la ley orgánica, **seis hallazgos, todos revisados y falsos**: cruces de numeración entre
las dos normas y salvedades recogidas con otras palabras. Documento, **las mismas cuatro cifras de
metadatos**.
