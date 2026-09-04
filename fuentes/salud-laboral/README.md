# Fuentes de salud laboral que no son legislación

Los temarios de **Enfermería de Empresa** y de **Medicina de Empresa** tienen puntos cuyo
enunciado **nombra un documento técnico concreto** en lugar de una norma. Cuando eso ocurre, el
documento se baja entero y se guarda aquí —el PDF y su texto extraído—, para que cualquier
afirmación del tema se pueda comprobar y para que la lente `refutar_documento.py` tenga contra
qué contrastar.

La legislación va donde va siempre: volcada con `herramientas/boe.py` a
`fuentes/corte-20221221/`.

| Fichero | Qué es | Edición | Para qué |
| --- | --- | --- | --- |
| `ntp-218.pdf` / `.txt` | **NTP 218: La espirometría forzada en Medicina del Trabajo**, redactada por Joaquín Pérez Nicolás, Diplomado en Enfermería, del Centro Nacional de Condiciones de Trabajo | **1988** | Tema 8 de Enfermería de Empresa, que el propio enunciado del programa remite a esta NTP |

## Cinco avisos

**1. Las NTP no son obligatorias.** El pie de la propia NTP 218 lo dice: «*Las NTP son guías de
buenas prácticas. Sus indicaciones no son obligatorias salvo que estén recogidas en una
disposición normativa vigente. A efectos de valorar la pertinencia de las recomendaciones
contenidas en una NTP concreta es conveniente tener en cuenta su fecha de edición.*» Se usa como
**fuente citable y estable**, no como derecho.

**2. La NTP 218 es de 1988 y ella misma pide que se tenga en cuenta su fecha.** No se ha
buscado ninguna edición posterior ni ninguna NTP que la actualice, y **el tema 8 lo declara**.

**3. El enunciado del programa pide más de lo que la NTP contiene.** Pide «indicaciones,
contraindicaciones relativas y absolutas» y «mantenimiento del espirómetro», y **ninguna de esas
tres cosas está en la NTP 218**. Se comprobó leyendo el documento entero. El tema 8 lo declara
como laguna, con la tarea que la cierra.

**4. Un cuadro de esta NTP es una imagen y no sale en la extracción de texto.** El cuadro de
**síndromes de alteración ventilatoria** es una figura: la extracción automática sólo devuelve
su leyenda. Se leyó **recortando esa zona de la página 4 del PDF y ampliándola a 300 puntos por
pulgada**, igual que se hizo con el cuadro 3 de la BT.601-7 en `fuentes/normas-tecnicas/`. Las
fórmulas de regresión y el criterio de calidad **sí salen en el texto extraído**, y aun así se
comprobaron a ojo del mismo modo, porque **son cifras** y una cifra mal extraída no se nota
leyendo.

**5. Los tres ejemplos resueltos de la NTP contienen cinco errores.** Se han rehecho a mano las
cinco fórmulas de los tres ejemplos y los porcentajes de sus tres cuadros de resultados. Cuatro son
erratas tipográficas —un signo perdido, una variable sin sustituir, una línea mal rotulada—, y **el
quinto es un valor teórico equivocado**: en el segundo ejemplo, el flujo espiratorio forzado entre el
25 y el 75 por ciento sale 3.82 al aplicar la fórmula y el documento imprime 3.02, aunque **el
porcentaje del propio cuadro está calculado con 3.82**. En ese mismo ejemplo el índice de Tiffeneau
teórico sale 79.87 y el documento imprime 85.00. Ninguno de los cinco cambia la interpretación de
ningún ejemplo. Todo ello está declarado en el epígrafe 9 del tema 8.

## Cómo se vuelve a bajar

```sh
cd fuentes/salud-laboral
curl -sSL -o ntp-218.pdf "https://www.insst.es/documents/d/portal-insst/ntp_218-pdf"
python3 -c "import pymupdf; d=pymupdf.open('ntp-218.pdf'); open('ntp-218.txt','w',encoding='utf-8').write('\n'.join(p.get_text() for p in d))"
```

La ruta que sirve para las NTP del portal del INSST es `documents/d/portal-insst/`, con el
nombre del fichero en la forma `ntp_NNN-pdf`. Conviene comprobar con `file` que lo bajado es un
PDF y no una página de error.
