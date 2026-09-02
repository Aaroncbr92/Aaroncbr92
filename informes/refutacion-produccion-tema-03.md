# Refutación del tema 3 del específico de Producción (Asistencia)

**El tema sin fuentes.** Ninguna de sus seis preguntas tiene norma detrás, y eso cambia lo que una
refutación puede hacer: aquí no se trata de comprobar citas —apenas hay una— sino de **verificar
que la declaración de ausencia es cierta** y que **nada se presenta como más sólido de lo que es**.

## Qué lente sirve aquí

Las cuatro, aunque tres de ellas tengan poco que morder:

| Lente | Contra qué | Resultado |
|---|---|---|
| Exactitud | Ley de Propiedad Intelectual | **4 negritas comprobadas, 3 no literales** |
| Modo verbal | Ley de Propiedad Intelectual | **0 hallazgos** |
| Documento | Ley de Propiedad Intelectual | **134 negritas, 125 no literales, 0 cifras huérfanas** |
| Prosa | El tema | **0 hallazgos** (tras glosar dos siglas) |

**El 93 % de negritas no literales es, aquí, la medida exacta y esperada del tema**: casi todo lo
que dice es vocabulario de oficio que **no está escrito en ninguna fuente**, y por eso no puede ser
literal de ninguna. Las tres no literales que marcó la lente de exactitud son el comentario del
propio tema *sobre* el artículo 87 —«no contesta ninguna de las seis preguntas», «el guion es una
obra protegida y su autor, coautor de la película», «la ley distingue el argumento del guion y el
guion de los diálogos»—, es decir, **lo que el tema dice de la norma, no lo que dice la norma**.
Ninguna se presenta entrecomillada.

## Un fallo de la lente que hubo que corregir, y no era del tema

La primera pasada de `refutar_exactitud.py` devolvió «**0 negritas comprobadas, 0 no literales**»,
que es exactamente el resultado del que avisa el apartado 10 del manual: **un tema sin revisar
parece un tema impecable**.

La causa estaba en **cómo el tema citaba el artículo**. Decía: «El texto refundido de la Ley de
Propiedad Intelectual, **en su artículo 87**, dice quiénes son autores». La lente distingue dos
clases de marcador: el que **abre párrafo**, que manda sobre todo el bloque, y el que va **dentro
de una frase**, al que sólo se le da **su propia frase** para que una remisión no arrastre texto
ajeno. El del tema iba dentro de la frase, así que el bloque comprobado era **la frase sola**, sin
la cita del artículo que venía después.

Se reescribió el epígrafe para que **el marcador abra el párrafo** —«**Artículo 87**, "Autores":» y
debajo la cita—, y la lente pasó de **0 a 4 comprobadas**.

**La lección, que vale para todo lo que queda**: cuando una lente devuelve cero, **la primera
sospecha no es que el tema esté limpio, sino que la lente no ha mirado**. Y aquí la causa no fue un
error de la herramienta: fue **cómo estaba escrito el tema**. Citar un artículo en mitad de una
frase subordinada lo saca del alcance de la comprobación.

## Lo que se comprobó y no se encontró

La declaración central de este tema —**que ninguna de sus seis respuestas tiene norma detrás**— es
una **conclusión negativa**, que es la clase de afirmación que más caro sale escribir sin
comprobar: el proyecto ya se llevó ese susto con las fichas de fabricante del tema 9.

Así que se comprobó. Los seis términos —**guion literario**, **escaleta**, **storyline**,
**secuencia**, **elipsis** y el formato de columnas— se buscaron en **todas** las fuentes volcadas:
el texto refundido de la Ley de Propiedad Intelectual, la Ley General de Comunicación Audiovisual,
la Ley General de Telecomunicaciones, el Plan Técnico Nacional de la Televisión Digital Terrestre,
el III Convenio Colectivo de la Corporación RTVE, los materiales institucionales de igualdad y
prevención, y las normas técnicas de la Unión Internacional de Telecomunicaciones, la SMPTE, el
ETSI y la AES. El resultado, exacto:

| Término buscado | Apariciones en las fuentes reunidas |
|---|---|
| **escaleta** | 0 |
| **storyline** / *story line* | 0 |
| **elipsis** | 0 |
| **guion literario** | 0 |
| **guion técnico** | 0 |
| **Mac Guffin** | 0 |
| **secuencia** | Aparece, **pero nunca como unidad narrativa**: todas sus apariciones son «en consecuencia», «consecuencias» o «secuenciación» |

Sólo hubo un acierto lateral: la palabra «guion» sale **una vez** en todo el corpus, en el
**artículo 87** de la Ley de Propiedad Intelectual, y de ahí salió el único apoyo normativo del
tema.

## Lo que este tema no puede sostener

- **Las seis respuestas se apoyan sólo en la plantilla oficial.** Va dicho en la portada, en la
  tabla de niveles, en cada epígrafe y en la tabla final.
- **Las dos escalas que el tema construye** —del *storyline* al guion técnico, y del plano a la
  secuencia— **son ordenaciones del oficio**. Se justifican porque explican los distractores del
  examen, y el tema no las presenta como clasificación normalizada.
- **El artículo 87 no contesta ninguna pregunta.** El tema lo dice dos veces, en el epígrafe y en
  la trazabilidad, para que nadie lo lea como respaldo de lo que viene después.
