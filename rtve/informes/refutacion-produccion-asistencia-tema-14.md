# Refutación del tema 14 del específico de Producción (Asistencia)

**Siglas de este informe**: cuaderno de admisión temporal (**ATA**).

Cuatro preguntas con tratado detrás y dos sin nada, y **un fallo de las lentes que este tema sacó a
la luz y obligó a arreglar la herramienta**.

## El fallo de la lente, y su arreglo

La primera pasada de `refutar_exactitud.py` contra el **Convenio de Estambul** devolvió **34
negritas comprobadas y 34 no literales**. Un cien por cien de discrepancias es tan sospechoso como
un cero: **algo estaba mirando mal**.

**La causa.** Las lentes por artículo indexan la fuente **por número de artículo**, con un
diccionario. Y el Convenio de Estambul **no es una ley: es un tratado con anexos, y cada anexo
numera sus artículos desde 1**. El volcado tiene **quince «Artículo 1», quince «Artículo 2»,
catorce «Artículo 3»…** Con un diccionario que sobrescribe, **sólo sobrevive el último de cada
número**, y todo lo que el tema dice del artículo 1 del anexo A **se contrastaba contra el artículo
1 de otro anexo cualquiera**, que habla de otra cosa.

**Lo grave no es el falso positivo: es que no daba ningún error.** Es exactamente el fallo del
apartado 10 del manual —una comprobación que no comprueba y no se queja—, y la misma trampa que
`herramientas/doue.py` ya evitaba al volcar normas europeas, con un aviso de números repetidos que
**a las lentes se les había olvidado poner**.

**El arreglo**, aplicado a `refutar_exactitud.py` y a `refutar_modo.py`:

- Las versiones de un mismo número **se guardan todas y se comprueban juntas**, de modo que una
  cita literal de cualquiera de ellas **cuenta como encontrada**.
- La lente **avisa por escrito** de qué números se repiten y de que **la atribución por número no es
  fiable en esa fuente**, remitiendo a la lente de documento.

Con el arreglo, las no literales bajaron de **34 a 25**: **nueve eran falsos positivos** producidos
por contrastar contra el artículo equivocado.

**Comprobación de que el arreglo no mueve nada más.** Se revisaron **todas** las fuentes volcadas
del proyecto en busca de números de artículo repetidos: **sólo el Convenio de Estambul los tiene**.
Ningún tema anterior usaba esa fuente con las lentes por artículo, de modo que **ninguna cifra de
ningún informe anterior cambia**.

## Qué lente sirve aquí, ya con el arreglo puesto

| Lente | Contra qué | Resultado |
|---|---|---|
| Exactitud | Convenio de Estambul | **34 comprobadas, 25 no literales**, con el aviso de números repetidos |
| Documento | Convenio + las dos fichas de la Cámara | **204 negritas comprobadas, 133 no literales, 0 cifras huérfanas** |
| Prosa | El tema | **0 hallazgos** |

**Y el aviso de la propia lente dice cuál manda**: en una fuente con la numeración repetida, **la
lente de documento dice más**, porque compara contra el texto completo y la duplicidad no le
afecta. Sus **cero cifras huérfanas** son el resultado que importa: los **82 territorios**, las
**63 cámaras**, los **5.800 cuadernos**, los **12 meses**, las **48 horas** y las fechas **20 de
agosto** y **2 de septiembre de 2026** aparecen todos en su fuente.

Las **25 no literales de la lente de exactitud** son, revisadas una a una, **el comentario del tema
sobre el convenio** —«no es un salvoconducto ni un permiso de viaje», «los derechos no se pagan
porque están garantizados», «un techo, no un suelo»—, no citas.

## El hallazgo de contenido: una fuente que decía lo contrario

El trabajo más delicado de este tema no lo dio ninguna lente. La pregunta por el territorio en que
hace falta el cuaderno ATA se buscó primero **en el tratado**, y la relación de **estados firmantes
y estados parte** que el BOE publicó con él **contradice la respuesta oficial**: **Irán no está** y
**Ghana sí, como firmante sin ratificar**.

Ante eso caben tres conductas. **Recortar la pregunta** —decir que la respuesta oficial es dudosa—,
que el manual prohíbe. **Callar la lista** y contestar sin fuente, que es peor. O **buscar mejor**,
que es lo que se hizo: la **Cámara de Comercio de España** publica la **lista viva** de territorios
que admiten cuadernos ATA, fechada el **20 de agosto de 2026**, y allí **Irán está y los otros tres
no**.

El tema recoge **las dos listas y explica por qué difieren**: la del tratado es **una foto de
1997** y el sistema ha crecido treinta años. **Una lista que cambia se cita con su fecha o no se
cita.**

## Lo que este tema no puede sostener

- **El convenio no nombra a la Cámara de Comercio**; dice «asociación expedidora autorizada por las
  autoridades aduaneras». La atribución al organismo español es **institucional, no normativa**, y
  va separada.
- **La lista de estados parte del tratado no vale para la pregunta de los territorios**, y el tema
  dice por qué.
- **Las dos preguntas que no son del cuaderno ATA tienen las fuentes cerradas**: la documentación
  del bono de cargos varios no está en la ruta que su asociación publica, y el portal del Gobierno
  de Israel responde «prohibido» también con agente de navegador, por tres rutas. Las dos respuestas
  van **sin verificar en su fuente**, y dicho.
- **Las fichas de la Cámara son páginas vivas**, no normas. Van fechadas al 2 de septiembre de 2026.
